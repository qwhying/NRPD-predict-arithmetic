# NRPD-predict-arithmetic
 Data, materials, and code for article ‘Neural representation precision of distance predicts arithmetic performance’     
 
## Data  
  
Under the `data` directory, you will find the processed data from three subjects, intended for decoding analysis. This includes:  
  
- Functional Magnetic Resonance Imaging (fMRI) data in `nii.gz` format.  
- Task parameter recording sheets in `.xls` format.  
  
These datasets are prepared and ready to be used for decoding analyses as described in our study.  
  
## Code  
  
The `Script` directory includes the scripts used for the decoding analysis presented in our article:  
  
- `Decode.py`: This script is used for performing the decoding analysis.  
- `permutation.py`: This script generates the null distribution for permutation testing.  
- `permutationGetPvalue.ipynb`: This Jupyter notebook is used to read the results from the previous two scripts and calculate the p-values.   
- `mvpa_utils.py`: This script contains utility functions that may be used by other scripts in the repository.  
  
## ROI  
  
Under the `ROI` directory, you will find mask files for specific regions of interest (ROIs): IPS(Left、Right、Bilateral) and hippocampus(Left、Right、Bilateral). These mask files are provided in a compatible format and can be used to extract the corresponding ROI data from the MRI scans for further analysis.  
