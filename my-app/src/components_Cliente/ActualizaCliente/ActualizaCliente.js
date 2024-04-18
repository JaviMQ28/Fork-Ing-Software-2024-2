import React from "react";

import './ActualizaCliente.css';
import ClienteForm from "./ClienteForm/ClienteForm";

const ActualizaCliente = (props) => {    

    const actualizaClienteHandler = (idIngresado) => {     
        props.onActualizarCliente(idIngresado);
    };

    return (
        <div className="actualiza-cliente">
            <ClienteForm onActualizarCliente={actualizaClienteHandler} />
        </div>
    )
}

export default ActualizaCliente;