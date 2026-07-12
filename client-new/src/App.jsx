import "./App.css";

function App() {
  return (
    <div className="login-container">
      <div className="login-box">
        <h1>TransitOps</h1>
        <h3>Login</h3>

        <input type="email" placeholder="Enter Email" />
        <input type="password" placeholder="Enter Password" />

        <button>Login</button>
      </div>
    </div>
  );
}

export default App;