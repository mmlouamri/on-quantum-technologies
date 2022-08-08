from qiskit import Aer, execute

def get_results(qc, shots=1000):
    job = execute(qc, Aer.get_backend("qasm_simulator"), shots=shots)
    counts = job.result().get_counts(qc)
    
    return counts