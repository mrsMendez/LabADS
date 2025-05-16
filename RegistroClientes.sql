create extension if not exists "uuid-ossp";

-- Tabla de Clientes
create table Clientes(
	id_cliente UUID primary key default uuid_generate_v4(),
	nombre varchar(100) not null,
	email  varchar(100) not null,
	fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Tabla de Direcciones 
create table Direcciones (
    id_direccion UUID primary key default uuid_generate_v4(),
    cliente_id UUID not null,
    direccion TEXT not null,
    ciudad VARCHAR(50) not null,
    pais VARCHAR(50) not null,
    foreign key (cliente_id) references Clientes(id_cliente)
);

-- Tabla de Teléfonos
create table Telefonos (
    id_telefono UUID primary key default uuid_generate_v4(),
    cliente_id UUID not null,
    numero VARCHAR(20) not null,
    foreign key (cliente_id) references Clientes(id_cliente)
);

-- Tabla de Productos
create table Productos (
    id_producto UUID primary key default uuid_generate_v4(),
    nombre VARCHAR(100) not null,
    descripcion varchar(100) not null,
    precio DECIMAL(10,2) NOT NULL,
    stock INT not null
);

-- Tabla de Compras
create table Compras (
    id_compra UUID primary key default uuid_generate_v4(),
    cliente_id UUID not null,
    fecha DATE,
    total DECIMAL(10,2) not null,
    foreign key (cliente_id) references Clientes(id_cliente)
);

-- Tabla de Facturas
create table Facturas (
    id_factura UUID primary key default uuid_generate_v4(),
    compra_id UUID not null,
    fecha DATE,
    total DECIMAL(10,2) NOT NULL,
    foreign key (compra_id) references Compras(id_compra)
);

-- Tabla de Pagos
create table Pagos (
    id_pago UUID primary key default uuid_generate_v4(),
    factura_id UUID not null,
    monto DECIMAL(10,2) not null,
    metodo_pago VARCHAR(50),
    fecha DATE,
    foreign key (factura_id) references Facturas(id_factura) 
);

-- Tabla de Descuentos
create table Descuentos (
    id_descuento UUID primary key default uuid_generate_v4(),
    producto_id UUID not null,
    porcentaje DECIMAL(5,2) ,
    fecha_inicio DATE not null,
    fecha_fin DATE not null,
    foreign key (producto_id) references Productos(id_producto) 
);

-- Tabla Historial de Compras
create table Historial (
    id_historial UUID primary key default uuid_generate_v4(),
    cliente_id UUID not null,
    producto_id UUID not null,
    fecha DATE,
    cantidad INT not null,
    precio_unitario DECIMAL(10,2) not null,
    foreign key (cliente_id) references Clientes(id_cliente) ,
    foreign key (producto_id) references Productos(id_producto) 
);

