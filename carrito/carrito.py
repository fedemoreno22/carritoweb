class Carrito:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carrito = self.session.get("carrito")
        if not carrito:
            carrito = self.session["carrito"] = {}
        #else:
        self.carrito = carrito

    def agregar(self, producto):
        if str(producto.id) not in self.carrito.keys():
            self.carrito[producto.id] = {
                "producto_id":producto.id,
                "nombre":producto.nombre,
                "precio":str(producto.precio),
                "cantidad":1,
                "imagen":producto.imagen.url,
            }
        else:
            self.carrito[str(producto.id)]["cantidad"] += 1
            '''for key, value in self.carrito.items():
                if key == str(producto.id):
                    value["cantidad"] = value["cantidad"] + 1
                    break'''
            self.carrito[str(producto.id)]["precio"] = float(self.carrito[str(producto.id)]["precio"]) + producto.precio
        self.guardar_carro()

    def guardar_carro(self):
        self.session["carrito"] = self.carrito
        self.session.modified = True

    def eliminar(self, producto):
        producto.id = str(producto.id)
        if producto.id in self.carrito:
            del self.carrito[producto.id]
            self.guardar_carro()

    def restar(self, producto):
        for key, value in self.carrito.items():
            if key == str(producto.id):
                value["cantidad"] = value["cantidad"] - 1
                value["precio"] = float(value["precio"]) - producto.precio
                if value["cantidad"] < 1:
                    self.eliminar(producto)
                break
        self.guardar_carro()

    def vaciar_carro(self):
        self.session["carrito"] = {}
        self.session.modified = True