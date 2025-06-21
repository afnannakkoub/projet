import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import Home from "./pages/Home";
import LoginForm from "./components/LoginForm";
import RegisterForm from "./components/RegisterForm";
import Dashboard from "./pages/Dashboard";
import MoodTracker from "./components/MoodTracker";
import ChatBox from "./components/ChatBox";

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/login" element={<LoginForm />} />
        <Route path="/register" element={<RegisterForm />} />
        <Route path="/dashboard" element={<Dashboard />} />
        <Route path="/moods" element={<MoodTracker />} />
        <Route path="/chat" element={<ChatBox />} />
      </Routes>
    </Router>
  );
}

export default App;
