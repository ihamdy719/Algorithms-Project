def is_triangular_triplet(A):
    n = len(A)
    triplets = []
    count = 0
    for P in range(n - 2):
        for Q in range(P + 1, n - 1):
            for R in range(Q + 1, n):
                if A[P] + A[Q] > A[R] and A[Q] + A[R] > A[P] and A[R] + A[P] > A[Q]:
                    triplets.append((A[P], A[Q], A[R]))
                    count += 1
    return count, triplets

input_string = input("Enter the numbers in the array separated by spaces: ")
A = []
number = ""
for char in input_string:
    if char == " ":
        if number:
            A.append(int(number))
            number = ""
    else:
        number += char
if number:
    A.append(int(number))

result = is_triangular_triplet(A)
print(f"Input: nums = {A}")
print(f"Output: {result}")









'''




PSEUDO-CODE for this code 


FUNCTION is_triangular_triplet(A)
{
    n := length(A)
    count := 0
    triplets := []

    For P := 0 to n-3 step 1 do
    {
        For Q := P+1 to n-2 step 1 do
        {
            For R := Q+1 to n-1 step 1 do
            {

                If A[P] + A[Q] > A[R] AND A[Q] + A[R] > A[P] AND A[R] + A[P] > A[Q] then
                {
                    count := count + 1
                    triplets.append((A[P], A[Q], A[R]))
                }
            }
        }
    }

    print("Input: nums = ", A)
    print("Output: (", count, ", ", triplets, ")")
}




'''