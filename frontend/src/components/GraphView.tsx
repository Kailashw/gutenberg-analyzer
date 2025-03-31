import ForceGraph2D from "react-force-graph-2d";

export default function GraphView({ data }: any) {
  return (
    <div style={{ height: "600px" }}>
      <ForceGraph2D
        graphData={data}
        nodeAutoColorBy="id"
        linkDirectionalParticles="value"
        linkDirectionalParticleSpeed={(d) => d.weight * 0.001}
      />
    </div>
  );
}
