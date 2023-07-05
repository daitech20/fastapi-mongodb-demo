import { useEffect, useState } from "react";


function ChatApp() {
    const [websckt, setWebsckt] = useState()
    const [message, setMessage] = useState([])
    const [messages, setMessages] = useState([])
    useEffect(() => {
        const url = "ws://localhost:8008/ws/" + "12345"
        const ws = new WebSocket(url)
        
        ws.onopen = (event) => {
            ws.send("connect")
        }
        ws.onmessage= (e) => {
            const message = JSON.parse(e.data)
            console.log("message: ", message)
        }

        setWebsckt(ws)

        return () => ws.close()
    }, [])


    return (
        <section>
            <div className="container py-5">

                <div className="row">

                <div className="col-md-6 col-lg-5 col-xl-4 mb-4 mb-md-0">

                    <h5 className="font-weight-bold mb-3 text-center text-lg-start">Member</h5>

                    <div className="card">
                    <div className="card-body">

                        <ul className="list-unstyled mb-0">
                        <li className="p-2 border-bottom">
                            <a href="#!" className="d-flex justify-content-between">
                            <div className="d-flex flex-row">
                                <img src="https://mdbcdn.b-cdn.net/img/Photos/Avatars/avatar-8.webp" alt="avatar"
                                className="rounded-circle d-flex align-self-center me-3 shadow-1-strong" width="60" />
                                <div className="pt-1">
                                <p className="fw-bold mb-0">John Doe</p>
                                <p className="small text-muted">Hello, Are you there?</p>
                                </div>
                            </div>
                            <div className="pt-1">
                                <p className="small text-muted mb-1">Just now</p>
                                <span className="badge bg-danger float-end">1</span>
                            </div>
                            </a>
                        </li>
                        <li className="p-2 border-bottom">
                            <a href="#!" className="d-flex justify-content-between">
                            <div className="d-flex flex-row">
                                <img src="https://mdbcdn.b-cdn.net/img/Photos/Avatars/avatar-1.webp" alt="avatar"
                                className="rounded-circle d-flex align-self-center me-3 shadow-1-strong" width="60"/>
                                <div className="pt-1">
                                <p className="fw-bold mb-0">Danny Smith</p>
                                <p className="small text-muted">Lorem ipsum dolor sit.</p>
                                </div>
                            </div>
                            <div className="pt-1">
                                <p className="small text-muted mb-1">5 mins ago</p>
                            </div>
                            </a>
                        </li>
                        <li className="p-2 border-bottom">
                            <a href="#!" className="d-flex justify-content-between">
                            <div className="d-flex flex-row">
                                <img src="https://mdbcdn.b-cdn.net/img/Photos/Avatars/avatar-2.webp" alt="avatar"
                                className="rounded-circle d-flex align-self-center me-3 shadow-1-strong" width="60"/>
                                <div className="pt-1">
                                <p className="fw-bold mb-0">Alex Steward</p>
                                <p className="small text-muted">Lorem ipsum dolor sit.</p>
                                </div>
                            </div>
                            <div className="pt-1">
                                <p className="small text-muted mb-1">Yesterday</p>
                            </div>
                            </a>
                        </li>
                        <li className="p-2 border-bottom">
                            <a href="#!" className="d-flex justify-content-between">
                            <div className="d-flex flex-row">
                                <img src="https://mdbcdn.b-cdn.net/img/Photos/Avatars/avatar-3.webp" alt="avatar"
                                className="rounded-circle d-flex align-self-center me-3 shadow-1-strong" width="60"/>
                                <div className="pt-1">
                                <p className="fw-bold mb-0">Ashley Olsen</p>
                                <p className="small text-muted">Lorem ipsum dolor sit.</p>
                                </div>
                            </div>
                            <div className="pt-1">
                                <p className="small text-muted mb-1">Yesterday</p>
                            </div>
                            </a>
                        </li>
                        <li className="p-2 border-bottom">
                            <a href="#!" className="d-flex justify-content-between">
                            <div className="d-flex flex-row">
                                <img src="https://mdbcdn.b-cdn.net/img/Photos/Avatars/avatar-4.webp" alt="avatar"
                                className="rounded-circle d-flex align-self-center me-3 shadow-1-strong" width="60"/>
                                <div className="pt-1">
                                <p className="fw-bold mb-0">Kate Moss</p>
                                <p className="small text-muted">Lorem ipsum dolor sit.</p>
                                </div>
                            </div>
                            <div className="pt-1">
                                <p className="small text-muted mb-1">Yesterday</p>
                            </div>
                            </a>
                        </li>
                        <li className="p-2 border-bottom">
                            <a href="#!" className="d-flex justify-content-between">
                            <div className="d-flex flex-row">
                                <img src="https://mdbcdn.b-cdn.net/img/Photos/Avatars/avatar-5.webp" alt="avatar"
                                className="rounded-circle d-flex align-self-center me-3 shadow-1-strong" width="60"/>
                                <div className="pt-1">
                                <p className="fw-bold mb-0">Lara Croft</p>
                                <p className="small text-muted">Lorem ipsum dolor sit.</p>
                                </div>
                            </div>
                            <div className="pt-1">
                                <p className="small text-muted mb-1">Yesterday</p>
                            </div>
                            </a>
                        </li>
                        <li className="p-2">
                            <a href="#!" className="d-flex justify-content-between">
                            <div className="d-flex flex-row">
                                <img src="https://mdbcdn.b-cdn.net/img/Photos/Avatars/avatar-6.webp" alt="avatar"
                                className="rounded-circle d-flex align-self-center me-3 shadow-1-strong" width="60"/>
                                <div className="pt-1">
                                <p className="fw-bold mb-0">Brad Pitt</p>
                                <p className="small text-muted">Lorem ipsum dolor sit.</p>
                                </div>
                            </div>
                            <div className="pt-1">
                                <p className="small text-muted mb-1">5 mins ago</p>
                                <span className="text-muted float-end"><i className="fas fa-check" aria-hidden="true"></i></span>
                            </div>
                            </a>
                        </li>
                        </ul>

                    </div>
                    </div>

                </div>

                <div className="col-md-6 col-lg-7 col-xl-8">

                    <ul className="list-unstyled">
                    <li className="d-flex justify-content-between mb-4">
                        <img src="https://mdbcdn.b-cdn.net/img/Photos/Avatars/avatar-6.webp" alt="avatar"
                        className="rounded-circle d-flex align-self-start me-3 shadow-1-strong" width="60"/>
                        <div className="card">
                        <div className="card-header d-flex justify-content-between p-3">
                            <p className="fw-bold mb-0">Brad Pitt</p>
                            <p className="text-muted small mb-0"><i className="far fa-clock"></i> 12 mins ago</p>
                        </div>
                        <div className="card-body">
                            <p className="mb-0">
                            Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut
                            labore et dolore magna aliqua.
                            </p>
                        </div>
                        </div>
                    </li>
                    <li className="d-flex justify-content-between mb-4">
                        <div className="card w-100">
                        <div className="card-header d-flex justify-content-between p-3">
                            <p className="fw-bold mb-0">Lara Croft</p>
                            <p className="text-muted small mb-0"><i className="far fa-clock"></i> 13 mins ago</p>
                        </div>
                        <div className="card-body">
                            <p className="mb-0">
                            Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque
                            laudantium.
                            </p>
                        </div>
                        </div>
                        <img src="https://mdbcdn.b-cdn.net/img/Photos/Avatars/avatar-5.webp" alt="avatar"
                        className="rounded-circle d-flex align-self-start ms-3 shadow-1-strong" width="60"/>
                    </li>
                    <li className="d-flex justify-content-between mb-4">
                        <img src="https://mdbcdn.b-cdn.net/img/Photos/Avatars/avatar-6.webp" alt="avatar"
                        className="rounded-circle d-flex align-self-start me-3 shadow-1-strong" width="60"/>
                        <div className="card">
                        <div className="card-header d-flex justify-content-between p-3">
                            <p className="fw-bold mb-0">Brad Pitt</p>
                            <p className="text-muted small mb-0"><i className="far fa-clock"></i> 10 mins ago</p>
                        </div>
                        <div className="card-body">
                            <p className="mb-0">
                            Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut
                            labore et dolore magna aliqua.
                            </p>
                        </div>
                        </div>
                    </li>
                    <li className="bg-white mb-3">
                        <div className="form-outline">
                        <textarea className="form-control" id="textAreaExample2" rows="4"></textarea>
                        <label className="form-label" for="textAreaExample2">Message</label>
                        </div>
                    </li>
                    <button type="button" className="btn btn-info btn-rounded float-end">Send</button>
                    </ul>

                </div>

                </div>

            </div>
        </section>
    );
}

export default ChatApp;
