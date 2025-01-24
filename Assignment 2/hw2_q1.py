"""
Write a program that will:
- Ask the user to input a value for the frequency
- Ask the user to input a value for the duration of the sound wave
- Calculate the value of the amplitude spectrum
- Display the result rounded to the third decimal place

"""
import math

frequency = float(input('Enter a value for the frequency, w: '))
duration = float(input('Enter a value for the duration of the sound wave, T: '))
fourier_transform = (2*math.sin(frequency*duration))/frequency
print('The amplitude spectrum of this Fourier transform is:', round(fourier_transform, 3))