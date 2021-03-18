from collections import Counter

class Solution:
    List = {str: 1}
    n=2
    def leastInterval(self, tasks: List[str], n: int) -> int:
        print(Solution.leastInterval.__annotations__)
        print(tasks,n)
        print("123")
        print(Solution.List[str])
        return 0
        # c,t = Counter(tasks),0
        # big_n = c.most_common(1)[0][1]
        # for k in c.values():
        #     if k == big_n: t += 1
        # res = (big_n-1)*(n+1)+t
        # return res if res >= len(tasks) else len(tasks)

# def sl(self,t:int):
#     print(t)
#     return t
#
#
if __name__ == '__main__':
    l=['A','A','A','B','B','B']
    s=Solution.leastInterval('',l,'11；1')