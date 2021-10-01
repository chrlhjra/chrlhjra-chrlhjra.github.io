import pandas as pd

b = pd.read_csv('irisversicolor.csv')

b.to_html('versicolor.html')

b = pd.read_csv('irisversicolor.csv')

b_mean = b["	SepalLengthCm"].mean()
b_median = b["	SepalLengthCm"].median()
b_mode = b["	SepalLengthCm"].mode()

b = pd.read_csv('irisversicolor.csv')

b_mean1 = b["	SepalLengthCm"].mean()
b_median1 = b["	SepalLengthCm"].median()
b_mode1 = b["	SepalLengthCm"].mode()

b = pd.read_csv('irisversicolor.csv')

b_mean2 = b["	SepalLengthCm"].mean()
b_median2 = b["	SepalLengthCm"].median()
b_mode2 = b["	SepalLengthCm"].mode()

b = pd.read_csv('irisversicolor.csv')

b_mean3 = b["	SepalLengthCm"].mean()
b_median3 = b["	SepalLengthCm"].median()
b_mode3 = b["	SepalLengthCm"].mode()

print(b.to_string())

print('\n"SepalLengthCm mean is:' + str(b_mean))
print('SepalLengthCm median is:' + str(b_median))
print('SepalLengthCm mode is:' + str(b_mode))

print('\n"SepalWidthCm mean is:' + str(b_mean1))
print('SepalWidthCm median is:' + str(b_median1))
print('SepalWidthCm mode is:' + str(b_mode1))

print('\n"PetaLengthCm mean is:' + str(b_mean2))
print('PetalLengthCm median is:' + str(b_median2))
print('PetalLengthCm mode is:' + str(b_mode2))

print('\n"PetalWidthCm mean is:' + str(b_mean3))
print('PetalWidthCm median is:' + str(b_median3))
print('PetalWidthCm mode is:' + str(b_mode3))
