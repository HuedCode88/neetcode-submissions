
'''
given an array of strs, group anagrams into sublists, then output


U: 
add em to a map after sorting 


'''
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map={}
        for i in strs:
            curr="".join(sorted(i))
            if curr in map:
                map[curr].append(i)
            else:
                map[curr]=[i]
        lst=[]
        for j in map:
            lst.append(map[j])
        return lst




        