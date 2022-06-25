
def page_choice():
    while True:
        page =input("enter l for login and s for sighn up:>")
        if page =='':
            print('please enter some thing')
            continue   
        
        if page =='l' or page =='s':
            return page
            break
        if page !='l' or page !='s':
            print('l or s')
            continue

print(page_choice())
