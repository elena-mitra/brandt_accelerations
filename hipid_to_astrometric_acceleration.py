########################################################
## This script takes user input HIPID and returns the ##
## astrometric aceleration in m/s/yr                  ##
########################################################
import pandas as pd
from astropy import units as u

# downloads data: Brandt Hipparcos-Gaia Catalog of Accelerations
catalog = pd.read_csv('Full-Catalog_WDS-HIRES-New-Chisq.csv')

# takes HIP ID user input, in this case: HD_159062/HIP_85653
hipid = 85653

# filters for the input hipid
catalog_select = catalog.hip_id== hipid
hip_select = catalog.loc[catalog_select,['hip_id',
                                         'radial_velocity',
                                         'pmra_hip',
                                         'pmdec_hip',
                                         'pmra_gaia',
                                         'pmdec_gaia',
                                         'pmra_hg',
                                         'pmdec_hg',
                                         'parallax_gaia',
                                         'epoch_ra_gaia',
                                         'epoch_dec_gaia',
                                         'epoch_ra_hip',
                                         'epoch_dec_hip']]

# Pulls values from hip_id-filtered Brandt Catalog (i.e. hip_select)
# for acceleration calculation and converts to Astropy units

pmrahip = hip_select['pmra_hip'].iloc[0]*u.mas/u.yr #mas/yr
pmragaia = hip_select['pmra_gaia'].iloc[0]*u.mas/u.yr #mas/yr
pmrahg = hip_select['pmra_hg'].iloc[0]*u.mas/u.yr #mas/yr
pmdechip = hip_select['pmdec_hip'].iloc[0]*u.mas/u.yr #mas/yr
pmdecgaia = hip_select['pmdec_gaia'].iloc[0]*u.mas/u.yr #mas/yr
pmdechg = hip_select['pmdec_hg'].iloc[0]*u.mas/u.yr #mas/yr

rahipepoch = hip_select['epoch_ra_hip'].iloc[0]*u.yr #yr
ragaiaepoch = hip_select['epoch_ra_gaia'].iloc[0]*u.yr #yr
dechipepoch = hip_select['epoch_dec_hip'].iloc[0]*u.yr #yr
decgaiaepoch = hip_select['epoch_ra_gaia'].iloc[0]*u.yr #yr

plx = (hip_select['parallax_gaia'].iloc[0])*u.mas #parallax in mas

# calls function script "f_calc_astrometric_acceleration" which contains
# the acceleration calculation
from f_calc_astrometric_acceleration import calc_astrometric_acceleration

# executes the acceleration calculation function
print(calc_astrometric_acceleration(plx,
                                  pmrahip,
                                  pmragaia,
                                  pmrahg,
                                  pmdechip,
                                  pmdecgaia,
                                  pmdechg,
                                  rahipepoch,
                                  ragaiaepoch,
                                  dechipepoch,
                                  decgaiaepoch))

