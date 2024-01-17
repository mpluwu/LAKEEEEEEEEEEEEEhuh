import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk
from tkinter import simpledialog
from tkinter import messagebox
from tkinter.ttk import *
from PIL import Image, ImageTk
ph=[8.5,8.5,8.4,8.4,8.5,8.5,8.5,8.4,8.3,8.3,8.3,8.4,8.3,8.3,0,8.6,8.6,8.6,8.6,8.6,8.6,8.6,8.6,8.6,8.6,8.6,8.5,8.6,8.6,8.6,8.6,8.6,8.6,8.5,8.6,8.5,8.4,8.2,8.4,7.9,8.1,7.8,7.9,8.2,8.4,7.9,7.8,7.7,7.9,0,8.7,8.2,8.6,8.2,7.9,8.1,7.8,8.4,8.3,8.6,8.3,8.4,8.3,9.3,8.9,8.8,8.5,8.6,8.2,9,8.7,9,9.1,8.7,8.6,8.8,9.06,0,8.6,8.2,8.9,8.6,8.5,8.4,7.4,8.6,8.4,8.4,8.5,8.6,8.7,8.1,8.4,8.6,9.2,9.4,9.6,9.1,0,8.9,8.64,8.77,8.5,9.2,8.7,0,8.5,8.3,8.5,8.5,8.4,8.5,9.7,8.5,8.4,8.6,8.3,8.7,8.4,8.7,8.8,8.4,8.7,8.8,8.6,8.7,8.4,8.4,8.4,8.3,8.4,8.3,8.7,8.3,8.4,8.6,8.7,8.2,8.5,8.4,8.7,8.6,8.2,8.4,8.7,8.6,8.8,8.4,8.4,8.5,8.4,8.4,8.5,8.3,8.2,8.5,8.4,8.6,8.6,8.5,8.3,8.0,8.4,8.5,8.5,8.5,8.4,8.4,0,8.4,8.4,8.3,8.6,8.4,8.4,0,8.4,8.4,8.3,8.6,8.4,8.4,8.4,8.4,8.5,8.4,8.5,8.3,8.4,8.4,8.6,8.6,8.5,8.5,8.6,8.4,8.2,8.3,8.3,8.5,8.4,8.2,8.3,8.5,0,0,0,0,0,0,8.7,8.7,8.7,8.6,8.6,8.5,8.6,8.4,8.5,8.5,8.4,8.5,8.5,8.6,8.4,8.4,8.5,8.4,8.5,8.3,8.4]
temp=[7.7,7.3,7.4,7.6,7.1,7.2,7,6.7,8.4,8.5,8.5,8.6,8.5,9.2,0,13.7,13.6,14,14.1,15.3,13.8,12.8,12.7,12.6,12.8,13.1,13.2,13,12.8,12.7,12.6,12.8,13.1,13.2,13,27.6,27.6,28.4,29.2,28.3,28.6,28.7,30.1,28.6,28.3,29.3,28.8,29.1,29.9,0,24.8,24,24.7,24.9,25,25.1,19.9,20,20.6,20.6,20.3,20.4,20,11.8,10.4,10.5,10.7,10.2,10.8,11.3,11.5,10.6,10.5,11.6,10.7,10.3,10.1,0,6.8,7.1,7.3,7.3,7.2,7.3,6.6,6.6,6.7,6.9,6.7,6.6,6.7,10,9.6,9.8,10.1,9.7,9.7,10,0,18.5,20.2,16.8,16.5,20.3,17.0,0,20.9,20.8,20.1,20.3,20.4,20.6,19.0,25.0,24.8,25.2,25.1,24.7,25.3,22.0,24.7,24.6,24.3,24.7,24.9,24.8,23,23.4,23.4,23.6,23.5,23.6,23.6,24.8,24.5,24.8,24.7,24.2,23.8,24.1,23.69,23.2,23.7,24.0,25.2,23.3,23.7,5.8,5.7,6.2,6.3,6.4,6.6,6.8,5.6,5.4,6.6,6.6,6.7,6.8,6.8,8.5,7.5,9.3,9.4,9.4,9.5,9.5,0,10.5,11.3,11.4,11.9,11.5,12.0,0,19.5,20.3,20.4,20.9,20.5,20.0,21.9,23.9,24.0,20.4,24.0,24.1,23.9,25.0,29.0,29.2,28.7,29.0,29.1,28.5,23.0,26.2,26.1,26.0,25.0,26.3,26.0,0,0,0,0,0,0,0,19.1,19.8,20.1,19.9,20.0,20.1,20.0,11.1,12.5,12.8,12.9,13.1,13.1,13.4,8.3,8.9,9.2,9.5,9.4,9.6,9.6]
asili_maddeler=[8,2,5,2,6,5,1,8,2,5,2,6,5,1,0,2,5,3,5,4,1,4,3,4,3,6,5,2,3,3,5,3,4,6,1,2,4,4,2,5,5,2,5,4,5,4,7,6,3,0,0,0,0,0,0,0,0,7,9,12,9,5,7,8,10,13,9,6,7,8,5,4,5,4,7,6,3,3,2,5,2,6,5,1,0,0,0,4,0,0,0,3,1,1,2,1,2,0,0,2,1,1,3,2,1,0,1,1,7,0,0,0,0,0,1,2,1,3,0,2,3,1,3,4,5,0,0,1,0,2,2,1,0,0,1,0,1.5,3,1,0,0,2,0,1,2,3,0,0.5,1,2,4,3,3,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,0.5,2.0,1.0,2.0,3.0,0.0,0.72,0.74,3.0,2.0,4.0,4.5,0.64,0.72,0.74,3.0,3.0,4.0,4.0,0.71,0,1.0,2.0,5.0,4.0,3.0,0.71,0,1.0,3.0,4.0,3.0,2.0,0.7,4.0,1.0,2.0,3.0,5.0,2.0,1.0,3.0,0.6,2.0,2.0,4.0,3.0,1.0,1.0,0.6,2.0,3.0,4.0,2.0,1.0,0,0,0,0,0,0,0,1.0,0.71,4.0,3.0,4.0,5.0,0.73,2.0,1.5,4.0,6.0,5.0,2.0,2.0,0.71,1.0,3.0,3.0,6.0,2.0,1.0]
bulaniqliq=[1,2,2,2,3,2.0,2.0,1,1,1,1,1,1.0,1.0,0,1,1,1,2,1.0,2.0,3,2,3,4,2,6.0,2.0,3,2,3,4,2,6.0,2.0,17,6,5,15,7,6.4,5.4,6.9,17.0,6.0,5.4,4.8,6.3,5.2,0,5.3,2.9,23.0,21.0,15.0,5.5,4.0,6.0,6.1,5.0,6.0,6.3,6.5,3.9,3.9,4.2,4.8,5.2,6.2,9.7,5,4,4,9,5,5.0,4.0,0,4,4.2,14.0,3,4,3,15,8,7,6,6,7,6,9,12,16,14,18,21,14,0,7.8,5.3,3.4,7.7,6.2,4.4,0,4,5,2,3,4,4,8,4,2,6,5,3,2,2,8,6,4,5.4,7.2,1.8,4,6,8,8,9,8,8,0.5,0.7,2.7,4.6,3.8,4.1,0.3,0.5,1,2,4,3,3,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,8.0,1.0,2.0,2.0,2.6,2.4,2.5,22.0,5.3,6.0,10.0,10.0,8.0,0,8.0,4.2,4.1,4.0,3.0,4.0,11.0,0,4.6,4.6,4.0,3.6,4.3,11.2,0,4.6,4.6,4.0,3.6,4.3,6.2,7.0,3.0,2.0,2.0,2.0,2.0,3.0,16.0,2.2,2.5,3.0,2.0,2.0,3.0,7.0,0.9,3.0,1.0,2.0,2.0,1.0,0,0,0,0,0,0,0,1.0,0.71,4.0,3.0,4.0,5.0,0.73,2.0,4.0,6.0,4.0,5.0,3.0,2.0,3.0,1.0,2.0,1.5,2.0,1.0,3.0]
elekkeciricilik=[438,596,593,597,594,592,593,467,653,671,668,657,663,647,0,683,681,672,678,669,687,459,883,888,879,881,867,890,459,883,888,879,881,867,890,370,326,364,1494,357,345,386,1601,349,508,1565,1311,988,1462,0,0,0,0,0,0,0,0,519,1672,1518,1504,418,584,363,744,710,3510,780,755,770,367,539,555,488,490,518,631,374,540,523,22000,528,529,523,0,539,522,534,1047,545,547,624,354,421,427,446,447,348,407,565,544,522,616,610,402,0,514,524,557,562,727,560,0,610,592,605,600,589,645,411,544,585,620,590,618,612,377,530,810,950,680,575,510,374,562,566,567,565,560,564,385,410,830,910,860,840,713,525,840,830,750,780,890,775,0,0,0,0,0,0,0,0,0,0,0,0,0,0,502.0,601.0,610.0,605.0,608.0,606.0,598.0,508.0,616.0,620.0,1348.0,1350.0,614.0,596.0,523.0,629.0,630.0,800.0,810.0,632.0,630.0,0,620.0,600.0,810.0,800.0,632.0,630.0,0,632.0,620.0,822.0,784.0,628.0,624.0,405.0,639.0,650.0,740.0,620.0,640.0,634.0,381.0,705.0,700.0,1195.0,1200.0,700.0,845.0,404.0,556.0,750.0,1200.0,800.0,700.0,764.0,0,0,0,0,0,0,0,452.0,572.0,630.0,2900.0,610.0,600.0,570.0,452.0,554.0,610.0,1200.0,600.0,594.0,570.0,400.0,560.0,600.0,941.0,620.0,640.0,634.0]
hellolmusqazlar_mql=[8.6,98,9.6,9.9,10,9.7,9.8,12.05,12.82,12.67,10.9,12.1,12.33,12.77,0,9.9,10.6,10.6,10,10.4,10.8,10.9,10.3,10.4,10.5,10,10.7,10.6,10.9,10.3,10.4,10.5,10,10.7,10.6,8.3,8.3,8.3,7.5,8,7.9,8.1,7.6,7.4,7.7,761.0,8,7.5,7.5,0,0,0,0,0,0,0,0,8.15,8.05,8,8.15,8.2,9.8,9.1,9.3,9.1,9.06,9.2,9.6,9.5,11.0,10.0,11.4,11.1,11,10.5,11.0,10,10,10.8,11,10.6,11,11,0,12.4,12.3,12.3,12,12.5,13.3,9,9.6,9.9,9.2,9,9.6,9.7,11.85,12.4,11.8,10.9,11.2,12.1,11.4,0,9.6,10,10.22,9.3,9.2,107.4,0,10.1,9.8,9.7,9.9,9.8,9.5,9.1,9.2,9.3,9.1,9.4,9.5,9.8,8.99,8.43,8.42,8.41,8.88,9.0,8.9,9.6,10.1,10.3,10.9,10.0,10.5,10.6,8.7,8.6,9.1,9.2,8.7,8.4,10.24,8.8,8.9,8.6,8.7,9.1,9.2,9.85,0,0,0,0,0,0,0,0,0,0,0,0,0,0,12.68,10.78,10.5,10.0,10.6,10.3,10.6,13.23,13.41,13.0,12.7,12.7,13.0,13.4,12.3,12.6,12.6,13.0,13.4,13.5,12.2,0,12.6,12.6,13.0,13.4,13.5,12.2,0,12.4,12.6,13.0,13.4,13.5,14.1,9.43,10.13,10.0,11.0,10.0,11.1,11.12,8.6,9.08,8.6,9.1,9.0,9.0,9.0,9.0,9.0,8.6,10.0,9.5,9.0,10.0,0,0,0,0,0,0,0,9.9,10.0,9.7,9.7,9.4,9.4,9.5,9.8,10.3,9.9,9.8,9.7,9.1,9.8,9.43,10.13,10.0,11.0,10.0,11.1,11.12]
hellolmusqazlar_faiz=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,102,102.3,107.3,102.3,107.4,117.1,100,100.7,101.2,96,99,100.6,101,104,105,103,99,102,103,102,0,102,104,105,103,102,112,0,103,99,97.8,100,99,98,100,102,103,100,106,107,111,100.6,102.8,100,101,106,109,109,89.6,101.8,101.9,102.0,101.0,101.9,102.0,105.4,104.6,111.6,113.2,105.4,103.2,126.2,103,103.1,102.8,102.9,104.9,105,116,0,0,0,0,0,0,0,0,0,0,0,0,0,0,104.9,98.5,99.6,96.7,99.8,97.5,99.8,105.6,104.2,104.1,104.0,104.0,104.1,104.2,104.3,103.3,103.3,106.0,107.0,108.1,105.9,0,103.3,103.3,106.0,107.0,108.1,105.9,0,103.0,104.0,105.0,108.0,109.0,105.4,108.9,121.1,118.0,123.0,118.0,121.0,121.3,109.6,120.4,109.6,122.0,115.0,122.0,122.0,101.0,102.0,109.6,109.0,107.0,102.0,109.0,0,0,0,0,0,0,0,101.0,102.2,103.0,103.0,99.3,99.2,99.5,99.8,102.2,101.0,99.8,99.5,98.2,99.9,108.9,121.1,118.0,123.0,118.0,121.0,121.3]
co2=[4,3,3,2,4,3,4,7,9,7,6,9,8,7,0,8,8,7,8,9,8,7,8,8,8,8,8,7,7,8,8,8,8,8,7,7,6,5,11,8,9,7,8,9,8,7,7,6,5,0,0,0,0,0,0,0,0,7,8,5,6,7,8,2,2,3,3,4,2,2,3,5,8,7,6,4,8,2,4,4,3,5,3,3,0,3,3,2,4,3,4,3,2,2,4,3,2,3,7,8,4,6,3,5,7,0,6,7,9,10,7,8,0,2,3,3,4,3,2,3,4,6,8,5,4,6,4,2,3,5,7,3,2,3,2,2,3,2,3,2,6,4,7,5,3,2,5,4,6,8,3,2,4,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4.0,3.0,4.0,4.0,3.0,4.0,3.0,4.0,2.0,4.0,5.0,5.0,5.0,2.0,4.0,2.0,2.0,1.0,3.0,2.0,2.0,0,2.0,2.0,1.0,3.0,2.0,2.0,0,3.0,1.0,2.0,3.0,2.0,2.0,1.0,2.0,2.0,2.0,3.0,2.0,2.0,3.0,2.0,3.0,3.0,2.0,2.0,3.0,2.0,1.0,2.0,1.0,2.0,1.0,3.0,0,0,0,0,0,0,0,3.0,2.0,4.0,3.0,4.0,3.0,3.0,3.0,3.0,5.0,4.0,3.0,2.0,4.0,1.0,2.0,2.0,2.0,3.0,2.0,2.0]
xlorlar_serbest=[0.06,0.05,0.03,0.06,0.08,0.06,0.06,0.02,0.09,0.07,0.02,0.05,0.04,0.08,0,0.11,0.07,0.10,0.08,0.07,0.09,0.08,0.06,0.08,0.07,0.06,0.09,0.08,0.04,0.06,0.08,0.07,0.06,0.09,0.08,0.09,0.00,0.00,0.22,0.00,0.00,0.14,0.10,0.07,0.07,0.04,0.07,0.04,0.05,0,0,0,0,0,0,0,0,0.03,0.03,0.04,0.08,0.03,0.04,0.08,0.04,0.05,0.06,0.12,0.06,0.04,0.05,0.06,0.08,0.04,0.05,0.06,0.07,0.14,0.05,0.05,0.15,0.07,0.10,0.08,0,0.05,0.07,0.03,0.04,0.04,0.05,0.11,0.02,0.04,0.06,0.05,0.06,0.08,0.13,0.08,0.04,0,0.04,0.35,0.01,0,0.04,0.05,0.08,0.07,0.04,0.05,0,0.03,0.05,0.05,0.06,0.04,0.06,0.03,0.04,0.02,0.04,0.06,0.07,0.07,0.04,0.05,0.07,0.08,0.05,0.06,0.04,0.03,0.03,0.05,0.02,0.03,0.05,0.06,0.19,0.06,0.14,0.08,0.08,0.07,0.04,0.03,0.04,0.02,0.04,0.07,0.08,0.07,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
xlorlar_umumi=[0.08,0.10,0.05,0.05,0.06,0.07,0.06,0.03,0.11,0.09,0.04,0.06,0.07,0.12,0,0.08,0.08,0.08,0.06,0.08,0.10,0.07,0.07,0.09,0.08,0.07,0.09,0.08,0.07,0.07,0.09,0.08,0.07,0.09,0.08,0.17,0.02,0.00,0.40,0.00,0.00,0.20,0.17,0.15,0.20,0.14,0.25,0.15,0.09,0,0,0,0,0,0,0,0,0.03,0.03,0.06,0.08,0.05,0.05,0.08,0.05,0.04,0.09,0.12,0.08,0.07,0.08,0.09,0.08,0.05,0.11,0.12,0.14,0.18,0.09,0.07,0.18,0.12,0.11,0.07,0,0.02,0.09,0.04,0.05,0.06,0.05,0.16,0.06,0.07,0.09,0.05,0.07,0.09,0.08,0.06,0.05,0.02,0.06,0.04,0,0,0.06,0.07,0.09,0.07,0.05,0.08,0,0.06,0.7,0.6,0.7,0.5,0.06,0.05,0.07,0.04,0.04,0.08,0.09,0.07,0.05,0.06,0.09,0.08,0.9,0.08,0.07,0.04,0.03,0.06,0.03,0.04,0.07,0.06,0.2,0.09,0.15,0.09,0.08,0.09,0.05,0.05,0.04,0.04,0.07,0.09,0.09,0.09,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
codluq=[3.2,3.2,3,3.3,3.4,3.3,3,3.4,3.8,4.2,3.4,3,2.92,3.2,0,3.2,3,3.1,3,2.9,3.3,3.2,4.1,3.7,6.5,3.4,4,4,3.2,4.1,3.7,6.5,3.4,4,4,2.2,3,2.8,3.6,3.2,3.3,2.8,2.4,2.6,3.1,2.9,4,3,2.8,0,0,0,0,0,0,0,0,2.5,2.7,3.3,3.6,4.2,2.5,2.6,2.8,2.9,3.2,3.6,4.7,2.7,2.6,2.8,3.1,3.3,2.8,2.4,2.6,3.4,3.8,4.2,3.4,3,2.92,3.2,0,2.9,2.8,2.2,2.9,2.5,3.6,3.2,4,3.8,3.,4,4.4,3.8,3.2,2.6,2.8,2.4,3,3.1,3.2,0,3.8,3.6,3.9,3.7,4.1,3.8,0,3.2,3.8,4.,3.,4.,4.2,2.8,2.9,3.2,3.4,3.8,3.4,2.6,3.6,3.8,4.2,4.9,4.8,3.9,3.4,3.5,3.4,3.6,4.6,4.8,4.4,3.2,3.6,3.6,3.4,4.8,4.6,5.6,4.2,3.5,3.6,3.4,4.2,4.4,4.2,3.2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3.5,3.9,4.0,4.2,4.4,3.7,3.3,3.8,3.4,4.4,4.6,5.2,3.9,3.3,3.9,3.7,4.4,4.1,4.2,3.8,3.6,0,3.1,4.1,4.3,4.2,3.6,3.4,0,3.2,4.1,4.2,4.1,3.7,3.5,4.1,4.2,5.1,5.2,5.1,4.7,5.5,3.0,2.0,3.0,3.0,2.0,2.0,3.0,3.5,4.1,4.6,5.2,4.5,3.9,3.5,0,0,0,0,0,0,0,3.8,3.9,4.2,4.4,5.6,3.9,3.7,3.8,3.7,4.0,4.2,5.4,3.7,3.4,4.1,4.2,5.1,5.2,5.1,4.7,5.5]
qelevilik=[150,173,176,173,170,167,179,840,900,890,840,850,890,900,0,350,325,345,380,325,345,141,162,159,159,159,159,162,141,162,159,159,159,159,162,132,138,123,150,482,135,129,112,120,92,135,133,118,117,0,0,0,0,0,0,0,0,150,1665,1615,1614,1504,620,150,173,170,600,170,176,173,114,102,110,122,118,131,120,120,170,150,300,153,163,173,0,173,170,182,173,176,170,173,183,181,150,153,158,150,134,118,124,141,112,108,120,0,180,193,200,207,183,197,0,173,145,153,157,153,150,153,140,120,133,152,144,135,120,134,142,151,144,144,110,132,150,153,156,147,150,153,131,122,141,152,146,136,117,130,140,120,150,136,124,142,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
esasion_cl=[8.6,38,42,44,72,68,51,20,60,60.2,61,67,61,63,0,34,36,44,82,28,33,11,57,84,740,77,82,75,11,57,84,740,77,82,75,13.6,38.1,38.4,218,40.9,48.3,48.5,10.8,31.3,286,35.5,34.8,37.9,267.3,0,0,0,0,0,0,0,0,33,56,204,221,187,43,38,36,34,860,280,290,42,38,42,34,128,131,136,42,12,40,42,62,41,48,44,0,42,134,147,112,80,43,40,120,110,130,96,124,38,44,58,64,62,70,50,48,0,56,46,68,72,76,38,0,38,86,120,140,134,82,153,140,120,133,152,144,135,36,34,42,186,192,170,88,34,38,42,86,82,76,44,36,38,110,122,134,116,26,48,42,84,76,64,66,38,0,0,0,0,0,0,0,0,0,0,0,0,0,0,44.0,46.0,79.0,75.0,88.0,64.0,57.0,48.0,38.0,52.0,74.0,78.0,64.0,42.0,44.0,48.0,68.0,72.0,66.0,52.0,46.0,0,48.0,68.0,72.0,66.0,52.0,46.0,0,50.0,68.0,75.0,67.0,51.0,49.0,38.0,42.0,56.0,82.0,96.0,62.0,39.0,39.0,41.0,55.0,84.0,98.0,64.0,36.0,36.0,45.0,59.0,88.0,92.0,62.0,39.0,0,0,0,0,0,0,0,42.0,46.0,112.0,108.0,104.0,54.0,48.0,44.0,49.0,111.0,109.0,105.0,58.0,50.0,38.0,42.0,56.0,82.0,96.0,62.0,39.0]
esasion_hco3=[168,153,181,139,135,175,178,169,172,165,140,155,148,137,0,169,177,153,179,156,129,165,152,170,144,122,168,174,165,152,170,144,122,168,174,142,175,185,163,149,182,163,145,175,162,180,166,154,165,0,0,0,0,0,0,0,0,126,153,122,140,128,137,126,128,131,232,158,162,131,120,125,134,240,250,210,180,153,151,145,157,152,148,149,0,140,120,151,160,145,125,140,157,153,157,142,139,140,144,158,155,159,144,133,142,0,140,151,170,180,160,190,0,160,180,190,195,200,170,160,155,170,190,185,192,172,145,155,170,210,224,216,160,139,141,132,223,216,197,163,130,134,220,248,264,218,125,140,142,184,166,175,160,130,0,0,0,0,0,0,0,0,0,0,0,0,0,0,140.0,144.0,158.0,182.0,194.0,171.0,162.0,140.0,152.0,164.0,172.0,168.0,156.0,144.0,140.0,152.0,164.0,172.0,168.0,156.0,144.0,0,156.0,161.0,176.0,170.0,151.0,147.0,0,157.0,162.0,172.0,179.0,155.0,150.0,162.0,160.0,164.0,178.0,176.0,166.0,148.0,169.0,162.0,164.0,175.0,176.0,168.0,149.0,164.0,163.0,165.0,171.0,173.0,169.0,145.0,0,0,0,0,0,0,0,172.0,168.0,184.0,224.0,222.0,176.0,164.0,170.0,165.0,181.0,221.0,220.0,171.0,162.0,162.0,160.0,164.0,178.0,176.0,166.0,148.0]
dates=["Yanvar 2018", "Fevral 2018", "Mart 2018", "Aprel 2018","May 2018","İyun 2018","İyul 2018","Sentyabr 2018","Oktyabr 2018","Noyabr 2018","Dekabr 2018","Yanvar 2019","Fevral 2019","Mart 2019","Aprel 2019","May 2019","İyun 2019","İyul 2019","Avqust 2019","Sentyabr 2019","Oktyabr 2019","Yanvar 2020","Fevral 2020","Mart 2020","Aprel 2020","May 2020","İyun 2020","İyul 2020","Avqust 2020","Sentyabr 2020","Oktyabr 2020","Noyabr 2020","Dekabr 2020"]
menteqeler=['Taxtakörpü-ceyranbatan kanalı','Su götürücü qurğunun yanı','Cənub nasos stansiyasının yanı','Cənub-qərb dambası, sızma suları','Cənub dambası, sızma suları','Şimal-şərq dambası, sızma suları','Meliorasiya nasos stansiyasının girişi']
def createceyran():
    ceyran=tk.Tk()
    ceyran.geometry("400x500")
    image=Image.open("ceyran.jpg")
    image= image.resize((300,205))
    image=ImageTk.PhotoImage(image)
    imaje=tk.Label(ceyran, image=image)
    mainbutton=Button(ceyran, text='Ceyranbatan infocenter',command=createstat)
    exitbtn=Button(ceyran, text='Cixis', command=ceyran.destroy)
    imaje.pack()
    mainbutton.pack()
    exitbtn.pack()
    ceyran.mainloop()
def createstat():
    ceyran.destroy
    stat=tk.Tk()
    stat.geometry('400x500') 
    def phstatistika():
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
        for i in range(7):
            h.append(ph[c])
            c+=1
        while 0 in h:
            k=h.index(0)
            del locations[k]
            del h[k]
        plt.plot(locations, h, 'g',marker='o')
        plt.grid()
        plt.show()
    def tempstatistika():
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
        for i in range(7):
            h.append(temp[c])
            c+=1
        while 0 in h:
            k=h.index(0)
            del locations[k]
            del h[k]
        b=plt
        plt.plot(locations,h,'g', marker='o')
        plt.grid()
        plt.show()
    def asilimaddestatistika():
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
        for i in range(7):
            h.append(asili_maddeler[c])
            c+=1
        while 0 in h:
            k=h.index(0)
            del locations[k]
            del h[k]
        plt.plot(locations,h,'g', marker='o')
        plt.grid()
        plt.show()
    def bulaniqliqstatistika():
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
        for i in range(7):
            h.append(bulaniqliq[c])
            c+=1
        while 0 in h:
            k=h.index(0)
            del locations[k]
            del h[k]
        plt.plot(locations,h,'g', marker='o')
        plt.grid()
        plt.show()
    def qelevilikstat():
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
        for i in range(7):
            h.append(ph[c])
            c+=1
        while 0 in h:
            k=h.index(0)
            del locations[k]
            del h[k]
        plt.plot(locations,h,'g', marker='o')
        plt.grid()
        plt.show()
    def elekstatistika():
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
        for i in range(7):
            h.append(elekkeciricilik[c])
            c+=1
        while 0 in h:
            k=h.index(0)
            del locations[k]
            del h[k]
        plt.plot(locations,h,'g', marker='o')
        plt.grid()
        plt.show()
    def hellolmusqazlar_mql_statistika():
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
        for i in range(7):
            h.append(hellolmusqazlar_mql[c])
            c+=1
        while 0 in h:
            k=h.index(0)
            del locations[k]
            del h[k]
        plt.plot(locations,h,'g', marker='o')
        plt.grid()
        plt.show()
    def hellolmusqazlar_faiz_statistika():
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
        for i in range(7):
            h.append(hellolmusqazlar_faiz[c])
            c+=1
        while 0 in h:
            k=h.index(0)
            del locations[k]
            del h[k]
        plt.plot(locations,h,'g', marker='o')
        plt.grid()
        plt.show()
    def co2_statistika():
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
        for i in range(7):
            h.append(co2[c])
            c+=1
        while 0 in h:
            k=h.index(0)
            del locations[k]
            del h[k]
        plt.plot(locations,h,'g', marker='o')
        plt.grid()
        plt.show()
    back=Button(stat, text='Geri', command=createceyran and stat.destroy)
    phbtn=Button(stat, text='Ph statistikası',command=phstatistika)
    tempbtn=Button(stat, text='Temperatur statistikası',command=tempstatistika)
    asilimaddebtn=Button(stat, text='Asılı maddələr statistikası', command=asilimaddestatistika)
    bulaniqbtn=Button(stat, text='Bulanıqlıq statistikası', command=bulaniqliqstatistika)
    qelevibtn=Button(stat, text='Qelevilik statistikası', command=qelevilikstat)
    elekbtn=Button(stat, text='Elektrik ke,iricilik statistikasi', command=elekstatistika)
    holmus_mqlbtn=Button(stat, text='Hell olmus qazlar mq/l statistikasi', command=hellolmusqazlar_mql_statistika)
    holmus_faizbtn=Button(stat, text='Hell olmus qazlar fazile statistikasi',command=hellolmusqazlar_faiz_statistika)
    co2btn=Button(stat, text='CO2 statistika', command=co2_statistika)
    back.pack(side='right')
    phbtn.pack()
    tempbtn.pack()
    asilimaddebtn.pack()
    bulaniqbtn.pack()
    elekbtn.pack()
    holmus_mqlbtn.pack()
    holmus_faizbtn.pack()
    co2btn.pack()
    qelevibtn.pack()
    stat.mainloop()
ceyran=tk.Tk()
ceyran.geometry("400x500")
image=Image.open("ceyran.jpg")
image= image.resize((300,205))
image=ImageTk.PhotoImage(image)
imaje=tk.Label(ceyran, image=image)
mainbutton=Button(ceyran, text='Ceyranbatan infocenter',command=createstat)
exitbtn=Button(ceyran, text='Cixis', command=ceyran.destroy)
imaje.pack()
mainbutton.pack()
exitbtn.pack()
ceyran.mainloop()
