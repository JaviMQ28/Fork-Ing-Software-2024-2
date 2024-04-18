import React, { useState } from "react";

import "./RentaForm.css";

const RentaForm = (props) => {
  const [idIngresado, setIdIngresado] = useState("");
  const [idUsuarioIngresado, setIdUsuarioIngresado] = useState("");
  const [idPeliculaIngresado, setIdPeliculaIngresado] = useState("");
  const [fechaIngresado, setFechaIngresado] = useState("");
  const [diasIngresado, setDiasIngresado] = useState("");
  const [estatusIngresado, setEstatusIngresado] = useState("");  

  const cambioIdHandler = (event) => {
    setIdIngresado(event.target.value);
  };
  
  const cambioIdUsuarioHandler = (event) => {
    setIdUsuarioIngresado(event.target.value);
  };

  const cambioIdPeliculaHandler = (event) => {
    setIdPeliculaIngresado(event.target.value);
  };

  const cambioFechaHandler = (event) => {
    setFechaIngresado(event.target.value);
  };

  const cambioDiasHandler = (event) => {
    setDiasIngresado(event.target.value);
  };

  const cambioEstatusHandler = (event) => {
    setEstatusIngresado(event.target.value);
  };

  const submitHandler = (event) => {
    event.preventDefault();

    const renta = {
      id: idIngresado,
      idUsuario: idUsuarioIngresado,
      idPelicula: idPeliculaIngresado,
      fecha: fechaIngresado,
      dias: diasIngresado,
      estatus: estatusIngresado,
    };
    if (
      idUsuarioIngresado === "" ||
      idPeliculaIngresado === "" ||
      fechaIngresado === "" ||
      diasIngresado === "" ||
      estatusIngresado === ""
    ) {
      alert("Campos vacíos!!");
      return;
    }
    props.onGuardarRenta(renta);
    setIdIngresado("");
    setIdUsuarioIngresado("");
    setIdPeliculaIngresado("");
    setFechaIngresado("");
    setDiasIngresado("");
    setEstatusIngresado("");    
  };

  return (
    <form onSubmit={submitHandler}>
      <div className="nueva-renta__controls">
        <div className="nueva-renta__control">
          <label>Identificador: </label>
          <input
            type="text"
            value={"Asignado"}
            onChange={cambioIdHandler}
            readonly
          />
        </div>
        <div className="nueva-renta__control">
          <label>Identificador del usuario: </label>
          <input
            type="text"
            value={idUsuarioIngresado}
            onChange={cambioIdUsuarioHandler}
          />
        </div>
        <div className="nueva-renta__control">
          <label>Identificador de la película: </label>
          <input
            type="text"
            value={idPeliculaIngresado}
            onChange={cambioIdPeliculaHandler}
          />
        </div>    
        <div className="nueva-renta__control">
          <label>Fecha de renta: </label>
          <input
            type="text"
            value={fechaIngresado}
            onChange={cambioFechaHandler}
          />
        </div>    
        <div className="nueva-renta__control">
          <label>Días de renta: </label>
          <input
            type="text"
            value={diasIngresado}
            onChange={cambioDiasHandler}
          />
        </div>
        <div className="nueva-renta__control">
          <label>Estado: </label>
          <input
            type="text"
            value={estatusIngresado}
            onChange={cambioEstatusHandler}
          />
        </div>
        <div className="nueva-renta__actions">
          <button type="submit">Agregar película</button>
        </div>
      </div>
    </form>
  );
};

export default RentaForm;
