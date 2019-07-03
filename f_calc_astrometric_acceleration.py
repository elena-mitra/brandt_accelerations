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

    #####################################################################
    # The following code converts velocities from angular to linear units
    # and calculates the accelerations.
    # The relationship between transverse velocity and proper motion is:
    # vT  = 4.74 d μ
    # where vT is the transverse velocity (measured in km/sec),
    # d is the distance in parsecs,
    # μ is the proper motion in arc seconds per year.
    # The numerical factor 4.74 is the conversion between angular
    # and transverse velocity in proper motion:
    # (km/sec) / [parsecs * arcsec/yr]
    # = (km/pc) / [(sec/yr) * (arcsec/radian)]
    # = (206,265 * 149.6 X 10^6) / (3.156  X 10^7 * 206,265)
    # = 4.74
    #####################################################################

    acc_ra_num = (pmragaia - pmrahg) * 4.74 * d  # ∆µ (in mas/yr) * parallax (in parsec) converted to (mas pc/yr)
    acc_ra_den = (ragaiaepoch - rahipepoch) / 2
    acc_dec_num = (pmdecgaia - pmdechg) * 4.74 * d
    acc_dec_den = (decgaiaepoch - dechipepoch) / 2
    acc_ra = acc_ra_num / acc_ra_den
    acc_dec = acc_dec_num / acc_dec_den

    # Vector add acceleration components, and convert to liner units using 4.74
    astrometric_acc = np.sqrt(acc_ra ** 2 + acc_dec ** 2)
    return astrometric_acc
