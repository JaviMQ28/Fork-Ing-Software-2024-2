import React, { useState } from "react";

import "./PeliculaForm.css";

const PeliculaForm = (props) => {
  const [idIngresado, setIdIngresado] = useState("");
  const [nombreIngresado, setNombreIngresado] = useState("");
  const [generoIngresado, setGeneroIngresado] = useState("");
  const [duracionIngresado, setDuracionIngresado] = useState("");
  const [inventarioIngresado, setInventarioIngresado] = useState("");  

  const cambioIdHandler = (event) => {
    setIdIngresado(event.target.value);
  };
  
  const cambioNombreHandler = (event) => {
    setNombreIngresado(event.target.value);
  };

  const cambioGeneroIngresadoHandler = (event) => {
    setGeneroIngresado(event.target.value);
  };

  const cambioDuracionIngresadoHandler = (event) => {
    setDuracionIngresado(event.target.value);
  };

  const cambioInventarioIngresadoHandler = (event) => {
    setInventarioIngresado(event.target.value);
  };

  const submitHandler = (event) => {
    event.preventDefault();

    const cliente = {
      id: idIngresado,
      nombre: nombreIngresado,
      genero: generoIngresado,
      duracion: duracionIngresado,
      inventario: inventarioIngresado,
    };
    if (
      idIngresado === ""
    ) {
      alert("Pon un identificador válido!!");
      return;
    }
    props.onActualizarPelicula(cliente);
  };

  return (
    <form onSubmit={submitHandler}>
      <div className="actualiza-pelicula__controls">
        <div className="actualiza-pelicula__controls">
          <label>Identificador: </label>
          <input
            type="text"
            value={idIngresado}
            onChange={cambioIdHandler}
            readonly
          />
        </div>
        <div className="actualiza-pelicula__controls">
          <label>Nombre: </label>
          <input
            type="text"
            value={nombreIngresado}
            onChange={cambioNombreHandler}
          />
        </div>
        <div className="actualiza-pelicula__controls">
          <label>Género: </label>
          <input
            type="text"
            value={generoIngresado}
            onChange={cambioGeneroIngresadoHandler}
          />
        </div>        
        <div className="actualiza-pelicula__controls">
          <label>Duración: </label>
          <input
            type="text"
            value={duracionIngresado}
            onChange={cambioDuracionIngresadoHandler}
          />
        </div>
        <div className="actualiza-pelicula__controls">
          <label>Inventario: </label>
          <input
            type="text"
            value={inventarioIngresado}
            onChange={cambioInventarioIngresadoHandler}
          />
        </div>
        <div className="actualiza-pelicula__actions">          
          <button type="submit">Actualizar película</button>          
        </div>
      </div>
    </form>
  );
};

export default PeliculaForm;
