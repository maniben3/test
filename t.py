impot numpy as np
import multiprocessing
import os
import time

def r(x):
  max=10**x
  res=np.full(max+10**6,True)

if __name__ == "__main__":
	# creating processes
  start = time.time()
  m=9
	p1 = multiprocessing.Process(target=r, args=(m, ))
	p2 = multiprocessing.Process(target=r, args=(m, ))
  p3 = multiprocessing.Process(target=r, args=(m, ))
	p4 = multiprocessing.Process(target=r, args=(m, ))
  p5 = multiprocessing.Process(target=r, args=(m, ))
	p6 = multiprocessing.Process(target=r, args=(m, ))
  p7 = multiprocessing.Process(target=r, args=(m, ))
	p8 = multiprocessing.Process(target=r, args=(m, ))
	# starting process 1
	p1.start()
	p2.start()
  p3.start()
	p4.start()
  p5.start()
	p6.start()
  p7.start()
	p8.start()
	p1.join()
	p2.join()
  p3.join()
	p4.join()
  p5.join()
	p6.join()
  p7.join()
	p8.join()
	print("Done!",time.time()-start)

