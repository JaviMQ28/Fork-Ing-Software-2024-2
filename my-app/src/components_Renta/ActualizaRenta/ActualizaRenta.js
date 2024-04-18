import React from "react";

import './ActualizaRenta.css';
import RentaForm from "./RentaForm/RentaForm";

const ActualizaRenta = (props) => {    

    const actualizaRentaHandler = (idIngresado) => {     
        props.onActualizarRenta(idIngresado);
    };

    return (
        <div className="actualiza-renta">
            <RentaForm onActualizarRenta={actualizaRentaHandler} />
        </div>
    )
}

export default ActualizaRenta;