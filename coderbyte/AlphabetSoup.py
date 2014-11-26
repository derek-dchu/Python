def AlphabetSoup(str): 

  # O(n log n) using default sorting provided by Python
  chars = list(str)
  chars.sort()
  return ''.join(chars)
    
    
# keep this function call here  
# to see how to enter arguments in Python scroll down
print AlphabetSoup(raw_input()) 