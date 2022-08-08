# Sukurkite klasę "Movie", kuri gebės sukurti objektus 3 savybėm ir 1 metodu.
# Naudojant šią klasę sukurkite bent du skirtingus objektus.

# Savybės:
# title: string
# director: string
# budget: number

# Metodas:
# wasExpensive() - jeigu filmo "budget" yra daugiau nei 100 000 000 mln USD, tada grąžins True, kitu atveju False.

class Movie:
    def __init__(self, title, director, budget):
        self.title = title
        self.director = director
        self.budget = budget

    def wasExpensive(self):
        if self.budget > 100000000:
            return True
        else:
            return False


movie1 = Movie('Avatar', 'J.Cameron', 200000000)
movie2 = Movie('Carie', 'S.King', 50000000)

print(movie1.wasExpensive())
print(movie2.wasExpensive())
