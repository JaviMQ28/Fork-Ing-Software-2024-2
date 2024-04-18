import React, { useState } from "react";

import "./App.css";

import Rentas from "./components_Renta/Rentas/Rentas";
import NuevaRenta from "./components_Renta/NuevaRenta/NuevaRenta";
import ActualizaRenta from "./components_Renta/ActualizaRenta/ActualizaRenta";

const CRU_Renta = ({onClick}) => {
  
  const [rentas, setRentas] = useState([
    { id: "1", idUsuario: "1", idPelicula: "1", fecha: "20/02/24", dias: "5", estatus: "0" },
    { id: "2", idUsuario: "2", idPelicula: "2", fecha: "09/10/23", dias: "10", estatus: "1" },
    { id: "3", idUsuario: "1", idPelicula: "2", fecha: "02/01/24", dias: "7", estatus: "1" },
  ]);

  const agregarRenta = (renta) => {
    const nuevaRenta = [...rentas, renta];    
    let i = 0;
    while(i <= rentas.length){
      i++;
    }
    nuevaRenta[rentas.length].id = "" + i;

    setRentas(nuevaRenta);
  };

  const actualizarRenta = (renta) => {
    let id = renta.id;
    let eliminar = rentas[0];
    let encontrado = false;
    for (let i = 0; i < rentas.length; i++) {
      console.log(rentas[i]);
      if (id === rentas[i].id) {
        eliminar = rentas[i];
        encontrado = true;
      }
    }    
    if (!encontrado) {
      alert("El identificador no existe!!");
      return;
    }    
    let nuevaListaRentas = rentas.filter(renta => renta !== eliminar);
    renta.id = eliminar.id;
    renta.idUsuario = eliminar.idUsuario;
    renta.idPelicula = eliminar.idPelicula;
    renta.fecha = eliminar.fecha;
    renta.dias = eliminar.dias;
    nuevaListaRentas = [...nuevaListaRentas, renta];
    setRentas(nuevaListaRentas);    
  };

  return (
    <div className="Renta">
      <NuevaRenta onAgregarRenta={agregarRenta} />                
      <ActualizaRenta onActualizarRenta={actualizarRenta} />            
      <Rentas rentas={rentas}/>
      <button onClick={() => onClick(0)}>Regresar</button>
    </div>
  );
}

export default CRU_Renta;
