#!/usr/bin/python3

def maximum(liste):
  m = liste[0]
  for e in liste:
    if e>m:
      m = e
  return m

def test_maximum():
  print('Test de la fonction maximum')
  assert maximum([-1, -3, -20]) == -1
  assert maximum([10])==10
  assert maximum([15,2,6,0])==15
  assert maximum([8,9,3,12])==12
  assert maximum([1,7,13,4])==13
  
  print('  OK')

test_maximum()