import React, { useEffect } from "react";
import Neo4jD3 from "./neo4jd3";
import dataJson from "./neo4jData.json"

function GraphVisualizer(props) {
  useEffect(() => {
    new Neo4jD3("#graph", {
      minCollision: 60,
      neo4jData: dataJson,
      nodeRadius: 25,
      zoomFit: true
    });
  }, []);

  return <div id="graph" />;
}

export default GraphVisualizer;
