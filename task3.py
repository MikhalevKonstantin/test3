def longest_sub_string(string1, string2):
    max_length = 0
    sub_string = ""
    for i in range(len(string1)):
        for g in range(len(string2)):
            if string1[i] == string2[g]:
                count = 1
                for k in range(1, min((len(string1)-i), (len(string2)-g))):
                    if string1[i+k] == string2[g+k]:
                        count += 1
                        if count > max_length:
                            max_length = count
                            sub_string = string1[i:i+k+1]
                    else:
                        if count > max_length:
                            max_length = count
                            sub_string = string1[i:i+k+1]
                        break

    return sub_string


print(longest_sub_string("aanavmvvaavv", "aamavv"))