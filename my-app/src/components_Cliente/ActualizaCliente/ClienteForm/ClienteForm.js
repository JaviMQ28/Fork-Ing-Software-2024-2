import React, { useState } from "react";

import "./ClienteForm.css";

const ClienteForm = (props) => {
  const [idIngresado, setIdIngresado] = useState("");
  const [nombreIngresado, setNombreIngresado] = useState("");
  const [apellidoPaternoIngresado, setApellidoPaternoIngresado] = useState("");
  const [apellidoMaternoIngresado, setApellidoMaternoIngresado] = useState("");
  const [contraseniaIngresado, setContraseniaIngresado] = useState("");
  const [correoIngresado, setCorreoIngresado] = useState("");
  const [fotoPerfilIngresado, setFotoPerfilIngresado] = useState("");
  const [superUsuarioIngresado, setSuperUsuarioIngresado] = useState("");

  const cambioIdHandler = (event) => {
    setIdIngresado(event.target.value);
  };
  
  const cambioNombreHandler = (event) => {
    setNombreIngresado(event.target.value);
  };

  const cambioApellidoPaternoHandler = (event) => {
    setApellidoPaternoIngresado(event.target.value);
  };

  const cambioApellidoMaternoHandler = (event) => {
    setApellidoMaternoIngresado(event.target.value);
  };

  const cambioContraseniaHandler = (event) => {
    setContraseniaIngresado(event.target.value);
  };

  const cambioCorreoHandler = (event) => {
    setCorreoIngresado(event.target.value);
  };

  const cambioFotoPerfilHandler = (event) => {
    setFotoPerfilIngresado(event.target.value);
  };

  const cambioSuperUsuarioHandler = (event) => {
    setSuperUsuarioIngresado(event.target.value);
  };

  const submitHandler = (event) => {
    event.preventDefault();

    const cliente = {
      id: idIngresado,
      nombre: nombreIngresado,
      apellidoPaterno: apellidoPaternoIngresado,
      apellidoMaterno: apellidoMaternoIngresado,
      contrasenia: contraseniaIngresado,
      correo: correoIngresado,
      fotoPerfil: fotoPerfilIngresado,
      superUsuario: superUsuarioIngresado,
    };
    if (
      idIngresado === ""
    ) {
      alert("Pon un identificador válido!!");
      return;
    }
    props.onActualizarCliente(cliente);
    /*
    setIdIngresado("");
    setNombreIngresado("");
    setApellidoPaternoIngresado("");
    setApellidoMaternoIngresado("");
    setContraseniaIngresado("");
    setCorreoIngresado("");
    setFotoPerfilIngresado("");
    setFotoPerfilIngresado("");
    setSuperUsuarioIngresado("");
    */
  };

  return (
    <form onSubmit={submitHandler}>
      <div className="actualiza-cliente__controls">
        <div className="actualiza-cliente__control">
          <label>Identificador: </label>
          <input
            type="text"
            value={idIngresado}
            onChange={cambioIdHandler}
            readonly
          />
        </div>
        <div className="actualiza-cliente__control">
          <label>Nombre: </label>
          <input
            type="text"
            value={nombreIngresado}
            onChange={cambioNombreHandler}
          />
        </div>
        <div className="actualiza-cliente__control">
          <label>Apellido Paterno: </label>
          <input
            type="text"
            value={apellidoPaternoIngresado}
            onChange={cambioApellidoPaternoHandler}
          />
        </div>
        <div className="actualiza-cliente__control">
          <label>Apellido Materno: </label>
          <input
            type="text"
            value={apellidoMaternoIngresado}
            onChange={cambioApellidoMaternoHandler}
          />
        </div>
        <div className="actualiza-cliente__control">
          <label>Contraseña: </label>
          <input
            type="text"
            value={contraseniaIngresado}
            onChange={cambioContraseniaHandler}
          />
        </div>
        <div className="actualiza-cliente__control">
          <label>Correo electrónico: </label>
          <input
            type="text"
            value={correoIngresado}
            onChange={cambioCorreoHandler}
          />
        </div>
        <div className="actualiza-cliente__control">
          <label>Foto de perfil: </label>
          <input
            type="text"
            value={fotoPerfilIngresado}
            onChange={cambioFotoPerfilHandler}
          />
        </div>
        <div className="actualiza-cliente__control">
          <label>Super usuario: </label>
          <input
            type="text"
            value={superUsuarioIngresado}
            onChange={cambioSuperUsuarioHandler}
          />
        </div>
        <div className="actualiza-cliente__actions">          
          <button type="submit">Actualizar cliente</button>          
        </div>
      </div>
    </form>
  );
};

export default ClienteForm;
