class Pokemon:
    def __init__(self, nombre, numero, tipos):
        self.nombre = nombre
        self.numero = numero
        self.tipos = tipos 

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None

class ArbolBusquedaBinaria:
    def __init__(self, indice):
        self.raiz = None
        self.indice = indice 

    def insertar(self, pokemon):
        self.raiz = self._insertar_recursivo(self.raiz, pokemon)

    def _insertar_recursivo(self, nodo, pokemon):
        if nodo is None:
            return Nodo(pokemon)
        
        clave = getattr(pokemon, self.indice)
        nodo_clave = getattr(nodo.valor, self.indice)

        if clave < nodo_clave:
            nodo.izquierdo = self._insertar_recursivo(nodo.izquierdo, pokemon)
        else:
            nodo.derecho = self._insertar_recursivo(nodo.derecho, pokemon)
        
        return nodo

    def buscar_por_numero(self, numero):
        return self._buscar_por_numero(self.raiz, numero)

    def _buscar_por_numero(self, nodo, numero):
        if nodo is None:
            return None
        if nodo.valor.numero == numero:
            return nodo.valor
        elif numero < nodo.valor.numero:
            return self._buscar_por_numero(nodo.izquierdo, numero)
        else:
            return self._buscar_por_numero(nodo.derecho, numero)

    def buscar_por_nombre(self, nombre):
        return self._buscar_por_nombre(self.raiz, nombre)

    def _buscar_por_nombre(self, nodo, nombre):
        if nodo is None:
            return None
        if nodo.valor.nombre == nombre:
            return nodo.valor
        elif nombre < nodo.valor.nombre:
            return self._buscar_por_nombre(nodo.izquierdo, nombre)
        else:
            return self._buscar_por_nombre(nodo.derecho, nombre)

    def buscar_por_proximidad_nombre(self, texto):
        resultados = []
        self._buscar_por_proximidad_nombre(self.raiz, texto, resultados)
        return resultados

    def _buscar_por_proximidad_nombre(self, nodo, texto, resultados):
        if nodo:
            if texto.lower() in nodo.valor.nombre.lower():
                resultados.append(nodo.valor)
            self._buscar_por_proximidad_nombre(nodo.izquierdo, texto, resultados)
            self._buscar_por_proximidad_nombre(nodo.derecho, texto, resultados)
    
    def contar_tipos(self, tipo_buscado):
        return self._contar_tipos(self.raiz, tipo_buscado)

    def _contar_tipos(self, nodo, tipo_buscado):
        if nodo is None:
            return 0
        contador = self._contar_tipos(nodo.izquierdo, tipo_buscado)
        contador += self._contar_tipos(nodo.derecho, tipo_buscado)
        if tipo_buscado in nodo.valor.tipos: 
            contador += 1
        return contador

    def listar_por_numero(self):
        return self._listar_por_numero(self.raiz)

    def _listar_por_numero(self, nodo):
        nombres = []
        if nodo:
            nombres.extend(self._listar_por_numero(nodo.izquierdo))
            nombres.append(nodo.valor.nombre)
            nombres.extend(self._listar_por_numero(nodo.derecho))
        return nombres

    def listar_por_nombre(self):
        return self._listar_por_nombre(self.raiz)

    def _listar_por_nombre(self, nodo):
        nombres = []
        if nodo:
            nombres.extend(self._listar_por_nombre(nodo.izquierdo))
            nombres.append(nodo.valor.nombre)
            nombres.extend(self._listar_por_nombre(nodo.derecho))
        return nombres

    def listar_por_tipo(self, tipo_buscado):
        nombres = []
        self._listar_por_tipo(self.raiz, tipo_buscado, nombres)
        return nombres

    def _listar_por_tipo(self, nodo, tipo_buscado, nombres):
        if nodo is None:
            return
        if tipo_buscado in nodo.valor.tipos:
            nombres.append(nodo.valor.nombre)
        self._listar_por_tipo(nodo.izquierdo, tipo_buscado, nombres)
        self._listar_por_tipo(nodo.derecho, tipo_buscado, nombres)

pokemon_datos = [
    Pokemon("Bulbasaur", 1, ["Planta", "Veneno"]),
    Pokemon("Charmander", 4, ["Fuego"]),
    Pokemon("Squirtle", 7, ["Agua"]),
    Pokemon("Pikachu", 25, ["Eléctrico"]),
    Pokemon("Jolteon", 135, ["Eléctrico"]),
    Pokemon("Lycanroc", 745, ["Roca"]),
    Pokemon("Tyrantrum", 697, ["Roca", "Dragón"]),
    Pokemon("Charizard", 6, ["Fuego", "Volador"]),
    Pokemon("Gengar", 94, ["Fantasma", "Veneno"]),
    Pokemon("Eevee", 133, ["Normal"]),
    Pokemon("Mewtwo", 150, ["Psíquico"]),
    Pokemon("Greninja", 658, ["Agua", "Siniestro"]),
    Pokemon("Lucario", 448, ["Lucha", "Acero"]),
    Pokemon("Incineroar", 727, ["Fuego", "Siniestro"]),
    Pokemon("Rowlet", 722, ["Planta", "Volador"]),
    Pokemon("Sobble", 816, ["Agua"]),
    Pokemon("Grookey", 810, ["Planta"]),
    Pokemon("Scorbunny", 813, ["Fuego"]),
    Pokemon("Rillaboom", 812, ["Planta"]),
    Pokemon("Cinderace", 815, ["Fuego"]),
    Pokemon("Toxtricity", 849, ["Eléctrico", "Veneno"]),
    Pokemon("Corviknight", 823, ["Volador", "Acero"]),
    Pokemon("Zacian", 888, ["Hada", "Acero"]),
    Pokemon("Eternatus", 890, ["Veneno", "Dragón"]),
    Pokemon("Regieleki", 894, ["Eléctrico"]),
    Pokemon("Dragapult", 887, ["Dragón", "Fantasma"]),
    Pokemon("Copperajah", 879, ["Acero"]),
    Pokemon("Rookidee", 821, ["Volador"]),
    Pokemon("Appletun", 842, ["Planta", "Dragón"]),
    Pokemon("Zamazenta", 889, ["Lucha", "Acero"]),
    Pokemon("Boltund", 836, ["Eléctrico"]),
    Pokemon("Grimmsnarl", 861, ["Siniestro", "Hada"]),
    Pokemon("Orbeetle", 826, ["Bicho", "Psíquico"]),
    Pokemon("Drednaw", 834, ["Agua", "Roca"]),
    Pokemon("Morpeko", 877, ["Eléctrico", "Siniestro"]),
    Pokemon("Hatterene", 858, ["Psíquico", "Hada"]),
    Pokemon("Cramorant", 845, ["Volador", "Agua"]),
    Pokemon("Frosmoth", 873, ["Hielo", "Bicho"]),
    Pokemon("Zarude", 893, ["Siniestro", "Planta"]),
]

arbol_por_nombre = ArbolBusquedaBinaria("nombre")
arbol_por_numero = ArbolBusquedaBinaria("numero")
arbol_por_tipo = ArbolBusquedaBinaria("tipos")

for pokemon in pokemon_datos:
    arbol_por_nombre.insertar(pokemon)
    arbol_por_numero.insertar(pokemon)
    arbol_por_tipo.insertar(pokemon)

print("Pokémons en orden ascendente por número:")
nombres_por_numero = arbol_por_numero.listar_por_numero()
for nombre in nombres_por_numero:
    print(nombre)

print("\nPokémons en orden ascendente por nombre:")
nombres_por_nombre = arbol_por_nombre.listar_por_nombre()
for nombre in nombres_por_nombre:
    print(nombre)

pokemons_a_mostrar = ["Jolteon", "Lycanroc", "Tyrantrum"]
for nombre in pokemons_a_mostrar:
    pokemon = arbol_por_nombre.buscar_por_nombre(nombre)
    if pokemon:
        print(f"\nDatos de {nombre}: {vars(pokemon)}")

numero = 25
pokemon = arbol_por_numero.buscar_por_numero(numero)
if pokemon:
    print(vars(pokemon))

nombre_parcial = "bul"
resultados = arbol_por_nombre.buscar_por_proximidad_nombre(nombre_parcial)
for pokemon in resultados:
    print(vars(pokemon))

tipo_buscado = "Eléctrico"
nombres_eléctricos = arbol_por_tipo.listar_por_tipo(tipo_buscado)
print(f"\nPokémons de tipo {tipo_buscado}: {nombres_eléctricos}")

tipo_buscado = "Agua"
nombres_agua = arbol_por_tipo.listar_por_tipo(tipo_buscado)
print(f"Pokémons de tipo {tipo_buscado}: {nombres_agua}")

tipo_buscado = "Fuego"
nombres_fuego = arbol_por_tipo.listar_por_tipo(tipo_buscado)
print(f"Pokémons de tipo {tipo_buscado}: {nombres_fuego}")

tipo_buscado = "Planta"
nombres_planta = arbol_por_tipo.listar_por_tipo(tipo_buscado)
print(f"Pokémons de tipo {tipo_buscado}: {nombres_planta}")

tipo_eléctrico = "Eléctrico"
cantidad_eléctricos = arbol_por_tipo.contar_tipos(tipo_eléctrico)
print(f"Cantidad de Pokémons de tipo {tipo_eléctrico}: {cantidad_eléctricos}")

tipo_acero = "Acero"
cantidad_aceros = arbol_por_tipo.contar_tipos(tipo_acero)
print(f"Cantidad de Pokémons de tipo {tipo_acero}: {cantidad_aceros}")
