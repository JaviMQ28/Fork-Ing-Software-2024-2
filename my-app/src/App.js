import React, { useState } from "react";

import "./App.css";
import Menu from "./Menu";
import CRUD_Cliente from "./CRUD_Cliente";
import CRUD_Pelicula from "./CRUD_Pelicula";
import CRU_Renta from "./CRU_Renta";

function App() {

  const [mostrarVista, setMostrarVista] = useState(0);

  const muestraVista = (vista) => {
    setMostrarVista(vista);
  };

  return (                
    <div className="App">
      {mostrarVista === 0 && <Menu onClick={muestraVista} />}
      {mostrarVista === 1 && <CRUD_Cliente onClick={muestraVista} />}
      {mostrarVista === 2 && <CRUD_Pelicula onClick={muestraVista} />}   
      {mostrarVista === 3 && <CRU_Renta onClick={muestraVista} />}   
    </div>
  );
}

export default App;
