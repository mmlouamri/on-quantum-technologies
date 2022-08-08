from qiskit import QuantumCircuit
from get_statevector import get_statevector
from IPython.display import display
from qiskit.visualization import plot_bloch_multivector
import numpy as np


def draw_phasekick():
    qc = QuantumCircuit(2)
    qc.h(0)
    qc.x(1)
    statevector1 = get_statevector(qc)
    qc.cp(np.pi / 4, 0, 1)
    statevector2 = get_statevector(qc)
    print("The Initial State:")
    display(plot_bloch_multivector(statevector1))
    print("The Final State:")
    display(plot_bloch_multivector(statevector2))