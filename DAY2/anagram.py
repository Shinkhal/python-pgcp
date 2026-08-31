def anagram():
    words = ["eat", "tea", "tan", "ate", "nat", "bat"]
    
    anagram_groups = {}
    
    for word in words :
        sorted_word = "".join(sorted(word))

        if sorted_word not in anagram_groups:
            anagram_groups[sorted_word] = []
        
        anagram_groups[sorted_word].append(word)
        
    res = list(anagram_groups.values())
    print(res)
    
    
print("-" *50)   
anagram()