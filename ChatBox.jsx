import { useState, useEffect } from "react";
import api from "../services/api";

export default function ChatBox() {
  const [messages, setMessages] = useState([]);
  const [content, setContent] = useState("");

  const sendMessage = async (e) => {
    e.preventDefault();
    await api.post("/messages", { content });
    setContent("");
    fetchMessages();
  };

  const fetchMessages = async () => {
    const res = await api.get("/messages");
    setMessages(res.data);
  };

  useEffect(() => {
    fetchMessages();
  }, []);

  return (
    <div>
      <h3>Forum / Discussion</h3>
      <form onSubmit={sendMessage}>
        <input value={content} onChange={e => setContent(e.target.value)} />
        <button type="submit">Envoyer</button>
      </form>
      <ul>
        {messages.map(msg => (
          <li key={msg.id}>{msg.content} ({new Date(msg.timestamp).toLocaleTimeString()})</li>
        ))}
      </ul>
    </div>
  );
}
