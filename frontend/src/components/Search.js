import React, { useState } from "react";
import axios from "axios";
// import { Button } from "bootstrap";

const searchQuery = { question: "your search query" };

export const Search = () => {
  const [searchQuery, setSearchQuery] = useState("");
  const [startupList, setStartupList] = useState();
  const handleSearch = () => {
    axios
      .get(`http://localhost:8000/question/${searchQuery}`)
      .then((response) => {
        console.log(response.data); // do something with the response data
        setStartupList(response.data);
      })
      .catch((error) => {
        console.error(error);
      });
  };
  console.log(searchQuery)
  // console.log(listData);
  console.log(searchQuery)
  return (
    <>
      <div>
        <input
          type="text"
          value={searchQuery}
          onChange={(event) => setSearchQuery(event.target.value)}
        />
        
        <button onClick={handleSearch} className="btn btn-primary">
          Search
        </button>
      </div>
      <div className="container-fluid">
        <div className="custom">
          <div className="text-center mt-5 test">
            <div className="card">
              <div className="card-body">
                <div className="card-title">
                  <h5>{startupList?.question}</h5>{" "}
                </div>
                <div className="card-text">
                  <textarea rows={5} style={{ width: '100%', resize: 'none', border: 'none', outline: 'none' }} className="text-area" value={startupList?.response}></textarea>{" "}
                </div>
              </div>
            </div>
            {" "}
          </div>
        </div>
      </div>
    </>
  );
};
//.split(" ").slice(0, 5).join(" ")
