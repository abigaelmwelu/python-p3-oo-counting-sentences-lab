#!/usr/bin/env python3
import re

class MyString:
   def __init__(self, value = ''):
    self._value = value
    
  
   def get_value(self):
    return self._value
  
   def set_value(self, value):
    if isinstance(value, str):
      self._value = value
    else:
      print("The value must be a string.")
      
   value = property(get_value, set_value)       
    
   def is_sentence(self):
    return self._value.endswith('.')
      
   def is_question(self):
    return self._value.endswith('?')      

   def is_exclamation(self):
    return self._value.endswith('!')
  
   def count_sentences(self):
        sentences = re.split(r'[.!?]', self._value)
        sentences = [sentence.strip() for sentence in sentences if sentence.strip()]  # Remove empty sentences
        return len(sentences)


sentence1 = MyString('This is a sentence.')
sentence1.is_sentence()
sentence1.is_question()
sentence1.is_exclamation()

sentences = MyString('This is 1. this is 2? this is two')
sen = sentences.count_sentences()
print(sen)