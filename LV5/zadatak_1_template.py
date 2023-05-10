import numpy as np
import matplotlib
import matplotlib.pyplot as plt

from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score
from sklearn.metrics import confusion_matrix , ConfusionMatrixDisplay


X, y = make_classification(n_samples=200, n_features=2, n_redundant=0, n_informative=2,
                            random_state=213, n_clusters_per_class=1, class_sep=1)

# train test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=5)


# Prikažite podatke za ucenje u x1 −x2 ravnini matplotlib biblioteke pri cemu podatke obojite s obzirom na klasu. 
# Prikažite i podatke iz skupa za testiranje, ali za njih koristite drugimarker (npr. ’x’). 
# Koristite funkciju scatter koja osim podataka prima i parametre c i cmap kojima je moguce definirati boju svake klase.

plt.scatter(X_train[:,0], X_train[:,1], c=y_train, cmap=matplotlib.colors.ListedColormap(["red", "blue"]))
plt.scatter(X_test[:,0], X_test[:,1], c=y_test, marker="x", cmap=matplotlib.colors.ListedColormap(["red", "blue"]))
plt.show()


# Izgradite model logisticke regresije pomocu scikit-learn biblioteke na temelju skupa podataka za ucenje.

Log_model = LogisticRegression()
Log_model.fit( X_train , y_train )



# Pronadite u atributima izgradenog modela parametre modela. 
# Prikažite granicu odluke naucenog modela u ravnini x1 − x2 zajedno s podacima za ucenje. 
# Napomena: granica odluke u ravnini x1 −x2 definirana je kao krivulja: θ0 +θ1x1 +θ2x2 = 0.

theta0=Log_model.intercept_[0]
theta12=Log_model.coef_[0]
pravac=-(theta0/theta12[1])-(theta12[0]/theta12[1])*X_train[:,0]
plt.scatter(X_train[:,0], X_train[:,1], c=y_train, cmap=matplotlib.colors.ListedColormap(["red", "blue"]))
plt.scatter(X_train[:,0], pravac)
plt.show()

# Crtanje granice odluke
# a = -logisticRegModel.coef_[0][0] / logisticRegModel.coef_[0][1]
# b = -logisticRegModel.intercept_ / logisticRegModel.coef_[0][1]
# x1 = np.linspace(X_train[:,0].min(), X_train[:,0].max(), 100)
# x2 = a*x1 + b

# plt.plot(x1, x2, label='Granica odluke')
# plt.legend()
# plt.show()


# Provedite klasifikaciju skupa podataka za testiranje pomocu izgradenog modela logisticke regresije. 
# Izracunajte i prikažite matricu zabune na testnim podacima. 
# Izracunajte tocnost, preciznost i odziv na skupu podataka za testiranje.

y_test_p = Log_model.predict( X_test )

print("Tocnost: ", accuracy_score(y_test, y_test_p))
print("Preciznost: ", precision_score(y_test, y_test_p))
print("Odziv: ", recall_score(y_test, y_test_p))

cm = confusion_matrix (y_test, y_test_p)
print("Matrica zabune: ", cm)
disp = ConfusionMatrixDisplay(confusion_matrix( y_test, y_test_p))
disp.plot()
plt.show()



# Prikažite skup za testiranje u ravnini x1 −x2. 
# Zelenom bojom oznacite dobro klasificirane primjere dok pogrešno klasificirane primjere oznacite crnom bojom
polje=np.array([])
for i in range(len(y_test_p)):
    if y_test[i]==y_test_p[i]:
        polje=np.append(polje,1)
    else:
        polje=np.append(polje,0)


plt.scatter(X_test[:,0], X_test[:,1], c=polje, cmap=matplotlib.colors.ListedColormap(["red", "green"]))

# moze i ovako
# y_color = (y_test == y_test_p)
# plt.scatter(X_test[:, 0], X_test[:, 1], marker="o", c=y_color, s=25, cmap=matplotlib.colors.ListedColormap(["red", "green"]))
plt.show()
