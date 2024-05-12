import math

INPUT : list[float] = [1.0, 1.0, 1.0, 1.0, -1.0, -1.0, -1.0, -1.0]
OUTPUT : list[float] = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

Pair = tuple[float, int]

FList : list[Pair] = [
	(0.0, 0),
	(0.0, 1),
	(0.0, 2),
	(0.0, 3),
	(0.0, 4),
	(0.0, 5),
	(0.0, 6),
	(0.0, 7),
]

# Square wave function
def square(x : float) -> float:
	return math.copysign(1.0, math.cos(x*math.pi))

# Calculate fourier magnitudes
for i, p in enumerate(FList):
	#print("Frequency: ", p[1])
	sum : float = 0.0
	
	for j, v in enumerate(INPUT):
		val : float = square((float(j)/7.0)*p[1])
		sum += val*v
		#print(j, ": ", val)
		pass
	
	sum = sum/len(INPUT)
	FList[i] = (sum, p[1])
	#print("Sum: ", sum)
	#print("\n")
	pass

# Calculate fourier series results
for j, v in enumerate(OUTPUT):
	for i, p in enumerate(FList):
		OUTPUT[j] += square((float(j)/7.0)*p[1])*p[0]
		pass
	pass

# Print results
print("-----  INPUT")
print(INPUT)
print("\n-----  Square Wave Fourier Values (Magnitude, Frequency)")
print(FList)
print("\n-----  OUTPUT (To test transform works correctly)")
print(OUTPUT)
