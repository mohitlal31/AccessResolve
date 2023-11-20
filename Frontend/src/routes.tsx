import { createBrowserRouter } from "react-router-dom";
import Dashboard from "../pages/Dashboard";
import { Login } from "../pages/Login";
import { Register } from "../pages/Register";
import ResetPassword from "../pages/ResetPassword";

export const router = createBrowserRouter([
    {
        path: "/",
        element: <Login />,
    },
    {
        path: "/login",
        element: <Login />,
    },
    {
        path: "/resetpassword",
        element: <ResetPassword />,
    },
    {
        path: "/dashboard",
        element: <Dashboard />,
    },
    {
        path: "/register",
        element: <Register />,
    },
]);
