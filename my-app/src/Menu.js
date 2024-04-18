// https://es.stackoverflow.com/questions/436281/navegacion-en-la-misma-pagina-con-react
// 
import React, { useState } from "react";

const Menu = ({onClick}) => {
  return (                
    <div className="Menu">
      <h1>Menu</h1>
      <button onClick={() => onClick(1)}>Cliente</button>
      <button onClick={() => onClick(2)}>Pelicula</button>
      <button onClick={() => onClick(3)}>Renta</button>
    </div>
  );
}

export default Menu;
