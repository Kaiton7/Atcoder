N=int(input())
x=N//100
if(100*x+10*x+x<N):
    print(100*(x+1)+10*(x+1)+x+1)
else:
    print(100*x+10*x+x)