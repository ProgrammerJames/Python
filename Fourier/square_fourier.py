import math

Pair = tuple[float, int]

# Square wave function (range -1..1)
def square(x : float) -> float:
	return math.copysign(1.0, math.cos(x*math.pi))

# Square wave function using bit shifting (range: 0..1)
def square_b(x : int, mx : int) -> float:
	return (x >> mx) & 1

# Calculate fourier series
def build_fourier_series(input : list[float]) -> list[Pair]:
	f_list : list[Pair] = [(0.0, 0)]*(len(input))
	count : float = float(len(input)-1)
	
	for i, p in enumerate(f_list):
		#print("Frequency: ", p[1])
		sum : float = 0.0
		
		for j, v in enumerate(input):
			val : float = square((float(j)/count)*i)
			sum += val*v
			#print(j, ": ", val)
			pass
		
		sum = sum/len(input)
		f_list[i] = (sum, i)
		#print("Sum: ", sum)
		#print("\n")
		pass
	return f_list

# Calculate fourier output
def calculate_result(f_list : list[Pair]) -> list[float]:
	output : list[float] = [0.0]*(len(f_list))
	count : float = float(len(f_list)-1)
	
	for j, v in enumerate(output):
		for i, p in enumerate(f_list):
			output[j] += square((float(j)/count)*p[1])*p[0]
		pass
	
	return output

# Perform transformation test for input
def test_fourier(input : list[float]):
	# Calculate fourier magnitudes
	f_list = build_fourier_series(input)
	
	# Calculate fourier series results
	output = calculate_result(f_list)
	
	# Print results
	print("")
	print("-----  INPUT")
	print(input)
	print("\n-----  Square Wave Fourier Values (Magnitude, Frequency)")
	print(f_list)
	print("\n-----  OUTPUT (To test transform works correctly)")
	print(output)
	print("")
	
	assert input == output


# Test Case
test_fourier([1.0, 1.0, 1.0, 1.0, -1.0, -1.0, -1.0, -1.0])
