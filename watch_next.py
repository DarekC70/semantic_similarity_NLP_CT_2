import spacy
# A description of the video that serves as a reference for comparison
des = '''Will he save
their world or destroy it? When the Hulk becomes too dangerous for the
Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a
planet where the Hulk can live in peace. Unfortunately, Hulk land on the
planet Sakaar where he is sold into slavery and trained as a gladiator.'''

nlp = spacy.load('en_core_web_md')
# Load movies text file
with open('movies.txt', 'r') as file:
    # Add movies from text file to the list
    movie_list = []
    for string in file:
        movie_list.append(string.strip()) 
# Definition of a function that analyzes the similarity between the video and 
# the description of the "des" pattern
def func(des, movie_list):
    max_val = 0
    movie_at_max = "" 
    for sentence in movie_list:
            doc_sentence = nlp(sentence)
            similarity = doc_sentence.similarity(nlp(des)) # Determining the similarity of the movie with the pattern "des"
            # Searching movie with maximum similarity
            if similarity > max_val:
                max_val = similarity
                movie_at_max = sentence

    print(movie_at_max) # Output - next movie to watch

print('recomandation - next film to the watch is:')
func(des, movie_list) # Calling the function