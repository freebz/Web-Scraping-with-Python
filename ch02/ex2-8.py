# 2.6 람다 표현식

# 태그를 애매변수로 받고, 불리언을 리턴하는 람다 함수를 받을 수 있음

soup.findAll(lambda tag: len(tag.attrs) == 2)
