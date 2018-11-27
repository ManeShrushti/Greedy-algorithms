scheduled={}
ans=[]
temp=[]
def sequence(d,p):
	dead=[int(x) for x in d]
	for i in dead:
		temp.append(i)

	profit=[int(x) for x in p]
	profit.sort(reverse=True)
	n=len(p)
	dead.sort()

	jobs=set(dead)
	job=list(jobs)

	for i in job:
		scheduled[i]='f'
	key=scheduled.keys()

	for i in range(n):

		val=temp[i]
		s=scheduled.get(val)

		if(s=='f'):
			scheduled[val]='t'
			ans.append(i+1)
		else:
		   j=temp[i]-1
		   while(j>=0):
			s1=scheduled.get(key[j])
			if(s1=='f'):
				scheduled[key[j]]='t'
				ans.append(i+1)
				break
			else:
			    j-=1	
		
	print_seq(ans)			
		
def print_seq(ans):
	print("The sequenced schedule of jobs is:\n")
	for i in range(len(ans)):
		print('J'+str(ans[i])+'\t')
	print('\n')

if __name__=='__main__':
	deadline=raw_input("Enter the deadlines\n")
	d=deadline.split(' ')
	profits=raw_input("Enter the profits\n")
	p=profits.split(' ')
	if(len(d)!=len(p)):
		print("pairs not entered in correspondence")
	sequence(d,p)
