import React from "react";

import Card from '../../UI/Card';
import './Cliente.css';

const Cliente = (props) => {
    return (
        <Card className='cliente'>
            <div className="cliente__description">
                <h2>{props.id}</h2>
                <h2>{props.nombre}</h2>
                <h2>{props.apellidoPaterno}</h2>
                <h2>{props.apellidoMaterno}</h2>
                <h2>{props.contrasenia}</h2>
                <h2>{props.correo}</h2>
                <h2>{props.fotoPerfil}</h2>
                <h2>{props.superUsuario}</h2>
            </div>
        </Card>
    );
}

export default Cliente