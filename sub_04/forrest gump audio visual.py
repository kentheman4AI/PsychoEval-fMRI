from matplotlib import pyplot as plt
import nibabel as nib

# data for Subject 04
path = 'C:/Users/kenne/OneDrive/Desktop/miscellaneous/education/Springboard/Machine Learning/datasets/PsycoEval_fMRI/sub_04/sub-04_ses-movie_func_sub-04_ses-movie_task-movie_run-1_bold.nii'

img = nib.load(path).get_fdata()
img.shape

# there are 35x451 fMRI brain scans for Study Subject #4 during Run #1 of multiple runs
# totaling 15,785 data samples of fMRI scans for just one run of one subject
# there are 15 subjects for this Task with eight Runs each
print(img.shape)

plt.style.use('default')
fig, axes = plt.subplots(4,4, figsize=(12,12))
for i, ax in enumerate(axes.reshape(-1)):
    ax.imshow(img[:,:,7,1 + i])
plt.show()
