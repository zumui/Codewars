def solution(string,markers):
    s_list = string.split("\n")
    print (s_list)
    n_list = []

    for item in s_list:
        s = ""
        for char in item:
            if char in markers:
                break #jika aada marker maka langsung continue ke item selanjutnya
            else:
                s = s + char
            print (s)
        n_list.append(s.strip())
        print (n_list)
    return "\n".join(n_list)
