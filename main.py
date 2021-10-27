import statistics as st
data = list()
for indice in range(1):
    data.append(float(input("Primer dato?: ")))
for indice in range(1):
    data.append(float(input("Segundo dato?: ")))
for indice in range(1):
        data.append(float(input("Tercer dato?: ")))
dato = st.mean(data)
print("Media:", dato)
dato2 = st.median(data)
print("Mediana:", dato2)
dato3 = st.variance(data)
print("Varianza:", dato3)