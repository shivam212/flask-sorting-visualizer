from flask import Flask, render_template, request, jsonify
import json
from flask_bootstrap import Bootstrap


app = Flask(__name__)
bootstrap = Bootstrap(app)


# Python program for implementation of Bubble Sort 
  
def bubbleSort(arr): 
    newlist = [] 
    n = len(arr) 
    newarr = arr.copy()
  
    # Traverse through all array elements 
    for i in range(n-1): 
    # range(n) also work but outer loop will repeat one time more than needed. 
  
        # Last i elements are already in place 
        for j in range(0, n-i-1): 
  
            # traverse the array from 0 to n-i-1 
            # Swap if the element found is greater 
            # than the next element 
            if newarr[j] > newarr[j+1] : 
                newarr[j], newarr[j+1] = newarr[j+1], newarr[j] 
            newlist.append(newarr.copy())
        # print(newarr,i)
    return newlist
listlistlist = []
def merge_sort(array, left_index, right_index, doit):
    if left_index >= right_index:
        return

    middle = (left_index + right_index)//2
    merge_sort(array, left_index, middle,doit)
    merge_sort(array, middle + 1, right_index,doit)
    merge(array, left_index, right_index, middle)
    # print(array)
    doit.append(array.copy())

    return doit


def merge(array, left_index, right_index, middle):
    # Make copies of both arrays we're trying to merge

    # The second parameter is non-inclusive, so we have to increase by 1
    left_copy = array[left_index:middle + 1]
    right_copy = array[middle+1:right_index+1]

    # Initial values for variables that we use to keep
    # track of where we are in each array
    left_copy_index = 0
    right_copy_index = 0
    sorted_index = left_index

    # Go through both copies until we run out of elements in one
    while left_copy_index < len(left_copy) and right_copy_index < len(right_copy):

        # If our left_copy has the smaller element, put it in the sorted
        # part and then move forward in left_copy (by increasing the pointer)
        if left_copy[left_copy_index] <= right_copy[right_copy_index]:
            array[sorted_index] = left_copy[left_copy_index]
            left_copy_index = left_copy_index + 1
        # Opposite from above
        else:
            array[sorted_index] = right_copy[right_copy_index]
            right_copy_index = right_copy_index + 1

        # Regardless of where we got our element from
        # move forward in the sorted part
        sorted_index = sorted_index + 1

    # We ran out of elements either in left_copy or right_copy
    # so we will go through the remaining elements and add them
    while left_copy_index < len(left_copy):
        array[sorted_index] = left_copy[left_copy_index]
        left_copy_index = left_copy_index + 1
        sorted_index = sorted_index + 1

    while right_copy_index < len(right_copy):
        array[sorted_index] = right_copy[right_copy_index]
        right_copy_index = right_copy_index + 1
        sorted_index = sorted_index + 1
@app.route('/sort', methods=['POST'])
def dosort():
    print("aaya")
    if request.method == "POST":
          arr = []
          dataArr = request.data.decode('utf-8') 
          str1 = ""
          str2 = ""
          flag=1
          for x in dataArr:
              if x=="x":
                  flag=0
                  continue
              if flag:
                  str1+=x
              else:
                str2+=x


          temp = ""
          for s in str1:
              if s==" ":
                arr.append(int(temp))
                temp=""
              else:
                  temp+=s
          arr.append(int(temp)) 
          print(str1,str2)
          if str2=="bubble sort":
            return jsonify({'array': bubbleSort(arr.copy())})
          else:
            doit = []
            return jsonify({'array': merge_sort(arr.copy(),0,len(arr)-1,doit)})

@app.route('/')
def index():
    # for array in arrayStates:
    #     array = json.dumps(array)
    # print(arrayStates)
    # array = [7,6,5,58,324,0,1,2,3,4,5,6,7,9,82]  
    array = [10,9,8,7,6,5,4,3,2,1,10,9,8,7,6,5,4,3,2,1,7,6,5,58,34,0,1,2,3,4,5,6,7,9,8]
    arrayStates = listlistlist
    arrayStates = json.dumps(arrayStates)
    data = json.dumps(array)
    # print(data)
    # print(arrayStates)
    labels = []
    for i in range(1,len(array)+1):
        labels.append(i)
    labels=json.dumps(labels)
    return render_template("base.html", data = data,
                        labels=labels, arrayStates = arrayStates)
    # return "yo"

if _name_ == '_main_':
    app.run()
