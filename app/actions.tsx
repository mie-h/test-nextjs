'use server'
import { z } from 'zod'

export async function startProcessing(prevState: any, formData: FormData) {
    const data = z.object({
        publickey: z.string(),
        prompt: z.string(),
    })
    const { publickey, prompt } = data.parse(Object.fromEntries(formData))

    console.log(publickey, prompt);

    const AWS = require("aws-sdk");
    const region = process.env.AWS_REGION || 'us-west-1';
    AWS.config.update({ region: region });
    const accessKeyId = process.env.AWS_ACCESS_KEY_ID;
    const secretAccessKey = process.env.AWS_SECRET_ACCESS_KEY;
    if (accessKeyId != null && secretAccessKey != null) {
        AWS.config.credentials = new AWS.Credentials(accessKeyId, secretAccessKey);
    }
    const lambda = new AWS.Lambda();

    const params = {
        FunctionName: "text_to_nft",
        InvocationType: "RequestResponse",
        Payload: JSON.stringify({
            "text": prompt,
            "name": "name",
            "symbol": "symbol",
            "receiver_public_key": publickey,
        })
    };
    await lambda.invoke(params).promise();
}