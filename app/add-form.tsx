"use client";
import { useFormState } from "react-dom";
import { startProcessing } from "@/app/actions";
import { useEffect, useState } from "react";

const initialState = {
    message: null,
}

export function AddForm() {
    const [showSuccess, setShowSuccess] = useState(false);
    const [, formAction] = useFormState(async (_: unknown, formData: FormData) => {
        console.log("Calling server action")
        await startProcessing(formData)
        console.log("Server action compeleted successfully")
        setShowSuccess(true)
    }, initialState)

    useEffect(() => { setTimeout(() => setShowSuccess(false), 2000) }, [showSuccess])

    return (
        <>
            <form className="flex flex-col w-fit" action={formAction}>
                <input className="w-72"
                    name="publickey"
                    placeholder="Enter Public Key"
                    required
                />
                <input className="w-36"
                    name="prompt"
                    placeholder="Enter Prompt"
                    required
                />
                <button type="submit">Submit</button>
            </form>
            {showSuccess && <div>Success</div>}
        </>
    )
}