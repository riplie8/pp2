# Dictionary of movies

movies = [
{
"name": "Usual Suspects",
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]
def is_high_score(movie):
    if movie["imdb"] > 5.5:
        return True
    else:
        return False

def high_score_movies(movie_list):
    result = []
    for m in movie_list:
        if m["imdb"] > 5.5:
            result.append(m)
    return result

def movies_by_category(movie_list, category):
    result = []
    for m in movie_list:
        if m["category"].lower() == category.lower():
            result.append(m)
    return result

def average_imdb(movie_list):
    total = 0
    for m in movie_list:
        total += m["imdb"]
    return total / len(movie_list)

def average_category(movie_list, category):
    total = 0
    count = 0
    for m in movie_list:
        if m["category"].lower() == category.lower():
            total += m["imdb"]
            count += 1
    return total / count

print(is_high_score(movies[0]))
print(high_score_movies(movies))
print(movies_by_category(movies, "Romance"))
print(average_imdb(movies))
print(average_category(movies, "Romance"))