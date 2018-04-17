class solution():
    def shengxu(self,l):
        n=len(l)
        left,right=0,n-1

        if n==0:
            return None
        if n==1:
            return l[0]
        while True:
            mid=(left+right)//2
            if l[mid]>l[mid-1]:
                left=mid+1
            if l[mid]>l[mid+1]:
                right=mid-1
            if l[mid-1]<l[mid] and l[mid]>l[mid+1]:
                break
        return l[mid]

p=solution()
x=[1,2,3,5,4,3,2]
print(p.shengxu(x))
