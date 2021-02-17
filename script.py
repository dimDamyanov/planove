import os

def print_tags(tags):
    for tag in tags:
        print(tag[0])
        for i in range(1, len(tag) - 1):
            print(' ' * 2 + tag[i].strip())
        print(tag[0])


files = [f for f in os.listdir() if f.endswith('.txt')]
for file in files:
    with open(file, 'r') as file:
        lines = file.readlines()
    tags = []
    tag_open = False
    for line in lines:
        if tag_open:
            if line.strip() == current_tag:
                tag_open = False
            tags[-1].append(line)
        elif line.strip().startswith('%'):
            current_tag = line.strip()
            tags.append([current_tag])
            tag_open = True

print_tags(tags)