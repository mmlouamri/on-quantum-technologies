from qiskit.circuit.library import QFT
from qiskit.visualization import plot_bloch_multivector
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from get_statevector import get_statevector
from get_results import get_results
from IPython.display import display

def qpe_explain(nb_qubits, theta):
    svs = []
    
    control = QuantumRegister(nb_qubits - 1, name="c")
    target = QuantumRegister(1, name="ev")
    result = ClassicalRegister(nb_qubits - 1, name="r")
    qc = QuantumCircuit(control, target, result)
    qc.x(target)
    qc.barrier()

    for i in range(control.size):
        qc.h(control[i])
            
    svs.append(get_statevector(qc))
    qc.barrier()

    
    for i in range(control.size):
        qc.cp(2**i * theta, control[i], target)
        svs.append(get_statevector(qc))
    qc.barrier()


    iqft = QFT(num_qubits=control.size, approximation_degree=0, do_swaps=True, inverse=True, insert_barriers=True, name='QFT')
    qc.compose(iqft, qubits=[i for i in range(control.size)], inplace=True)
    svs.append(get_statevector(qc))
    qc.barrier()

    
    qc.measure(range(control.size), range(result.size))

    display(qc.draw(output="mpl"))
    

    res = get_results(qc)
    dec_res = int(res.most_frequent(), 2)
    base_angle = 1 / 2 **(control.size - 1)
    
    print("The measurement results are:")
    print(res)
    print()
    
    if len(res.keys()) == 1:
        print(f"Theta was precisely measured to be: {dec_res * base_angle}π")
    else:
        print(f"Theta was estimated to be close to: {dec_res * base_angle}π")
        
    print("\n\n\nThe Algorithm steps:\n\n\n")
    
    print("The state after the initialization step")
    display(plot_bloch_multivector(svs[0]))
    
    for i in range(control.size):
        print(f"The state after the {i+1}-th CU")
        display(plot_bloch_multivector(svs[i + 1]))
    
    print("The state after the Inverse Quantum Fourier Transform")
    display(plot_bloch_multivector(svs[-1]))
    
    print(f"The bases angle is: {base_angle}π, and the decimal result is: {dec_res}")
    print(f"So the result is: {dec_res} * {base_angle}π = {dec_res * base_angle}π")