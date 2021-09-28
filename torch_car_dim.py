import torch

"""
探究torch.cat中dim=的用法
"""
# 两个（2,3,4）的张量
x = torch.tensor(
    [[[1, 2, 3, 4],
      [5, 6, 7, 8],
      [9, 10, 11, 12]],

     [[13, 14, 15, 16],
      [17, 18, 19, 20],
      [21, 22, 23, 24]]])
y = torch.arange(24).reshape(2, 3, 4)

a = torch.cat((x, y), dim=0)
print(a, '\n', a.shape)
b = torch.cat((x, y), dim=1)
print(b, '\n', b.shape)
c = torch.cat((x, y), dim=2)
print(c, '\n', c.shape)

# 两个（2,3）的张量
matrix1 = torch.tensor([[1, 2, 3],
                        [4, 5, 6]])

matrix2 = torch.arange(6).reshape(2, 3)

d = torch.cat((matrix1, matrix2), dim=0)
print(d, '\n', d.shape)
e = torch.cat((matrix1, matrix2), dim=1)
print(e, '\n', e.shape)
