for i in range(1,4): # outer loop = represents row
    for j in range(1,4): # inner loop = represents column
      print(i, end=" ") 
    print() # to jump on next line

      # explaination 
      #(i,j)=(1,1) , (1,2) , (1,3) , (1,4) (condition false) , (2,1) , (2,2) , (2,3) , (2,4) (condition false) , (3,1) , (3,2) , (3,3) , (3,4) (condition false)
      #         1   2   3
      #-> 1     1   1   1
      #   2     2   2   2
      #   3     3   3   3 