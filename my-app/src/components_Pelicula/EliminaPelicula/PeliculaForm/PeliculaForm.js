import React, { useState } from "react";

import "./PeliculaForm.css";

const PeliculaForm = (props) => {
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
    props.onEliminarPelicula(idIngresado);
  };

  return (
    <form onSubmit={submitHandler}>
      <div className="elimina-pelicula__controls">
        <div className="elimina-pelicula__control">
          <label>Identificador: </label>
          <input
            type="text"
            value={idIngresado}
            onChange={cambioIdHandler}
          />
        </div>
        <div className="elimina-pelicula__actions">
          <button type="submit">Eliminar película</button>
        </div>
      </div>
    </form>
  );
};

export default PeliculaForm;
