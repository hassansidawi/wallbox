# Exercice 1

def first_repeated(list1, list2):
  res = None
  for i in list1:
    if i in list2:
      res = i
      break
  return res

# Exercice 3

def count_coin_flips(seq):
  # We suppose that seq is formed by 0's and 1's
  n = len(seq)
  if n <= 2:
    # Nothing to do
    return 0
  
  # n greater than 2
  n0 = seq.count(0) # How many 0's
  n1 = seq.count(1) # How many 1's
  if n0 > n1+1 or n1 > n0 + 1:
    # no solution, no tries
    return 0
  
  # Recursive function. res contains the sequence transformed
  res, count = flip(seq, [], 0)
  return count


def flip(seq, res, count):
  if len(seq) == 0:
    # Stop recursion
    return res, count
  
  if len(res) == 0:
    # First step
    n0 = seq.count(0) # How many 0's
    n1 = seq.count(1) # How many 1's
    if n0 > n1+1 or n1 > n0+1:
      # No solution, no tries
      return seq, count
    
    idx = 0
    if n0 == n1+1:
      idx = seq.index(0) # Start with 0
    elif:
      idx = seq.index(1)
      
    # Transfer from seq to res
    res.append(seq[idx])
    seq.pop(idx)
    if idx != 0:
      count += 1
      
    return flip(seq, res, count) # recursive call
  
  else:
    i = res[-1] # last element
    if i == 0:
      if 1 in seq:
        idx = seq.index(1) # find the first 1
    else:
      if 0 in seq:
        idx = seq.index(0) # find the first 0
        
    # Transfer from seq to res
    res.append(seq[idx])
    seq.pop(idx)
    
    if idx != 0:
      count += 1
      
    return flip(seq, res, count) # recursive call
    
