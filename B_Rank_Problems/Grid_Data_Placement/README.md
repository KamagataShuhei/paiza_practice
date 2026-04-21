# 反省
```python
for i in range(H):
    ans = ""
    for j in range(W):
        ans += A[i][j]
    print(ans)
```

というふうに書いたがjoin()を使えばスマートにかける

```python
for row in A:
    print("".join(row))
```

