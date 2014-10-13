class Heap():
	def __init__(self, arr = None):
		if arr:
			self.array = arr[:]
			self.buildHeap()
		else:
			self.array = []
			

	def storeAt(self,i,val):
		if i >= len(self.array):
			self.array.append(val)
		else:
			self.array[i] = val

	def add(self,val):
		i = len(self.array)
		parent = (i-1)/2
		while i>0 and val > self.array[parent]:
			self.storeAt(i, self.array[parent])
			i = parent
			parent = (i-1)/2
		self.storeAt(i, val)

	def heapify(self,i):
		left = i*2+1
		right = i*2+2
		if left>0 and left<len(self.array) and self.array[left]>self.array[i]:
			s = left
		else:
			s = i
		if right>0 and right<len(self.array) and self.array[right]>self.array[s]:
			s = right
		
		if s != i:
			self.array[s], self.array[i] = self.array[i], self.array[s]
			self.heapify(s)

	def popMax(self):
		if len(self.array)==0:
			raise None
		a = self.array[0]
		del self.array[0]
		self.buildHeap()
		return a

	def buildHeap(self):
		for v in range(len(self.array)/2,-1,-1):
			self.heapify(v)

	def stringifyNode(self, i):
		if i >= len(self.array):
			return ''
		leftChild = self.stringifyNode(i*2+1)
		leftChild = ('\n' if len(leftChild)>0 else '') + leftChild
		rightChild = self.stringifyNode(i*2+2)
		rightChild = ('\n' if len(rightChild)>0 else '') + rightChild
		indentLen = ((i-1)/2) + (1 if i>0 else 0)
		lastWs = '\n'+' '*indentLen if len(leftChild)+len(rightChild)>0 else ''
		return ' '*indentLen+'('+str(self.array[i])+leftChild+rightChild+lastWs+')'

	def __str__(self):
		return self.stringifyNode(0)

	def __len__(self):
		return len(self.array)

	def generator(self):
		while True:
			if len(self.array)==0
				raise StopIteration
			yield self.popMax()

def heapsort(a):
	h = Heap(a)
	b = []
	for i in range(len(h)):
		b.append(h.popMax())
	return b


h = Heap()
h.add(1)
h.add(2)
h.add(3)
h.add(4)
h.add(5)
h.add(6)
h.add(7)
print h.popMax()
