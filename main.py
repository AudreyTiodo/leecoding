from leetcode import LeetCode

if __name__ == "__main__":
    lc = LeetCode()

    liste = [2, 7, 11, 15]
    cible = 9
    resultat = lc.deux_nombres(liste, cible)
    print("Indices trouvés (deux_nombres) :", resultat)

    nombre = 121
    est_palindrome = lc.palindrome(nombre)
    print(f"Le nombre {nombre} est un palindrome ? {est_palindrome}")

    nombre2 = 123
    est_palindrome2 = lc.palindrome(nombre2)
    print(f"Le nombre {nombre2} est un palindrome ? {est_palindrome2}")

