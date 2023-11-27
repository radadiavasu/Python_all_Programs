movies =[ 
         {"name": "Gazi Attack", "director": "Krishnan"},         
         {"name": "Uri The Surgical Strike", "director": "Narayan"},
         {"name": "Major", "director": "Venu Gopal"},
         {"name": "State of Siege-Temple Attack", "director": "Akash Chopra"},
]

def find_movie(expected, finder):
    for movie in movies:
        found = [] # if the director name was same
        if finder(movie) == expected:
            found.append(movie) # append this movie director name if director name was same.
    return found 
        
find_by = input("Which movie or director that you want to searching for?: ")
searched_by = input("What are you looking for?: ")
movie = find_movie(searched_by, lambda movie: movie[find_by])
# print(movie)
print(movies or 'No movies found.')