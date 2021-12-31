def topologicalSort(jobs, deps):
  # create adjacency dictionary 
	# create indegrees dictionary
  
	def getAdjLst(): 
		adj_lst = {job:[] for job in jobs}
		for dep in deps: 
			A, B = dep[0], dep[1]
			adj_lst[A].append(B)
		return adj_lst
  
	adj_lst = getAdjLst() 
	indegrees = {i:0 for i in jobs}
	#1. populate indegrees
	for job in jobs: 
		for neighbor in adj_lst[job]:  
			indegrees[neighbor] += 1

	#2. populate q with nodes with indegree == 0 
	from collections import deque 
	res, q = [], deque()
	for job, indegree in indegrees.items(): 
		if indegree == 0: 
			q.append(job)
			res.append(job)
	
	#3. return list of order in which jobs are completed 
	while q: 
		node = q.popleft() 
		for nei in adj_lst[node]: 
			indegrees[nei] -= 1
			if indegrees[nei] == 0:
				q.append(nei)
				res.append(nei)

	return res if len(res) == len(jobs) else []
