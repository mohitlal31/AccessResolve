import { Button } from "@mantine/core";
import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import { api } from "../utilities/api";

export default function Dashboard() {
    const navigate = useNavigate();
    const [accommodations, setAccommodations] = useState(null);

    useEffect(() => {
        api.get("/accommodations/", { withCredentials: true }).then((res) => {
            setAccommodations(res.data);
            console.log(res);
        });
    }, []);

    function logout() {
        api.post("/logout/").then((res) => {
            if (res.status == 200) {
                navigate("/login");
            } else {
                console.log(res.data);
            }
        });
    }
    return (
        <>
            <div>{accommodations && JSON.stringify(accommodations)}</div>
            <Button onClick={logout}>Logout</Button>
        </>
    );
}
