import numpy as np
from scipy.fft import ifft

def get_fbasis_statevectors(nb_qbits):
    big_n = 2**nb_qbits
    ret = np.zeros((big_n, big_n), dtype=complex)
    for i in range(big_n):
        arr = np.zeros(big_n)
        arr[i] =  1
        ret[i] = ifft(arr, norm = "ortho")
    return ret