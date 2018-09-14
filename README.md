# HashtagK

Read all text documents on "docs" directory of the program and return the 10 most detected words and generate an HTML file with the output.

## Requisites:

Python 3 or above
NLTK Toolkit, link here: https://www.nltk.org/install.html
 

## How to run:

Clone the repository (git clone https://github.com/bjanuario/HashtagK)

Install the NLTK dependency (`sudo pip3 install -U nltk`)

Run `python3 HashtagK.py`

Open the html file created inside the program directory

## Sample data

You can download here de docs directory files and put them in the same dir where you will run the application

## What word tags are avaiable:

As I am using NLTK I rely ony on Noums, singular or mass to be more precise on usefull hotwords but the list of possibilities are these:

CC - Coordinating conjunction

CD - Cardinal number

DT - Determiner

EX - Existential there

FW - Foreign word

IN - Preposition or subordinating conjunction

JJ - Adjective

JJR - Adjective, comparative

JJS - Adjective, superlative

LS - List item marker

MD - Modal

NN - Noun, singular or mass

NNS - Noun, plural

NNP - Proper noun, singular

NNPS - Proper noun, plural

PDT - Pre determiner

POS - Possessive ending

PRP - Personal pronoun

PRP$ - Possessive pronoun

RB - Adverb

RBR - Adverb, comparative

RBS - Adverb, superlative

RP - Particle

S - Simple declarative clause, i.e. one that is not introduced by a (possible empty) subordinating conjunction or a wh-word and that does not exhibit subject-verb inversion

SBAR - Clause introduced by a (possibly empty) subordinating conjunction

SBARQ - Direct question introduced by a wh-word or a wh-phrase. Indirect questions and relative clauses should be bracketed as SBAR, not SBARQ

SINV - Inverted declarative sentence, i.e. one in which the subject follows the tensed verb or modal.

SQ - Inverted yes/no question, or main clause of a wh-question, following the wh-phrase in SBARQ.

SYM - Symbol

VBD - Verb, past tense

VBG - Verb, gerund or present participle

VBN - Verb, past participle

VBP - Verb, non-3rd person singular present

VBZ - Verb, 3rd person singular present

WDT - Wh-determiner

WP - Wh-pronoun

WP$ - Possessive wh-pronoun

WRB - Wh-adverb