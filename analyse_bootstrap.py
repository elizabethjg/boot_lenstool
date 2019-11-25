import os as os
import numpy as np
from astropy.io import fits
from astropy.wcs import WCS
from ang_sep import ang_sep
from astropy.cosmology import LambdaCDM
cosmo = LambdaCDM(H0=70, Om0=0.3, Ode0=0.7)


def aperture_mass(folder,centre,radius):

      wcs = WCS(folder+'meanmass.fits')
      mass = fits.open(folder+'meanmass.fits')[0].data.T
      sn   = fits.open(folder+'snmass.fits')[0].data.T
      std = fits.open(folder+'stdmass.fits')[0].data.T
      
      x = np.arange(mass.shape[0])+0.5
      y = np.arange(mass.shape[1])+0.5
      x, y = np.meshgrid(x,y)
      
      ra, dec = wcs.all_pix2world(x, y, 1)
      dra, ddec = ra-centre[0], dec-centre[1]
      dra  *= 3600.	
      ddec *= 3600.
      dist  = ang_sep(centre[0],centre[1],ra,dec).T*3600
      
      mask = dist < radius
      
      return mass[mask].sum(),std[mask].sum(),np.median(sn[mask])


folder = '../main/grid1.0/'

z = 0.397
dl  = cosmo.angular_diameter_distance(z).value 	# in kpc
kpcscale = dl*np.deg2rad(1.0/3600.0)*1000.0

r_100 = 100./kpcscale
r_200 = 200./kpcscale

S1c = [64.011542, -24.093647]
S2c = [64.016187, -24.075967]
S3c = [64.031547, -24.048917]
S4c = [64.061442, -24.053878]
S1p = [64.134196, -24.088425]

S1c_mass200 = []
S2c_mass200 = []
S3c_mass200 = []
S4c_mass200 = []
S1p_mass200 = []     

S1c_std200 = []
S2c_std200 = []
S3c_std200 = []
S4c_std200 = []
S1p_std200 = []     

S1c_sn200 = []
S2c_sn200 = []
S3c_sn200 = []
S4c_sn200 = []
S1p_sn200 = []     

S1c_mass100 = []
S2c_mass100 = []
S3c_mass100 = []
S4c_mass100 = []
S1p_mass100 = []     

S1c_std100 = []
S2c_std100 = []
S3c_std100 = []
S4c_std100 = []
S1p_std100 = []     

S1c_sn100 = []
S2c_sn100 = []
S3c_sn100 = []
S4c_sn100 = []
S1p_sn100 = []     


for j in range():
      
      folder = 'main_'+str(j)
      
      #############################
      m,std,sn = aperture_mass(folder,S1c,r_100)

      S1c_mass100 = np.append(S1c_mass100,m)
      S1c_std100  = np.append(S1c_std100,std)
      S1c_sn100   = np.append(S1c_sn100,sn)
      
      m,std,sn = aperture_mass(folder,S1c,r_200)

      S1c_mass200 = np.append(S1c_mass200,m)
      S1c_std200  = np.append(S1c_std200,std)
      S1c_sn200   = np.append(S1c_sn200,sn)
      #############################
      
      m,std,sn = aperture_mass(folder,S2c,r_100)

      S2c_mass100 = np.append(S2c_mass100,m)
      S2c_std100  = np.append(S2c_std100,std)
      S2c_sn100   = np.append(S2c_sn100,sn)
      
      m,std,sn = aperture_mass(folder,S2c,r_200)

      S2c_mass200 = np.append(S2c_mass200,m)
      S2c_std200  = np.append(S2c_std200,std)
      S2c_sn200   = np.append(S2c_sn200,sn)

      #############################

      m,std,sn = aperture_mass(folder,S3c,r_100)

      S3c_mass100 = np.append(S3c_mass100,m)
      S3c_std100  = np.append(S3c_std100,std)
      S3c_sn100   = np.append(S3c_sn100,sn)
      
      m,std,sn = aperture_mass(folder,S1c,r_200)

      S3c_mass200 = np.append(S3c_mass200,m)
      S3c_std200  = np.append(S3c_std200,std)
      S3c_sn200   = np.append(S3c_sn200,sn)

      m,std,sn = aperture_mass(folder,S1c,r_100)

      #############################

      S4c_mass100 = np.append(S4c_mass100,m)
      S4c_std100  = np.append(S4c_std100,std)
      S4c_sn100   = np.append(S4c_sn100,sn)
      
      m,std,sn = aperture_mass(folder,S1c,r_200)

      S4c_mass200 = np.append(S4c_mass200,m)
      S4c_std200  = np.append(S4c_std200,std)
      S4c_sn200   = np.append(S4c_sn200,sn)
