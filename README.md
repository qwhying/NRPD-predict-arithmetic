# NRPD-predict-arithmetic
 Data, materials, and code for article ‘Neural representation precision of distance predicts arithmetic performance’     
 
## Data  
  
Under the `data` directory, you will find the processed data from three subjects, intended for decoding analysis. This includes:  
  
- Magnetic Resonance Imaging (MRI) data in `nii.gz` format.  
- Task parameter recording sheets in `.xls` format.  
  
These datasets are prepared and ready to be used for decoding analyses as described in our study.  
  
## Code  
  
The `code` directory includes the scripts and notebooks used for the decoding analysis presented in our article:  
  
- `decode.py`: This script is used for performing the decoding analysis.  
- `permutation.py`: This script generates the null distribution for permutation testing.  
- `permutationGetPvalue.ipynb`: This Jupyter notebook is used to read the results from the previous two scripts and calculate the p-values.   
  
## ROI  
  
Under the `ROI` directory, you will find mask files for specific regions of interest (ROIs): IPS(Left、Right、Bilateral) and hippocampus(Left、Right、Bilateral). These mask files are provided in a compatible format and can be used to extract the corresponding ROI data from the MRI scans for further analysis.  
  
---  
  
Feel free to explore, use, and modify the data and code as per your research needs. If you have any questions or encounter any issues, please feel free to open an issue in this repository.
