# PsychoEval-fMRI
This repository explores the use of fMRI brain scans for psychological evaluations

Source:  [https://www.studyforrest.org/data.html, ](https://www.studyforrest.org/data.html#3TfMRIon2hMovieEyegazeCardiacRespiration)
Publication:  https://www.nature.com/articles/sdata201692
Task Title:  3T fMRI on 2h Movie, Eyegaze (+Cardiac/Respiration)
Task Description:  "Two-hour 3 Tesla fMRI acquisition while 15 participants were shown an audio-visual version of the stimulus motion picture, simultaneously recording eye gaze location, heart beat, and breathing."

Data:  https://openneuro.org/datasets/ds000113/versions/1.3.0

Data Statistics:
Uploaded data has 35x451 fMRI brain scans for Study Subject #4 during Run #1 of multiple runs.
This totals 15,785 data samples of fMRI scans for just one run of one subject.
There are 15 subjects for this Task with eight Runs each, thus totaling over 1.8 million images.

Data Type/Size:
The uploaded dataset is a gunzip file with .nii files of size 61MB and "Git Large File Extension" was used to facilitate the transfer and version control.

Data Inspection:
File "forrest gump audio visual.py" has code that was used to look at the images in the dataset which are .nii files.
Python package "nibabel" is necessary to view .nii files.

