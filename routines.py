def first_repeated(list1, list2):
  res = None
  for i in list1:
    if i in list2:
      res = i
      break
  return res


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


def
