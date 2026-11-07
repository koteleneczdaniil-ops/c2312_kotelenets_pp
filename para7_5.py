def raise_to_degrees(number, max_degree):
    i = 0
    for x in range(max_degree):
        yield number **i
        i+=1


res = raise_to_degrees(122, 100)
print(res)
for r in res:
    print(r)
    print('---')
