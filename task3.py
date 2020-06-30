book_library = set()
num_n = int(input())
book_list = set()
num_m = int(input())
for i in range(num_n):
    book = input()
    book_library.add(book)
for i in range(num_m):
    book = input()
    book_list.add(book)
    if book in book_library:
        print('YES')
    else:
        print('NO')