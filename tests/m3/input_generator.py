import random



def generate_input():

    i = random.randint(1, 15)
    catalog = f"books_{i}.txt"

    # INPUT FOR TITLE SEARCH
    f = open(catalog, encoding="utf8")
    lines = f.readlines()
    num_titles = len(lines)
    title = lines[random.randint(0, num_titles-1)].split("^")[1]
    f.close()

    file1 = open("input_1.txt", 'w')
    file1.write(f"2\n1\n{catalog}\n2\n5\n{title}\nq\nq")
    file1.close()

    # INPUT FOR CART BEST-SELLER
    file2 = open("input_2.txt", 'w')
    file2.write(f"2\n1\n{catalog}\n2\n6\n")
    for i in range(random.randint(3, 5)):
        idx = random.randint(0, num_titles-1)
        file2.write(f"1\n{idx}\n")
    file2.write(f"3\nq\nq\nq")
    file2.close()


generate_input()