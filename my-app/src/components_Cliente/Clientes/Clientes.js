import React from "react";
import Card from '../UI/Card';
import Cliente from "./Cliente/Cliente";
import './Clientes.css';

const Clientes = (props) => {    
    const clientes = props.clientes;
    const sidebar = (
        <ul style={{ textAlign: 'left'}}>            
            {clientes.map((cliente) =>
                <div key={cliente.id}>                
                <li>Usuario: {cliente.nombre} {cliente.apellidoPaterno} {cliente.apellidoMaterno}
                    <br/>- Identificador: {cliente.id}
                    <br/>- Contraseña: {cliente.contrasenia}
                    <br/>- Correo electrónico: {cliente.correo}
                    <br/>- Foto de perfil: {cliente.fotoPerfil}
                    <br/>- Super Usuario = {cliente.superUsuario}
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

export default Clientes;