class Solution:
    def compareVersion(self, version1, version2):
        """
        Compare two version numbers version1 and versoin2. If version1 > version2 return 1, if version1 < version2 return -1, otherwise return 0.

        Args:
            version1: a string as a version
            version2: a string as a version
        
        Returns:
            an integer
        """
        version_numbers1 = version1.split('.')
        version_numbers2 = version2.split('.')
        len1 = len(version_numbers1)
        len2 = len(version_numbers2)

        for i in range(0, min(len1, len2)):
            if int(version_numbers1[i]) > int(version_numbers2[i]):
                return 1
            elif int(version_numbers1[i]) < int(version_numbers2[i]):
                return -1

        if len1 > len2:
            for i in range(len2, len1):
                if int(version_numbers1[i]) != 0:
                    return 1
        elif len1 < len2:
            for i in range(len1, len2):
                if int(version_numbers2[i]) != 0:
                    return -1
        return 0