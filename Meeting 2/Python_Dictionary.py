movie = { 
    'title': 'Jumanji : The Next Level',
    'year': 2017,
    'genre' :'Adventure',  
}

movie_2 = { 
    'title': 'Frozen 2',
    'year': 2019,
    'genre' :'Family',  
}

print(movie["title"])

movie.update({'viewers': 44324578}) #Added new items
movie["genre"] = "Adventure/Comedy" #Changing the value of the genre key
del movie['year'] #Removing year items

movie_2.update({'viewers': 98698637}) #Added new items
movie_2["genre"] = "Family/Musical" #Changing the value of the genre key

print(movie)
print(movie_2)