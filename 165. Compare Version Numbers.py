# approach
# split each version based on '.'
# iterate through maximum of both parts
# convert each part to int and compare values
# Time complexity -> O(max(len(version1),len(version2))
# Space complexity -> O(len(version1) + len(version2))
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split('.')
        v2 = version2.split('.')
        for i in range(max(len(v1),len(v2))):
            if i < len(v1):
                part1 = int(v1[i])
            else:
                part1 = 0
            if i < len(v2):
                part2 = int(v2[i])
            else:
                part2 = 0
            if part1 > part2:
                return 1
            elif part1 < part2:
                return -1
        return 0
        
