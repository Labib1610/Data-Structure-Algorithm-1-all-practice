from our_library import Stack

str = input("Enter Bracket Sequence: ")
st = Stack()

balanced = True

for c in str:
    if c == "(":
        st.push(c)
    else:
        if st.isEmpty() == False:
            st.pop()
        else:
            balanced = False
            break

if balanced == False:
    print("Imbalanced")
else:
    if st.isEmpty() == True:
        print("Balanced")
    else:
        print("Imbalanced")