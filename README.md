# Data Augmentation Techniques

Data augmentation is employed to expand existing datasets when training data is limited, especially in Machine Learning (ML) or Deep Learning (DL) applications. The primary concept involves altering text while retaining its meaning to enhance the dataset's diversity.

Basic idea: Change the words in the text slighty without changing the meaning of the sentence.


### Update 2024: 
The project shows the draft code from 2018 and has to be cleansed / updated. With regards to LLMs recently appeared, it can make more sense to explore LLMs' capabilities for augmenting more data, though, for use cases when the risk of halizinating (a current LLMs issue) is too high, the shown Data Augmentation techniques are still usable.

The project's code, initially drafted in 2018, necessitates some cleansing and updating. However, recent advancements in Large Language Models' (LLMs) capabilities, offer promising avenues for augmenting datasets. Nevertheless, for scenarios where LLMs pose a risk of hallucinating data (a current issue), the showcased Data Augmentation techniques remain viable.

# Experiment Overview:
The experiment aimed at binary and multi-label classification using datasets such as fetch_20newsgroups from sklearn and the Enron Email Dataset, distinguishing between spam and non-spam emails.


Two different methods:
 - Backtranslation: Translate to another language and then back into the target language
"In a recent Kaggle competition (Jigsaw Toxic Comment Classification) a really neat regularization strategy was used, which ended up being a big factor in the First Place Winner’s solution.
The idea was to create augmented text data by translating it into some foreign language, and then translating it back to English.
The performance gain was huge.
Presumably, Google Translate would make errors in the translation processes, which helped prevent the RNNs from overfitting to irrelevant features." (Quora)

 - Thesaurus: Using a Thesaurus (dictonary for synonyms), replace a certain percentage of words with synonyms


# Methods Explored:

## - Backtranslation:
Translate to another language and then back into the target language.
"In a recent Kaggle competition (Jigsaw Toxic Comment Classification) a really neat regularization strategy was used, which ended up being a big factor in the First Place Winner’s solution. The idea was to create augmented text data by translating it into some foreign language, and then translating it back to English. The performance gain was huge. Presumably, Google Translate would make errors in the translation processes, which helped prevent the RNNs from overfitting to irrelevant features." (Quora)

## - Thesaurus:
Leveraging a thesaurus (a dictionary for synonyms) to replace a certain percentage of words within text samples with their synonyms, aiming to diversify the dataset.

# Results

Please check the [pdf report]().

# Future Directions:
Refinement and optimization of data augmentation techniques.
Exploration and integration of recent language models (LLMs) to augment datasets, balancing risks associated with hallucination.
