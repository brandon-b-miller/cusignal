# Copyright (c) 2019-2020, NVIDIA CORPORATION.
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import pytest
import cupy as cp
import numpy as np


# Fixtures with (scope="session") will execute once
# and be shared will all tests that need it.

# Generate data for using linspace
@pytest.fixture(scope="session")
def linspace_data_gen():
    def _generate(start, stop, num_samps, endpoint=False):

        cpu_time = np.linspace(start, stop, num_samps, endpoint)
        cpu_sig = np.cos(-(cpu_time ** 2) / 6.0)
        gpu_sig = cp.asarray(cpu_sig)

        return cpu_sig, gpu_sig

    return _generate


# Generate data for using linspace
@pytest.fixture(scope="session")
def linspace_range_gen():
    def _generate(num_samps):

        cpu_sig = np.arange(num_samps) / num_samps
        gpu_sig = cp.asarray(cpu_sig)

        return cpu_sig, gpu_sig

    return _generate


# Generate array with random data
@pytest.fixture(scope="session")
def rand_data_gen():
    def _generate(num_samps):

        cpu_sig = np.random.rand(num_samps)
        gpu_sig = cp.asarray(cpu_sig)

        return cpu_sig, gpu_sig

    return _generate


# Generate array with random complex data
@pytest.fixture(scope="session")
def rand_complex_data_gen():
    def _generate(num_samps):

        cpu_sig = np.random.rand(num_samps) + 1j * np.random.rand(num_samps)
        gpu_sig = cp.asarray(cpu_sig)

        return cpu_sig, gpu_sig

    return _generate


# Generate 2d array with random data
@pytest.fixture(scope="session")
def rand_2d_data_gen():
    def _generate(num_samps):

        cpu_sig = np.random.rand(num_samps, num_samps)
        gpu_sig = cp.asarray(cpu_sig)

        return cpu_sig, gpu_sig

    return _generate


# Generate time array with linspace
@pytest.fixture(scope="session")
def time_data_gen():
    def _generate(start, stop, num_samps):

        cpu_sig = np.linspace(start, stop, num_samps)
        gpu_sig = cp.asarray(cpu_sig)

        return cpu_sig, gpu_sig

    return _generate


# Generate input for lombscargle
@pytest.fixture(scope="session")
def lombscargle_gen(rand_data_gen):
    def _generate(num_in_samps, num_out_samps):

        A = 2.0
        w = 1.0
        phi = 0.5 * np.pi
        frac_points = 0.9  # Fraction of points to select

        r, _ = rand_data_gen(num_in_samps)
        cpu_x = np.linspace(0.01, 10 * np.pi, num_in_samps)

        cpu_x = cpu_x[r >= frac_points]

        cpu_y = A * np.cos(w * cpu_x + phi)

        cpu_f = np.linspace(0.01, 10, num_out_samps)

        gpu_x = cp.asarray(cpu_x)
        gpu_y = cp.asarray(cpu_y)
        gpu_f = cp.asarray(cpu_f)

        return cpu_x, cpu_y, cpu_f, gpu_x, gpu_y, gpu_f

    return _generate
