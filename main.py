#Benjamin  Lemus 4°B
n = input('Nombre del artículo que va a comprar: ')
p = int(input('Precio neto de cada unidad de ese producto: '))
u = int(input('Unidades que comprara: '))
pu = p*u
iva = (p*u)*0.19
t = iva+p*u
print('Producto:', n,)
print('Unidades:', u,)
print('Subtotal:', pu,)
print('IVA:', iva,)
print('Total: ', t,)