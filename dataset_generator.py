# -*- coding: utf-8 -*-
"""
DATASET GENERATOR
"""
import random
import json 
import uuid

age_and_genre=['a young _ girl','a young _ boy','a young _ woman','a young _ men','an adult _ woman','an adult _ men','an old _ woman','an old _ man']
clothing=['t-shirt','shirt','sweater','jacket','dress','long coat','swimsuit','sweatshirt','gym clothes','wedding dress','hoodie','uniform','long-sleeve top','coat','sheath dress']
clothing_color=['black','gray','red','brown','blue','purple','white','green','orange','yellow']
hair_color=['blonde','brown','black','red','blue','purple','white','green','gray']
skin_color=['white','brown','black']

questions=['what is the age of the person?','what is the skin color of the person?',
          'what is the gender of the person?', 'what is the color of the person\'s hair?',
          'what is the color of the person\'s clothes?']
answers=[]
paragraphs=[]

def find_nth(haystack, needle, n):
    start = haystack.find(needle)
    while start >= 0 and n > 1:
        start = haystack.find(needle, start+len(needle))
        n -= 1
    return start

for i in range(25000):
    ag_index=random.randint(0, len(age_and_genre)-1)
    cl_index=random.randint(0, len(clothing)-1)
    cc_index=random.randint(0, len(clothing_color)-1)
    hc_index=random.randint(0, len(hair_color)-1)
    sc_index=random.randint(0, len(skin_color)-1)
        
    context=age_and_genre[ag_index].replace('_', skin_color[sc_index])+' with '+hair_color[hc_index]+' hair wearing a '+clothing_color[cc_index]+' '+clothing[cl_index]
    '''
    if ag_index<2:
        answers.append('kid')
    elif ag_index>=2 and ag_index<4:
        answers.append('young')
    else:
        answers.append('adult')
    '''
    answers.append(context[find_nth(context," ",1)+1:find_nth(context," ",2)])
    answers.append(skin_color[sc_index])
    answers.append(context[find_nth(context," ",3)+1:find_nth(context," ",4)])
    '''
    if ag_index%2 == 0:
        answers.append('female')
    else:
        answers.append('male')
    '''
    answers.append(hair_color[hc_index])
    answers.append(clothing_color[cc_index])
    
    qas=[]
    for count, value in enumerate(questions):
        if count == 0:
            qas.append({"question":value,"is_impossible":False,"id":str(uuid.uuid4()),"answers":[{"answer_start":find_nth(context," ",1)+1,"text":answers[count]}]})
        elif count == 2:
            qas.append({"question":value,"is_impossible":False,"id":str(uuid.uuid4()),"answers":[{"answer_start":find_nth(context," ",3)+1,"text":answers[count]}]})
        elif count == 1:
            qas.append({"question":value,"is_impossible":False,"id":str(uuid.uuid4()),"answers":[{"answer_start":find_nth(context," ",2)+1,"text":answers[count]}]})
        elif count == 3:
            qas.append({"question":value,"is_impossible":False,"id":str(uuid.uuid4()),"answers":[{"answer_start":find_nth(context," ",5)+1,"text":answers[count]}]})
        else:
            qas.append({"question":value,"is_impossible":False,"id":str(uuid.uuid4()),"answers":[{"answer_start":find_nth(context," ",9)+1,"text":answers[count]}]})
        
    paragraphs.append({"context":context,"qas":qas})


dictionary ={  
    #"version": "v2.0",
	"data" : [{"title": "People search", "paragraphs": paragraphs}],
    "version": "1.1"
} 

with open("dev-v1.1.json", "w") as outfile: 
	json.dump(dictionary, outfile) 

#https://github.com/makcedward/nlpaug/blob/master/example/textual_augmenter.ipynb

#pip --no-cache-dir install nlpaug
#pip install Cython
    
'''
Basic elements of nlpaug includes:
Character: OCR Augmenter, QWERTY Augmenter and Random Character Augmenter
Word: WordNet Augmenter, word2vec Augmenter, GloVe Augmenter, fasttext Augmenter, BERT Augmenter, Random Word Character
Flow: Sequential Augmenter, Sometimes Augmenter
  

import nlpaug.augmenter.char as nac
import nlpaug.augmenter.word as naw
import nlpaug.augmenter.sentence as nas
import nlpaug.flow as nafc

from nlpaug.util import Action

text = 'look for a young white boy with black hair wearing a gray jacket'
print(text)

# model_type: word2vec, glove or fasttext
# https://github.com/makcedward/nlpaug/issues/73
# pip install transformers

aug = naw.ContextualWordEmbsAug(
    model_path='distilbert-base-uncased', action="substitute")
augmented_text = aug.augment(text)
print("Original:")
print(text)
print("Augmented Text:")
print(augmented_text)

'''  