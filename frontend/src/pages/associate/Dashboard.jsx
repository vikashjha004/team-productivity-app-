import { useEffect, useState } from "react";
import api from "../../services/api";

export default function Dashboard() {
  const [tasks, setTasks] = useState([]);

  useEffect(() => {
    api.get("/tasks/my/1").then(res => setTasks(res.data));
  }, []);

  return (
    <div>
      <h2>My Tasks</h2>
      {tasks.map(t => (
        <div key={t.id}>{t.name}</div>
      ))}
    </div>
  );
}
