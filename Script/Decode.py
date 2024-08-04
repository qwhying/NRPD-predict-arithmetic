import os
import pandas as pd
import numpy as np
from nilearn.image import index_img
from nilearn.maskers import NiftiMasker
from mvpa_utils import train_and_evaluate_model, train_model, evaluate_model

# Path settings
data_dir = 'path_to_data'  # Directory containing the data

script_dir = f"{data_dir}/Script"  # Directory containing scripts
result_dir = f"{data_dir}/Result"  # Directory to store results
beta_dir = f"{data_dir}/Data"  # Directory containing beta images

result_name = "BIPSDistance"
subres_dir = f"{result_dir}/{result_name}"  # Directory to store the specific result
if not os.path.exists(subres_dir):
        os.makedirs(subres_dir)
ROI_mask = f"{data_dir}/ROI/Bilateral_IPS.nii"  # Path to the ROI mask

# Dataframe to store results
results_df = pd.DataFrame(columns=['subject_id','mean_acc', 'overall_acc'])

# List of subjects
subject_list = ['sub-01', 'sub-02', 'sub-03']


# Loop through each subject
for sub_no, subject_id in enumerate(subject_list):
    subject_dir = f"{beta_dir}/{subject_id}"  # Directory for the specific subject
    
    # Load and process data
    beta_image_path = f"{subject_dir}/4D_beta.nii.gz"  # Path to the 4D beta image
    trial_info = pd.read_excel(f"{subject_dir}/parameter_Correct.xls")  # Load trial information


    # Standardize and mask the fMRI data, taking runs into account
    nifti_masker_run = NiftiMasker(mask_img=ROI_mask, standardize='zscore_sample', runs=trial_info.run)
    X_train = nifti_masker_run.fit_transform(beta_image_path)


    y_train = trial_info.distance.to_numpy()  # Extract distance information for training
    mean_acc, overall_acc, predictions = train_and_evaluate_model(X_train, y_train)  # Train and evaluate model
    svr_decoder = train_model(X_train, y_train)  # Train the model

    # Store results
    results_df.loc[sub_no] = [subject_id, mean_acc, overall_acc]
    results_df.to_excel(f"{subres_dir}/accuracy.xlsx")  # Save results to Excel
