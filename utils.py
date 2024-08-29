import SimpleITK as sitk
import os
import numpy as np


def getVolumn(tp_gy,ori_rt_dose,resampled_rt_dose,t2_image):

    t2_spacing = t2_image.GetSpacing()

    dose_grid_scale=float(ori_rt_dose.GetMetaData('3004|000e'))#3004|000e=key for get dose grid scale

    dose_threshold = tp_gy/dose_grid_scale
    max_value = sitk.GetArrayFromImage(resampled_rt_dose).max()

    mask_image = sitk.BinaryThreshold(resampled_rt_dose, lowerThreshold=dose_threshold, upperThreshold=float(max_value), insideValue=1, outsideValue=0)
    mask_array = sitk.GetArrayFromImage(mask_image)
    roi_volume_mm3 = mask_array.sum() * (t2_spacing[0] * t2_spacing[1] * t2_spacing[2])
    roi_volume_ml = roi_volume_mm3 / 1000

    return roi_volume_ml


def getMaxDiameter(tp_gy,ori_rt_dose,resampled_rt_dose,t2_image):

    t2_spacing = t2_image.GetSpacing()

    dose_grid_scale=float(ori_rt_dose.GetMetaData('3004|000e'))#3004|000e=key for get dose grid scale

    dose_threshold = tp_gy/dose_grid_scale
    max_value = sitk.GetArrayFromImage(resampled_rt_dose).max()

    mask_image = sitk.BinaryThreshold(resampled_rt_dose, lowerThreshold=dose_threshold, upperThreshold=float(max_value), insideValue=1, outsideValue=0)
    mask_array = sitk.GetArrayFromImage(mask_image)

    d_Max=np.max(np.sum(mask_array, axis=(0)))*t2_spacing[2]/10
    h_Max=np.max(np.sum(mask_array, axis=(1)))*t2_spacing[0]/10
    w_Max=np.max(np.sum(mask_array, axis=(2)))*t2_spacing[1]/10

    return d_Max,h_Max,w_Max

def getCenter(tp_gy,ori_rt_dose,resampled_rt_dose):


    dose_grid_scale=float(ori_rt_dose.GetMetaData('3004|000e'))#3004|000e=key for get dose grid scale

    dose_threshold = tp_gy/dose_grid_scale
    max_value = sitk.GetArrayFromImage(resampled_rt_dose).max()

    mask_image = sitk.BinaryThreshold(resampled_rt_dose, lowerThreshold=dose_threshold, upperThreshold=float(max_value), insideValue=1, outsideValue=0)
    mask_array = sitk.GetArrayFromImage(mask_image)
    non_zero_indices = np.transpose(np.nonzero(mask_array))

    d=0
    h=0
    w=0
    for _,coordinate in enumerate(non_zero_indices):
        d+=coordinate[0]
        h+=coordinate[1]
        w+=coordinate[2]

    return int(d/len(non_zero_indices)) ,int(h/len(non_zero_indices)) ,int(w/len(non_zero_indices))

def get_resampled_rt_dose(t2_image,rt_dose):

    rt_dose
    affine_transform = sitk.AffineTransform(3)
    interpolator = sitk.sitkLinear
    resampled_rt_dose= sitk.Resample(rt_dose, t2_image, affine_transform, interpolator)

    return resampled_rt_dose
