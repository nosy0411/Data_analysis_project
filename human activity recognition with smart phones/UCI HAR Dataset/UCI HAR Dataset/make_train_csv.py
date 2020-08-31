import csv
import os
path = os.path.dirname(os.path.realpath(__file__))
txt_path = os.path.join(path, "train")

feat = open(os.path.join(path, "features.txt"), 'r', encoding='utf-8')
sub = open(os.path.join(txt_path, "subject_train.txt"), "r")
activity = open(os.path.join(txt_path, "y_train.txt"), "r")

fin = open(os.path.join(path, "train.csv"), 'w')

label = feat.readlines()
subject = sub.readlines()
act = activity.readlines()

feat.close()
sub.close()
activity.close()

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

fin.write(labels + "\n")

sub_lines = [x.rstrip() for x in subject]
act_lines = [x.rstrip() for x in act]
act_dict = {1: "WALKING", 2: "WALKING_UPSTAIRS",
            3: "WALKING_DOWNSTAIRS", 4: "SITTING", 5: "STANDING", 6: "LAYING"}

lines1 = []
with open(os.path.join(txt_path, "X_train.txt"), 'r', encoding='utf-8') as f1:
    for line in f1:
        row = [x.rstrip() for x in line.split(' ')]
        item = []
        for val in row:
            if val == '':
                continue
            item.append(val)

        lines1.append(" ".join(item))
f1.close()

for idx, line in enumerate(lines1):
    line = line.split(" ")
    line = ",".join(line)
    line = line + ',' + sub_lines[idx] + ',' + act_dict[int(act_lines[idx])]
    fin.write(line + "\n")

fin.close()
