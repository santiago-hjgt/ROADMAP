def isMutant(dna):
   # funcion que detecta
   
    n = len(dna)
    
    # Un tablero menor a 4x4 no puede tener secuencias de 4 letras [cite: 13]
    if n < 4:
        return False

    secuencias_encontradas = 0

    # Definimos las direcciones de búsqueda: (cambio_fila, cambio_columna) [cite: 13]
    # Horizontal, Vertical, Diagonal Derecha, Diagonal Izquierda
    direcciones = [(0, 1), (1, 0), (1, 1), (1, -1)]

    # Recorremos la matriz NxN [cite: 6, 17]
    for f in range(n):
        for c in range(n):
            letra_actual = dna[f][c]

            # Verificamos cada una de las 4 direcciones posibles
            for df, dc in direcciones:
                # Calculamos el punto final de una secuencia de 4 letras
                f_final = f + (3 * df)
                c_final = c + (3 * dc)

                # Verificamos que la búsqueda no se salga de los límites de la tabla 
                if 0 <= f_final < n and 0 <= c_final < n:
                    # Comprobamos si las siguientes 3 posiciones tienen la misma letra
                    if (dna[f + df][c + dc] == letra_actual and
                        dna[f + 2*df][c + 2*dc] == letra_actual and
                        dna[f + 3*df][c + 3*dc] == letra_actual):
                        
                        secuencias_encontradas += 1

                        # Si ya encontramos más de una, es mutante 
                        if secuencias_encontradas > 1:
                            return True

    # Si revisamos todo y no hay más de una secuencia, es humano 
    return False

# Bloque de ejecución para probar en consola 
if __name__ == "__main__":
    # Ejemplo del PDF 
    dna_mutante = ["ATGCGA", "CAGTGC", "TTATGT", "AGAAGG", "CCCCTA", "TCACTG"]
    
    # Llamada a la función 
    if isMutant(dna_mutante):
        print("Resultado: True (Es Mutante)")
    else:
        print("Resultado: False (Es Humano)")
