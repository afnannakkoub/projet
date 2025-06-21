import { Link } from "react-router-dom";

export default function Home() {
  return (
    <div>
      <h1>Bienvenue sur la plateforme santé mentale</h1>
      <Link to="/login">Connexion</Link>
      <Link to="/register">Inscription</Link>
    </div>
  );
}

