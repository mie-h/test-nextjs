
import React from 'react'
import { AddForm } from '@/app/add-form';


export default async function Home() {

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



  // async function handleSubmit(e: React.FormEvent) {
  //   e.preventDefault();

  //   let formData = new FormData();

  //   for (let [key, value] of Object.entries(state)) {
  //     formData.append(key, value);
  //   }

  //   const AWS = require("aws-sdk");
  //   AWS.config.update({ region: 'us-west-1' });

  //   const lambda = new AWS.Lambda();

  //   const params = {
  //     FunctionName: "hello-world-python",
  //     InvocationType: "RequestResponse",
  //     Payload: JSON.stringify({
  //       "text": { prompt },
  //       "name": "name",
  //       "symbol": "symbol",
  //       "receiver_public_key": "",
  //     })
  //   };
  // lambda.invoke(params);
  // await lambda.invoke(params).promise();

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
    <main>
      <AddForm />
      {/* <form onSubmit={handleSubmit}>
      <button type="submit">Submit</button>
    </form>  */}
    </main >
  )
}
