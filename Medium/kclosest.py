class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l=len(arr)
        if k==l:
            return arr
        def findcrossover(self,arr,low,high,x):
            if x<=low:
                return low
            if x>=high:
                return high
            mid=low+high//2
            if mid<x:
                return self.findcrossover(arr,mid+1,high,x)
            else:
                return self.findcrossover(arr,low,mid+1,x)
        point=self.findcrossover(arr,0,l-1,x)
        r=point+1
        returnarr=[]
        cnt=0
        if(arr[point]==x):
            point-=1
        while(point>=0 and r<n and cnt<k+1):
            if x-arr[point]<=arr[r]-x:
                returnarr.append(arr[point])
                point-=1
                cnt+=1
            else:
                returnarr.append(arr[r])
                r+=1
                cnt+=1
        while(point>=0 and cnt<k+1):
            returnarr.append(arr[point])
            point-=1
            cnt+=1
        while(r<n and cnt<k+1):
            returnarr.append(arr[point])
            r+=1
            cnt+=1
        return reversearr
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if len(arr) == k:
            return arr
        
        start, end = 0, len(arr)-k
        while start+1 < end:
            mid = start+(end-start)//2
            if abs(x-arr[mid]) <= abs(arr[mid+k]-x): # start is more preferred
                end = mid
            else: # end is more preferred
                start = mid
        
        if abs(x-arr[start]) <= abs(arr[start+k]-x):
            return arr[start:start+k]
       	else:
            return arr[end:end+k]
                   
            
            
        