import os
import pandas as pd
import numpy as np
from nilearn.image import index_img
from nilearn.maskers import NiftiMasker
from sklearn.utils import shuffle
from mvpa_utils import train_and_evaluate_model, train_model, evaluate_model

# Path settings
data_dir = 'path_to_data'  # Base directory for data


script_dir = f"{data_dir}/Script"  # Directory for scripts
result_dir = f"{data_dir}/Result/permutation"  # Directory for saving results
beta_dir = f"{data_dir}/Data"  # Directory containing beta images

result_name = "BIPSDistance"  # Name for result files
subres_dir = f"{result_dir}/{result_name}"  # Directory to save subject-specific results
ROI_mask = f"{data_dir}/ROI/Bilateral_IPS.nii"  # Path to the ROI mask

permutation_samples = 1000  # Number of permutations

# List of subjects
subject_list = ['sub-01', 'sub-02', 'sub-03']

# Create DataFrame to store results
df = pd.DataFrame(columns=['sub-ID', 'permutation_step', 'mean_acc', 'R-z(mean__acc)', 'overall_acc', 'R-z2(overall_acc)'])

# Iterate through each subject
for sub_no, subject_id in enumerate(subject_list):
    subject_dir = f"{beta_dir}/{subject_id}"  # Directory for the specific subject

    # Paths for beta images and trial information
    beta_image_path = f"{subject_dir}/4D_beta.nii.gz"
    trial_info_path = f"{subject_dir}/parameter_Correct.xls"

    # Load trial information
    trial_info = pd.read_excel(trial_info_path)

    # Initialize NiftiMasker with ROI mask
    nifti_masker = NiftiMasker(mask_img=ROI_mask, standardize=True)

    # Initialize NiftiMasker for the current run with z-score standardization
    nifti_masker_run = NiftiMasker(mask_img=ROI_mask, standardize='zscore_sample', runs=trial_info.run)
    X_train = nifti_masker_run.fit_transform(beta_image_path)  # Feature matrix for training

    # Create output directory if it does not exist
    output_dir = f"{subres_dir}"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Filter training data for the main task type
    y_train = trial_info.distance.to_numpy()

    # Train model using the training data
    SVR_decoderT = train_model(X_train, y_train)

    # Perform permutation testing
    for i in range(permutation_samples):
        y_trainP = shuffle(y_train, random_state=i)  # Shuffle labels for permutation
        mean_acc, overall_acc, predictions = train_and_evaluate_model(X_train, y_trainP)  # Train and evaluate model

        # Store results for the main task type
        df.loc[sub_no * permutation_samples + i] = [
            subject_id,
            i + 1,
            mean_acc,
            np.arctanh(mean_acc),
            overall_acc,
            np.arctanh(overall_acc)
        ]

    # Save results to Excel files
    df.to_excel(f"{output_dir}/accuracy.xlsx")

    # Increment subject counter
    sub_no += 1
