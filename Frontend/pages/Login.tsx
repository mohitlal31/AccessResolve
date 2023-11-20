import {
    Anchor,
    Button,
    Checkbox,
    Container,
    Group,
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

export function Login() {
    const navigate = useNavigate();

    function submitLogin(e: FormEvent<HTMLFormElement>) {
        e.preventDefault();
        api.post("/login/", {
            username: form.values.username,
            password: form.values.password,
        }).then(function (res) {
            console.log(res.data);
            navigate("/dashboard");
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
                Welcome back!
            </Title>
            <Text c="dimmed" size="sm" ta="center" mt={5}>
                Do not have an account yet?{" "}
                <Anchor
                    size="sm"
                    component="button"
                    onClick={() => navigate("/register")}
                >
                    Create account
                </Anchor>
            </Text>

            <Paper withBorder shadow="md" p={30} mt={30} radius="md">
                <form onSubmit={submitLogin}>
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
                    <Group justify="space-between" mt="lg">
                        <Checkbox label="Remember me" />
                        <Anchor component="button" size="sm">
                            Forgot password?
                        </Anchor>
                    </Group>
                    <Button type="submit" fullWidth mt="xl">
                        Sign in
                    </Button>
                </form>
            </Paper>
        </Container>
    );
}
