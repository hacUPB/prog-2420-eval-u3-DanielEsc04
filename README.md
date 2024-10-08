[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/PehQeuqy)
# Unidad 3
---
## Documentación del proyecto
Nombre: Daniel Arango Escobar
ID: 000536416
---

### Gestion de entrenamientos
#### Descripción detallada
Se realizará el codigo que gestione los datos de entrenamiento de un atleta. En este se podrá definir si es un codigo gestione una sola disciplina o si serán multiples en caso de que dicho atleta realice varios tipos de entrenamiento, permitirá recopilar sesiones de entrenamiento para posteriormente mostrar datos como el tiempo total o la cantidad de kilometros recorridos en todos los entrenamientos.

#### Importancia 
Preparar un objetivo deportivo es complicado y necesita una organizacion, este programa podrá brindarle a un atleta toda la información de su rendimiento y le dará una mejor percepción de su proceso. 

#### Funcionalidad del programa 
Crear y almacenar planes de entrenamiento diarios o semanales.
Registrar detalles de cada sesión de entrenamiento (tipo de ejercicio, duración, distancia).
Registrar los detalles de las sesiones de entrenamiento realizadas.
Consultar el progreso a lo largo del tiempo.

#### Estructuras de datos
Diccionarios: Para almacenar la información de los entrenamientos

Listas: Para manejar las sesiones de entrenamiento 

#### Pseudocodigo
` ` ` 
funcion planificar_entrenamiento(dia, tipo, duracion, distancia):
    si dia no está en entrenamientos:
        entrenamientos[dia] = {'tipo': tipo, 'duracion': duracion, 'distancia': distancia}
        imprimir("Entrenamiento planificado para", dia, ":", tipo, ",", duracion, "minutos,", distancia, "km")
    sino:
        imprimir("Ya existe un entrenamiento planificado para el día", dia)

funcion registrar_entrenamiento(dia, tipo, duracion, distancia):
    si dia en entrenamientos:
        entrenamientos[dia]['tipo'] = tipo
        entrenamientos[dia]['duracion'] = duracion
        entrenamientos[dia]['distancia'] = distancia
        imprimir("Entrenamiento registrado para", dia, ":", tipo, ",", duracion, "minutos,", distancia, "km")
    sino:
        imprimir("No hay entrenamiento planificado para", dia)

funcion consultar_progreso():
    para cada dia en entrenamientos:
        imprimir(dia, ":", entrenamientos[dia]['tipo'], ",", entrenamientos[dia]['duracion'], "minutos,", entrenamientos[dia]['distancia'], "km")
` ` ` 
