# Definir cantidades necesarias para hacer una arepa
harina_por_arepa = 200 #gramos
agua_por_arepa = 120  # mililitros
sal_por_arepa = 5  # gramos

#Definir tiempo de preparación y tiempo de cocción
tiempo_preparacion = 10 #minutos
tiempo_coccion_1 = 2 #minutos
tiempo_coccion_2 = 2 #minutos

#Definir un diccionario con los ingredientes recomendados
ingredientes_recomendados = { 
    "harina": ["agua", "sal"],
    "agua": ["harina", "sal"],
    "sal": ["harina", "agua"],
    "queso": ["harina", "agua"],
    "carne": ["harina", "agua"]
}

#Cantidad de ingredientes que tenemos
harina_usuario = int(input("¿Cuántos gramos de harina tienes? "))

agua_usuario = int(input("¿Cuántos mililitros de agua tienes? "))

sal_usuario = int(input("¿Cuántos gramos de sal tienes? "))


# Calculamos la cantidad de arepas que se pueden hacer con los ingredientes del usuario
arepas_posibles = min(harina_usuario // harina_por_arepa, agua_usuario // agua_por_arepa, sal_usuario // sal_por_arepa)

#Calcular tiempo de total de preparación + cocción
tiempo_total_preparacion = tiempo_preparacion * arepas_posibles
tiempo_total_coccion = (tiempo_coccion_1 + tiempo_coccion_2) * arepas_posibles

#Mostramos el resultado mediante print
print(f"Puedes hacer {arepas_posibles} arepas con los ingredientes que tienes.")
print(f"El tiempo total de preparación será de {tiempo_total_preparacion} minutos.")
print(f"El tiempo total de cocción será de {tiempo_total_coccion} minutos.")
