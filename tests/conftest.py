# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

import pytest

from pywaterinfo.waterinfo import Waterinfo

# use a session for VMM that can be used among tests
vmm_client = (
    "MzJkY2VlY2UtODI2Yy00Yjk4LTljMmQtYjE2OTc4ZjBjYTZhOj"
    "RhZGE4NzFhLTk1MjgtNGI0ZC1iZmQ1LWI1NzBjZThmNGQyZA=="
)

hic_client = ""  # TODO - add test token


@pytest.fixture(scope="module")
def vmm_connection():
    return Waterinfo("vmm", token=vmm_client)


@pytest.fixture(scope="module")
def hic_connection():
    return Waterinfo("hic", token=hic_client)


@pytest.fixture(scope="module")
def df_timeseries(vmm_connection):
    return vmm_connection.get_timeseries_values(
        78124042, start="20190501", end="20190502"
    )
