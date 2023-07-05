import { LockOutlined, UserOutlined } from '@ant-design/icons';
import { Button, Checkbox, Form, Input, message } from 'antd';
import { Layout } from 'antd';
import { useState } from 'react';
import { fetchToken, setToken, setUser } from "../Auth";
import { useLocation,Navigate } from "react-router-dom"
import { useNavigate } from "react-router";
import axios from "axios";



const LoginPage = () => {
	const [messageApi, contextHolder] = message.useMessage();
	const [username, setUsername] = useState("")
	const [password, setPassword] = useState("")
	let location = useLocation()
	const navigate = useNavigate();

	if (fetchToken() != null) {
		return <Navigate to='/' state ={{from : location}} />
	}
	

	const errorNoti = () => {
		messageApi.open({
		type: 'error',
		content: 'Sai tài khoản hoặc mật khẩu!',
		});
	};


	const login = () => {
		axios.post("http://localhost:8008/api/v1/user/login", {
			username: username,
			password: password,
		})
		.then(function (response) {
			if (response.data.data) {
				setToken(response.data.data[0].access_token);
				setUser(JSON.stringify(response.data.data[0].user))
				navigate("/");
			}
		})
		.catch(function (error) {
			console.log(error, "error");
			errorNoti();
		});
	}

	const goRegister = () => {
		navigate("/register");
	}


	return (
		<Layout className="layout" style={{ alignItems: 'center', height: '1000px', position: 'relative' }}>
			{contextHolder}
			<Form
				name="normal_login"
				className="login-form"
				initialValues={{
					remember: true,
				}}
				onFinish={login}
				style={{ top: '30%', position: 'absolute' }}
				
				>
				<Form.Item
					name="username"
					rules={[
					{
						required: true,
						message: 'Please input your Username!',
					},
					]}
				>
					<Input prefix={<UserOutlined className="site-form-item-icon" />} placeholder="Username" onChange={(e) => setUsername(e.target.value)} />
				</Form.Item>
				<Form.Item
					name="password"
					rules={[
					{
						required: true,
						message: 'Please input your Password!',
					},
					]}
				>
					<Input
					prefix={<LockOutlined className="site-form-item-icon" />}
					type="password"
					placeholder="Password"
					onChange={(e) => setPassword(e.target.value)}
					/>
				</Form.Item>
				<Form.Item>
					<Form.Item name="remember" valuePropName="checked" noStyle>
					<Checkbox>Remember me</Checkbox>
					</Form.Item>

					<a className="login-form-forgot" href="">
					Forgot password
					</a>
				</Form.Item>

				<Form.Item>
					<Button type="primary" htmlType="submit" className="login-form-button">
					Log in
					</Button>
					 Or
					<a onClick={goRegister}> register now!</a>
				</Form.Item>
				</Form>
		</Layout>
		
	);
	};
export default LoginPage;