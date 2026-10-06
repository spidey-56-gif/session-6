arr = [12,45,7,89,23]
n = 5
i =1
max_val = arr[0]
while(i<n):
    if(arr[i]>max_val):
        max_val = arr[i]
    i=i+1
print("Largest element is "+ str(max_val))
