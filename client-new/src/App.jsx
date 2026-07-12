import "./App.css";
import { useState } from "react";
import users from "./data/user";

function App() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [message, setMessage] = useState("");

  const handleLogin = () => {
    const user = users.find(
      (u) => u.email === email && u.password === password
    );

    if (user) {
      setMessage("Welcome " + user.role);
      setRole(user.role);
    } else {
      setMessage("Invalid Email or Password");
    }
  };

  return (
    <div className="login-container">
      <div className="login-box">
        <h1>TransitOps</h1>
        <h3>Login</h3>

        <input
          type="email"
          placeholder="Enter Email"
          onChange={(e) => setEmail(e.target.value)}
        />

        <input
          type="password"
          placeholder="Enter Password"
          onChange={(e) => setPassword(e.target.value)}
        />

        <button onClick={handleLogin}>Login</button>

        <p>{message}</p>
        {role && (
  <div>
    <h2>Dashboard</h2>
    <p>Active Vehicles: 25</p>
    <p>Drivers: 18</p>
    <p>Trips Today: 42</p>
    <p>Revenue: ₹1,20,000</p>
  </div>
)}
      </div>
    </div>
  );
}

export default App;