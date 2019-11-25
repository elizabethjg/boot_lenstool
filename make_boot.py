import os as os
import numpy as np
from astropy.stats import bootstrap
from astropy.utils import NumpyRNGContext
from multiprocessing import Pool
from multiprocessing import Process

def run_lenstool(folder):
      print folder
      os.system(
      

ncores = 2

backgx = np.loadtxt('main/background_galaxies_main.lenstool')

infile = open('main/background_galaxies_main.lenstool', 'r')
header = infile.readline()[2:-2]

os.system('rm -r main_*')
index = np.arange(len(backgx))

with NumpyRNGContext(1):
	bootresult = (bootstrap(index, ncores)).astype(int)

total_folders = []

for j in range(ncores):
      os.system('mkdir main_'+str(j))
      os.system('cp -r main/* main_'+str(j)+'/')
      
      total_folders = np.append(total_folders, 'main_'+str(j))
      
      lenstool_catalogue = backgx[bootresult[j,:]]
      lenstool_catalogue[:,0] = np.arange(1,len(backgx)+1)
      
      np.savetxt( 'main_'+str(j)+'/background_galaxies_main.lenstool',lenstool_catalogue,\
			fmt='%i %f %f %f %f %f %f %f', header=header)                    


pool = Pool(processes=(ncores))
salida=np.array(pool.map(run_lenstool, total_folders))
