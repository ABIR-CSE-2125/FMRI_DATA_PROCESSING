import numpy as np
from PIL import Image
import pydicom as pydcm
# # print("helo")
# im = pydcm.dcmread('G:\ADNI\ADNI\\011_S_4827\Perfusion_Weighted\\2012-10-02_10_30_41.0\I338210\ADNI_011_S_4827_MR_Perfusion_Weighted_br_raw_20121012100133078_1_S169700_I338210.dcm')
im = pydcm.dcmread('G:\ADNI\ADNI\\002_S_0685\Resting_State_fMRI\\2012-07-27_09_17_54.0\I322442\ADNI_002_S_0685_MR_Resting_State_fMRI_br_raw_20120808113658163_3826_S160105_I322442.dcm')
im = im.pixel_array.astype(float)
rescaled_image = (np.maximum(im,0)/im.max())*255

final_image = np.uint8(rescaled_image)

final_image = Image.fromarray(final_image)
# final_image.show()
png_path = 'G:\\ADNI\\output_image.png'
final_image.save(png_path, format='PNG')