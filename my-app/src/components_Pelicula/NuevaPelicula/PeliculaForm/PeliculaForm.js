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

  const cambioGeneroHandler = (event) => {
    setGeneroIngresado(event.target.value);
  };

  const cambioDuracionHandler = (event) => {
    setDuracionIngresado(event.target.value);
  };

  const cambioInventarioHandler = (event) => {
    setInventarioIngresado(event.target.value);
  };

  const submitHandler = (event) => {
    event.preventDefault();

    const pelicula = {
      id: idIngresado,
      nombre: nombreIngresado,
      genero: generoIngresado,
      duracion: duracionIngresado,
      inventario: inventarioIngresado,
    };
    if (
      nombreIngresado === "" ||
      generoIngresado === "" ||
      duracionIngresado === "" ||
      inventarioIngresado === ""
    ) {
      alert("Campos vacíos!!");
      return;
    }
    props.onGuardarPelicula(pelicula);
    setIdIngresado("");
    setNombreIngresado("");
    setGeneroIngresado("");
    setDuracionIngresado("");
    setInventarioIngresado("");
  };

  return (
    <form onSubmit={submitHandler}>
      <div className="nueva-pelicula__controls">
        <div className="nueva-pelicula__control">
          <label>Identificador: </label>
          <input
            type="text"
            value={"Asignado"}
            onChange={cambioIdHandler}
            readonly
          />
        </div>
        <div className="nueva-pelicula__control">
          <label>Nombre: </label>
          <input
            type="text"
            value={nombreIngresado}
            onChange={cambioNombreHandler}
          />
        </div>
        <div className="nueva-pelicula__control">
          <label>Género: </label>
          <input
            type="text"
            value={generoIngresado}
            onChange={cambioGeneroHandler}
          />
        </div>        
        <div className="nueva-pelicula__control">
          <label>Duración: </label>
          <input
            type="text"
            value={duracionIngresado}
            onChange={cambioDuracionHandler}
          />
        </div>
        <div className="nueva-pelicula__control">
          <label>Inventario: </label>
          <input
            type="text"
            value={inventarioIngresado}
            onChange={cambioInventarioHandler}
          />
        </div>
        <div className="nueva-pelicula__actions">
          <button type="submit">Agregar película</button>
        </div>
      </div>
    </form>
  );
};

export default PeliculaForm;
