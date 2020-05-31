# Chappie : Q/A android application
This project aims at developing a system which organizations/startups can use to improve customer experience. In AI any system in which machines can comprehend and answers the questions on its own generally called Chatbots.

## System Architecture
This system follows a client-server architecture where an android application as a client sends the human query to the web-server where SOTA ML algorithms starts comprehending the query and tries to return the best possible answers.

Well I specifically talk about backend because that's my part of work. I will discuss the following things  
- How to Set up backend with the following details
  - Frameworks
  - Research papers
  - Libraries
- How to use Framework for your own data?
- References for more detail information

## Backend

### DrQA Framework & Libraries

On backend side I am Using Facebook's 2017 release framework called `DrQA`.
You will find more information about how to setup and install this framework [here.](https://github.com/facebookresearch/DrQA)

### Research papers
Probably you'll required to read the research paper to get more detail information about SOTA ML algorithms which you will find [here.](https://arxiv.org/abs/1704.00051)

### Quick Walkthrough over the Framework
DrQA is a pretty well designed framework for MRS(machine reading at scale) task which has two main components
- Document Retriever (Non-ML component)
- Document Reader (ML component)

#### Document Retriever
This component operates first on the query and then starts retrieving the best N (5 in my case) documents/articles out of the millions of documents/articles.
It's a Non-ML component and uses the following techniques
- Tf-Idf
- Bigram hashing

#### Document Reader
On receiving the best N documents from retriever component this component start reading those documents and start searching the best possible answer to the query. This is a ML component which uses SOTA `Bidirectional Multilayer RNN` trained with the following techniques on the top of basic model.
- Multitask learning
- Distant supervision



### DataSet
Following dataset are used to train `Bidirectional Multilayer RNN`
- SQuAD
- CuratedTREC
- WebQuestions
- WikiMovies

### Using DrQA on your own Data
If you want to use `DrQA` on your own data you need to
- Create a sqlite db from a corpus of documents
- Build a TF-IDF weighted word-doc sparse matrix from the documents stored in the sqlite db

For that I will refer you [here.](https://github.com/facebookresearch/DrQA/tree/master/scripts/retriever)

I have used Flask for creating a web server which you can check out here `scripts/pipeline/server.py`

## Acknowledgments
- Android application by @KSdhanjal

## References
[![Facebook DrQA](http://img.youtube.com/vi/1RN88O9C13U/0.jpg)](http://www.youtube.com/watch?v=1RN88O9C13U)
