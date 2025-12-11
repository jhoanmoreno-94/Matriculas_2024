import pandas as pd
archivo = 'https://github.com/jhoanmoreno-94/Matriculas_2024/raw/refs/heads/main/notas.xlsx'
df = pd.read_excel(archivo)
def menu():
  print("MENU")
  print("1. Agregar")
  print("2. Buscar")
  print("3. Modificar")
  print("4. Cancelación de materias")
  print("5. Resultados por estudiante")
  print("6. Salir")
  return int(input("Digite una opción: "))

def agregar (df,archivo):
  while True:
    id_nuevo = int(input("Digite el número de identificación: "))
    if id_nuevo in df['Identificación'].values:
      print("El número de identificación ya existe. Por favor digite otro.")
    else:
      break
  nuevo = {
        "Identificación": id_nuevo,
        "Nombre": input("Digite el nombre: "),
        "Email": input("Digite el correo electrónico: "),
        "Telefono": input("Digite el número de teléfono: ").strip(),
        "F_nacimiento": input("Digite la fecha de nacimiento (dd-mm-aa): "),
        "Nota_1": float(input("Digite la nota 1: ")),
        "Nota_2": float(input("Digite la nota 2: ")),
        "Nota_3": float(input("Digite la nota 3: ")),
        "Nota_4": float(input("Digite la nota 4: "))
        }
  nuevo_df = pd.DataFrame([nuevo])
  df = pd.concat([df, nuevo_df], ignore_index=True)
  df.to_excel(archivo, index=False)
  print("Estudiante agregado correctamente. \n")
  return df

def buscar(df):
  busc = int(input("Digite el número de identificación del estudiante: "))
  resultado = df[df['Identificación']==busc]
  if resultado.empty:
    print("El estudiante no existe")
    return None
  else:
    print("Estudiante encontrado")
    print(resultado.T.to_string(header=False))
    return resultado

def modificar(df, archivo):
  modifi = int(input("Digite el número de identificación, el cual desea modificar las notas: "))
  modiresul = df[df['Identificación']==modifi]
  if modiresul.empty:
    print("El estudiante no existe")
    return df
  est = modiresul.iloc[0]
  print(f"\nNotas actuales: {est['Nota_1']}, {est['Nota_2']}, {est['Nota_3']}, {est['Nota_4']}")

  nueva_nota_1 = float(input("Digite la nueva nota 1: "))
  nueva_nota_2 = float(input("Digite la nueva nota 2: "))
  nueva_nota_3 = float(input("Digite la nueva nota 3: "))
  nueva_nota_4 = float(input("Digite la nueva nota 4: "))

  df.loc[df['Identificación']== modifi, ['Nota_1', 'Nota_2', 'Nota_3', 'Nota_4']] = [
      nueva_nota_1, nueva_nota_2, nueva_nota_3, nueva_nota_4
  ]
  df.to_excel(archivo, index=False)
  print("Notas modificadas correctamente")
  return df
def eliminar_registro(df, archivo):
  buscaelim = int(input("Digite el número de identificación que desea eliminar: "))
  found_regis = df[df['Identificación']==buscaelim]
  if found_regis.empty:
    print("El estudiante no existe")
    return df
  confirm = input("¿Está seguro que desea eliminar este estudiante? (si/no):").lower()
  if confirm == 'si':
    df = df[df['Identificación']!= buscaelim]
    df.to_excel(archivo, index=False)
    print("Estudiante eliminado correctamente")
  else:
    print("Operación cancelada")
  return df

def resul_estudiantes(df):
   resultado = buscar(df)
   if resultado is None:
      return
   est = resultado.iloc[0]
   nota_final = (est['Nota_1'] + est['Nota_2'] + est['Nota_3'] + est['Nota_4']) / 4
   print(f"La nota final del estudiante {est['Nombre']} es {nota_final}")
   if nota_final >= 3:
      print("El estudiante ganó el curso")
   else:
      print("El estudiante perdió el curso")
   promedios = df[['Nota_1','Nota_2','Nota_3','Nota_4']].mean(axis=1)
   promedio_grupo = promedios.mean()
   print(f"Promedio del grupo: {promedio_grupo:.2f}")

   
   if nota_final > promedio_grupo:
      print("El estudiante está por encima de la media")
   else:
      print("El estudiante está por debajo de la media")

   percentiles = promedios.rank(pct=True) * 100
   percentil_est = percentiles.loc[df['Identificación'] == est['Identificación']].iloc[0]
   print(f"Percentil del estudiante dentro del grupo: {percentil_est:.2f}")

opcion = 0

while opcion != 6:
    opcion = menu()

    if opcion == 1:
        df = agregar(df, archivo)

    elif opcion == 2:
        _ = buscar(df)

    elif opcion == 3:
        df = modificar(df, archivo)

    elif opcion == 4:
        df = eliminar_registro(df, archivo)

    elif opcion == 5:
        resul_estudiantes(df)

    elif opcion == 6:
        print("Saliendo del sistema...")

    else:
        print("Opción inválida, intente de nuevo.")