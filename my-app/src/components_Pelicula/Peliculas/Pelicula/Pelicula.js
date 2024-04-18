import React from "react";

import Card from '../../UI/Card';
import './Pelicula.css';

const Pelicula = (props) => {
    return (
        <Card className='pelicula'>
            <div className="pelicula__description">
                <h2>{props.id}</h2>
                <h2>{props.nombre}</h2>
                <h2>{props.genero}</h2>
                <h2>{props.duracion}</h2>
                <h2>{props.inventario}</h2>
            </div>
        </Card>
    );
}

export default Pelicula