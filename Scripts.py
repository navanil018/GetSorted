import SelSort as sv
import BubbleSort as bs
import InsertionSort as ins

print("Script running")
print("Please select the Sort you want to see:")
print("1) Selection Sort")
print("2) Bubble Sort")
print("3) Insertion Sort")

x =  input()

if x == '1':
    sv.main()
elif x == '2':
    bs.main()
elif x == '3':
    ins.main()
else:
    print('Wrong Choice')

