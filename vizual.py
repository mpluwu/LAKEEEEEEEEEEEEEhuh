import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import simpledialog
from tkinter import messagebox
from tkinter.ttk import *
from tkinter import ttk
from PIL import Image, ImageTk
import tkinter.font as font
ph=[8.5,8.5,8.4,8.4,8.5,8.5,8.5,8.4,8.3,8.3,8.3,8.4,8.3,8.3,0,8.6,8.6,8.6,8.6,8.6,8.6,8.6,8.5,8.6,8.6,8.6,8.6,8.6,8.6,8.5,8.6,8.5,8.4,8.2,8.4,7.9,8.1,7.8,7.9,8.2,8.4,7.9,7.8,7.7,7.9,0,8.7,8.2,8.6,8.2,7.9,8.1,7.8,8.4,8.3,8.6,8.3,8.4,8.3,9.3,8.9,8.8,8.5,8.6,8.2,9,8.7,9,9.1,8.7,8.6,8.8,9.06,0,8.6,8.2,8.9,8.6,8.5,8.4,7.4,8.6,8.4,8.4,8.5,8.6,8.7,8.1,8.4,8.6,9.2,9.4,9.6,9.1,0,8.9,8.64,8.77,8.5,9.2,8.7,0,8.5,8.3,8.5,8.5,8.4,8.5,9.7,8.5,8.4,8.6,8.3,8.7,8.4,8.7,8.8,8.4,8.7,8.8,8.6,8.7,8.4,8.4,8.4,8.3,8.4,8.3,8.7,8.3,8.4,8.6,8.7,8.2,8.5,8.4,8.7,8.6,8.2,8.4,8.7,8.6,8.8,8.4,8.4,8.5,8.4,8.4,8.5,8.3,8.2,8.5,8.4,8.6,8.6,8.5,8.3,8.0,8.4,8.5,8.5,8.5,8.4,8.4,0,8.4,8.4,8.3,8.6,8.4,8.4,0,8.4,8.4,8.3,8.6,8.4,8.4,8.4,8.4,8.5,8.4,8.5,8.3,8.4,8.4,8.6,8.6,8.5,8.5,8.6,8.4,8.2,8.3,8.3,8.5,8.4,8.2,8.3,8.5,0,0,0,0,0,0,8.7,8.7,8.7,8.6,8.6,8.5,8.6,8.4,8.5,8.5,8.4,8.5,8.5,8.6,8.4,8.4,8.5,8.4,8.5,8.3,8.4]
temp=[7.7,7.3,7.4,7.6,7.1,7.2,7,6.7,8.4,8.5,8.5,8.6,8.5,9.2,0,13.7,13.6,14,14.1,15.3,13.8,12.8,12.7,12.6,12.8,13.1,13.2,13,12.8,12.7,12.6,12.8,13.1,13.2,13,27.6,27.6,28.4,29.2,28.3,28.6,28.7,30.1,28.6,28.3,29.3,28.8,29.1,29.9,0,24.8,24,24.7,24.9,25,25.1,19.9,20,20.6,20.6,20.3,20.4,20,11.8,10.4,10.5,10.7,10.2,10.8,11.3,11.5,10.6,10.5,11.6,10.7,10.3,10.1,0,6.8,7.1,7.3,7.3,7.2,7.3,6.6,6.6,6.7,6.9,6.7,6.6,6.7,10,9.6,9.8,10.1,9.7,9.7,10,0,18.5,20.2,16.8,16.5,20.3,17.0,0,20.9,20.8,20.1,20.3,20.4,20.6,19.0,25.0,24.8,25.2,25.1,24.7,25.3,22.0,24.7,24.6,24.3,24.7,24.9,24.8,23,23.4,23.4,23.6,23.5,23.6,23.6,24.8,24.5,24.8,24.7,24.2,23.8,24.1,23.69,23.2,23.7,24.0,25.2,23.3,23.7,5.8,5.7,6.2,6.3,6.4,6.6,6.8,5.6,5.4,6.6,6.6,6.7,6.8,6.8,8.5,7.5,9.3,9.4,9.4,9.5,9.5,0,10.5,11.3,11.4,11.9,11.5,12.0,0,19.5,20.3,20.4,20.9,20.5,20.0,21.9,23.9,24.0,20.4,24.0,24.1,23.9,25.0,29.0,29.2,28.7,29.0,29.1,28.5,23.0,26.2,26.1,26.0,25.0,26.3,26.0,0,0,0,0,0,0,0,19.1,19.8,20.1,19.9,20.0,20.1,20.0,11.1,12.5,12.8,12.9,13.1,13.1,13.4,8.3,8.9,9.2,9.5,9.4,9.6,9.6]
elekkeciricilik=[438,596,593,597,594,592,593,467,653,671,668,657,663,647,0,683,681,672,678,669,687,459,883,888,879,881,867,890,459,883,888,879,881,867,890,370,326,364,1494,357,345,386,1601,349,508,1565,1311,988,1462,0,0,0,0,0,0,0,0,519,1672,1518,1504,418,584,363,744,710,3510,780,755,770,367,539,555,488,490,518,631,374,540,523,22000,528,529,523,0,539,522,534,1047,545,547,624,354,421,427,446,447,348,407,565,544,522,616,610,402,0,514,524,557,562,727,560,0,610,592,605,600,589,645,411,544,585,620,590,618,612,377,530,810,950,680,575,510,374,562,566,567,565,560,564,385,410,830,910,860,840,713,525,840,830,750,780,890,775,0,0,0,0,0,0,0,0,0,0,0,0,0,0,502.0,601.0,610.0,605.0,608.0,606.0,598.0,508.0,616.0,620.0,1348.0,1350.0,614.0,596.0,523.0,629.0,630.0,800.0,810.0,632.0,630.0,0,620.0,600.0,810.0,800.0,632.0,630.0,0,632.0,620.0,822.0,784.0,628.0,624.0,405.0,639.0,650.0,740.0,620.0,640.0,634.0,381.0,705.0,700.0,1195.0,1200.0,700.0,845.0,404.0,556.0,750.0,1200.0,800.0,700.0,764.0,0,0,0,0,0,0,0,452.0,572.0,630.0,2900.0,610.0,600.0,570.0,452.0,554.0,610.0,1200.0,600.0,594.0,570.0,400.0,560.0,600.0,941.0,620.0,640.0,634.0]
codluq=[3.2,3.2,3,3.3,3.4,3.3,3,3.4,3.8,4.2,3.4,3,2.92,3.2,0,3.2,3,3.1,3,2.9,3.3,3.2,4.1,3.7,6.5,3.4,4,4,3.2,4.1,3.7,6.5,3.4,4,4,2.2,3,2.8,3.6,3.2,3.3,2.8,2.4,2.6,3.1,2.9,4,3,2.8,0,0,0,0,0,0,0,0,2.5,2.7,3.3,3.6,4.2,2.5,2.6,2.8,2.9,3.2,3.6,4.7,2.7,2.6,2.8,3.1,3.3,2.8,2.4,2.6,3.4,3.8,4.2,3.4,3,2.92,3.2,0,2.9,2.8,2.2,2.9,2.5,3.6,3.2,4,3.8,3.,4,4.4,3.8,3.2,2.6,2.8,2.4,3,3.1,3.2,0,3.8,3.6,3.9,3.7,4.1,3.8,0,3.2,3.8,4.,3.,4.,4.2,2.8,2.9,3.2,3.4,3.8,3.4,2.6,3.6,3.8,4.2,4.9,4.8,3.9,3.4,3.5,3.4,3.6,4.6,4.8,4.4,3.2,3.6,3.6,3.4,4.8,4.6,5.6,4.2,3.5,3.6,3.4,4.2,4.4,4.2,3.2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3.5,3.9,4.0,4.2,4.4,3.7,3.3,3.8,3.4,4.4,4.6,5.2,3.9,3.3,3.9,3.7,4.4,4.1,4.2,3.8,3.6,0,3.1,4.1,4.3,4.2,3.6,3.4,0,3.2,4.1,4.2,4.1,3.7,3.5,4.1,4.2,5.1,5.2,5.1,4.7,5.5,3.0,2.0,3.0,3.0,2.0,2.0,3.0,3.5,4.1,4.6,5.2,4.5,3.9,3.5,0,0,0,0,0,0,0,3.8,3.9,4.2,4.4,5.6,3.9,3.7,3.8,3.7,4.0,4.2,5.4,3.7,3.4,4.1,4.2,5.1,5.2,5.1,4.7,5.5]
qelevilik=[150,173,176,173,170,167,179,840,900,890,840,850,890,900,0,350,325,345,380,325,345,141,162,159,159,159,159,162,141,162,159,159,159,159,162,132,138,123,150,482,135,129,112,120,92,135,133,118,117,0,0,0,0,0,0,0,0,150,1665,1615,1614,1504,620,150,173,170,600,170,176,173,114,102,110,122,118,131,120,120,170,150,300,153,163,173,0,173,170,182,173,176,170,173,183,181,150,153,158,150,134,118,124,141,112,108,120,0,180,193,200,207,183,197,0,173,145,153,157,153,150,153,140,120,133,152,144,135,120,134,142,151,144,144,110,132,150,153,156,147,150,153,131,122,141,152,146,136,117,130,140,120,150,136,124,142,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
qoxu=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
asili_maddeler=[8,2,5,2,6,5,1,8,2,5,2,6,5,1,0,5,3,5,4,1,4,3,4,3,6,5,2,3,3,5,3,4,6,1,2,4,4,2,5,5,2,5,4,5,4,7,6,3,0,0,0,0,0,0,0,0,7,9,12,9,5,7,8,10,13,9,6,7,8,5,4,5,4,7,6,3,3,2,5,2,6,5,1,0,0,0,4,0,0,0,3,1,1,2,1,2,0,0,2,1,1,3,2,1,0,1,1,7,0,0,0,0,0,1,2,1,3,0,3,1,3,4,5,0,0,1,0,2,2,1,0,0,1,0,1.5,3,1,0,0,2,0,1,2,3,0,0.5,1,2,4,3,3,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,0.5,2.0,1.0,2.0,3.0,0.0,0.72,0.74,3.0,2.0,4.0,4.5,0.64,0.72,0.74,3.0,3.0,4.0,4.0,0.71,0,1.0,2.0,5.0,4.0,3.0,0.71,0,1.0,3.0,4.0,3.0,2.0,0.7,4.0,1.0,2.0,3.0,5.0,2.0,1.0,3.0,0.6,2.0,2.0,4.0,3.0,1.0,1.0,0.6,2.0,3.0,4.0,2.0,1.0,0,0,0,0,0,0,0,1.0,0.71,4.0,3.0,4.0,5.0,0.73,2.0,1.5,4.0,6.0,5.0,2.0,2.0,0.71,1.0,3.0,3.0,6.0,2.0,1.0]
bulaniqliq=[1,2,2,2,3,2.0,2.0,1,1,1,1,1,1.0,1.0,0,1,1,1,2,1.0,2.0,3,2,3,4,2,6.0,2.0,3,2,3,4,2,6.0,2.0,17,6,5,15,7,6.4,5.4,6.9,17.0,6.0,5.4,4.8,6.3,5.2,0,5.3,2.9,23.0,21.0,15.0,5.5,4.0,6.0,6.1,5.0,6.0,6.3,6.5,3.9,3.9,4.2,4.8,5.2,6.2,9.7,5,4,4,9,5,5.0,4.0,0,4,4.2,14.0,3,4,3,15,8,7,6,6,7,6,9,12,16,14,18,21,14,0,7.8,5.3,3.4,7.7,6.2,4.4,0,4,5,2,3,4,4,8,4,2,6,5,3,2,2,8,6,4,5.4,7.2,1.8,4,6,8,8,9,8,8,0.5,0.7,2.7,4.6,3.8,4.1,0.3,0.5,1,2,4,3,3,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,8.0,1.0,2.0,2.0,2.6,2.4,2.5,22.0,5.3,6.0,10.0,10.0,8.0,0,8.0,4.2,4.1,4.0,3.0,4.0,11.0,0,4.6,4.6,4.0,3.6,4.3,11.2,0,4.6,4.6,4.0,3.6,4.3,6.2,7.0,3.0,2.0,2.0,2.0,2.0,3.0,16.0,2.2,2.5,3.0,2.0,2.0,3.0,7.0,0.9,3.0,1.0,2.0,2.0,1.0,0,0,0,0,0,0,0,1.0,0.71,4.0,3.0,4.0,5.0,0.73,2.0,4.0,6.0,4.0,5.0,3.0,2.0,3.0,1.0,2.0,1.5,2.0,1.0,3.0]
biogen_no3=[0.5,0.6,0.7,0.4,0.5,0.6,0.4,0.4,0.2,0.2,0.3,0.2,0.3,0.3,0,0.3,0.3,0.3,0.3,0.2,0.3,0.4,0.5,0.4,0.4,0.5,0.4,0.3,0.4,0.5,0.4,0.4,0.5,0.4,0.3,0.9,1.2,0.8,0.8,0.7,1.5,1.2,1,0.8,0.9,0.8,0.8,2.9,0.7,0,0,0,0,0,0,0,0,0.4,0.3,0.3,0.3,0.3,0.2,0.4,0.3,0.3,0.4,0.3,0.4,0.3,0.3,0.3,0.6,0.9,0.8,0.8,0.5,0.6 ,0.2,0.3,0.5,0.3,0.3,0.3,0,0.3,0.4,0.6,0.5,0.7,0.4,0.1,0,0.2,0.3,0.4,0.3,0.4,0.6,0.4,0.6,0.5,0.8,0.9,0.6,0,0.8,0.4,0.2,0.3,0.3,0.4,0,0.5,0.6,0.5,0.5,0.6,0.6,0.6,0.6,0.7,0.8,0.5,0.5,0.3,0.4,0.4,0.6,1.4,46,1.2,0.3,1.5,0.7,0.6,0.6,1,1.5,1,0.4,0.3,0.6,0.8,0.8,0.7,0.5,0.4,0.6,0.7,0.8,0.9,0.7,0.3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.3,0.4,0.7,0.6,0.8,0.4,0.3,0.4,0.4,0.6,0.8,1.1,0.8,0.9,0.5,0.5,0.7,0.7,0.6,0.5,0.4,0,0.4,0.8,0.6,0.5,0.6,0.3,0,0.3,0.7,0.9,0.8,0.7,0.5,0.5,0.4,0.6,0.8,0.9,0.8,0.6,0.5,0.5,0.7,0.9,0.8,0.7,0,0.4,0.6,0.9,0.8,0.7,0.9,0.8,0,0,0,0,0,0,0,0.4,0.5,0.4,0.6,0.7,1.1,0.4,0.3,0.4,0.7,0.7,0.6,1.0,0.3,0.6,0.3,0.6,0.7,0.8,0.7,0.8]
biogen_po43=[2.5,2.61,2.58,2.7,2.8,2.1,1.9,1.5,1.1,1.3,1.2,1.4,1.8,1.06,0,0.98,1.26,0.88,1.1,1.8,1,0.81,1.11,1.32,1.90,1.27,1.25,1.19,0.81,1.11,1.32,1.90,1.27,1.25,1.19,0.8,0.9,0.7,0.7,0.5,1.1,0.8,2.55,1.53,2.12,1.40,1.20,1.60,2.70,0,0,0,0,0,0,0,0,2.10,1.44,3.20,2.80,2.20,1.50,0.90,1.10,1.50,3.10,2.70,1.80,1.40,1.50,1.80,1.40,2.10,2.50,2.80,1.30,41,38,58,60,41,32,21,0,0.85,0.90,1.20,1.40,1.70,1.30,1.10,1.30,2.20,2.60,2.30,1.80,1.20,1.1,1.3,1.8,2.1,2.4,1.8,0.7,0,0.74,1.6,1.37,6.63,0.58,2.0,0,2.48,2.11,2.67,1.95,2.3,1.58,2.2,2.4,2.6,2.1,2.3,1.9,1.5,1.8,1.2,1.4,3.3,3.2,3.1,1.9,1.87,1.05,2.39,3.67,15.4,8.53,2.09,4.53,4.22,6.8,7.2,5.6,3.5,3.05,1.8,1.5,2.4,2.2,3.2,3.3,1.6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1.4,1.4,1.7,2.1,2.3,2.8,1.3,1.8,1.4,2.6,2.5,2.3,1.7,1.4,1.6,1.8,1.9,2.2,2.2,2.1,2.0,0,1.7,1.6,2.3,2.1,2.2,2.1,0,1.5,1.7,2.1,2.2,2.1,2.0,1.5,1.4,1.6,2.0,2.1,2.0,2.2,1.3,1.5,1.4,2.1,2.5,2.0,2.1,1.4,1.6,1.3,2.0,2.4,2.3,2.1,0,0,0,0,0,0,0,1.1,1.4,1.5,1.6,2.2,1.8,1.4,1.3,1.6,1.4,1.7,2.6,1.9,1.9,1.8,1.6,1.7,2.2,2.0,2.1,1.9]
esasioncl=[8.6,38,42,44,72,68,51,20,60,60.2,61,67,61,63,0,34,36,44,82,28,33,11,57,84,740,77,82,75,11,57,84,740,77,82,75,13.6,38.1,38.4,218,40.9,48.3,48.5,10.8,31.3,286,35.5,34.8,37.9,267.30,0,0,0,0,0,0,0,33,56,204,221,187,43,38,36,34,860,280,290,42,38,42,34,128,131,136,42,12,40,42,62,41,48,44,0,42,134,147,112,80,43,40,120,110,130,96,124,38,44,58,64,62,70,50,48,56,46,68,72,76,38,0,38,86,120,140,134,82,153,140,120,133,152,144,135,36,34,42,186,192,170,88,34,38,42,86,82,76,44,36,38,110,122,134,116,26,48,42,84,76,64,66,38,0,0,0,0,0,0,0,0,0,0,0,0,0,0,44.0,46.0,79.0,75.0,88.0,64.0,57.0,48.0,38.0,52.0,74.0,78.0,64.0,42.0,44.0,48.0,68.0,72.0,66.0,52.0,46.0,0,48.0,68.0,72.0,66.0,52.0,46.0,0,50.0,68.0,75.0,67.0,51.0,49.0,38.0,42.0,56.0,82.0,96.0,62.0,39.0,39.0,41.0,55.0,84.0,98.0,64.0,36.0,36.0,45.0,59.0,88.0,92.0,62.0,39.0,0,0,0,0,0,0,0,42.0,46.0,112.0,108.0,104.0,54.0,48.0,44.0,49.0,111.0,109.0,105.0,58.0,50.0,38.0,42.0,56.0,82.0,96.0,62.0,39.0]
biogen_no2=[0.007,0.005,0.003,0.002,0.002,0.005,0.004,0.006,0.007,0.01,0.006,0.01,0.006,0.004,0,0.006,0.008,0.01,0.012,0.006,0.006,0.007,0.008,0.02,0.011,0.005,0.008,0.007,0.007,0.008,0.02,0.011,0.005,0.008,0.007,0.031,0.009,0.018,0.073,0.003,0.006,0.038,0.11,0.029,0.79,0.051,0.049,0.033,0.028,0,0,0,0,0,0,0,0,0.027,0.011,0.034,0.031,0.027,0.019,0.033,0.013,0.026,0.026,0.024,0.018,0.012,0.032,0.014,0.025,0.026,0.023,0.027,0.018,0.018,0.005,0.009,0.045,0.004,0.01,0.006,0,0.01,0.015,0.018,0.021,0.007,0.008,0.035,0.009,0.011,0.014,0.016,0.008,0.007,0,0.03,0.009,0.011,0.012,0.052,0.044,0,0.069,0.022,0.055,0.045,0.002,0.006,0,0.034,0.011,0.018,0.037,0.043,0.018,0.033,0.012,0.019,0.034,0.036,0.045,0.012,0.033,0.29,0.04,0.046,0.073,0.53,0.039,0.036,0.013,0.072,0.045,0.124,0.117,0.072,0.046,0.022,0.025,0.017,0.066,0.034,0.026,0.061,0.022,0.051,0.042,0.016,0.011,0.024,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.028,0.023,0.048,0.076,0.062,0.086,0.054,0.024,0.019,0.067,0.058,0.044,0.028,0.018,0.022,0.018,0.031,0.048,0.051,0.031,0.019,0,0.017,0.030,0.047,0.052,0.033,0.017,0,0.016,0.031,0.046,0.051,0.031,0.016,0.019,0.018,0.037,0.045,0.055,0.032,0.017,0.020,0.019,0.035,0.042,0.053,0.037,0.020,0.021,0.018,0.033,0.046,0.051,0.039,0.022,0,0,0,0,0,0,0,0.019,0.014,0.034,0.076,0.101,0.022,0.031,0.021,0.017,0.031,0.071,0.098,0.021,0.030,0.018,0.021,0.039,0.047,0.051,0.034,0.019]
biogen_nh4=[0.06,0.05,0.06,0.07,0.06,0.09,0.01,0.04,0.06,0.05,0.07,0.05,0.08,0.05,0,0.04,0.06,0.07,0.09,0.06,0.05,0.13,0.22,0.25,0.56,0.18,0.21,0.19,0.13,0.22,0.25,0.56,0.18,0.21,0.19,0.07,0.08,0.11,0.05,0.04,0.08,0.06,0.19,0.23,0.21,0.19,0.18,0.23,0.18,0,0,0,0,0,0,0,0,0.18,0.22,0.34,0.28,0.25,0.19,0.15,0.18,0.21,0.45,0.34,0.31,0.24,0.14,0.12,0.18,0.21,0.23,0.22,0.11,0.46,0.34,0.32,0.41,0.19,0.30,0.12,0,0.13,0.22,0.24,0.26,0.22,0.18,0.11,0.18,0.20,0.24,0.25,0.21,0.19,0.24,0.22,0.26,0.31,0.34,0.36,0.18,0,0.22,0.24,0.18,0.34,0.28,0.12,0,0.18,0.14,0.21,0.24,0.25,0.09,0.18,0.15,0.22,0.24,0.32,0.28,0.18,0.18,0.15,0.19,0.44,0.41,0.34,0.14,0.19,0.06,0.02,0.09,0.17,0.35,0.22,0.18,0.15,0.34,0.32,0.28,0.32,0.14,0.22,0.24,0.31,0.33,0.32,0.28,.018,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.21,0.13,0.20,0.27,0.22,0.28,0.16,0.22,0.18,0.31,0.33,0.35,0.19,0.22,0.21,0.28,0.18,0.31,0.28,0.22,0.22,0,0.26,0.19,0.33,0.29,0.21,0.23,0,0.25,0.18,0.32,0.28,0.22,0.21,0.21,0.22,0.17,0.28,0.31,0.28,0.25,0.21,0.23,0.19,0.29,0.30,0.29,0.24,0.23,0.25,0.16,0.23,0.31,0.23,0.21,0,0,0,0,0,0,0,0.18,0.14,0.22,0.25,0.31,0.22,0.19,0.19,0.18,0.24,0.27,0.34,0.26,0.20,0.20,0.24,0.18,0.29,0.33,0.27,0.24]
esasion_mg2=[13,13,10,11,8,9,9,12.2,18,22,12.2,6.7,4.5,11,0,12,12,13.3,12,11.9,11.9,9.7,24.3,18.4,51,11.1,19.7,17.5,9.7,24.3,18.4,51,11.1,19.7,17.5,0,7.2,14.4,19.2,14,20.4,2.4,0.8,0.8,1.54,0.8,1.54,1.8,1.32,0,0,0,0,0,0,0,0,10.8,13.8,15.6,23.4,25.8,13.2,0.8,0.8,1.54,0.8,1.54,1.8,1.32,1.5,2.4,3,3.2,3.6,2.1,1.1,12.2,18,22,12.2,6.7,4.5,11,0,0,6,2.4,7.8,1.2,7.2,23.1,29.1,25.5,11,25.6,29.3,24.5,16.8,14.4,15.6,13.8,12,15.6,16.8,0,7.41,7.2,14.5,7.2,10.9,9.84,0,21,26.4,25.2,14.4,24,28.8,16.8,16.8,18,21.6,16.4,9.6,15.6,10.5,14.2,15.6,13.2,14.4,6,10.2,16.8,12,16.8,21.6,26.4,14.4,19.2,6,6,18,18,16.8,14.4,9.6,13.2,21.6,20.4,16.8,18,22.2,13.2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,15.8,16.1,12.5,12.7,6.3,8.2,17.8,19.2,15.6,22.2,22.2,24.6,23.4,19.2,18.0,13.2,13.2,18.6,17.4,25.2,20.4,0,13.2,13.2,18.6,17.4,25.2,20.4,0,13.2,13.2,18.6,17.4,25.2,20.4,12.2,13.2,13.2,18.6,17.4,25.2,20.4,12.2,13.2,13.2,18.6,17.4,25.2,20.4,12.2,13.2,13.2,18.6,17.4,25.2,20.4,0,0,0,0,0,0,0,20.4,23.4,24.0,15.6,16.8,22.8,21.0,20.4,23.1,24.2,15.3,16.1,22.5,20.8,12.2,13.2,13.2,18.6,17.4,25.2,20.4]
reng=["<25","<25","<25","<25","<25","<25","<25","<25","<25","<25","<25","<25","<25","<25","0","<25","<25","<25","<25","<25","<25","<25","<25","<25","<25","<25","<25","<25","<25","<25","<25","<25","<25","<25","<25","<25","<25","<25","<25","<25","<25","<25","<25","<25","<25","<25","<25","<25","<25","0","0","0","0","0","0","0","0","<25","<25","<25","<25","<25","<25","<25","<25","<25","<25","<25","<25","<25","<25","<25","<25","<25","<25","<25","<25","<25","<25","<25","<25","<25","<25","<25","<25","<25","<25","<25","<25","<25","<25","25|50","<25","<25","<25","<25","25|50","<25","<25","<25","<25","<25","<25","<25","<25","<25","<25","<25","<25","<25","<25","<25","<25","<25","<25","<25","<25","<25","<25","<25","<25","<25","<25","<25","<25","<25","<25","<25","<25","<25","<25","<25","<25","<25","<25","<25","<25","<25","<25","<25","<25","<25","<25","<25","<25","<25","<25","<25","<25","<25","<25","<25","<25","<25","<25","<25","<25","<25","<25","<25","<25","<25","<25","<25","<25","<25","<25","<25","<25","<25","<25","<25","<25","<25","<25","<25","<25","<25","<25","<25","<25","<25","<25","<25","<25","<25","<25","<25","<25","<25","<25","<25","<25","<25","<25","<25","<25","<25","<25","<25","<25","<25","<25","<25","<25","<25","<25","<25","<25","<25","<25","<25","<25","<25","<25","<25","<25","<25","<25","<25","<25","<25","<25","<25","<25","<25","<25","<25","<25","<25","<25","<25","<25","<25","<25","<25","<25","<25","<25","<25","<25","<25","<25","<25","<25","<25","<25","<25","<25","<25","<25","<25"]
minerallasdirilma=[245,345,346,324,361,354,378,504,705,712,704,706,701,721,0,730,738,731,734,733,740,360,953,950,932,941,950,948,360,953,950,932,941,950,948,405,526,696,1656,482,467,418,1500,342,517,1604,1408,490,1507,0,0,0,0,0,0,0,0,530,1665,1615,1604,1504,620,158,173,170,600,170,176,173,211,287,302,350,318,328,340,200,205,207,1330,207,204,205,0,277,286,524,272,271,274,318,167,164,167,166,168,164,202,290,280,274,313,310,201,0,271,273,295,281,351,281,0,305,296,303,300,295,345,206,272,292,310,295,309,306,146,345,405,480,440,286,260,188,280,284,286,283,282,282,192,205,415,460,430,420,655,265,420,415,375,390,395,385,0,0,0,0,0,0,0,0,0,0,0,0,0,0,251.0,300.0,305.0,302.0,304.0,303.0,244.0,254.0,308.0,310.0,674.0,680.0,306.0,298.0,261.0,314.0,315.0,400.0,405.0,316.0,315.0,0,310.0,300.0,405.0,400.0,316.0,315.0,0,316.0,310.0,400.0,405.0,314.0,312.0,203.0,320.0,325.0,370.0,310.0,320.0,312.0,190.5,352.0,350.0,597.0,600.0,350.0,423.0,202.0,278.0,375.0,600.0,400.0,350.0,282.0,0,277.0,0,0,0,0,0,226.0,286.0,315.0,1450.0,305.0,300.0,275.0,226.0,277.0,305.0,600.0,300.0,297.0,285.0,200.0,280.0,300.0,470.0,310.0,320.0,312.0]
###############FLOATLA###########################################################################################################
def xadd(n):
    if len(n)//7!=36:
        for i in range(7):
            n.insert(49, 0)
        for i in range(7):
            n.insert(154,0)
        for i in range(7):
            n.insert(161, 0)
    n=[float(i) for i in n]
xadd(ph)
xadd(temp)
xadd(elekkeciricilik)
xadd(codluq)
xadd(biogen_nh4)
xadd(biogen_no2)
xadd(biogen_no3)
xadd(biogen_po43)
xadd(esasion_mg2)
xadd(esasioncl)
xadd(qelevilik)
xadd(asili_maddeler)
xadd(qoxu)
xadd(bulaniqliq)
xadd(minerallasdirilma)
##########QIYMETSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSss
dates=["Yanvar 2018", "Fevral 2018", "Mart 2018", "Aprel 2018","May 2018","Iyun 2018","Iyul 2018",'Avqust 2018',"Sentyabr 2018","Oktyabr 2018","Noyabr 2018","Dekabr 2018","Yanvar 2019","Fevral 2019","Mart 2019","Aprel 2019","May 2019","Iyun 2019","Iyul 2019","Avqust 2019","Sentyabr 2019","Oktyabr 2019",'Noyabr 2019','Dekabr 2019',"Yanvar 2020","Fevral 2020","Mart 2020","Aprel 2020","May 2020","Iyun 2020","Iyul 2020","Avqust 2020","Sentyabr 2020","Oktyabr 2020","Noyabr 2020","Dekabr 2020"]
menteqeler=['Taxtakörpü-Ceyranbatan kanalı','Su götürücü qurğunun yanı','Cənub nasos stansiyasının yanı','Cənub-qərb dambası, sızma suları','Cənub dambası, sızma suları','Şimal-şərq dambası, sızma suları','Meliorasiya nasos stansiyasının girişi']
abbs=['Taxtakörpü',"Su götürücü","Cənub nasos","Cənub-qərb","Cənub dambası", "Şimal-şərq","Meliorasiya"]
###########IMAGESSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSs
path1='photo_1.jpeg'
path2='photo_2.jpeg'
path3='photo_3.jpeg'
path4='photo_4.jpeg'
path5='photo_5.jpg'
path6='photo_6.jpg'
path7='photo_7.jpg'
multimetr='multimetr.jpg'
phmetr='phmetr.jpg'
analizator='analizator.jpg'
spektrometr='spektroFOTOmetr.png'
nh4photo='nh4.png'
mgphoto='mg2.png'
clphoto='cl-.png'
no2photo='no2.png'
po43photo='po43.jpg'
no3photo='no3.png'
ceyranbb='JJAYRANBATAN.jpg'
def createceyran():
    ceyran=tk.Toplevel()
    ceyran.geometry("400x500")
    image=Image.open(ceyranbb)
    image= image.resize((300,205))
    image=ImageTk.PhotoImage(image)
    imaje=tk.Label(ceyran, image=image)
    buttonfont=font.Font(family='Helvetica', size=10, weight='bold')
    mainbutton=tk.Button(ceyran, text='Ceyranbatan Su Anbarı İnfocenter',command=createinfo, width=30, font=buttonfont)
    earlierbtn=tk.Button(ceyran, text='Texniki vasitələr', command=createitems,width=30, font=buttonfont)
    secondbutton=tk.Button(ceyran, text='Qalereya', command=createGallery, width=30, font=buttonfont)
    exitbtn=tk.Button(ceyran, text='Çıxış', command=ceyran.destroy, width=15, font=buttonfont)
    imaje.pack()
    mainbutton.pack()
    earlierbtn.pack()
    secondbutton.pack()
    exitbtn.pack()
    ceyran.mainloop()
def createstat():
    stat=tk.Toplevel()
    stat.geometry('200x200')
    def esasionmg_stat():
        def esasionmginfo():
            mg_info=tk.Toplevel()
            mg_info.geometry("400x400")
            mg_info.title("Mg2+ haqda")
            img1 = ImageTk.PhotoImage((Image.open(mgphoto)).resize((150,150)))
            panel1 = tk.Label(mg_info, image = img1)
            T=tk.Text(mg_info, height = 8, width = 60)
            back=Button(mg_info, text='ÇIXIŞ', command=mg_info.destroy)
            T.pack()
            panel1.pack()
            back.pack()
            T.insert(tk.END, 'Mg2 çoxsaylı fizioloji rollara malikdir, bunlar arasında neyron fəaliyyətinə nəzarət, ürəyin həyəcanlılığı, sinir-əzələ ötürülməsi, əzələ daralması, vazomotor ton, qan təzyiqi və periferik qan axını daxildir.')
            mg_info.mainloop()
        k=0
        plt.clf()
        while k not in dates:
            k=simpledialog.askstring(title='Sorğu',prompt='Hansı ay və il üzrə?')
            k=k.capitalize()
        c=dates.index(k)
        c=c*7
        h=[]
        locations=menteqeler
        abbs1=abbs
        for i in range(7):
            h.append(esasion_mg2[c])
            c+=1
        root=tk.Toplevel()
        root.geometry('500x400')
        root.title("Əsas ion - Mg 2+ , "+k)
        tree = Treeview(root, columns='qiymetler')
        tree.heading("#0", text='Məntəqə')
        tree.heading('qiymetler', text='Qiyməti')
        for i in range(len(locations)):
            tree.insert('',tk.END,text=locations[i], values=h[i])
        sonrabtn=Button(root, text='Qələvilik', command=qelevilikstat)
        Infomg=Button(root, text='Əlavə məlumat', command=esasionmginfo)
        tree.pack()
        sonrabtn.pack()
        Infomg.pack()
        plt.rc('xtick',labelsize=8)
        plt.plot(abbs1, h, 'g',marker='o')
        plt.title("Əsas ion - Mg 2+ ")
        plt.grid()
        plt.show()
        root.mainloop()
    def biogen_nh4_stat():
        def nh4info():
            nh4_info=tk.Toplevel()
            nh4_info.geometry("400x400")
            nh4_info.title("NH4 haqda")
            img1 = ImageTk.PhotoImage((Image.open(nh4photo)).resize((150,150)))
            panel1 = tk.Label(nh4_info, image = img1)
            T=tk.Text(nh4_info, height = 8, width = 60)
            back=Button(nh4_info, text='ÇIXIŞ', command=nh4_info.destroy)
            T.pack()
            panel1.pack()
            back.pack()
            T.insert(tk.END, 'Ammonyak həm qaz, həm də maye şəklində qələvi təbiətinə görə gözləri, tənəffüs yollarını və dərini qıcıqlandıra bilər. Kəskin təsirlərdən sonra insanlarda ammonyakın bioloji təsiri doza ilə bağlıdır - onlar ətrafdakı konsentrasiyadan, orqanizm tərəfindən qəbul edilən miqdardan və məruz qalma müddətindən asılıdır.')
            nh4_info.mainloop()
        k=0
        plt.clf()
        while k not in dates:
            k=simpledialog.askstring(title='Sorğu',prompt='Hansı ay və il üzrə?')
            k=k.capitalize()
        c=dates.index(k)
        c=c*7
        h=[]
        locations=menteqeler
        abbs1=abbs
        for i in range(7):
            h.append(biogen_nh4[c])
            c+=1      
        root=tk.Toplevel()
        root.geometry('500x400')
        root.title("Biogen maddə - NH4 , "+k)
        tree = Treeview(root, columns='qiymetler')
        tree.heading("#0", text='Məntəqə')
        tree.heading('qiymetler', text='Qiyməti')
        for i in range(len(locations)):
            tree.insert('',tk.END,text=locations[i], values=h[i])
        sonrabtn=Button(root, text='Biogen maddə - NO2', command=biogen_no2_stat)
        Infonh4=Button(root, text='Əlavə məlumat', command=nh4info)
        tree.pack()
        sonrabtn.pack()
        Infonh4.pack()
        plt.rc('xtick',labelsize=8)
        plt.plot(abbs1, h, 'g',marker='o')
        plt.title("Biogen maddə - NH4 ")
        plt.grid()
        plt.show()
        root.mainloop()
    def esasion_cl_stat():
        def esasionclinfo():
            cl_info=tk.Toplevel()
            cl_info.geometry("400x400")
            cl_info.title("Cl- haqda")
            img1 = ImageTk.PhotoImage((Image.open(clphoto)).resize((150,150)))
            panel1 = tk.Label(cl_info, image = img1)
            T=tk.Text(cl_info, height = 8, width = 60)
            back=Button(cl_info, text='ÇIXIŞ', command=cl_info.destroy)
            T.pack()
            panel1.pack()
            back.pack()
            T.insert(tk.END, 'Xlorid hüceyrələrə daxil olan və çıxan mayenin miqdarını və qida növlərini tənzimləməyə kömək edir. O, həmçinin lazımi pH səviyyələrini saxlayır, həzm üçün lazım olan mədə turşusunu stimullaşdırır, sinir və əzələ hüceyrələrinin fəaliyyətini stimullaşdırır və hüceyrələrdə oksigen və karbon qazının axını asanlaşdırır.')
            cl_info.mainloop()
        k=0
        plt.clf()
        while k not in dates:
            k=simpledialog.askstring(title='Sorğu',prompt='Hansı ay və il üzrə?')
            k=k.capitalize()
        c=dates.index(k)
        c=c*7
        h=[]
        locations=menteqeler
        abbs1=abbs
        for i in range(7):
            h.append(esasioncl[c])
            c+=1
        root=tk.Toplevel()
        root.geometry('500x400')
        root.title("Əsas ion - Cl- , "+k)
        tree = Treeview(root, columns='qiymetler')
        tree.heading("#0", text='Məntəqə')
        tree.heading('qiymetler', text='Qiyməti')
        for i in range(len(locations)):
            tree.insert('',tk.END,text=locations[i], values=h[i])
        sonrabtn=Button(root, text='Əsas ion - Mg 2+', command=esasionmg_stat)
        Infocl=Button(root, text='Əlavə məlumat', command=esasionclinfo)
        tree.pack()
        sonrabtn.pack()
        Infocl.pack()
        plt.rc('xtick',labelsize=8)
        plt.plot(abbs1, h, 'g',marker='o')
        plt.title("Əsas ion - Cl-")
        plt.grid()
        plt.show()
        root.mainloop()
    def biogen_no2_stat():
        def no2info():
            no2_info=tk.Toplevel()
            no2_info.geometry("400x400")
            no2_info.title("NO2 haqda")
            img1 = ImageTk.PhotoImage((Image.open(no2photo)).resize((150,150)))
            panel1 = tk.Label(no2_info, image = img1)
            T=tk.Text(no2_info, height = 12, width = 60)
            back=Button(no2_info, text='ÇIXIŞ', command=no2_info.destroy)
            T.pack()
            panel1.pack()
            back.pack()
            T.insert(tk.END, 'Yüksək konsentrasiyalı NO2 ilə tənəffüs havası insanın tənəffüs sistemində tənəffüs yollarını qıcıqlandıra bilər. Qısa müddət ərzində bu cür məruz qalmalar tənəffüs xəstəliklərini, xüsusən də astmanı ağırlaşdıra bilər, tənəffüs simptomlarına (öskürək, hırıltı və ya nəfəs almaqda çətinlik), xəstəxanaya yerləşdirilməyə və təcili yardıma baş çəkməyə səbəb ola bilər. NO2-nin yüksək konsentrasiyalarına daha uzun müddət məruz qalma astmanın inkişafına kömək edə bilər və tənəffüs yoluxucu infeksiyalara qarşı həssaslığı artıra bilər. Astma xəstəsi olan insanlar, eləcə də uşaqlar və yaşlılar NO2-nin sağlamlığa təsirləri üçün daha çox risk altındadırlar.')
            no2_info.mainloop()
        k=0
        plt.clf()
        while k not in dates:
            k=simpledialog.askstring(title='Sorğu',prompt='Hansı ay və il üzrə?')
            k=k.capitalize()
        c=dates.index(k)
        c=c*7
        h=[]
        locations=menteqeler
        abbs1=abbs
        for i in range(7):
            h.append(biogen_no2[c])
            c+=1
        root=tk.Toplevel()
        root.geometry('500x400')
        root.title("Biogen maddə - NO2 , "+k)
        tree = Treeview(root, columns='qiymetler')
        tree.heading("#0", text='Məntəqə')
        tree.heading('qiymetler', text='Qiyməti')
        for i in range(len(locations)):
            tree.insert('',tk.END,text=locations[i], values=h[i])
        sonrabtn=Button(root, text='Biogen maddə - PO43', command=biogen_po43_stat)
        Infono2=Button(root, text='Əlavə məlumat', command=no2info)
        tree.pack()
        sonrabtn.pack()
        Infono2.pack()
        plt.rc('xtick',labelsize=8)
        plt.plot(abbs1, h, 'g',marker='o')
        plt.title("Biogen maddə - NO2 ")
        plt.grid()
        plt.show()
        root.mainloop()
    def biogen_po43_stat():
        def po43info():
            po43_info=tk.Toplevel()
            po43_info.geometry("400x400")
            po43_info.title("PO43 haqda")
            img1 = ImageTk.PhotoImage((Image.open(po43photo)).resize((150,150)))
            panel1 = tk.Label(po43_info, image = img1)
            T=tk.Text(po43_info, height = 8, width = 60)
            back=Button(po43_info, text='ÇIXIŞ', command=po43_info.destroy)
            T.pack()
            panel1.pack()
            back.pack()
            T.insert(tk.END, 'Orqanizmdəki ümumi fosfatın 85%-i sümüklərdə və dişlərdə, 1%-i hüceyrədənkənar mayedə, qalan 14%-i isə hüceyrə membranlarının, nuklein turşularının, yüksək enerjili fosfat efirlərinin mühüm tərkib hissəsi olan digər toxumalarda paylanır.')
            po43_info.mainloop()
        k=0
        plt.clf()
        while k not in dates:
            k=simpledialog.askstring(title='Sorğu',prompt='Hansı ay və il üzrə?')
            k=k.capitalize()
        c=dates.index(k)
        c=c*7
        h=[]
        locations=menteqeler
        abbs1=abbs
        for i in range(7):
            h.append(biogen_po43[c])
            c+=1
        root=tk.Toplevel()
        root.geometry('500x400')
        root.title("Biogen maddə - PO43 , "+k)
        tree = Treeview(root, columns='qiymetler')
        tree.heading("#0", text='Məntəqə')
        tree.heading('qiymetler', text='Qiyməti')
        for i in range(len(locations)):
            tree.insert('',tk.END,text=locations[i], values=h[i])
        sonrabtn=Button(root, text='Biogen maddə - NO3', command=biogen_no3_stat)
        Infopo43=Button(root, text='Əlavə məlumat', command=po43info)
        tree.pack()
        sonrabtn.pack()
        Infopo43.pack()
        plt.rc('xtick',labelsize=8)
        plt.plot(abbs1, h, 'g',marker='o')
        plt.title("Biogen maddə - PO43 ")
        plt.grid()
        plt.show()
        root.mainloop()        
    def biogen_no3_stat():
        def no3_info():
            no3_info=tk.Toplevel()
            no3_info.geometry("400x400")
            no3_info.title("NO3 haqda")
            img1 = ImageTk.PhotoImage((Image.open(no3photo)).resize((150,150)))
            panel1 = tk.Label(no3_info, image = img1)
            T=tk.Text(no3_info, height = 8, width = 60)
            back=Button(no3_info, text='ÇIXIŞ', command=no3_info.destroy)
            T.pack()
            panel1.pack()
            back.pack()
            T.insert(tk.END, 'Əsasən, nitratlar təkcə ürəkdə deyil, həm də bədənin başqa yerlərində arteriya və venaları genişləndirir, yəni genişlənir və ya rahatlaşır. Ürəyin qan damarlarını genişləndirərək, nitratlar ürək əzələsinə qan axını yaxşılaşdıraraq ürəkdəki stressi azalda bilər. Bu, angina simptomlarını aradan qaldıracaq.')
            no3_info.mainloop()
        k=0
        plt.clf()
        while k not in dates:
            k=simpledialog.askstring(title='Sorğu',prompt='Hansı ay və il üzrə?')
            k=k.capitalize()
            if k not in dates:
                messagebox.showerror('Xəta', 'Axtardığınız sorğu üzrə nəticə tapılmadı.')
        c=dates.index(k)
        c=c*7
        h=[]
        locations=menteqeler
        abbs1=abbs
        for i in range(7):
            h.append(biogen_no3[c])
            c+=1
        root=tk.Toplevel()
        root.geometry('500x400')
        root.title("Biogen maddə - NO3 , "+k)
        tree = Treeview(root, columns='qiymetler')
        tree.heading("#0", text='Məntəqə')
        tree.heading('qiymetler', text='Qiyməti')
        for i in range(len(locations)):
            tree.insert('',tk.END,text=locations[i], values=h[i])
        sonrabtn=Button(root, text='Əsas ion - Cl', command=esasion_cl_stat)
        Infono3=Button(root, text='Əlavə məlumat', command=no3_info)
        tree.pack()
        sonrabtn.pack()
        Infono3.pack()
        plt.rc('xtick',labelsize=8)
        plt.plot(abbs1, h, 'g',marker='o')
        plt.title("Biogen maddə - NO3 ")
        plt.grid()
        plt.show()
        root.mainloop()
    def bulaniqliqstat():
        k=0
        plt.clf()
        while k not in dates:
            k=simpledialog.askstring(title='Sorğu',prompt='Hansı ay və il üzrə?')
            k=k.capitalize()
        c=dates.index(k)
        c=c*7
        h=[]
        locations=menteqeler
        for i in range(7):
            h.append(bulaniqliq[c])
            c+=1
        abbs1=abbs
        root=tk.Toplevel()
        root.geometry('500x400')
        root.title("Bulanıqlıq , "+k)
        tree = Treeview(root, columns='qiymetler')
        tree.heading("#0", text='Məntəqə')
        tree.heading('qiymetler', text='Qiyməti')
        for i in range(len(locations)):
            tree.insert('',tk.END,text=locations[i], values=h[i])
        sonrabtn=Button(root, text='Asılı maddələr', command=asili_maddestat)
        tree.pack()
        sonrabtn.pack()
        plt.rc('xtick',labelsize=8)
        plt.plot(abbs1, h, 'g',marker='o')
        plt.title("Bulanıqlıq ")
        plt.grid()
        plt.show()
        root.mainloop()
    def asili_maddestat(): 
        k=0
        plt.clf()
        while k not in dates:
            k=simpledialog.askstring(title='Sorğu',prompt='Hansı ay və il üzrə?')
            k=k.capitalize()
        c=dates.index(k)
        c=c*7
        h=[]
        locations=menteqeler
        for i in range(7):
            h.append(asili_maddeler[c])
            c+=1
        abbs1=abbs
        root=tk.Toplevel()
        root.geometry('500x400')
        root.title("Asılı maddələr , "+k)
        tree = Treeview(root, columns='qiymetler')
        tree.heading("#0", text='Məntəqə')
        tree.heading('qiymetler', text='Qiyməti')
        for i in range(len(locations)):
            tree.insert('',tk.END,text=locations[i], values=h[i])
        sonrabtn=Button(root, text='Ph', command=phstatistika)
        tree.pack()
        sonrabtn.pack()
        plt.rc('xtick',labelsize=8)
        plt.plot(abbs1, h, 'g',marker='o')
        plt.title("Asılı maddələr ")
        plt.grid()
        plt.show()
        root.mainloop()
    def phstatistika():
        k=0
        plt.clf()
        while k not in dates:
            k=simpledialog.askstring(title='Sorğu',prompt='Hansı ay və il üzrə?')
            k=k.capitalize()
        c=dates.index(k)
        c=c*7
        h=[]
        locations=menteqeler
        for i in range(7):
            h.append(ph[c])
            c+=1
        abbs1=abbs
        root=tk.Toplevel()
        root.geometry('500x400')
        root.title("pH , "+k)
        tree = Treeview(root, columns='qiymetler')
        tree.heading("#0", text='Məntəqə')
        tree.heading('qiymetler', text='Qiyməti')
        for i in range(len(locations)):
            tree.insert('',tk.END,text=locations[i], values=h[i])
        sonrabtn=Button(root, text='Temperatur', command=tempstatistika)
        tree.pack()
        sonrabtn.pack()
        plt.rc('xtick',labelsize=8)
        plt.plot(abbs1, h, 'g',marker='o')
        plt.title("pH ")
        plt.grid()
        plt.show()
        if ((sum(h)-h.count(0))/(len(h)-h.count(0)))>8.5 or ((sum(h)-h.count(0))/(len(h)-h.count(0)))<6.5:
            answer=messagebox.askyesno("pH , "+k,"Qiymətlərdə uyğunsuzluq müşahidə olunur. Müvafiq orqanlara xəbərdarlıq göndərilsinmi?")
            if answer:
                messagebox.showinfo("sending", "Xəbərdarlıq göndərilir.")
            else:
                messagebox.showinfo("not sent", "Xəbərdarlıq göndərilmədi.")
        root.mainloop()
    def tempstatistika():
        k=0
        plt.clf()
        while k not in dates:
            k=simpledialog.askstring(title='Sorğu',prompt='Hansı ay və il üzrə?')
            k=k.capitalize()
        c=dates.index(k)
        c=c*7
        h=[]
        locations=menteqeler
        for i in range(7):
            h.append(temp[c])
            c+=1
        abbs1=abbs
        root=tk.Toplevel()
        root.geometry('500x400')
        root.title("Temperatur , "+k)
        tree = Treeview(root, columns='qiymetler')
        tree.heading("#0", text='Məntəqə')
        tree.heading('qiymetler', text='Qiyməti')
        for i in range(len(locations)):
            tree.insert('',tk.END,text=locations[i], values=h[i])
        sonrabtn=Button(root, text='Elektrik keçiricilik', command=elekstatistika)
        tree.pack()
        sonrabtn.pack()
        plt.rc('xtick',labelsize=8)
        plt.plot(abbs1, h, 'g',marker='o')
        plt.title("Temperatur ")
        plt.grid()
        plt.show()
        root.mainloop()
    def qelevilikstat():
        k=0
        plt.clf()
        while k not in dates:
            k=simpledialog.askstring(title='Sorğu',prompt='Hansı ay və il üzrə?')
            k=k.capitalize()
        c=dates.index(k)
        c=c*7
        h=[]
        locations=menteqeler
        for i in range(7):
            h.append(qelevilik[c])
            c+=1
        abbs1=abbs
        root=tk.Toplevel()
        root.geometry('500x400')
        root.title("Qələvilik , "+k)
        tree = Treeview(root, columns='qiymetler')
        tree.heading("#0", text='Məntəqə')
        tree.heading('qiymetler', text='Qiyməti')
        for i in range(len(locations)):
            tree.insert('',tk.END,text=locations[i], values=h[i])
        sonrabtn=Button(root, text='Codluq', command=codluqstatistika)
        tree.pack()
        sonrabtn.pack()
        plt.rc('xtick',labelsize=8)
        plt.plot(abbs1, h, 'g',marker='o')
        plt.title("Qələvilik ")
        plt.grid()
        plt.show()
        root.mainloop()
    def elekstatistika():
        k=0
        plt.clf()
        while k not in dates:
            k=simpledialog.askstring(title='Sorğu',prompt='Hansı ay və il üzrə?')
            k=k.capitalize()
        c=dates.index(k)
        c=c*7
        h=[]
        locations=menteqeler
        for i in range(7):
            h.append(elekkeciricilik[c])
            c+=1
        abbs1=abbs
        root=tk.Toplevel()
        root.geometry('500x400')
        root.title("Elektrik keçiricilik , "+k)
        tree = Treeview(root, columns='qiymetler')
        tree.heading("#0", text='Məntəqə')
        tree.heading('qiymetler', text='Qiyməti')
        for i in range(len(locations)):
            tree.insert('',tk.END,text=locations[i], values=h[i])
        #sonrabtn=Button(root, text='Digər', command=qelevilikstat)
        tree.pack()
        #sonrabtn.pack()
        plt.rc('xtick',labelsize=8)
        plt.plot(abbs1, h, 'g',marker='o')
        plt.title("Elektrik keçiricilik ")
        plt.grid()
        plt.show()
        root.mainloop()
    def codluqstatistika():
        k=0
        plt.clf()
        while k not in dates:
            k=simpledialog.askstring(title='Sorğu',prompt='Hansı ay və il üzrə?')
            k=k.capitalize()
        c=dates.index(k)
        c=c*7
        h=[]
        locations=menteqeler
        for i in range(7):
            h.append(codluq[c])
            c+=1
        abbs1=abbs
        root=tk.Toplevel()
        root.geometry('500x400')
        root.title("Codluq , "+k)
        tree = Treeview(root, columns='qiymetler')
        tree.heading("#0", text='Məntəqə')
        tree.heading('qiymetler', text='Qiyməti')
        for i in range(len(locations)):
            tree.insert('',tk.END,text=locations[i], values=h[i])
        #sonrabtn=Button(root, text='Qələvilik', command=qelevilikstat)
        tree.pack()
        #sonrabtn.pack()
        plt.rc('xtick',labelsize=8)
        plt.plot(abbs1, h, 'g',marker='o')
        plt.title("Codluq ")
        plt.grid()
        plt.show()
        root.mainloop()
    def qoxustat():
        k=0
        plt.clf()
        while k not in dates:
            k=simpledialog.askstring(title='Sorğu',prompt='Hansı ay və il üzrə?')
            k=k.capitalize()
        c=dates.index(k)
        c=c*7
        h=[]
        locations=menteqeler
        abbs1=abbs
        for i in range(7):
            h.append(qoxu[c])
            c+=1      
        root=tk.Toplevel()
        root.geometry('500x400')
        root.title("Elektrik keçiricilik , "+k)
        tree = Treeview(root, columns='qiymetler')
        tree.heading("#0", text='Məntəqə')
        tree.heading('qiymetler', text='Qiyməti')
        for i in range(len(locations)):
            tree.insert('',tk.END,text=locations[i], values=h[i])
        sonrabtn=Button(root, text='Rəng', command=rengstat)
        tree.pack()
        sonrabtn.pack()
        plt.plot(abbs1, h, 'g',marker='o')
        plt.title("Qoxu ")
        plt.grid()
        plt.show()
        root.mainloop()
    def rengstat():
        k=0
        plt.clf()
        while k not in dates:
            k=simpledialog.askstring(title='Sorğu',prompt='Hansı ay və il üzrə?')
            k=k.capitalize()
        c=dates.index(k)
        c=c*7
        h=[]
        locations=menteqeler
        abbs1=abbs
        for i in range(7):
            h.append(reng[c])
            c+=1      
        root=tk.Toplevel()
        root.geometry('500x400')
        root.title("Rəng , "+k)
        tree = Treeview(root, columns='qiymetler')
        tree.heading("#0", text='Məntəqə')
        tree.heading('qiymetler', text='Qiyməti')
        for i in range(len(locations)):
            tree.insert('',tk.END,text=locations[i], values=h[i])
        tree.pack()
        plt.plot(abbs1, h, 'g',marker='o')
        plt.title("Rəng ")
        plt.grid()
        plt.show()
        root.mainloop()
    back=Button(stat, text='Geri', command=stat.destroy)
    def fizikpler():
        fizikiler=tk.Toplevel()
        fizikiler.geometry("200x200")
        bulanbtn=Button(fizikiler, text="Bulanıqlıq ",command=bulaniqliqstat, width=17)
        phbtn=Button(fizikiler, text='Ph ',command=phstatistika, width=17)
        tempbtn=Button(fizikiler, text='Temperatur ',command=tempstatistika, width=17)
        elekbtn=Button(fizikiler, text='Elektrik keçiricilik ', command=elekstatistika, width=17)
        asilimaddebtn=Button(fizikiler, text='Asılı maddələr ', command=asili_maddestat, width=17)
        back=Button(fizikiler, text='Geri', command=fizikiler.destroy)
        bulanbtn.pack()
        asilimaddebtn.pack()
        phbtn.pack()
        tempbtn.pack()
        elekbtn.pack()
        back.pack(side='right')
        fizikiler.mainloop()
    def kimyepler():
        kimyalar=tk.Toplevel()
        kimyalar.geometry("250x300")
        biogen_nh4_btn=Button(kimyalar, text="Biogen maddə - NH4 ", command=biogen_nh4_stat, width=20)
        biogen_no2_btn=Button(kimyalar, text="Biogen maddə - NO2 ", command=biogen_no2_stat, width=20)
        biogen_po43_btn=Button(kimyalar, text="Biogen maddə - PO43 ", command=biogen_po43_stat, width=20)
        biogen_no3_btn=Button(kimyalar, text="Biogen maddə - NO3 ",command=biogen_no3_stat, width=20)
        qelevibtn=Button(kimyalar, text='Qələvilik ', command=qelevilikstat, width=20)
        codbtn=Button(kimyalar, text='Codluq ', command=codluqstatistika, width=20)
        esasion_cl_btn=Button(kimyalar, text="Əsas ion - Cl ", command=esasion_cl_stat, width=20)
        esasionmg_btn=Button(kimyalar, text='Əsas ion - Mg 2+ ', command=esasionmg_stat, width=20)
        back=Button(kimyalar, text='Geri', command=kimyalar.destroy)
        biogen_nh4_btn.pack()
        biogen_no2_btn.pack()
        biogen_po43_btn.pack()
        biogen_no3_btn.pack()
        esasion_cl_btn.pack()
        esasionmg_btn.pack()
        qelevibtn.pack()
        codbtn.pack()
        back.pack(side='right')
    def orqanlar():
        orqanaleptik=tk.Toplevel()
        orqanaleptik.geometry("200x200")
        qoxubtn=Button(orqanaleptik, text='Qoxu ', command=qoxustat)
        rengbtn=Button(orqanaleptik, text="Rəng ",command=rengstat)
        back=Button(orqanaleptik, text='Geri', command=orqanaleptik.destroy)
        qoxubtn.pack()
        rengbtn.pack()
        back.pack(side='right')
        orqanaleptik.mainloop()
    fiziki_btn=Button(stat, text='Fiziki parametrlər', command=fizikpler)
    kimya_btn=Button(stat, text="Kimyəvi parametrlər", command=kimyepler)
    orqanaleptik_btn=Button(stat, text='Orqanaleptik parametrlər', command=orqanlar)
    fiziki_btn.pack()
    kimya_btn.pack()
    orqanaleptik_btn.pack()
    back.pack(side='right')
    stat.mainloop()
def createGallery():
    Gallery=tk.Toplevel()
    Gallery.geometry('600x600')
    img1 = ImageTk.PhotoImage((Image.open(path1)).resize((300,250)))
    panel1 = tk.Label(Gallery, image = img1)
    img2 = ImageTk.PhotoImage((Image.open(path2)).resize((300,250)))
    panel2 = tk.Label(Gallery, image = img2)
    img3 = ImageTk.PhotoImage((Image.open(path3)).resize((300,250)))
    panel3 = tk.Label(Gallery, image = img3)
    img4 = ImageTk.PhotoImage((Image.open(path4)).resize((300,250)))
    panel4 = tk.Label(Gallery, image = img4)
    back=Button(Gallery, text='Geri', command=createceyran and Gallery.destroy)
    back.pack(side='right')
    panel1.pack(side='left')
    panel2.pack(side='bottom')
    panel3.pack(side='top')
    panel4.pack()
    Gallery.mainloop()
def createinfo():
    Info=tk.Toplevel()
    Info.geometry('700x700')
    T=tk.Text(Info, height = 5, width = 57)
    l = Label(Info, text = "Məlumat")
    back=Button(Info, text='Geri', command=Info.destroy)
    lookatstats=Button(Info, text='Statlara bax', command=createstat)
    melumat='Samur-Abşeron kanalından qidalanan Ceyranbatan su anbarı və anbarın sahilində tikilmiş su təmizləyici qurğular kompleksi Abşeron yarımadasının içməli su təchizatında böyük paya malikdir.'
    image=Image.open("map.jpeg")
    image= image.resize((500,500))
    image=ImageTk.PhotoImage(image)
    imaje=tk.Label(Info, image=image)
    l.pack()
    T.pack()
    imaje.pack()
    back.pack()
    lookatstats.pack()
    T.insert(tk.END, melumat)
    Info.mainloop()
def createitems():
    def createspektrofotometr():
        sp=tk.Toplevel()
        sp.geometry("600x600")
        sp.title('Spektrofotometr')
        T=tk.Text(sp, height = 5, width = 57)
        back=Button(sp, text='Çıxış', command=sp.destroy)
        imgs = ImageTk.PhotoImage((Image.open(spektrometr)).resize((400,400)))
        panels = tk.Label(sp, image = imgs)
        T.pack()
        panels.pack()
        back.pack()
        T.insert(tk.END, 'Spektrofotometr - müxtəlif elektromaqnit şüalanma növlərini (görünən, infraqırmızı, ultrabənövşəyi) şüalar vasitəsilə məhlulların, maddələrin udulma, ötürülmə, optik sıxlıq və konsentrasiya dərəcəsinin spektral asılılığını ölçmək üçün zəruri olan yüksək texnologiyalı bir cihazdır.')
        sp.mainloop()
    def createmultimetr():
        sp=tk.Toplevel()
        sp.geometry("600x600")
        sp.title('Multimetr')
        T=tk.Text(sp, height = 5, width = 57)
        back=Button(sp, text='Çıxış', command=sp.destroy)
        imgm = ImageTk.PhotoImage((Image.open(multimetr)).resize((450,450)))
        panelm = tk.Label(sp, image = imgm)
        T.pack()
        panelm.pack()
        back.pack()
        T.insert(tk.END, 'Spektrofotometr - müxtəlif elektromaqnit şüalanma növlərini (görünən, infraqırmızı, ultrabənövşəyi) şüalar vasitəsilə məhlulların, maddələrin udulma, ötürülmə, optik sıxlıq və konsentrasiya dərəcəsinin spektral asılılığını ölçmək üçün zəruri olan yüksək texnologiyalı bir cihazdır.')
        sp.mainloop()
    def createanalizator():
        sp=tk.Toplevel()
        sp.geometry("600x600")
        sp.title('Analizator')
        T=tk.Text(sp, height = 5, width = 57)
        back=Button(sp, text='Çıxış', command=sp.destroy)
        imgm = ImageTk.PhotoImage((Image.open(analizator)).resize((450,450)))
        panelm = tk.Label(sp, image = imgm)
        T.pack()
        panelm.pack()
        back.pack()
        T.insert(tk.END, 'Suyun keyfiyyət analizatorları real vaxt rejimində yüksək keyfiyyət testini aparmağa və müəyyən obyektdə içməli, məişət, tullantı su standartlarına uyğunluğa nəzarət etməyə imkan verir.')
        sp.mainloop()
    def createphmetr():
        sp=tk.Toplevel()
        sp.geometry("600x600")
        sp.title('pH-metr')
        T=tk.Text(sp, height = 5, width = 57)
        back=Button(sp, text='Çıxış', command=sp.destroy)
        imgm = ImageTk.PhotoImage((Image.open(phmetr)).resize((450,450)))
        panelm = tk.Label(sp, image = imgm)
        T.pack()
        panelm.pack()
        back.pack()
        T.insert(tk.END, 'pH-metr - sənaye və fabriklərdə, məişət cihazlarını, akvariumda istifadə olunan mayelərin keyfiyyətinə nəzarət etmək üçün suyun pH göstəricilərinin (hidrogen ionlarının aktivliyi) ölçülərini aparır.')
        sp.mainloop()
    items=tk.Toplevel()
    items.geometry("500x900")
    items.title("Texniki vasitələr")
    imgs = ImageTk.PhotoImage((Image.open(spektrometr)).resize((100,100)))
    panels = tk.Label(items, image = imgs)
    imgm = ImageTk.PhotoImage((Image.open(multimetr)).resize((100,100)))
    panelm = tk.Label(items, image = imgm)
    imga = ImageTk.PhotoImage((Image.open(analizator)).resize((100,100)))
    panela = tk.Label(items, image = imga)
    imgh = ImageTk.PhotoImage((Image.open(phmetr)).resize((100,100)))
    panelh = tk.Label(items, image = imgh)
    buttonfont=font.Font(family='Helvetica', size=15, weight='bold')
    spekbtn=tk.Button(items, text='Spektrofotometr haqda', command=createspektrofotometr,font=buttonfont, width=20)
    multimetrbtn=tk.Button(items, text='Multimetr haqda', command=createmultimetr,font=buttonfont, width=20)
    analizatorbtn=tk.Button(items, text='Analizator haqda', command=createanalizator,font=buttonfont, width=20)
    phmetrbtn=tk.Button(items, text='pH-metr haqda', command=createphmetr,font=buttonfont, width=20)
    back=tk.Button(items, text='Çıxış', command=items.destroy,font=buttonfont)
    spekbtn.pack()
    panels.pack(side='top')
    multimetrbtn.pack()
    panelm.pack(side='top')
    analizatorbtn.pack()
    panela.pack(side='top')
    phmetrbtn.pack()
    panelh.pack(side='top')
    back.pack(side="right")
    items.mainloop()
titul=tk.Tk()
titul.geometry('1500x706')
titul.attributes('-fullscreen', True)
image=Image.open("ceyran.png")
image= image.resize((1500,706))
image=ImageTk.PhotoImage(image)
titulbtn=Button(titul, text = 'kliklə', image = image, command=createceyran).pack()
buttonfont=font.Font(family='Helvetica', size=25, weight='bold')
back=tk.Button(titul, text='Çıxış', command=titul.destroy, width=20, font=buttonfont)
style=ttk.Style(titul)
def on_enter(n):
    back.config(background='grey')
def on_leave(n):
    back.config(background='white',foreground= 'black')
back.bind('<Enter>', on_enter)
back.bind('<Leave>', on_leave)
style.theme_use('clam')
back.pack(fill='x')
titul.mainloop()
