"""
"""
import numpy as np


def read_orig_fire_data(fn):
    """Read original fire data and return history arrays

    This dummy implementation should be deleted and replaced with actual code

    Parameters
    ----------
    fname : string
        Filename of data originally downloaded from FIRE team

    Returns
    -------
    stellar_age_bins : ndarray, shape (n_bins+1,)

    stellar_age_bincounts : ndarray, shape (n_bins,)

    sfr_redshifts : ndarray, shape (n_bins,)

    sfr_times : ndarray, shape (n_bins,)

    sfr_values : ndarray, shape (n_bins,)

    halo_mass_redshifts : ndarray, shape (n_bins,)

    halo_mass_values : ndarray, shape (n_bins,)

    """
    n_bins = 512
    stellar_age_bins = np.empty(n_bins + 1)
    stellar_age_bincounts = np.empty(n_bins)
    sfr_redshifts = np.empty(n_bins)
    sfr_times = np.empty(n_bins)
    sfr_values = np.empty(n_bins)
    halo_mass_redshifts = np.empty(n_bins)
    halo_mass_values = np.empty(n_bins)

    return (
        stellar_age_bins,
        stellar_age_bincounts,
        sfr_redshifts,
        sfr_times,
        sfr_values,
        halo_mass_redshifts,
        halo_mass_values,
    )
