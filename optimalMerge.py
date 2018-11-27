import sys
slist=[]
left=[]
right=[]
def omp(num):
	n=len(num)
	for i in num:
		slist.append(i)
	rootlist=[]
	slist.sort()
	
	root=0
	left.append(slist[0])
	right.append(slist[1])
	r=0
	cl=0
	cr=0
	root=left[0]+right[0]
	rootlist.append(root)
	counter=2

	while (counter<n):
		root=0
		flag=0
		for i in range(counter,n):
			flag=0
			if(rootlist[r]<=slist[i]):
				flag=1
			else:	
				store=rootlist[r]
				break

		if(flag==1):
			left.append(rootlist[r])
			right.append(slist[counter])
			
			cl+=1
			cr+=1
			root=left[cl]+right[cr]
			rootlist.append(root)
			r+=1
			counter+=1
		else:
			left.append(slist[counter])
			right.append(slist[counter+1])
			cl+=1
			cr+=1
			root=left[cl]+right[cr]
			rootlist.append(root)
			r+=1
			counter+=2
	if(counter==n):
		root=rootlist[r]+rootlist[r-1]
		rootlist.append(root)
		
	
	sumroot=0
	print("The optimal merge pattern is: ")
	for j in range(len(rootlist)):
		sumroot=sumroot+rootlist[j]
		print(rootlist[j]),
	print(' = '+str(sumroot))
		

if __name__ == "__main__":
	num=raw_input("Enter the file sizes separated by spaces\n")
	n=num.split(' ')
	listn=[]
	for i in n:
		listn.append(int(i))
	omp(listn)
