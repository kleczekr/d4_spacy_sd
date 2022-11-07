import spacy

nlp = spacy.load('en_core_web_sm')

sentence = 'Pick up the red plastick tank toy from the floor and put it on the table'

def lemma_or_chunk(sentence):
    '''
    A function which receives a sentence, processes it through spaCy,
    and returns a list of lemmas or noun chunks. Tokens which are members
    of noun chunks are not included in the list of lemmas, because they are
    represented within the noun chunks. The other tokens are lemmatized, with
    some (punctuation) excluded.
    '''
    element_list = []
    chunk_reference = []
    doc = nlp(sentence)
    chunks = list(doc.noun_chunks)
    for chunk in chunks:
        chunk_reference.append({'start': chunk.start, 'end': chunk.end, 'text': chunk.text})
    counter = 0
    while counter < len(doc):
        if any([chunk['start'] <= counter < chunk['end'] for chunk in chunk_reference]):
            for chunk in chunk_reference:
                if chunk['start'] <= counter < chunk['end']:
                    element_list.append(chunk['text'])
                    counter = chunk['end']
        elif doc[counter].is_punct:
            counter += 1
            continue
        else:
            element_list.append(doc[counter].lemma_)
            counter += 1
    return element_list

print(lemma_or_chunk(sentence))
