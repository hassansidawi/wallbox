# wallbox
pytest exercises
Functions defined in routines.py

Exercise 1

Return the first repeated number from 2 lists:
res = first_repeated(list1,list2)

To test this function, use pytest executing on a terminal:
python -m pytest -v -k repeated --disable-pytest-warnings

it will execute the parametrized test:
test_repeated(list1, list2, res)


Exercise 3

Return quantity of changes to turn a sequence of 0's and 1's interspersed.
Return 0 if it is not possible.
count = count_coin_flips(seq)

This function uses a recursive function:
  res, count = flip(seq, res, count)
which tries to transform seq into a intersperced list (res)

To test this function, use pytest executing on a terminal:
python -m pytest -v -k coin --disable-pytest-warnings

it will execute the parametrized test:
test_count_coin(seq, count)

Exercice 2 

Check if a directory contains an .exe file that meets some requirements.
In this case, the function returns the file name:
filename = request(root_dir)

To test this function, use pytest executing on a terminal:
python -m pytest -v -k file --disable-pytest-warnings

it will execute the parametrized test:
test_file(root_dir, filename)

