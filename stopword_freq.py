import csv
import os
import sys
from collections import defaultdict

def stopword_usage(fi,num):
    with open('./package/training_set_'+str(num)+'.csv','r') as csvinput:
        with open('./package/training_'+str(num)+'.csv', 'w') as csvoutput:
            writer = csv.writer(csvoutput)
            f = open(fi, 'r')
            a=0
            count=0
	    d1 = defaultdict(int)
	    p = open('./package/previous_stopwords_'+str(num)+'.txt','a')
            
            stopword = ['a','able','about','across','after','all','almost','also','am','among','an','and','any','are','as','at','be','because','been','but','by','can','cannot','could','dear','did','do','does','either','else','ever','every','for','from','get','got','had','has','have','he','her','hers','him','his','how','however','i','if','in','into','is','it','its','just','least','let','like','likely','may','me','might','most','must','my','neither','no','nor','not','of','off','often','on','only','or','other','our','own','rather','said','say','says','she','should','since','so','some','than','that','the','their','them','then','there','these','they','this','tis','to','too','twas','us','wants','was','we','were','what','when','where','which','while','who','whom','why','will','with','would','yet','you','your']

            s = open('./package/stopword_usage_'+str(num)+'.txt','a')
                
            for row,line in zip(csv.reader(csvinput),f):    
                #print 'yeah'
                if a==0:
                    writer.writerow(row+["stopword_usage"])   
                else:   
                    for t in line.split():
			for be in stopword:
			    if t==be:
				#print t,be
				count=count+1
				d1[t]+=1
	
                    #if (a%10) == 0: 
                    #print 'yes'
                    s.write(str(a) + " " + str(count))
                    writer.writerow(row+[count])
                    s.write("\n")
                    count=0
                a+=1
            for key, value in d1.items():
		p.write(str(key) + " " + str(value))
		p.write("\n")
            s.close()

            f.close()
            
            os.rename('./package/training_'+str(num)+'.csv', './package/training_set_'+str(num)+'.csv')

f = sys.argv
if __name__ == "__main__":
    stopword_usage(str(f[1]),1)






