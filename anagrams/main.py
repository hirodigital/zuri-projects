# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True



from gettext import find


def find_anagram(word, anagram):
    if sorted(word)==sorted(anagram):
        return True
    else:
        return False

print(find_anagram("below", "elbow"))

print(find_anagram("hello","check"))

