import React from "react";
import Card from '../UI/Card';
import Renta from "./Renta/Renta";
import './Rentas.css';

const Rentas = (props) => {    
    const rentas = props.rentas;
    const sidebar = (
        <ul style={{ textAlign: 'left'}}>            
            {rentas.map((renta) =>
                <div key={renta.id}>                
                <li>Renta-id: {renta.id}
                    <br/>- Identificador de usuario: {renta.idUsuario}
                    <br/>- Identificador de película: {renta.idPelicula}
                    <br/>- Fecha de renta: {renta.fecha}
                    <br/>- Días de renta: {renta.dias}
                    <br/>- Estado: {renta.estatus}
                </li>
                </div>
            )}
        </ul>
    );
    return (
        <div>
            {sidebar}      
            <hr />  
        </div>
    );
};

export default Rentas;