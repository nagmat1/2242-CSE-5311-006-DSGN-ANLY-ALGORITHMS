# Hands-On 10 

Implement a hash table and upload your code to github:

Use the multiplication AND division method for your hash function. 
Note your code should be generic enough to allow for ANY hash function. 
For simplicity assume your keys are integers and the values (data) are integers. 
Use collision resolution by chaining : Use a doubly linked list and you must write your own (so for example you can't use "list" in C++)
You are only allowed to use C-style array's for this implementation (so for example no C++ vectors)
Your Hash table should grow and shrink : When it's full double the array size and re-hash everything or When it's becoming empty e.g. 1/4 empty, then half the size of the array and re-hash everything

# Program Output : 

```
[0]: (5, 50) -> None
[1]: (2, 20) -> (10, 100) -> None
[2]: (7, 70) -> None
[3]: (4, 40) -> None
[4]: (1, 10) -> (9, 90) -> None
[5]: (6, 60) -> None
[6]: (3, 30) -> None
[7]: (8, 80) -> None
Value for key 5: 50
[0]: None
[1]: (2, 20) -> (10, 100) -> None
[2]: (7, 70) -> None
[3]: (4, 40) -> None
[4]: (1, 10) -> (9, 90) -> None
[5]: (6, 60) -> None
[6]: (3, 30) -> None
[7]: (8, 80) -> None

```
