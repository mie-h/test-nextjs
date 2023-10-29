// "use client";
import Image from 'next/image'
import React from 'react'
import axios from 'axios'
import { FormEvent, useState } from 'react'

interface User {
  id: number
  name: string
  username: string
  email: string
  address: {
    street: string
    suite: string
    city: string
    zipcode: string
    geo: {
      lat: number
      lng: number
    }
  }
  phone: string
  website: string
  company: {
    name: string
    catchPhrase: string
    bs: string
  }
}

export default async function Home() {
  const message = `
    {"text": "Hello World"}
  `;

  // fetch('https://api.github.com/graphql', {
  //   method: 'POST',
  //   headers: {
  //     'Content-Type': 'application/json',
  //   },
  //   body: JSON.stringify({ message }),
  // })
  //   .then((response) => response.json())
  //   .then((data) => console.log(data));

  // const AWS = require("aws-sdk");
  // AWS.config.update({ region: 'us-west-1' });

  // const lambda = new AWS.Lambda();

  // const params = {
  //   FunctionName: "text_to_nft",
  //   InvocationType: "RequestResponse",
  //   Payload: JSON.stringify({
  //     "text": "zen temple",
  //     "name": "name",
  //     "symbol": "symbol",
  //     "receiver_public_key": "By3RECZEGmkfkqd5FqeJAEAJBsV3ko8qbvMxQRck8uzy"
  //   })
  // };

  // await lambda.invoke(params).promise();

  // const res = await fetch("https://jsonplaceholder.typicode.com/users")
  // const data: User[] = await res.json()
  // const [state, setState] = React.useState({
  //   email: "",
  //   message: ""
  // });

  // function handleChange(e: React.FormEvent) {
  //   const target = e.target as HTMLTextAreaElement;
  //   setState({ ...state, [target.name]: target.value });
  // }

  // async function handleSubmit(e: React.FormEvent) {
  //   e.preventDefault();

  //   let formData = new FormData();

  //   for (let [key, value] of Object.entries(state)) {
  //     formData.append(key, value);
  //   }

  //   // Use fetch or axios to submit the form
  //   await axios
  //     .post("{Formeezy-Endpoint}", formData)
  //     .then(({ data }) => {
  //       const { redirect } = data;
  //       // Redirect used for reCAPTCHA and/or thank you page
  //       window.location.href = redirect;
  //     })
  //     .catch((e) => {
  //       window.location.href = e.response.data.redirect;
  //     });
  return (
    <main><h1>Hello World</h1>
      {/* <ul>{data.map(d => <li>{d.name}</li>)}</ul> */}
      {/* <form onSubmit={handleSubmit}>
          <input
            name="email"
            type="email"
            placeholder="Enter email"
            onChange={handleChange}
            value={state.email}
            required
          />
          <textarea
            name="message"
            placeholder="Enter message"
            onChange={handleChange}
            value={state.message}
            required
          />
          <button type="submit">Send</button>
        </form> */}
    </main>
  )
}

