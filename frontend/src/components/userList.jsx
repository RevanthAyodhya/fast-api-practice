import { useEffect, useState } from "react";
import { getUsers, createUser,deleteUser,updateUser } from "../api/userApi";

function UserList() {
  const [users, setUsers] = useState([]);
  const [name, setName] = useState("");
  const [age, setAge] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const [editingId, setEditingId] = useState(null);

  
 useEffect(() => {
    fetchUsers();
  }, []);
  const fetchUsers = async () => {
  setLoading(true);
  setError(null);

  try {
    const data = await getUsers();
    setUsers(data);
  } catch (err) {
    console.error(err);
    setError("Failed to load users");
  } finally {
    setLoading(false);
  }
};
  const handleAddUser = async () => {
  try {
    await createUser({
      name,
      age: Number(age),
      email: "test@example.com",
    });

    setName("");
    setAge("");

    fetchUsers();
  } catch (err) {
    console.error(err);
    alert("Failed to create user");
  }
};

const handleDelete = async (id) => {
  try {
    await deleteUser(id);
    fetchUsers();
  } catch (err) {
    console.error(err);
    alert("Delete failed");
  }
};
const handleUpdate = async (id) => {
  try {
    await updateUser(id, {
      name,
      age: Number(age),
      email: "test@example.com",
    });

    setEditingId(null);
    setName("");
    setAge("");

    fetchUsers();
  } catch (err) {
    console.error(err);
    alert("Update failed");
  }
};

if (loading) return <p>Loading...</p>;
if (error) return <p>{error}</p>;
  return (
    <div>
      <h2>Users</h2>

      <input
  placeholder="name"
  value={name}
  onChange={(e) => setName(e.target.value)}
/>

<input
  placeholder="age"
  value={age}
  onChange={(e) => setAge(e.target.value)}
/>
      <button onClick={handleAddUser}>Add</button>

      {users.map((u) => (
  <div key={u.id}>
    {editingId === u.id ? (
      <>
        <input
          value={name}
          onChange={(e) => setName(e.target.value)}
        />
        <input
          value={age}
          onChange={(e) => setAge(e.target.value)}
        />
        <button onClick={() => handleUpdate(u.id)}>Save</button>
      </>
    ) : (
      <>
        {u.name} - {u.age}
        <button onClick={() => {
          setEditingId(u.id);
          setName(u.name);
          setAge(u.age);
        }}>
          Edit
        </button>
        <button onClick={() => handleDelete(u.id)}>
          Delete
        </button>
      </>
    )}
  </div>
))}
    </div>
  );
}

export default UserList;