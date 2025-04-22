with open ("samuelfile","w") as sam:
    sam.write("testing writting test")
    print("escribiendo")

try:
    with open("samuelfile11","r") as sam:
        contenido = sam.read()
        print(contenido)

except Exception as e:
    print(e)

finally:
    print("close db connection")