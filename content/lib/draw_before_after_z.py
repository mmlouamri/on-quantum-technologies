from get_circuit import get_circuit
from get_statevector import get_statevector
from qiskit.visualization import plot_bloch_multivector
from IPython.display import display


def draw_before_after_z(qubit_state, qubit=[0]):
    circuit = get_circuit(qubit_state)
    print("Before the Z-Gate is applied:")
    statevector = get_statevector(circuit)
    display(plot_bloch_multivector(statevector))
    
    if type(qubit) is not list:
        qubit = [qubit]
    for q in qubit:
        circuit.z(q)
        
    print("After the Z-Gate is applied:")
    statevector = get_statevector(circuit)
    display(plot_bloch_multivector(statevector))