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
    const content = clientes.map((cliente) => 
        <div>      
            Nombre = {cliente.nombre} {cliente.apellidoPaterno} {cliente.apellidoMaterno}, Contraseña: {cliente.contrasenia}, Correo electrónico: {cliente.correo}, Foto de perfil: {cliente.fotoPerfil}, Super Usuario = {cliente.superUsuario}
        </div>
    );
    return (
        <div>
            {sidebar}      
            <hr />
            {content}    
        </div>
    );
};

export default Clientes;