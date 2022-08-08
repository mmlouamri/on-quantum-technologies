from qiskit import Aer, execute

def get_statevector(circuit):
    be_sv = Aer.get_backend("statevector_simulator")
    job = execute(circuit, be_sv, optimization_level = 0)
    precision = 3
    current_quantum_state = job.result().get_statevector(circuit, precision).data
    
    return current_quantum_state