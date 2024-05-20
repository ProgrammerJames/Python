import math

Pair = tuple[float, int]
Series = list[Pair]

# Square wave function (range -1..1)
def square(x : float) -> float:
	return math.copysign(1.0, math.cos(x*math.pi))

# Square wave function using bit shifting (range: 0..1)
def square_b(x : int, mx : int) -> float:
	return float((x >> mx) & 1)

def magn(p : Pair) -> float:
	return abs(p[0])

# Calculate fourier series
def build_fourier_series(input : list[float]) -> Series:
	f_list : list[Pair] = [(0.0, 0)]*(len(input))
	count : float = float(len(input)-1)
	
	f_sum = 0.0
	
	for i, p in enumerate(f_list):
		#print("Frequency: ", p[1]) # DEBUG
		#print("Frequency: ", i) # DEBUG
		sum : float = 0.0
		
		for j, v in enumerate(input):
			val : float = square((float(j)/count)*i)
			sum += val*v
			#print(j, ": ", val, " (", (val*v), ")") # DEBUG
			pass
		
		sum = sum/len(input)
		f_sum += abs(sum)
		f_list[i] = (sum, i)
		#print("Sum: ", sum) # DEBUG
		#print("\n") # DEBUG
		pass
	
	#f_list[0] = (f_list[0][0]-8.0, f_list[0][1])
	
	return f_list

# Calculate fourier output (for square waves with range -1..1)
def calculate_result(series : Series) -> list[float]:
	f_list : list[Pair] = series
	output : list[float] = [0.0]*(len(f_list))
	count : int = float(len(f_list)-1)
	
	for j, v in enumerate(output):
		for i, p in enumerate(f_list):
			val = square((float(j)/count)*p[1])*p[0]
			output[j] += val
		pass
	
	return output

# Calculate fourier output (for square waves with range 0..1)
def calculate_psign_result(series : Series) -> list[float]:
	f_list : list[Pair] = series
	output : list[float] = [0.0]*(len(f_list))
	count : int = float(len(f_list)-1)
	
	for j, v in enumerate(output):
		for i, p in enumerate(f_list):
			val = (square((float(j)/count)*p[1])+1.0)*p[0]
			output[j] += val*0.5
		pass
	
	return output

def adjust_sample_range(series : Series) -> Series:
	f_sum : float = 0.0
	
	for i, v in enumerate(series):
		f_sum += v[0]
		series[i] = (v[0]*2.0, v[1])
	
	series[0] = (series[0][0]-f_sum, series[0][1])
	
	return series

# Perform transformation test for input
def test_fourier(input : list[float]):
	# Calculate fourier magnitudes
	f_list = build_fourier_series(input)
	
	# Adjust series so that input can be produced with square wave of range 0..1
	f_list = adjust_sample_range(f_list)
	
	# Calculate fourier series results (for square waves with range 0..1)
	output = calculate_psign_result(f_list)
	
	# Print results
	if (True):
		print("")
		print("-----  INPUT")
		print(input)
		print("\n-----  Square Wave Fourier Values (Magnitude, Frequency)")
		print(f_list)
		print("\n-----  OUTPUT (To test transform works correctly)")
		print(output)
		print("")
	
	assert input == output

# Test Transformation Cases
test_fourier([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
test_fourier([1.0, 1.0, 1.0, 1.0, -1.0, -1.0, -1.0, -1.0])
test_fourier([0.0, 0.0, 1.0, 1.0, 0.0, 0.0, -1.0, -1.0])
test_fourier([1.0, 1.0, 1.0, 2.0, -1.0, -1.0, -1.0, -1.0])
test_fourier([-2.0, -3.0, -1.0, -1.0, -2.0, 0.0, 0.0, 2.0])
test_fourier([-9.0, 9.0, 2.0, 9.0, -6.0, -5.0, 10.0, -5.0])
test_fourier([0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0])

# Test Series Arithmetic Cases
# TODO
