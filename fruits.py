from sklearn import tree

fruits = { "pera": 1, "laranja": 2, "amora": 3, "maca": 4 }
colors = { "amarela": 1, "roxa": 2, "verde": 3, "vermelha": 4 }

fruits_weight = [[colors["verde"], 100], [colors["verde"], 110], [colors["verde"], 118],
                [colors["amarela"], 130], [colors["amarela"], 150],
                [colors["roxa"], 20],[colors["roxa"],30], [colors["roxa"], 24], [colors["roxa"],32],
                [colors["vermelha"], 50], [colors["vermelha"], 60], [colors["vermelha"], 70]]

result = [fruits["pera"], fruits["pera"],fruits["pera"],
             fruits["laranja"], fruits["laranja"],
             fruits["amora"], fruits["amora"],fruits["amora"],fruits["amora"],
             fruits["maca"], fruits["maca"],fruits["maca"]]


clf = tree.DecisionTreeClassifier()
clf = clf.fit(fruits_weight, result)

weight = input("Digite o peso da fruta: ")
color  = input("Digite a cor da fruta: ")

response = clf.predict([[colors[color], weight]])

print([k for k,v in fruits.items() if v == response ])

