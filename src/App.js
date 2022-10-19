import { useState } from "react";

function App() {
  const [todo, setTodo] = useState("");
  const [todos, setTodos] =useState([]);
  const onChange = (event) => setTodo(event.target.value);
  const onSubmit = (event) => {
    event.preventDefault();
    if (todo === ""){
      return;
    }
    setTodo("");
    setTodos(currentArray => [todo, ...currentArray]);
  };
  const deleteBtn = (index) => {
    setTodos(todos.filter((item, todoIndex) => index !== todoIndex));
  };
  
  const modifyBtn = (index) => {
    const li = index.target.parentElement;
    
  }
  console.log(todos);
  return (
    <div id="root"> 
      <h1> my to do ({todos.length})</h1>
      <form onSubmit={onSubmit}>
        <input value={todo} onChange={onChange} type="text" placeholder="Write your to do..." /> 
        <button>ADD TODO</button>
      </form>
      <hr />
      {todos.map((item, index)=> (
        <li key={index}>
          {item}
        <button onClick={modifyBtn}>수정</button>  
        <button onClick={()=>deleteBtn(index)}>삭제</button>
        </li>
      ))}

    </div>
  );
}

export default App;
