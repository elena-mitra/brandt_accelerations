import numpy as np
from astropy import units as u
from f_calc_astrometric_acceleration import calc_astrometric_acceleration

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

    expected_acceleration = 24.9 * u.mas*u.pc/u.yr**2
    assert np.isclose(calculated_acceleration.value, expected_acceleration.value, atol=0.9)
    print(np.isclose(calculated_acceleration.value, expected_acceleration.value, atol=0.9))
    print("it's 5 o'clock")


test_calcacc_HD159062()

