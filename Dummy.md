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

### Word Tokenization
In **BLTK**, the word_tokenizer() method of the Tokenizer class performs word tokenization. It takes a text string and returns a list of tokenized words. The Following code shows how it is done.

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
['আমি', 'জানি', 'আমার', 'এই', 'লেখাটির', 'জন্য', 'আমাকে', 'অনেক', 'গালমন্দ', 'শুনতে', 'হবে', ',', 'তারপরেও', 'লিখছি', '।', 'লিখে', 'খুব', 'কাজ', 'হয়', 'সে', 'রকম', 'উদাহরণ', 'আমার', 'হাতে', 'খুব', 'বেশী', 'নেই', 'কিন্তু', 'অন্তত', 'নিজের', 'ভেতরের', 'ক্ষোভটুকু', 'বের', 'করা', 'যায়', 'সেটাই', 'আমার', 'জন্যে', 'অনেক', '।']

```
