import React, { useState, useEffect, useCallback } from 'react';
import { useParams } from 'react-router-dom';
import { buildApiUrl } from '../../config';
import "./Dealers.css";
import "../assets/style.css";


const PostReview = () => {
  const [dealer, setDealer] = useState({});
  const [review, setReview] = useState("");
  const [model, setModel] = useState();
  const [year, setYear] = useState("");
  const [date, setDate] = useState("");
  const [carmodels, setCarmodels] = useState([]);
  const [loading, setLoading] = useState(false);

  let curr_url = window.location.href;
  let root_url = curr_url.substring(0,curr_url.indexOf("postreview"));
  let params = useParams();
  let id =params.id;
  let dealer_url = buildApiUrl(`/djangoapp/dealer/${id}`);
  let review_url = buildApiUrl(`/djangoapp/add_review`);
  let carmodels_url = buildApiUrl(`/djangoapp/get_cars`);

  // Function to get CSRF token
  const getCSRFToken = () => {
    const cookies = document.cookie.split(';');
    for (let cookie of cookies) {
      const [name, value] = cookie.trim().split('=');
      if (name === 'csrftoken') {
        return value;
      }
    }
    return null;
  };

  const postreview = async ()=>{
    if (loading) return; // Prevent double submission
    
    let name = sessionStorage.getItem("firstname")+" "+sessionStorage.getItem("lastname");
    //If the first and second name are stores as null, use the username
    if(name.includes("null")) {
      name = sessionStorage.getItem("username");
    }
    if(!model || review === "" || date === "" || year === "" || model === "") {
      alert("All details are mandatory")
      return;
    }

    setLoading(true);

    let model_split = model.split(" ");
    let make_chosen = model_split[0];
    let model_chosen = model_split[1];

    let jsoninput = JSON.stringify({
      "name": name,
      "dealership": id,
      "review": review,
      "purchase": true,
      "purchase_date": date,
      "car_make": make_chosen,
      "car_model": model_chosen,
      "car_year": year,
    });

    console.log("Posting review:", jsoninput);
    
    try {
      const headers = {
        "Content-Type": "application/json",
      };
      
      // Add CSRF token if available
      const csrfToken = getCSRFToken();
      if (csrfToken) {
        headers['X-CSRFToken'] = csrfToken;
      }

      const res = await fetch(review_url, {
        method: "POST",
        headers: headers,
        credentials: 'include', // Include cookies for authentication
        body: jsoninput,
      });

      console.log("Response status:", res.status);
      
      if (!res.ok) {
        const errorText = await res.text();
        console.error("Error response:", errorText);
        alert(`Error posting review: ${res.status} - ${errorText}`);
        setLoading(false);
        return;
      }

      const json = await res.json();
      console.log("Response JSON:", json);
      
      if (json.status === 200) {
        alert("Review posted successfully!");
        window.location.href = window.location.origin+"/dealer/"+id;
      } else {
        alert(`Error: ${json.message || 'Failed to post review'}`);
      }
    } catch (error) {
      console.error("Network error:", error);
      alert("Network error: Unable to post review. Please check your connection.");
    } finally {
      setLoading(false);
    }
  }
  
  const get_dealer = useCallback(async ()=>{
    try {
      const res = await fetch(dealer_url, {
        method: "GET",
        credentials: 'include'
      });
      const retobj = await res.json();
      
      if(res.ok && retobj.status === 200) {
        // Our API returns a single dealer object, not an array
        setDealer(retobj.dealer)
      }
    } catch (error) {
      console.error("Error fetching dealer:", error);
    }
  }, [dealer_url]);

  const get_cars = useCallback(async ()=>{
    try {
      const res = await fetch(carmodels_url, {
        method: "GET",
        credentials: 'include'
      });
      const retobj = await res.json();
      
      let carmodelsarr = Array.from(retobj.CarModels)
      setCarmodels(carmodelsarr)
    } catch (error) {
      console.error("Error fetching cars:", error);
    }
  }, [carmodels_url]);

  useEffect(() => {
    get_dealer();
    get_cars();
  },[get_dealer, get_cars]);


  return (
    <div  style={{margin:"5%"}}>
      <h1 style={{color:"darkblue"}}>{dealer.full_name}</h1>
      <textarea id='review' cols='50' rows='7' onChange={(e) => setReview(e.target.value)} placeholder="Write your review here..."></textarea>
      <div className='input_field'>
      Purchase Date <input type="date" onChange={(e) => setDate(e.target.value)}/>
      </div>
      <div className='input_field'>
      Car Make 
      <select name="cars" id="cars" onChange={(e) => setModel(e.target.value)}>
      <option value="" disabled hidden>Choose Car Make and Model</option>
      {carmodels.map(carmodel => (
          <option key={carmodel.id} value={carmodel.CarMake+" "+carmodel.CarModel}>{carmodel.CarMake} {carmodel.CarModel}</option>
      ))}
      </select>        
      </div >

      <div className='input_field'>
      Car Year <input type="number" onChange={(e) => setYear(e.target.value)} max={2023} min={2015} placeholder="Enter year"/>
      </div>

      <div>
      <button 
        className='postreview' 
        onClick={postreview}
        disabled={loading}
      >
        {loading ? 'Posting...' : 'Post Review'}
      </button>
      </div>
    </div>
  )
}
export default PostReview
