#From codereview.stackexchange.com
def partitions(set_):
    if not set_:
        yield []
        # print('yielded')
        return
    for i in range(2**len(set_)//2):
        parts = [set(), set()]
        for item in set_:
            # print('SET',set_)
            # print('item; ', item)
            print(i)
            parts[i&1].add(item)
            i >>= 1
            # print('check ', end =" ")
#        print(parts)
        for b in partitions(parts[1]):
#             print('b yield: ',[parts[0]]+ b)
#             print('b: ', b, ' type b :', type(b))
             yield [parts[0]]+b


# This is a helper function that will fetch all of the available
# partitions for you to use for your brute force algorithm.
def get_partitions(set_):
    for partition in partitions(set_):
        # print('other y1ielded')
        yield [list(elt) for elt in partition]

### Uncomment the following code  and run this file
### to see what get_partitions does if you want to visualize it:

for item in (get_partitions(['a','b','c','d'])):
    print(item)