n=5
board=[[0]*n for _ in range(n)]

def isSafe(row,col):
    for i in range(row):
        if board[i][col]==1:
            return False
        
    i,j=row-1,col-1
    while i>=0 and j>=0:
        if board[i][j]==1:
            return False
        
        i-=1
        j-=1

    
    i,j=row-1,col+1
    while i>=0 and j<n:
        if board[i][j]==1:
            return False
        
        i-=1
        j+=1

    return True

def solve(row):

    if row==n:
        print("\nSolution")
        for i in board:
            print(i)
        return True
    
    for col in range(n):
        if isSafe(row,col):
            board[row][col]=1

            if solve(row+1):
                return True
            
            board[row][col]=0

    return False

solve(0)



#worst case tc = O(n!)
#best case =O(n)
#sc=O{n^2}
"""
Give me a complete block-by-block explanation of the code.

Follow STRICT format:

First show the code block
Immediately below it write: EXPLANATION :
Then give a very detailed explanation in paragraph form

IMPORTANT INSTRUCTIONS:

Explain each and every word, keyword, function, operator, and symbol used
Explain what it does, why it is used, and what is the need of it
Do not skip any line or concept
Maintain same depth for ALL blocks (not just first block)
No emojis
No short explanations
Make it beginner-friendly so even a person with zero knowledge can understand
Keep explanation clean and directly copy-paste usable
Do not separate explanation elsewhere, keep it directly below each code block
also you are giving it in a para manner which is making it very boring to read for each new line use new line 

Explain internally what happens step-by-step in the function wherever applicable and also can you give what actually are we doing in this code
also give input and output"""