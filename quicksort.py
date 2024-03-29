from random import randrange, shuffle

def quicksort(list, start, end):
  # this portion of list has been sorted
  if start >= end:
    return
  print("Running quicksort on {0}".format(list[start: end + 1]))
  # select random element to be pivot
  pivot_idx = randrange(start, end + 1)
  pivot_element = list[pivot_idx]
  print("Selected pivot {0}".format(pivot_element))
  # swap random element with last element in sub-lists
  list[end], list[pivot_idx] = list[pivot_idx], list[end]

  # tracks all elements which should be to left (lesser than) pivot
  less_than_pointer = start
  
  for i in range(start, end):
    # we found an element out of place
    if list[i] < pivot_element:
      # swap element to the right-most portion of lesser elements
      print("Swapping {0} with {1}".format(list[i], pivot_element))
      list[i], list[less_than_pointer] = list[less_than_pointer], list[i]
      # tally that we have one more lesser element
      less_than_pointer += 1
  # move pivot element to the right-most portion of lesser elements
  list[end], list[less_than_pointer] = list[less_than_pointer], list[end]
  print("{0} successfully partitioned".format(list[start: end + 1]))
  # recursively sort left and right sub-lists
  quicksort(list, start, less_than_pointer - 1)
  quicksort(list, less_than_pointer + 1, end)


    
  
list = [5,3,1,7,4,6,2,8]
shuffle(list)
print("PRE SORT: ", list)
print(quicksort(list, 0, len(list) -1))
print("POST SORT: ", list)


# Output:
# PRE SORT:  [7, 4, 3, 1, 6, 5, 2, 8]
# Running quicksort on [7, 4, 3, 1, 6, 5, 2, 8]
# Selected pivot 1
# [1, 4, 3, 8, 6, 5, 2, 7] successfully partitioned
# Running quicksort on [4, 3, 8, 6, 5, 2, 7]
# Selected pivot 3
# Swapping 2 with 3
# [2, 3, 8, 6, 5, 4, 7] successfully partitioned
# Running quicksort on [8, 6, 5, 4, 7]
# Selected pivot 4
# [4, 6, 5, 7, 8] successfully partitioned
# Running quicksort on [6, 5, 7, 8]
# Selected pivot 6
# Swapping 5 with 6
# [5, 6, 7, 8] successfully partitioned
# Running quicksort on [7, 8]
# Selected pivot 7
# [7, 8] successfully partitioned
# None
# POST SORT:  [1, 2, 3, 4, 5, 6, 7, 8]
