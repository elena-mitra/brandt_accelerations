import numpy as np
from astropy import units as u

def calc_astrometric_acceleration(plx,
                                  pmrahip,
                                  pmragaia,
                                  pmrahg,
                                  pmdechip,
                                  pmdecgaia,
                                  pmdechg,
                                  rahipepoch,
                                  ragaiaepoch,
                                  dechipepoch,
                                  decgaiaepoch):
    '''returns astrometric acceleration'''

    # Converts parallax to parsec
    d = plx.to(u.parsec, equivalencies=u.parallax())

    acc_ra_num = (pmragaia - pmrahg)* d  # ∆µ (in mas/yr) * parallax (in parsec) converted to (mas pc/yr)
    acc_ra_den = (ragaiaepoch - rahipepoch) / 2
    acc_dec_num = (pmdecgaia - pmdechg) * d
    acc_dec_den = (decgaiaepoch - dechipepoch) / 2
    # Conversion to acceleration units m/s/yr
    acc_ra_num = acc_ra_num.to(u.m / u.second, equivalencies=u.dimensionless_angles())
    acc_dec_num = acc_dec_num.to(u.m / u.second, equivalencies=u.dimensionless_angles())

    acc_ra = acc_ra_num / acc_ra_den
    acc_dec = acc_dec_num / acc_dec_den

    # Vector add acceleration components, and convert to liner units using 4.74
    astrometric_acc = np.sqrt(acc_ra ** 2 + acc_dec ** 2)
    return astrometric_acc
