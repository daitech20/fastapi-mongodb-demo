import logo from './logo.svg';
import './App.css';
import ChatApp from './views/ChatPage';
import LoginPage from './views/LoginPage';
import Room from './views/RoomPage';
import RegisterPage from './views/RegisterPage';

import { RequireToken } from "./Auth";

import { BrowserRouter, Route, Routes } from "react-router-dom";


function App() {
	return (
		<div className="App">
			<BrowserRouter>
			<Routes>
				<Route
					path="/"
					element={
						<RequireToken>
							<Room />
						</RequireToken>
					} 
				/>
				<Route path="/login" element={<LoginPage />} />
				<Route path="/register" element={<RegisterPage />} />
				<Route path="/chat" element={<ChatApp />} />
				<Route render={() => <h1>Not found!</h1>} />
			</Routes>
			</BrowserRouter>
		</div>
	);
}

export default App;