#Given an array of strings, group anagrams together.
#
#For example, given: ["eat", "tea", "tan", "ate", "nat", "bat"], 
#Return:
#
#[
#  ["ate", "eat","tea"],
#  ["nat","tan"],
#  ["bat"]
#]

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        d = {}
        for w in strs:
            key = tuple(sorted(w))
            d[key] = d.get(key, []) + [w]
        return d.values()
