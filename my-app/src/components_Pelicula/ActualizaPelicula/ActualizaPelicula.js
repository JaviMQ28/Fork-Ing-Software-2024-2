import React from "react";

import './ActualizaPelicula.css';
import PeliculaForm from "./PeliculaForm/PeliculaForm";

const ActualizaPelicula = (props) => {    

    const actualizaPeliculaHandler = (idIngresado) => {     
        props.onActualizarPelicula(idIngresado);
    };

    return (
        <div className="actualiza-pelicula">
            <PeliculaForm onActualizarPelicula={actualizaPeliculaHandler} />
        </div>
    )
}

export default ActualizaPelicula;