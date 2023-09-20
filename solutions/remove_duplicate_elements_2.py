def remove_groups(s: str, k: int) -> str:

    if k <= 1:  # Edge case, if k is 1, the result will be an empty string
        return ""
    
    found = True
    while found:
        if not s:  # If the string is empty, break out of the loop
            break
        
        found = False
        count = 1
        prev_char = s[0]
        new_string = []

        for i in range(1, len(s)):
            if s[i] == prev_char:
                count += 1
            else:
                if count != k:
                    new_string.extend([prev_char] * count)
                else:
                    found = True
                count = 1

            prev_char = s[i]

        if count != k:  # For the last group
            new_string.extend([prev_char] * count)
        else:
            found = True

        s = ''.join(new_string)

    return s
