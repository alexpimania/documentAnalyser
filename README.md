# documentAnalyser
This program *attempts* to extract terms and phrases from a set of documents that best describe each document.
It does this by first gathering all of the "ngrams" (up to trigrams) from each document and each ngrams corresponding frequency in that document by diving the amount of times it was found by the total amount of words in the document. It then gets the average frequency of all of the ngrams accross all of the documents not just for each. 
The next step is the process that it attempts to utilise to find what words are most relevant to each document:
It look at the frequency of each word in each document and compares it to the average frequency of that word throughout all of the documents. It then prints out the top 10 terms for each document that were found most in that document compared to the average occurance of that word.
This method does not seem to be working that well unforunately and is returning a list of seemingly not important words. 
I put it up here anyway just incase anyone was interested in it or had ideas in regards to how to fix it.

Thanks,
Alex :)
