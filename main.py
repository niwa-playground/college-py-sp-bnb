from graph import graph
from data import denah, all_etalase
from utils import search_etalase

belanja = ["mie instan", "pasta gigi", "shampo",
           "sabun", "roti", "deterjen", "sosis", "nugget"]
kasus = search_etalase(all_etalase, belanja)

denah = graph(denah)

print(kasus)

# tanpa step
# denah.bnb_tree(lokasi=kasus)

# dengan step
denah.bnb_tree(lokasi=kasus, showStep=True)
