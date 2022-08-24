"""read lines till a dollar sign '$' is entered and display those lines where the word 'document' is used twice"""
while True:
    st=input("Enter a string:")
    l=st.split()
    c=l.count('document' or 'Document')
    if '$' in l:
        print("Dollar sign found! so the program will stop")
        break
    elif c==2:
        print("Document found and the string entered is : ", st)




