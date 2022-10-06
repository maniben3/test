import gmpy2
import time
start=time.time()
print("negative","1")
t = 0xe5c8de231c0a0d1868a963f277a504e60d0419444b384f7ac18c081a84c2c890*5*7*11*13*17*19*23*29*31*37*41*43*47
for r in range(2,10**9):
  i =8*r+1
  h=t*i-1
  p=2*t*i-1
  q=4*t*i-1
  r=8*t*i-1
  s=16*t*i-1
  a=32*t*i-1
  b=64*t*i-1
  #c=128*t*i+1
  #d=256*t*i+1
  #e=512*t*i+1
  if gmpy2.is_fermat_prp(h,2) ==1 :
    if gmpy2.is_fermat_prp(p,2) ==1 :
       if gmpy2.is_fermat_prp(q,2) ==1 :
         if gmpy2.is_fermat_prp(r,2) ==1 :
            if gmpy2.is_fermat_prp(s,2) ==1 :
              print(i,"6")
              print(time.time()-start)
              if gmpy2.is_fermat_prp(a,2) ==1 :
                print(i,"7")
                print(time.time()-start)
                if gmpy2.is_fermat_prp(b,2) ==1 :
                 # if gmpy2.is_fermat_prp(c,2) ==1 :
                  #  if gmpy2.is_fermat_prp(d,2) ==1 :
                   #  if gmpy2.is_fermat_prp(e,2) ==1 :
                          print(i)
                          print(time.time()-start)
print(time.time()-start)
