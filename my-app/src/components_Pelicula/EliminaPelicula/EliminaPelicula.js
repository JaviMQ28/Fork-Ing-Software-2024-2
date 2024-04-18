import React from "react";

import './EliminaPelicula.css';
import PeliculaForm from "./PeliculaForm/PeliculaForm";

const EliminaPelicula = (props) => {
    
    const eliminaPeliculaHandler = (idIngresado) => {     
        props.onEliminarPelicula(idIngresado);
    };

    return (
        <div className="elimina-pelicula">
            <PeliculaForm onEliminarPelicula={eliminaPeliculaHandler} />
        </div>
    )
}

export default EliminaPelicula;