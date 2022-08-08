import numpy as np
from qiskit import QuantumCircuit

def get_circuit(qubit_state):
    if type(qubit_state) is not str:
        raise TypeError("TypeError: qubit_state should be a string of 0, 1, +, -, a")
        
    if len(qubit_state) == 0:
          raise ValueError("Empty qubit_state")
            
    nb_qubits = len(qubit_state)
    qc = QuantumCircuit(nb_qubits)
    for i, q_state in enumerate(qubit_state):
        curr_qubit = nb_qubits - i - 1
        if q_state == "1":
            qc.x(curr_qubit)
        if q_state == "+":
            qc.h(curr_qubit)
        if q_state == "-":
            qc.h(curr_qubit)
            qc.z(curr_qubit)
        if q_state == "a": # arbitrary 
            qc.ry(np.random.rand() % (2 * np.pi), curr_qubit)
            qc.rz(np.random.rand() % (2 * np.pi), curr_qubit)
    return qc