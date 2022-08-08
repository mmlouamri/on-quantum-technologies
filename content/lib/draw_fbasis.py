from qiskit.visualization import plot_bloch_multivector
from IPython.display import display, Latex

from get_fbasis_statevector import get_fbasis_statevectors
from dec_to_bin import dec_to_bin

def draw_fbasis(nb_qbits):
    statevectors = get_fbasis_statevectors(nb_qbits)
    for i in range(2**nb_qbits):
        display(Latex(f"$\ket{{\widetilde{{{dec_to_bin(i, nb_qbits)}}}}} = QFT \ket{{{dec_to_bin(i, nb_qbits)}}} \equiv QFT \ket{{{i}}} $"))
        display(plot_bloch_multivector(statevectors[i]))
        print()
    