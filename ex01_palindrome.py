#!/usr/bin/python3

def est_palindrome(mot):
  debut = 0
  fin = len(mot) - 1
  while debut != fin:
    if fin == -1 or not mot[debut] == mot[fin]:
      return False
    debut += 1
    fin -= 1
  return True


def test_palindrome():
  print('Test de la fonction palindrome')
  assert not est_palindrome('')
  assert est_palindrome("kayak")
  assert est_palindrome("a")
  assert not est_palindrome("abc")
  print('  OK')

test_palindrome()


