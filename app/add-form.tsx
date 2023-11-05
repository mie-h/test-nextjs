"use client";
import { useFormState } from "react-dom";
import { startProcessing } from "@/app/actions";
import { useEffect, useState } from "react";
import Button from '@mui/material/Button';
import TextField from "@mui/material/TextField";
import Stack from "@mui/material/Stack";
import { Grid, ThemeProvider, Typography, createTheme } from "@mui/material";

const initialState = {
    message: null,
}
const theme = createTheme({
    typography: {
        fontSize: 10,
    },
});

export function AddForm() {
    const [showSuccess, setShowSuccess] = useState(false);
    const [, formAction] = useFormState(async (_: unknown, formData: FormData) => {
        console.log("Calling server action")
        // await startProcessing(formData)
        console.log(formData)
        console.log("Server action compeleted successfully")
        setShowSuccess(true)
    }, initialState)

    useEffect(() => { setTimeout(() => setShowSuccess(false), 2000) }, [showSuccess])

    return (
        <>
            <Grid container justifyContent="center" sx={{ mt: 10 }}>
                <Stack spacing={2} alignItems="center" justifyContent="center" sx={{ width: 1 / 2 }}>
                    <ThemeProvider theme={theme}>
                        <Typography variant="h4">Text To NFT</Typography>
                        <Typography variant="h6">Enter a prompt and a public key of your wallet to generate an NFT.
                            The NFT will be minted to the wallet associated with the public key.
                            The prompt will be used to generate the NFT.
                            *The NFT is minted on the testnet. </Typography>
                    </ThemeProvider>
                </Stack>
            </Grid>
            <form action={formAction}>
                <Grid container justifyContent="center">
                    <Stack spacing={2} alignItems="center" justifyContent="center" sx={{ mt: 10, width: 1 / 2 }}>
                        <TextField id="outlined-basic" name="publickey" label="Enter Public Key" variant="outlined" sx={{ width: 1 }} required />
                        <TextField id="outlined-basic" name="prompt" label="Enter Prompt" variant="outlined" sx={{ width: 1 }} required />
                        <Button variant="outlined" type="submit">Submit</Button>
                    </Stack>
                </Grid>
            </form>
            <Grid container justifyContent="center">
                {showSuccess && <div>Success</div>}
            </Grid>
        </>
    )
}