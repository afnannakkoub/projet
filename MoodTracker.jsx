import { useEffect, useState } from "react";
import api from "../services/api";

export default function MoodTracker() {
  const [mood, setMood] = useState("");
  const [note, setNote] = useState("");
  const [entries, setEntries] = useState([]);

  const handleSubmit = async (e) => {
    e.preventDefault();
    await api.post("/moods", { mood, note });
    loadMoods();
  };

  const loadMoods = async () => {
    const res = await api.get("/moods");
    setEntries(res.data);
  };

  useEffect(() => {
    loadMoods();
  }, []);

  return (
    <div>
      <h3>Suivi de l’humeur</h3>
      <form onSubmit={handleSubmit}>
        <input value={mood} onChange={e => setMood(e.target.value)} placeholder="Humeur du jour" />
        <textarea value={note} onChange={e => setNote(e.target.value)} placeholder="Note" />
        <button type="submit">Enregistrer</button>
      </form>
      <ul>
        {entries.map(e => (
          <li key={e.id}>{e.mood} - {new Date(e.date).toLocaleString()}</li>
        ))}
      </ul>
    </div>
  );
}
