from unit6_lesson_04_understanding_fileio import open_input_file

__author__ = 'Krish'

notes = '''
 This problem will require you to put together many things you have learnt
 in earlier units to solve a problem.

 In particular you will use functions, nested functions, file i/o, functions, lists, dicts, iterators, generators,
 comprehensions,  sorting etc.

 Read the constraints carefully and account for all of them. This is slightly
 bigger than problems you have seen so far, so decompose it to smaller problems
 and solve and test them independently and finally put them together.

 Write subroutines which solve specific subproblems and test them independently instead of writing one big
 mammoth function.

 Do not modify the input file, the same constraints for processing input hold as for unit6_assignment_02
'''

problem = '''
 Given an input file of words (mixed case). Group those words into anagram groups and write them
 into the destination file so that words in larger anagram groups come before words in smaller anagram sets.

 With in an anagram group, order them in case insensitive ascending sorting order.

 If 2 anagram groups have same count, then set with smaller starting word comes first.

 For e.g. if source contains (ant, Tan, cat, TAC, Act, bat, Tab), the anagram groups are (ant, Tan), (bat, Tab)
 and (Act, cat, TAC) and destination should contain Act, cat, TAC, ant, Tan, bat, Tab (one word in each line).
 the (ant, Tan) set comes before (bat, Tab) as ant < bat.

 At first sight, this looks like a big problem, but you can decompose into smaller problems and crack each one.

 source - file containing words, one word per line, some words may be capitalized, some may not be.
 - read words from the source file.
 - group them into anagrams. how?
 - sort each group in a case insensitive manner
 - sort these groups by length (desc) and in case of tie, the first word of each group
 - write out these groups into destination
'''

import unit6utils
import string

def are_anagrams(first, second):
    if first is None or second is None: return False
    word1 = list(first.lower())
    word2 = list(second.lower())
    for c in word1:
        if c not in word2: return False
        word2.remove(c)
    return True

def anagram_sort(source, destination):
    f = open(source, 'r')
    words = []
    for line in f:
        if len(line) <= 1 or line.split()[0] == '#': continue
        words.extend(line.split())

    anagram_groups = []
    processed_words = []
    for i in range(len(words)):
        word = words[i]
        if word in processed_words: continue
        anagram_group = (word,)
        processed_words.append(word)
        for j in range(i+1,len(words)):
            if are_anagrams(word,words[j]):
                anagram_group += (words[j],)
                processed_words.append(words[j])
        if len(anagram_group) > 0:
            anagram_group = sorted(anagram_group, key=lambda s: s.lower())
            anagram_groups.append(anagram_group)

    anagram_groups = sorted(anagram_groups, key=lambda lst: lst[0].lower())
    anagram_groups = sorted(anagram_groups, key=lambda lst: (len(lst)), reverse=True)
    print(anagram_groups)

    f.close()

    f = open(destination,'w')

    output = ""
    for group in anagram_groups:
        output += '\n'.join(group)
        output += '\n'
    f.write(output)
    f.close()

def test_anagram_sort():
    source = unit6utils.get_input_file("unit6_testinput_03.txt")
    expected = unit6utils.get_input_file("unit6_expectedoutput_03.txt")
    destination = unit6utils.get_temp_file("unit6_output_03.txt")
    anagram_sort(source, destination)
    result = [word.strip() for word in open(destination)]
    expected = [word.strip() for word in open(expected)]
    print(len(result),result)
    print(len(expected),expected)
    assert expected == result
