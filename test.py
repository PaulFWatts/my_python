class Film:
    def __init__(self, title, genre, director):
        self.title = title
        self.genre = genre
        self.director = director
    def __str__(self):
        return ("`%s` by %s, is a %s film") % (self.title,self.director,self.qenre)

aFilm = Film("Star Wars", "Science Fiction", "George Lucas")
    
print(aFilm)
