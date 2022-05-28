file="story.txt"

def read_file_content(myfile):
    
    with open(myfile, 'r') as file:
        data = file.read().replace('\n','')
    return data

def count_words(myfile):
    big_string = read_file_content(myfile)
   
    s = big_string.lower().split()
    dict = {}

    for word in s:
        
        if word in dict:
           
            dict[word] = dict[word] + 1
        else:
            
            dict[word] = 1
    
    return dict

print(count_words(file))