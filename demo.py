import DevPricing.MonteCarlo as mc
import DevPricing.BlackScholes as bs


print(f'Analytic Solution: {bs.EuroCall(420, 400, 1, 0.2, 0.01)}')
print(f'n=10000: {mc.EuroCall(420, 400, 1, 0.2, 0.01, 10000)}')
print(f'n=100000: {mc.EuroCall(420, 400, 1, 0.2, 0.01, 100000)}')
print(f'n=1000000: {mc.EuroCall(420, 400, 1, 0.2, 0.01, 1000000)}')