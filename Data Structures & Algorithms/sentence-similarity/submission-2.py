class Solution(object):
    def areSentencesSimilar(self, sentence1, sentence2, similarPairs):
        if len(sentence1) != len(sentence2):
            return False

        pair = set()
        for i, j in similarPairs:
            pair.add((i, j))
            pair.add((j, i))

        for i in range(len(sentence1)):
            if sentence1[i] != sentence2[i] and (sentence1[i], sentence2[i]) not in pair:
                return False

        return True