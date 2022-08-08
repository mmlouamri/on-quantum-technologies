from qiskit.visualization import plot_bloch_multivector
from get_circuit import get_circuit
from get_statevector import get_statevector
from IPython.display import display

def draw_qubits(qubit_state):
    circuit = get_circuit(qubit_state)
    statevector = get_statevector(circuit)
    display(plot_bloch_multivector(statevector))