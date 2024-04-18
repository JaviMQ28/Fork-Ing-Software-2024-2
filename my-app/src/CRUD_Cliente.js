// https://es.stackoverflow.com/questions/436281/navegacion-en-la-misma-pagina-con-react
// 
import React, { useState } from "react";

import "./App.css";

import Clientes from "./components_Cliente/Clientes/Clientes";
import NuevoCliente from "./components_Cliente/NuevoCliente/NuevoCliente";
import EliminaCliente from "./components_Cliente/EliminaCliente/EliminaCliente";
import ActualizaCliente from "./components_Cliente/ActualizaCliente/ActualizaCliente";

const CRUD_Cliente = ({onClick}) => {

///*
  const [clientes, setClientes] = useState([
    {
      id: "1",
      nombre: "Fernando",
      apellidoPaterno: "Ramírez",
      apellidoMaterno: "Ortiz",
      contrasenia: "esta_es_mia",
      correo: "fer@gmail.com",
      fotoPerfil: "-",
      superUsuario: "1",
    },
    {
      id: "2",
      nombre: "Javier Alejandro",
      apellidoPaterno: "Mancera",
      apellidoMaterno: "Quiroz",
      contrasenia: "mi_contra",
      correo: "javi@outlook.com",
      fotoPerfil: "-",
      superUsuario: "0",
    },
    {
      id: "3",
      nombre: "Lourdes",
      apellidoPaterno: "Zapata",
      apellidoMaterno: "Martínez",
      contrasenia: "otra_contra",
      correo: "lou@gmail.com",
      fotoPerfil: "-",
      superUsuario: "0",
    },
  ]);
//*/

///*
  const agregarCliente = (cliente) => {
    const nuevoCliente = [...clientes, cliente];    
    let i = 0;
    while(i <= clientes.length){
      i++;
    }
    nuevoCliente[clientes.length].id = "" + i;
    setClientes(nuevoCliente);
  };
//*/

///*
  const eliminarCliente = (id) => {
    let eliminar = clientes[0];
    let encontrado = false;
    for (let i = 0; i < clientes.length; i++) {
      console.log(clientes[i]);
      if (id === clientes[i].id) {
        eliminar = clientes[i];
        encontrado = true;
      }
    }    
    if (!encontrado) {
      alert("El identificador no existe!!");
      return;
    }    
    const nuevaListaClientes = clientes.filter(cliente => cliente !== eliminar);
    for (let i = 0; i < nuevaListaClientes.length; i++) {      
      nuevaListaClientes[i].id = "" + (i + 1);      
    }
    setClientes(nuevaListaClientes);    
  };
//*/

///*
const actualizarCliente = (cliente) => {
  let id = cliente.id;
  let eliminar = clientes[0];
  let encontrado = false;
  for (let i = 0; i < clientes.length; i++) {
    console.log(clientes[i]);
    if (id === clientes[i].id) {
      eliminar = clientes[i];
      encontrado = true;
    }
  }    
  if (!encontrado) {
    alert("El identificador no existe!!");
    return;
  }    
  let nuevaListaClientes = clientes.filter(cliente => cliente !== eliminar);
  cliente.id = eliminar.id;
  nuevaListaClientes = [...nuevaListaClientes, cliente];
  setClientes(nuevaListaClientes);    
};
//*/

  return (
    <div className="Cliente">
      <NuevoCliente onAgregarCliente={agregarCliente} />       
      <EliminaCliente onEliminarCliente={eliminarCliente} />            
      <ActualizaCliente onActualizarCliente={actualizarCliente} />            
      <Clientes clientes={clientes}/>
      <button onClick={() => onClick(0)}>Regresar</button>
    </div>
  );
}

export default CRUD_Cliente;
