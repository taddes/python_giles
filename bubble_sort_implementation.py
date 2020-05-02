test_list = [45, 95, 2, 16, 24, 5, 57, 65, 55, 24]

# Copy list to not change original
data_copy = test_list[:]

for i in range(len(data_copy)):
    for j in range(0, len(data_copy) -1 -i):
        if data_copy[j] > data_copy[j+1]:
            data_copy[j], data_copy[j+1] = data_copy[j+1], data_copy[j]

print(data_copy)