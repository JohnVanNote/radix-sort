#!usr/bin/python
#
# radix.py
#
#

import sys

# Main sorting function sorted by Least Significant Digit
# num_list is an unordered list of integers
# returns a list of ordered integers
def radixSort( num_list ):
  if len( num_list ) == 0:
    return
  max_digit = largestDigit( num_list )
  buckets = makeBuckets( 10 )
  for i in num_list:
    key_value = i % 10
    buckets[ key_value ].append( i )
  if max_digit == 0:
    return oneList( buckets )
  else:
    count = 1
    while count <= max_digit:
        buckets = advRadixSort( buckets, count )
        count += 1 
  return oneList( buckets )

# This function is used if a value has more than one significant digit
# buckets is a list of list of buckets from the previous significant digit
# digit is the significant digit for the numbers to be sorted at
# returns a new list of list or buckets
def advRadixSort( buckets, digit ):
  tens = pow( 10, digit )
  more_buckets = makeBuckets( 10 )
  for i in buckets:
    for j in i:
      if j/tens != 0:
        key_value = (j/tens) % 10
        more_buckets[ key_value ].append( j )
      else:
        more_buckets[ 0 ].append( j )
  return more_buckets
  
# Finds the largest significant digit in a list of integers
def largestDigit( num_list ):
  max_val = largestValue( num_list )
  count = 0
  place = 10
  while max_val/place != 0:
    count += 1
    place *= 10
  return count
 
# Finds the max value in a list of integers
def largestValue( num_list ):
  return max( i for i in num_list )
 
# creates buckets
def makeBuckets( num ):
  return [[] for i in range( num )]

# Makes a list of integers from input string
def makeUnorderedList( input_string ):
  unordered_list = []
  for i in input_string.strip().split(' '):
    unordered_list.append( int( i ))   
  return unordered_list

# Takes a list of list and makes it into one list
def oneList( listOfList ):
  one_list = []
  for i in listOfList:
    for j in i:
      one_list.append( j )
  return one_list

def main():
  data = raw_input( "Enter a set of numbers seperated by white space: " )
  unordered_list = makeUnorderedList( data )
  sorted_list = radixSort( unordered_list )
  print( "The numbers in order are as follows: " )
  for i in sorted_list:
    print i

if __name__ == "__main__":
  main()
