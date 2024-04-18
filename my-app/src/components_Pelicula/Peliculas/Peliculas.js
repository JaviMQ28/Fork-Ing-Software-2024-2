import React from "react";
import Card from '../UI/Card';
import Pelicula from "./Pelicula/Pelicula";
import './Peliculas.css';

const Peliculas = (props) => {    
    const peliculas = props.peliculas;
    const sidebar = (
        <ul style={{ textAlign: 'left'}}>            
            {peliculas.map((pelicula) =>
                <div key={pelicula.id}>                
                <li>Pelicula: {pelicula.nombre}
                    <br/>- Identificador: {pelicula.id}
                    <br/>- Género: {pelicula.genero}
                    <br/>- Duración: {pelicula.duracion}
                    <br/>- Inventario: {pelicula.inventario}
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

export default Peliculas;