
def bestFit(blockSize, m, processSize, n):

	allocation = [-1] * n
	

	for i in range(n):
		
		
		bestIdx = -1
		for j in range(m):
			if blockSize[j] >= processSize[i]:
				if bestIdx == -1:
					bestIdx = j
				elif blockSize[bestIdx] > blockSize[j]:
					bestIdx = j

		# If we could find a block for
		# current process
		if bestIdx != -1:
			
			# allocate block j to p[i] process
			allocation[i] = bestIdx

			# Reduce available memory in this block.
			blockSize[bestIdx] -= processSize[i]

	print("Best Fit\nProcess No. Process Size	 Block no.")
	for i in range(n):
		print(i + 1, "		 ", processSize[i],
								end = "		 ")
		if allocation[i] != -1:
			print(allocation[i] + 1)
		else:
			print("Not Allocated")

def worstFit(blockSize, m, processSize, n):
     
   
    allocation = [-1] * n
     
    
    for i in range(n):
         
        
        wstIdx = -1
        for j in range(m):
            if blockSize[j] >= processSize[i]:
                if wstIdx == -1:
                    wstIdx = j
                elif blockSize[wstIdx] < blockSize[j]:
                    wstIdx = j
 
        
        if wstIdx != -1:
             
            
            allocation[i] = wstIdx
 
            
            blockSize[wstIdx] -= processSize[i]
 
    print("Worst Fit\nProcess No. Process Size Block no.")
    for i in range(n):
        print(i + 1, "         ",
              processSize[i], end = "     ")
        if allocation[i] != -1:
            print(allocation[i] + 1)
        else:
            print("Not Allocated")

def firstFit(blockSize, m, processSize, n):
     
    allocation = [-1] * n
    for i in range(n):
        for j in range(m):
            if blockSize[j] >= processSize[i]:
                 
               
                allocation[i] = j
 
                
                blockSize[j] -= processSize[i]
 
                break
 
    print("First Fit\nProcess No. Process Size      Block no.")
    for i in range(n):
        print(" ", i + 1, "         ", processSize[i],
                          "         ", end = " ")
        if allocation[i] != -1:
            print(allocation[i] + 1)
        else:
            print("Not Allocated")

if __name__ == '__main__':
    n = int(input("Enter block size : "))
blockSize = list(map(int,input("Enter the numbers separated by space : ").strip().split()))[:n]    
print("List is - ", blockSize)

no = int(input("\nEnter process size : "))
processSize = list(map(int,input("Enter the numbers separated by space : ").strip().split()))[:no]    
print("List is - ", processSize)
# blockSize = [100 500 200 300 600]
# processSize = [212 417 112 426]
m = len(blockSize)
n = len(processSize)
print("1: BEST FIT\n2: WORST FIT\n3: FIRST FIT")
x = input("Enter choice: ")
if (x == "1"):
	bestFit(blockSize, m, processSize, n)
elif(x == "2"):
    worstFit(blockSize, m, processSize, n)
elif (x == "3"):
	firstFit(blockSize, m, processSize, n)



