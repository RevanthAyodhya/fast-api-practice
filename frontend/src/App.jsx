import { useEffect, useState } from "react";

function App() {
  const [users, setUsers] = useState([]);
  const [name, setName] = useState("");
  const [age, setAge] = useState("");

  useEffect(() => {
    fetchUsers();
  }, []);

  const fetchUsers = () => {
    fetch("http://127.0.0.1:8000/users")
      .then(res => res.json())
      .then(data => setUsers(data));
  };

  const createUser = () => {
    fetch("http://127.0.0.1:8000/users", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        name: name,
        age: Number(age),
        email: "test@example.com"
      })
    }).then(() => {
      fetchUsers(); // refresh list
    });
  };

  return (
    <div>
      <h1>Users</h1>

      <input
        placeholder="name"
        onChange={(e) => setName(e.target.value)}
      />
      <input
        placeholder="age"
        onChange={(e) => setAge(e.target.value)}
      />
      <button onClick={createUser}>Add User</button>

      {users.map((u) => (
        <div key={u.id}>
          {u.name} - {u.age}
        </div>
      ))}
    </div>
  );
}

export default App;