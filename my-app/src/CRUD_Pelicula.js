import React, { useState } from "react";

import "./App.css";

import Peliculas from "./components_Pelicula/Peliculas/Peliculas";
import NuevaPelicula from "./components_Pelicula/NuevaPelicula/NuevaPelicula";
import EliminaPelicula from "./components_Pelicula/EliminaPelicula/EliminaPelicula";
import ActualizaPelicula from "./components_Pelicula/ActualizaPelicula/ActualizaPelicula";

const CRUD_Pelicula = ({onClick}) => {

  const [peliculas, setPeliculas] = useState([
    { id: "1", nombre: "Spiderman", genero: "Acción", duracion: "1:00", inventario: "2" },
    { id: "2", nombre: "Batman", genero: "Acción", duracion: "2:00", inventario: "10" },
    { id: "3", nombre: "Inception", genero: "Ficción", duracion: "3:00", inventario: "4" },
  ]);

  const agregarPelicula = (pelicula) => {
    const nuevaPelicula = [...peliculas, pelicula];    
    let i = 0;
    while(i <= peliculas.length){
      i++;
    }
    nuevaPelicula[peliculas.length].id = "" + i;
    setPeliculas(nuevaPelicula);
  };

  const eliminarPelicula = (id) => {
    let eliminar = peliculas[0];
    let encontrado = false;
    for (let i = 0; i < peliculas.length; i++) {
      console.log(peliculas[i]);
      if (id === peliculas[i].id) {
        eliminar = peliculas[i];
        encontrado = true;
      }
    }    
    if (!encontrado) {
      alert("El identificador no existe!!");
      return;
    }    
    const nuevaListaPeliculas = peliculas.filter(pelicula => pelicula !== eliminar);
    for (let i = 0; i < nuevaListaPeliculas.length; i++) {      
      nuevaListaPeliculas[i].id = "" + (i + 1);      
    }
    setPeliculas(nuevaListaPeliculas);    
  };

  const actualizarPelicula = (pelicula) => {
    let id = pelicula.id;
    let eliminar = peliculas[0];
    let encontrado = false;
    for (let i = 0; i < peliculas.length; i++) {
      console.log(peliculas[i]);
      if (id === peliculas[i].id) {
        eliminar = peliculas[i];
        encontrado = true;
      }
    }    
    if (!encontrado) {
      alert("El identificador no existe!!");
      return;
    }    
    let nuevaListaPeliculas = peliculas.filter(pelicula => pelicula !== eliminar);
    pelicula.id = eliminar.id;
    nuevaListaPeliculas = [...nuevaListaPeliculas, pelicula];
    setPeliculas(nuevaListaPeliculas);    
  };

  return (
    <div className="Pelicula">
      <NuevaPelicula onAgregarPelicula={agregarPelicula} />       
      <EliminaPelicula onEliminarPelicula={eliminarPelicula} />            
      <ActualizaPelicula onActualizarPelicula={actualizarPelicula} />            
      <Peliculas peliculas={peliculas}/>
      <button onClick={() => onClick(0)}>Regresar</button>
    </div>
  );
}

export default CRUD_Pelicula;
