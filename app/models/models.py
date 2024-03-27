models = [
    '''
    CREATE TABLE tema (
    id VARCHAR(60) PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL
    );
    ''',
    '''
    CREATE TABLE colores_tema (
    id VARCHAR(60) PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    valor VARCHAR(20),
    temas VARCHAR(60),
    FOREING KEY (temas) REFERENCES tema(id)
    );
    ''',
    '''
    CREATE TABLE perfil (
    id VARCHAR(60) PRIMARY KEY,
    alias VARCHAR(50) NOT NULL
    );
    ''',
    '''
    CREATE TABLE datos_perfil (
    id VARCHAR(60) PRIMARY KEY,
    nombre VARCHAR(150) NOT NULL,
    presentacion VARCHAR(500),
    titulo VARCHAR(100),
    sobre_mi VARCHAR(600),
    perfil VARCHAR(60),
    FOREING KEY (perfil) REFERENCES perfil(id)
    );
    ''',
    '''
    CREATE TABLE configuraciones (
    id VARCHAR(60) PRIMARY KEY,
    clave VARCHAR(100) NOT NULL,
    valor VARCHAR(20)
    );
    ''',

]