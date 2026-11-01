def permutation(s):
    result = []
    path = []
    used = [False] * len(s)

    def backtrack():
        if len(path) == len(s):
            result.append(''.join(path))
            return

        for i in range(len(s)):
            if not used[i]:
                path.append(s[i])
                used[i] = True
                backtrack()
                path.pop()
                used[i] = False

    backtrack()
    return result

s = "abc"
print(permutation(s))