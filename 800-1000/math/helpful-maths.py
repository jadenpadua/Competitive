def main():
    res = []
    s = input()
    split = s.split('+')
    sorted_split = sorted(split)
    for i in range(len(sorted_split)):
        res.append(sorted_split[i])
        res.append('+')

    print(''.join(res[:len(res)-1]))

main()