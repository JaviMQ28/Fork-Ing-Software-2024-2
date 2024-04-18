import React, { useState } from "react";

import "./RentaForm.css";

const RentaForm = (props) => {
  const [idIngresado, setIdIngresado] = useState("");
  const [estatusIngresado, setEstatusIngresado] = useState("");  

  const cambioIdHandler = (event) => {
    setIdIngresado(event.target.value);
  };

  const cambioEstatusHandler = (event) => {
    setEstatusIngresado(event.target.value);
  };

  const submitHandler = (event) => {
    event.preventDefault();

    const renta = {
      id: idIngresado,
      estatus: estatusIngresado,
    };
    if (
      idIngresado === ""
    ) {
      alert("Pon un identificador válido!!");
      return;
    }
    props.onActualizarRenta(renta);
  };

  return (
    <form onSubmit={submitHandler}>
      <div className="actualiza-renta__controls">
        <div className="actualiza-renta__controls">
          <label>Identificador: </label>
          <input
            type="text"
            value={idIngresado}
            onChange={cambioIdHandler}
            readonly
          />
        </div>
        <div className="actualiza-renta__controls">
          <label>Estado: </label>
          <input
            type="text"
            value={estatusIngresado}
            onChange={cambioEstatusHandler}
          />
        </div>
        <div className="actualiza-renta__actions">          
          <button type="submit">Actualizar renta</button>          
        </div>
      </div>
    </form>
  );
};

export default RentaForm;
