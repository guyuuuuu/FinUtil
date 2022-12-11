import DevPricing.MonteCarlo as mc
import DevPricing.BlackScholes as bs

print('Problem 1, 1-3')
print(f'Euro Call Analytic Solution: {bs.EuroCall(420, 400, 1, 0.2, 0.01)}')
print(f'n=10000: {mc.EuroCall(420, 400, 1, 0.2, 0.01, 10000)}')
print(f'n=100000: {mc.EuroCall(420, 400, 1, 0.2, 0.01, 100000)}')
print(f'n=1000000: {mc.EuroCall(420, 400, 1, 0.2, 0.01, 1000000)}')
print()
print('Problem 1, 4-5, 7-8')
print(f'Binary Analytic Solution: {bs.BinaryCall(1, 420, 400, 1, 0.2, 0.01)}')
print(f'n=10000: {mc.BinaryCall(1, 420, 400, 1, 0.2, 0.01, 10000)}')
print(f'n=100000: {mc.BinaryCall(1, 420, 400, 1, 0.2, 0.01, 100000)}')
print(f'n=1000000: {mc.BinaryCall(1, 420, 400, 1, 0.2, 0.01, 1000000)}')