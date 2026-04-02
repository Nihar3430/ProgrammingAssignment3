import time
from pathlib import Path
import matplotlib.pyplot as plt
from main import parse_input, hvlcs

TESTS_DIRRectory = Path("tests")

x_vals = []
y_vals = []

for i in range(1, 11):
    file_path = TESTS_DIRRectory / f"example{i}.in"
    input_text = file_path.read_text()

    value, A, B = parse_input(input_text)

    runs = []
    for _ in range(20):
        start = time.perf_counter()
        hvlcs(value, A, B)
        end = time.perf_counter()
        runs.append(end - start)

    avg_time = sum(runs) / len(runs)

    x_vals.append(len(A))
    y_vals.append(avg_time)

    print(f"example{i}.in -> length {len(A)}, runtime {avg_time:.8f} seconds")

plt.plot(x_vals, y_vals, marker="o")
plt.xlabel("Input String Length")
plt.ylabel("Average Runtime (seconds)")
plt.title("Runtime of HVLCS vs Input Size")
plt.tight_layout()
plt.show()