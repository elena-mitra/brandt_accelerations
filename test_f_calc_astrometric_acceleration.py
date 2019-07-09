########################################################################
## This script is a test for f_calc_astrometric_acceleration function ##
########################################################################

import numpy as np
from astropy import units as u
from f_calc_astrometric_acceleration import calc_astrometric_acceleration

######################
# Test for HD 159062
######################
def test_calcacc_HD159062():
    # HD 159062 data, should return an astrometric acceleration of 24.9 m/s/yr

    plx = 46.118473*u.mas
    pmrahip = 174.259960*u.mas/u.yr #mas/yr
    pmragaia = 169.747220*u.mas/u.yr #mas/yr
    pmrahg = 172.403370*u.mas/u.yr #mas/yr
    pmdechip = 75.398400*u.yr #mas/yr
    pmdecgaia = 77.163860*u.mas/u.yr #mas/yr
    pmdechg = 75.815170*u.mas/u.yr #mas/yr
    rahipepoch = 1991.197277*u.yr #yr
    ragaiaepoch = 2015.688858*u.yr #yr
    dechipepoch = 1991.122985*u.yr #yr
    decgaiaepoch = 2015.773882*u.yr #yr
    calculated_acceleration = calc_astrometric_acceleration(plx,
                                  pmrahip,
                                  pmragaia,
                                  pmrahg, 
                                  pmdechip, 
                                  pmdecgaia, 
                                  pmdechg, 
                                  rahipepoch,
                                  ragaiaepoch,
                                  dechipepoch,
                                  decgaiaepoch)

    expected_acceleration = 24.9 * u.m/u.s/u.yr
    assert np.isclose(calculated_acceleration.value, expected_acceleration.value, atol=.2)
    print(np.isclose(calculated_acceleration.value, expected_acceleration.value, atol=.2))


test_calcacc_HD159062()

#####################
# Test for HD 68017
#####################

def test_calcacc_HD68017():

    plx = 46.327320*u.mas
    pmrahip = -461.601650*u.mas/u.yr #mas/yr
    pmragaia = -484.315120*u.mas/u.yr #mas/yr
    pmrahg = -471.298460*u.mas/u.yr #mas/yr
    pmdechip = -644.467300*u.yr #mas/yr
    pmdecgaia = -642.974370*u.mas/u.yr #mas/yr
    pmdechg = -639.023440*u.mas/u.yr #mas/yr
    rahipepoch = 1991.069888*u.yr #yr
    ragaiaepoch = 2015.762001*u.yr #yr
    dechipepoch = 1991.335952*u.yr #yr
    decgaiaepoch = 2015.713990*u.yr #yr
    calculated_acceleration = calc_astrometric_acceleration(plx,
                                  pmrahip,
                                  pmragaia,
                                  pmrahg,
                                  pmdechip,
                                  pmdecgaia,
                                  pmdechg,
                                  rahipepoch,
                                  ragaiaepoch,
                                  dechipepoch,
                                  decgaiaepoch)
    expected_acceleration = 113.8 * u.m/u.s/u.yr
    assert np.isclose(calculated_acceleration.value, expected_acceleration.value, atol=1)
    print(np.isclose(calculated_acceleration.value, expected_acceleration.value, atol=1))


test_calcacc_HD68017()

#####################
# Test for Gl 86
#####################

def test_calcacc_Gl86():

    plx = 92.715950*u.mas
    pmrahip = 2091.883000*u.mas/u.yr #mas/yr
    pmragaia = 2124.853000*u.mas/u.yr #mas/yr
    pmrahg = 2106.955000*u.mas/u.yr #mas/yr
    pmdechip = 654.345200*u.yr #mas/yr
    pmdecgaia = 638.091550*u.mas/u.yr #mas/yr
    pmdechg = 641.619450*u.mas/u.yr #mas/yr
    rahipepoch = 1991.226010*u.yr #yr
    ragaiaepoch = 2015.771176*u.yr #yr
    dechipepoch = 1991.377859*u.yr #yr
    decgaiaepoch = 2015.753104*u.yr #yr
    calculated_acceleration = calc_astrometric_acceleration(plx,
                                  pmrahip,
                                  pmragaia,
                                  pmrahg,
                                  pmdechip,
                                  pmdecgaia,
                                  pmdechg,
                                  rahipepoch,
                                  ragaiaepoch,
                                  dechipepoch,
                                  decgaiaepoch)
    expected_acceleration = 76.5 * u.m/u.s/u.yr
    assert np.isclose(calculated_acceleration.value, expected_acceleration.value, atol=.5)
    print(np.isclose(calculated_acceleration.value, expected_acceleration.value, atol=.5))


test_calcacc_Gl86()

print("astrometric acceleration test complete!")