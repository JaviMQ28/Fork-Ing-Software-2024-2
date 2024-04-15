import React, { useState } from "react";

import "./App.css";

import Clientes from "./components/Clientes/Clientes";
import NuevoCliente from "./components/NuevoCliente/NuevoCliente";
import EliminaCliente from "./components/EliminaCliente/EliminaCliente";

function App() {
  const [peliculas, setPeliculas] = useState([
    { id: 1, title: "Spiderman", director: "Sam R." },
    { id: 2, title: "Batman", director: "Tim Burton" },
    { id: 3, title: "Inception", director: "Christopher Nolan", inventario: 4 },
  ]);

///*
  const [clientes, setClientes] = useState([
    {
      id: "1",
      nombre: "Fernando",
      apellidoPaterno: "Fong",
      apellidoMaterno: "Fong",
      contrasenia: "hola",
      correo: "no",
      fotoPerfil: "si",
      superUsuario: "1",
    },
    {
      id: "2",
      nombre: "Javi",
      apellidoPaterno: "Man",
      apellidoMaterno: "Qui",
      contrasenia: "adios",
      correo: "yes",
      fotoPerfil: "no",
      superUsuario: "0",
    },
  ]);
//*/

///*
  const agregarCliente = (cliente) => {
    const nuevoCliente = [cliente, ...clientes];
    setClientes(nuevoCliente);
    console.log(nuevoCliente);
  };
//*/

/*
const eliminarCliente = (cliente) => {
  const nuevoCliente = [cliente, ...clientes];
  setClientes(nuevoCliente);
  console.log(nuevoCliente);
};
*/

  return (
    <div className="App">
      <NuevoCliente onAgregarCliente={agregarCliente} />      
      <Clientes clientes={clientes} />
    </div>
  );
}

export default App;
