# Encoder/Embedding

- This holds Basic DL and NLP concepts
- Text preprocessing
- Basic STATIC Encoding examples

### 1. STATIC BASIC - EMBEDDING/ENCODING:

###### This wont carry any semantic meaning

- One Hot Encoding
- Freq/Count based: - BOW - TF/IDF - N-GRAM

### 2. DP Learning based./Prediction based Embedding:

- WORD2VEC
- CBOW
- SKIP GRAM

        - Based on set of features it produce weights to each token. Which holds semantic meaning. Which gives average weight based on all the sentence)
        - This is static vector for each Token/word. and produces vector based on Overall conext of the whole data
        - **Contextual/Dynamic vector** was **NOT** there in this embedding. So Vector going to be same throught the process Even if custom fine tune the embedding with our data. For new data again it shows OOV(Out of vacabulary)

###### Issue:

    But this holds semantic meaning but holds static info. If Bank as river bank or Financial bank both will have same vector

To solve this issue Dynamic embedding, self attention/Transformer arrived. Embedding should change based on sentence for same word

### Dynamic/CONTEXTUAL EMBEDDING:- Advnavced EMBEDDING:

- **Self attention** inside **Transformer** - Which creates embedding Dynamically
