# -*- coding:utf-8 -*-
#author  :honghuichao
#data    :2017-12-31

##to build labels!!
import csv
import random 
labels_index_raw=[]
data_index_raw=[]
with open('../data/labels.csv', 'rb') as f:      
	reader = csv.reader(f)
	
	for row in reader:
		labels_index_raw.append(row[1])
		print row[0]
		print row[1]
		data_index_raw.append(row[0])
	labels_index=[]
	for i in labels_index_raw: 
		if not i in labels_index: 
			labels_index.append(i) 
	count=0
	for x in labels_index:
			labels_index_raw = map(lambda y:[y,count][y==x],labels_index_raw)
			count=count+1
#print labels_index_raw
#print data_index_raw
data_root='/home/administrator/桌面/DogBreedIdentification/data/train/'
labels_shuffle=[]
with open('../data/labels.txt','wb') as f:
	for x in xrange(1,len(labels_index_raw)-1):
		f.write(data_root+data_index_raw[x]+'.jpg'+' '+str(labels_index_raw[x])+'\n')
		labels_shuffle.append(data_root+data_index_raw[x]+'.jpg'+' '+str(labels_index_raw[x]))

random.shuffle(labels_shuffle)
#split train set and val_set
with open('../data/train_labels.txt','wb') as t, open('../data/val_labels.txt','wb') as v:

	for x in xrange(1,len(labels_shuffle)/3):
		v.write(labels_shuffle[x]+'\n')

	for x in xrange(len(labels_shuffle)/3+1,len(labels_shuffle)):
		t.write(labels_shuffle[x]+'\n')



	
		