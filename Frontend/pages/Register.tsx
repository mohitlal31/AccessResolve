import {
    Anchor,
    Button,
    Container,
    Paper,
    PasswordInput,
    Text,
    TextInput,
    Title,
} from "@mantine/core";
import { useForm } from "@mantine/form";
import { FormEvent } from "react";
import { useNavigate } from "react-router-dom";
import classes from "../css/Login.module.css";
import { api } from "../utilities/api";

export function Register() {
    const navigate = useNavigate();

    function submitRegister(e: FormEvent<HTMLFormElement>) {
        e.preventDefault();
        api.post("/register/", {
            username: form.values.username,
            password: form.values.password,
        }).then(function (res) {
            console.log(res.data);
            navigate("/login");
        });
    }

    const form = useForm({
        initialValues: {
            username: "",
            password: "",
        },
    });
    return (
        <Container size={420} my={40}>
            <Title ta="center" className={classes.title}>
                Welcome to AccessResolve!
            </Title>
            <Text c="dimmed" size="sm" ta="center" mt={5}>
                Already have an account?{" "}
                <Anchor
                    size="sm"
                    component="button"
                    onClick={() => navigate("/login")}
                >
                    Login
                </Anchor>
            </Text>

            <Paper withBorder shadow="md" p={30} mt={30} radius="md">
                <form onSubmit={submitRegister}>
                    <TextInput
                        name="username"
                        label="Username"
                        placeholder="you@mantine.dev"
                        {...form.getInputProps("username")}
                        required
                    />
                    <PasswordInput
                        label="Password"
                        placeholder="Your password"
                        {...form.getInputProps("password")}
                        required
                        mt="md"
                    />
                    <Button type="submit" fullWidth mt="xl">
                        Register
                    </Button>
                </form>
            </Paper>
        </Container>
    );
}
