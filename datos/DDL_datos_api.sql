CREATE TABLE Publicaciones (
    id INT PRIMARY KEY, 
    userId INT NOT NULL, 
    title VARCHAR(200),
    body VARCHAR(300)
);

CREATE TABLE Comentarios (
    id INT PRIMARY KEY, 
    postId INT NOT NULL, 
    name VARCHAR(150),
    email VARCHAR(100),
    body VARCHAR(200),
    FOREIGN KEY (postId) REFERENCES Publicaciones(id) 
);
