import SimpleITK as sitk
import os
import numpy as np
from utils import *


if __name__=="__main__":

    rtdose_path=input("input rtdose file path:")
    ori_rt_dose=sitk.ReadImage(rtdose_path)

    T2_path=input("input T2 file path:")
    t2_image=sitk.ReadImage(T2_path)

    resampled_rt_dose = sitk.Resample(ori_rt_dose, t2_image)
    tp_gy=float(input("input Tp(Gy):"))

    print(getVolumn(tp_gy,ori_rt_dose,resampled_rt_dose,t2_image))
    print(getMaxDiameter(tp_gy,ori_rt_dose,resampled_rt_dose,t2_image))
    print(getCenter(tp_gy,ori_rt_dose,resampled_rt_dose))
   
