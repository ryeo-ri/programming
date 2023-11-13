import { useState, useEffect } from "react";

function App() {
  const [toDo, setTodo] = useState("");
  const onChange = (event) => setTodo(event.target.value);
  //const onSubmit = (event) => event.
  console.log(toDo);
  return (
    <div>
      <input
        onChange={onChange}
        value={toDo}
        type="text"
        placeholder="write your todo..."
      ></input>
    </div>
  );
}

export default App;
