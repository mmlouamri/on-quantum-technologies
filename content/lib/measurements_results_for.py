from get_circuit import get_circuit
from get_results import get_results

def measurement_results_for(qubit_state):
    circuit = get_circuit(qubit_state)
    circuit.measure_all()
    return get_results(circuit)