from qiskit.visualization import plot_bloch_multivector
import imageio.v2 as imageio
from time import time
import ipywidgets as widgets
import numpy as np

from get_fbasis_statevector import get_fbasis_statevectors
from IPython.display import display

def animate_fbasis(nb_qbits):
    big_n = 2**nb_qbits
    statevectors = get_fbasis_statevectors(nb_qbits)
    
    filename = f'./images/tmp/final_{str(time())}.gif'
    
    images = []
    
    for i in range(big_n):
        plot_bloch_multivector(statevectors[i]).savefig('./images/tmp/temp_file.png')
        images.append(imageio.imread('./images/tmp/temp_file.png'))
        
    imageio.mimsave(f'{filename}', images, duration = 0.5)
    
    
    display(widgets.HTML(f'<img src="{filename}" width="{np.min([200 * nb_qbits, 600])}"/>'))