from tqdm import tqdm
import numpy as np

def char_to_vocab (sentence):
    vocabulary = ['а','б','в','г','д','е','ё','ж','з','и','й','к','л','м','н','о','п','р','с','т','у','ф','х','ц','ч','ш','щ','ъ','ы','ь','э','ю','я',
              'А','Б','В','Г','Д','Е','Ё','Ж','З','И','Й','К','Л','М','Н','О','П','Р','С','Т','У','Ф','Х','Ц','Ч','Ш','Щ','Ъ','Ы','Ь','Э','Ю','Я',
             '!','@','#','$','%','^','&','*','(',')',':',';','/',',','.','%','№','?','~','-','+','=',' ',
              'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
             'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    result = []
    for char in sentence:
        if char in vocabulary:
            result.append(vocabulary.index(char)+1)
            
    result = np.array(result)
    #encoded = one_hot(sentence)
    num_of_lett = 300
    if len(result)<num_of_lett:
        result = np.concatenate((result, np.zeros(num_of_lett-result.shape[0])))
    if len(result)>num_of_lett:
        result = result[:num_of_lett]
    return list(result)

def encode (X):
    X_encoded = []
    for sentence in tqdm(X):
        X_encoded.append(char_to_vocab(sentence))
    return np.array(X_encoded)