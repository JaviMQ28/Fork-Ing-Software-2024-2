import React, { useState } from "react";

import "./ClienteForm.css";
import "../../Clientes/Clientes.css"

const ClienteForm = (props) => {  
  const [idIngresado, setIdIngresado] = useState("");

  const cambioIdHandler = (event) => {
    setIdIngresado(event.target.value);
  };

  const submitHandler = (event) => {
    event.preventDefault();

    if (
      idIngresado === ""
    ) {
      alert("Campos vacíos!!");
      return;
    }

    /*
    setlista((prevState) =>
      prevState.filter((listaClientes, index) => index !== indexItem)
    );
    */

    /*
    if (
      idIngresado === ""
    ) {
      alert("Campos vacíos!!");
      return;
    }
    
    const clientes_lista = props.clientes    
    for (let i = 0; i < clientes_lista.length; i++) {
      if (id === clientes_lista[i].id) {
        cliente = {
          id: idIngresado,
          nombrePaterno: idIngresado,      
        };
      }      
    }
    
    if (
      props.cliente.id !== id
    ) {
      alert("El identificador no existe!!");
      return;
    }
    */

    props.onEliminarCliente(idIngresado);
  };

  return (
    <form onSubmit={submitHandler}>
      <div className="elimina-cliente__controls">
        <div className="elimina-cliente__control">
          <label>Identificador: </label>
          <input
            type="text"
            value={idIngresado}
            onChange={cambioIdHandler}
          />
        </div>
        <div className="elimina-cliente__actions">
          <button type="submit">Eliminar cliente</button>
        </div>
      </div>
    </form>
  );
};

export default ClienteForm;
