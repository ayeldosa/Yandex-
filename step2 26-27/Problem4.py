import sys
import random

n_machines = 10
budget = 200

successes = [0] * n_machines
failures = [0] * n_machines

for _ in range(budget):
    # Thompson Sampling
    sampled_p = [random.betavariate(successes[i]+1, failures[i]+1) for i in range(n_machines)]
    machine = sampled_p.index(max(sampled_p))
    
    # Вывод строго по протоколу
    print(machine)
    sys.stdout.flush()
    
    # Чтение результата интерактора
    result = int(input())
    
    # Обновляем статистику
    if result == 1:
        successes[machine] += 1
    else:
        failures[machine] += 1