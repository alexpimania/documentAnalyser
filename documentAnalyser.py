def getConfig():
   import json
   config = json.loads(open("config.json").read())
   return config


def getDocumentList():
   import glob, os
   documents = {}
   #os.chdir("analysisDocuments")
   for document in glob.glob("/home/pimania/analysisDocuments/*.txt"):
      documentName = document.replace(".txt", "").replace("/home/pimania/analysisDocuments/", "")
      with open(document) as documentFile:
         documentContents = cleanText(documentFile.read().strip().lower())
         documents[documentName] = documentContents
   return documents

      
def removeStopWords(wordsList):
   config = getConfig()
   wordsList = [word for word in wordsList if not word.replace("'", "") in config["stopWords"]]
   return wordsList
   
   
def cleanText(text):
   import string
   #removePunctuation
   text = "".join([item for item in list(text) if item not in list(string.punctuation + "#!()-$@/")])
   #removeStopWords
   #text = " ".join(removeStopWords(text.split()))
   return text
  
def extractNgrams(document):
   import nltk
   ngrams = []
   ngrams.extend([" ".join(list(ngram)) for ngram in nltk.ngrams(document.split(), 2)])
   ngrams.extend([" ".join(list(ngram)) for ngram in nltk.ngrams(document.split(), 3)])
   return ngrams
  
def getNgramFrequencies():
   from nltk import FreqDist
   wordFrequencies = {}
   documents = getDocumentList()
   for document in documents:
      wordFrequencies[document] = {}
      #allWords = documents[document].split()
      #allWords.extend(extractNgrams(documents[document]))
      allWords = extractNgrams(documents[document])
      wordOccurences = FreqDist(allWords).most_common()
      totalWordCount = len(allWords)
      for word in wordOccurences:
         wordFrequencies[document][word[0]] = word[1] / totalWordCount
   return wordFrequencies
         
         
def getAverageNgramFrequencies():
   averageWordFrequencies = {}
   wordFrequencies = getNgramFrequencies()
   allWords = []
   for document in wordFrequencies:
      allWords.extend(list(wordFrequencies[document].keys()))
   allWords = list(set(allWords))
   for word in allWords:
      documentCount = 0
      totalFrequency = 0
      for document in wordFrequencies:
         if word in wordFrequencies[document]:
            documentCount += 1
            totalFrequency += wordFrequencies[document][word]
      averageWordFrequencies[word] = totalFrequency/documentCount
   return averageWordFrequencies
   
   
def getDocumentWordRatios():
   documentWordDeltas = {}
   wordFrequencies = getNgramFrequencies()
   averageWordFrequencies = getAverageNgramFrequencies()
   for document in wordFrequencies:
      for word in wordFrequencies[document]:
         documentWordFrequency = wordFrequencies[document][word]
         averageWordFrequency = averageWordFrequencies[word]
         wordFrequencyRatio = documentWordFrequency/averageWordFrequency
         if document not in documentWordDeltas:
            documentWordDeltas[document] = {}
         documentWordDeltas[document][word] = wordFrequencyRatio
   return documentWordDeltas
   
def printTopDocumentWords():
   documentWordRatios = getDocumentWordRatios()
   for document in documentWordRatios:
      sortedDocumentWords = sorted(documentWordRatios[document].items(), key=lambda x: x[1])
      sortedDocumentWords2 = [word[0] for word in sortedDocumentWords]
      print(sortedDocumentWords[-10:])
      print("\n\nDocument: " + document + "\nTop words: " + " || ".join(sortedDocumentWords2[-10:]) + "\n\n")
      
      
if __name__ == "__main__":
   printTopDocumentWords()
