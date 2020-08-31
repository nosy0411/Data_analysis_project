import csv

l1 = open('label1.txt', 'r', encoding='utf-8')
sub = open("subject1.txt", "r")
f3 = open("train3.txt", "r")

f2 = open('train2.csv', 'w')

label = l1.readlines()
subject = sub.readlines()
act = f3.readlines()

lines1 = []
with open('train1.txt', 'r', encoding='utf-8') as f1:
    for line in f1:
        row = [x.rstrip() for x in line.split(' ')]
        item = []
        for val in row:
            if val == '':
                continue
            item.append(val)

        lines1.append(" ".join(item))
f1.close()


l1.close()
sub.close()
f3.close()

labels = [x.rstrip() for x in label]
label_fin = []
for lab in labels:
    for i in lab:
        if i == ' ':
            lab = lab.replace(lab[:lab.index(i)+1], '')
            lab = '"' + lab + '"'
            label_fin.append(lab)
            break

labels = ",".join(label_fin)
labels = labels + ',' + 'subject' + ',' + 'Activity'

f2.write(labels + "\n")

sub_lines = [x.rstrip() for x in subject]
act_lines = [x.rstrip() for x in act]
act_dict = {1: "WALKING", 2: "WALKING_UPSTAIRS",
            3: "WALKING_DOWNSTAIRS", 4: "SITTING", 5: "STANDING", 6: "LAYING"}

for idx, line in enumerate(lines1):
    line = line.split(" ")
    line = ",".join(line)
    line = line + ',' + sub_lines[idx] + ',' + act_dict[int(act_lines[idx])]
    f2.write(line + "\n")

f2.close()
