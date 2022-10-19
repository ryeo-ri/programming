
import { useState , useEffect} from "react";

function App() {
  const [counter, setCounter]= useState(0);
  const [keyword, setKeyword] = useState("");
  const onClick = () => setCounter((prev) => prev + 1);
  const onChange = (event) =>  setKeyword(event.target.value);
  useEffect(()=> {
    console.log("i run only one")
  },[]);
  useEffect(()=> {
    if(keyword !== "" && keyword.length>5){
      console.log("keword change")
    }
  },[keyword]);
  
  useEffect(()=> {
    console.log("counter")
  },[counter]);

  return (
    <div id="root"> 
    <input value={keyword} onChange={onChange} type = "text" placeholder="Search here..." />
      <h1> {counter} </h1>
    <button onClick={onClick}> click me! </button>
    </div>
  );
}

export default App;
