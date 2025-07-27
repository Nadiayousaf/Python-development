def string_methods():
    txt="pyTHOn is AweSome, isn't it ?Python is   FUN!"
    print(txt.lower())
    parts=" ".join(txt.split())
    print(parts)
    word='python'
    result=txt.upper()
    result=txt.replace(word,word.upper())
    print(result)
def count_specific_word():
 count=0
 specific_word='is'
 txt="pyTHOn is AweSome, isn't it ?Python is   FUN!"
 count=txt.count(specific_word)
 print(f"The '{specific_word}'appears in {count}times")
 final_string=txt.center(60,"*")
 print(final_string)
 return count
count_specific_word()
string_methods()

