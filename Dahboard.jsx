import { useEffect, useState } from "react";
import api from "../services/api";

export default function Dashboard() {
  const [resources, setResources] = useState([]);

  useEffect(() => {
    api.get("/resources").then((res) => setResources(res.data));
  }, []);

  return (
    <div>
      <h2>Contenu éducatif</h2>
      <ul>
        {resources.map((r) => (
          <li key={r.id}>
            <strong>{r.title}</strong> ({r.type})<br />
            <p>{r.content}</p>
          </li>
        ))}
      </ul>
    </div>
  );
}
