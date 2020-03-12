# BLTK: The Bengali Natural Language Processing Toolkit

A lightweight but robust toolkit for processing Bengali Language.

[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=102)](https://github.com/ellerbrock/open-source-badge/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

## Supported Functionalities
- Word Tokenization
- Sentence Tokenization
- Sentence Splitting
- Stopwords Filtering
- Part-of-speech Tagging
- Phrase Chunking/Named-Entity Recognition
- Stemming

## Contribution

For contribution you can refer to [CONTRIBUTING.md](CONTRIBUTING.md)



## Installation
To get BLTK up and running, run the following command.
```sh
pip install bltk
```

## Usage

### 1) The Bengali Characters
In **BLTK**, the *banglachars* module contains 7 lists of characters specific to the Bengali Language.
1. vowels
2. vowel signs
3. consonants
4. digits
5. punctuation marks
6. operators
7. others

#### Code
```python
from bltk.langtools.banglachars import (vowels,
                                        vowel_signs,
                                        consonants,
                                        digits,
                                        operators,
                                        punctuations,
                                        others)
print(f'Vowels: {vowels}')
print(f'Vowel signs: {vowel_signs}')
print(f'Consonants: {consonants}')
print(f'Digits: {digits}')
print(f'Operators: {operators}')
print(f'Punctuation marks: {punctuations}')
print(f'Others: {others}')
```

#### Output
```
Vowels: ['অ', 'আ', 'ই', 'ঈ', 'উ', 'ঊ', 'ঋ', 'ঌ', 'এ', 'ঐ', 'ও', 'ঔ']
Vowel signs: ['া', 'ি', 'ী', 'ু', 'ূ', 'ৃ', 'ৄ', 'ে', 'ৈ', 'ো', 'ৌ']
Consonants: ['ক', 'খ', 'গ', 'ঘ', 'ঙ', 'চ', 'ছ', 'জ', 'ঝ', 'ঞ', 'ট', 'ঠ', 'ড', 'ঢ', 'ণ', 'ত', 'থ', 'দ', 'ধ', 'ন', 'প', 'ফ', 'ব', 'ভ', 'ম', 'য', 'র', 'ল', 'শ', 'ষ', 'স', 'হ', 'ড়', 'ঢ়', 'য়', 'ৎ', 'ং', 'ঃ', 'ঁ']
Digits: ['০', '১', '২', '৩', '৪', '৫', '৬', '৭', '৮', '৯']
Operators: ['=', '+', '-', '*', '/', '%', '<', '>', '×', '÷']
Punctuation marks: ['।', ',', ';', ':', '?', '!', "'", '.', '"', '-', '[', ']', '{', '}', '(', ')', '–', '—', '―', '~']
Others: ['৳', '৺', '্', 'ঀ', 'ঽ', '#', '$']

```



### 2) Word Tokenization
In **BLTK**, the word_tokenizer(text: str) method of the Tokenizer class performs word tokenization. It takes a text string and returns a list of tokenized words. The Following code shows how it is done.

#### Code
```python
from bltk.langtools import Tokenizer

# Sample text
text = "আমি জানি আমার এই লেখাটির জন্য আমাকে অনেক গালমন্দ শুনতে হবে, তারপরেও লিখছি। "\
       "লিখে খুব কাজ হয় সে রকম উদাহরণ আমার হাতে খুব বেশী নেই কিন্তু অন্তত নিজের ভেতরের ক্ষোভটুকু বের করা " \
       "যায় সেটাই আমার জন্যে অনেক।"

# Creating an instance
tokenizer = Tokenizer()

# Tokenizing words
print('TOKENIZED WORDS')
words = tokenizer.word_tokenizer(text)
print(words)
```

#### Output
```
TOKENIZED WORDS
['আমি', 'জানি', 'আমার', 'এই', 'লেখাটির', 'জন্য', 'আমাকে', 'অনেক', 'গালমন্দ', 'শুনতে', 'হবে', ',', 'তারপরেও', 'লিখছি', '।', 'লিখে', 'খুব', 'কাজ', 'হয়', 'সে', 'রকম', 'উদাহরণ', 'আমার', 'হাতে', 'খুব', 'বেশী', 'নেই', 'কিন্তু', 'অন্তত', 'নিজের', 'ভেতরের', 'ক্ষোভটুকু', 'বের', 'করা', 'যায়', 'সেটাই', 'আমার', 'জন্যে', 'অনেক', '।']

```

### 3) Sentence Tokenization
In Bangla, most of the sentence delimiters are same as in English except full-stop. Statements and imperative sentences are terminated by । - the Devanagari Danda.
Questions and exclamatory sentences are terminated by ? and ! respectively. 

In **BLTK**, the sentence_tokenizer(text: str) method of the Tokenizer class performs sentence tokenization. It takes a text string and returns a list of tokenized sentences. The Following code shows how it is done.

#### Code
```python
from bltk.langtools import Tokenizer

# Sample text
text = "আমি জানি আমার এই লেখাটির জন্য আমাকে অনেক গালমন্দ শুনতে হবে, তারপরেও লিখছি। " \
       "লিখে খুব কাজ হয় সে রকম উদাহরণ আমার হাতে খুব বেশী নেই কিন্তু অন্তত নিজের ভেতরের ক্ষোভটুকু বের করা " \
       "যায় সেটাই আমার জন্যে অনেক।"

# Creating an instance
tokenizer = Tokenizer()


# Tokenizing Sentences
print("TOKENIZED SENTENCES")
sentences = tokenizer.sentence_tokenizer(text)
print(sentences)
```

#### Output
```
TOKENIZED SENTENCES
['আমি জানি আমার এই লেখাটির জন্য আমাকে অনেক গালমন্দ শুনতে হবে, তারপরেও লিখছি।', 'লিখে খুব কাজ হয় সে রকম উদাহরণ আমার হাতে খুব বেশী নেই কিন্তু অন্তত নিজের ভেতরের ক্ষোভটুকু বের করা যায় সেটাই আমার জন্যে অনেক।']
```




### 4) Sentence Split
The sentence_splitter(sentence: list) method takes a list of tokened sentences and then splits them into their corresponding list of tokened words with the help of word_tokenizer() method. The return value is a list of tokened words lists.

#### Code
```python
from bltk.langtools import Tokenizer

# Sample text
text = "আমি জানি আমার এই লেখাটির জন্য আমাকে অনেক গালমন্দ শুনতে হবে, তারপরেও লিখছি। " \
       "লিখে খুব কাজ হয় সে রকম উদাহরণ আমার হাতে খুব বেশী নেই কিন্তু অন্তত নিজের ভেতরের ক্ষোভটুকু বের করা " \
       "যায় সেটাই আমার জন্যে অনেক।"

# Creating an instance
tokenizer = Tokenizer()


# Tokenizing Sentences
sentences = tokenizer.sentence_tokenizer(text)

print("SPLIT SENTENCES")
sentence_list = tokenizer.sentence_splitter(sentences)
print(sentence_list)

print("INDIVIDUAL SENTENCE")
for i in sentence_list:
    print(i)

```

#### Output
```
SPLIT SENTENCES
[['আমি', 'জানি', 'আমার', 'এই', 'লেখাটির', 'জন্য', 'আমাকে', 'অনেক', 'গালমন্দ', 'শুনতে', 'হবে', ',', 'তারপরেও', 'লিখছি', '।'], ['লিখে', 'খুব', 'কাজ', 'হয়', 'সে', 'রকম', 'উদাহরণ', 'আমার', 'হাতে', 'খুব', 'বেশী', 'নেই', 'কিন্তু', 'অন্তত', 'নিজের', 'ভেতরের', 'ক্ষোভটুকু', 'বের', 'করা', 'যায়', 'সেটাই', 'আমার', 'জন্যে', 'অনেক', '।']]

INDIVIDUAL SENTENCE

['আমি', 'জানি', 'আমার', 'এই', 'লেখাটির', 'জন্য', 'আমাকে', 'অনেক', 'গালমন্দ', 'শুনতে', 'হবে', ',', 'তারপরেও', 'লিখছি', '।']
['লিখে', 'খুব', 'কাজ', 'হয়', 'সে', 'রকম', 'উদাহরণ', 'আমার', 'হাতে', 'খুব', 'বেশী', 'নেই', 'কিন্তু', 'অন্তত', 'নিজের', 'ভেতরের', 'ক্ষোভটুকু', 'বের', 'করা', 'যায়', 'সেটাই', 'আমার', 'জন্যে', 'অনেক', '।']


```

