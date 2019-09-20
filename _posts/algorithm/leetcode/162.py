# 进制转换10->26
class Solution:
    def convertToTitle(self, n: int) -> str:
      A = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
      m = []
      if n==1:
          return 'A'
      else:
          while (n>1):
              temp = int(n % 26)
              a = A[temp-1]
              m.append(a)
              # n = n/26
            # str = ''.join(str(i) for i in m[::-1])
          return str

s=Solution()
print(s.convertToTitle(2))
