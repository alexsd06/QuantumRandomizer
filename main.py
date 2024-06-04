import os
from dotenv import load_dotenv
from qiskit import QuantumCircuit, transpile, assemble
from qiskit_aer import Aer
from qiskit.visualization import plot_histogram
from qiskit_ibm_runtime import QiskitRuntimeService, SamplerV2 as Sampler

load_dotenv()
API_TOKEN = os.getenv("API_TOKEN")

service = QiskitRuntimeService(channel="ibm_quantum", token=API_TOKEN)
print(service.backends())
backend = service.least_busy(operational=True, simulator=False)
print("Chosen backend:", backend)

qc = QuantumCircuit(1, 1)
qc.h(0)
qc.measure([0], [0])
print(qc)
input("Press enter to continue...")
# qc.draw(output='mpl')
#simulator = Aer.get_backend('qasm_simulator')
sampler = Sampler(backend)
result = job = sampler.run([qc], shots=1).result()[0].data.c.array[0][0]
if result == 0:
    print("The winner is Toma!")
elif result == 1:
    print("The winner is Alex!")
else:
    print("How did we even get to this branch!?")
