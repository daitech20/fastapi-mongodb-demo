import { useLocation,Navigate } from "react-router-dom"

export const setToken = (token)=>{

    localStorage.setItem('token', token)// make up your own token
}

export const fetchToken = ()=>{

    return localStorage.getItem('token')
}

export const setUser = (user)=>{

    return localStorage.setItem('user', user)
}

export const getUser = ()=>{

    return JSON.parse(localStorage.getItem('user'))
}

export const clearAuth = ()=>{
    localStorage.removeItem('user')
    localStorage.removeItem('token')
}

export function RequireToken({children}){

    let auth = fetchToken()
    let location = useLocation()

    if(!auth){
        return <Navigate to='/login' state ={{from : location}}/>;
    }

    return children;
}
