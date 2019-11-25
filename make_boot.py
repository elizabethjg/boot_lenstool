import os as os
import numpy as np
from astropy.stats import bootstrap
from astropy.utils import NumpyRNGContext
from multiprocessing import Pool
from multiprocessing import Process
import argparse

def run_lenstool_parallel(folder,ini,ncores):

      def run_lenstool(folder):
            print folder
            os.chdir(folder)
            os.system('lenstool hex.par -n')
            os.system('bayesMap hex.par')
            os.system('bayesMap.py hex.par')
            
      
      backgx = np.loadtxt(folder+'/background_galaxies_main.lenstool')
      
      infile = open(folder+'/background_galaxies_main.lenstool', 'r')
      header = infile.readline()[2:-2]
      
      
      index = np.arange(len(backgx))
      
      with NumpyRNGContext(1):
            bootresult = (bootstrap(index, ncores)).astype(int)
      
      total_folders = []
      
      for j in np.arange(ini,ini+ncores):
            os.system('rm -r '+folder+'_'+str(j))
            os.system('mkdir '+folder+'_'+str(j))
            os.system('cp -r '+folder+'/* '+folder+'_'+str(j)+'/')
            
            total_folders = np.append(total_folders, folder+'_'+str(j))
            
            lenstool_catalogue = backgx[bootresult[j,:]]
            lenstool_catalogue[:,0] = np.arange(1,len(backgx)+1)
            
            np.savetxt( folder+'_'+str(j)+'/background_galaxies_main.lenstool',lenstool_catalogue,\
                        fmt='%i %f %f %f %f %f %f %f', header=header)                    
      
      
      pool = Pool(processes=(ncores))
      salida=np.array(pool.map(run_lenstool, total_folders))


if __name__ == '__main__':
      parser = argparse.ArgumentParser(description = 'Run lenstool bootstrap in parallel')
      parser.add_argument('folder')
      parser.add_argument('-init', action='store', default=0, dest='init', 
                  type=int, help='init of the name folder')
      parser.add_argument('-ncores', action='store', dest='ncores', default=2, 
                  type=int, help='ncores')
      args = parser.parse_args()
      
      print args.folder,args.init,args.ncores
      
      run_lenstool_parallel(args.folder,args.init,args.ncores)
      
