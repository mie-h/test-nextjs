"use client";
import { useFormState } from "react-dom";
import { startProcessing } from "@/app/actions";

const initialState = {
    message: null,
}

export function AddForm() {
    const [state, formAction] = useFormState(startProcessing, initialState)
    return (
        <form action={formAction}>
            <input
                name="publickey"
                placeholder="Enter Public Key"
                required
            />
            <input
                name="prompt"
                placeholder="Enter Prompt"
                required
            />
            <button type="submit">Submit</button>
        </form>
    )
}