import React from "react";

import './EliminaCliente.css';
import ClienteForm from "./ClienteForm/ClienteForm";

const EliminaCliente = (props) => {
    
    const eliminaClienteHandler = (idIngresado) => {     
        props.onEliminarCliente(idIngresado);
    };

    return (
        <div className="elimina-cliente">
            <ClienteForm onEliminarCliente={eliminaClienteHandler} />
        </div>
    )
}

export default EliminaCliente;