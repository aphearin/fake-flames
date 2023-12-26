"""
"""
import os

import numpy as np

from ..read_fire_sfh import read_orig_fire_data

_THIS_DRNAME = os.path.dirname(os.path.abspath(__file__))
_SRC_DRN = os.path.dirname(os.path.dirname(_THIS_DRNAME))
TEST_DATA_DRN = os.path.join(os.path.join(_SRC_DRN, "tests"), "testing_data")


def test_read_fire_sfh_mah():
    """Test that the data stored in data_m12f.npz is reproduced when
    the read_fire_sfh_mah function reads and processes the original source data"""
    m12f_history_data_fn = os.path.join(TEST_DATA_DRN, "data_m12f.npz")
    m12f_test_data = np.load(m12f_history_data_fn)

    m12f_orig_data_fn = os.path.join(TEST_DATA_DRN, "orig_data_m12f.dat")
    m12f_test_data = read_orig_fire_data(m12f_orig_data_fn)

    gen = zip(m12f_test_data, m12f_test_data)
    for orig_array, processed_array in gen:
        assert np.allclose(orig_array, processed_array, rtol=1e-3)
