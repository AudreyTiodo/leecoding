"""


"""

class LeetCode:
    def deux_nombres(self, nums, cible):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == cible:
                    return [i, j] 
                
    def palindrome(self, nombre):
        if nombre < 0:
            return False

        original = nombre
        inverse = 0

        while nombre > 0:
            chiffre = nombre % 10       
            inverse = inverse * 10 + chiffre  
            nombre = nombre // 10          

        return original == inverse
    