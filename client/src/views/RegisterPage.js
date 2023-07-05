import { LockOutlined, UserOutlined } from '@ant-design/icons';
import { Button, Checkbox, Form, Input, message } from 'antd';
import { Layout } from 'antd';
import { useState } from 'react';
import { fetchToken, setToken, setUser } from "../Auth";
import { useLocation,Navigate } from "react-router-dom"
import { useNavigate } from "react-router";
import axios from "axios";


const tailFormItemLayout = {
    wrapperCol: {
        xs: {
        span: 24,
        offset: 0,
        },
        sm: {
        span: 16,
        offset: 8,
        },
    },
};

const formItemLayout = {
    labelCol: {
      xs: {
        span: 24,
      },
      sm: {
        span: 8,
      },
    },
    wrapperCol: {
      xs: {
        span: 24,
      },
      sm: {
        span: 16,
      },
    },
};


const RegisterPage = () => {
	const [messageApi, contextHolder] = message.useMessage();
	const [username, setUsername] = useState("")
	const [password, setPassword] = useState("")
    const [email, setEmail] = useState("")
    const [fullname, setFullname] = useState("")
	let location = useLocation()
	const navigate = useNavigate();
    const [form] = Form.useForm();
	

	const errorNoti = (message) => {
		messageApi.open({
		type: 'error',
		content: message,
		});
	};


	const register = () => {
		axios.post("http://localhost:8008/api/v1/user/register", {
			username: username,
			password: password,
            fullname: fullname,
            email: email
		})
		.then(function (response) {
			if (response.data.data) {
				navigate("/login");
			}
		})
		.catch(function (error) {
			errorNoti(error.response.data.detail);
		});
	}


	return (
		<Layout className="layout" style={{ alignItems: 'center', height: '1000px', position: 'relative' }}>
			{contextHolder}
			<Form
                {...formItemLayout}
                form={form}
                name="register"
                onFinish={register}
                style={{
                    maxWidth: 600,
                    top: '20%',
                    position: 'absolute'
                }}
                scrollToFirstError
                >
                <Form.Item
                    name="email"
                    label="E-mail"
                    rules={[
                    {
                        type: 'email',
                        message: 'The input is not valid E-mail!',
                    },
                    {
                        required: true,
                        message: 'Please input your E-mail!',
                    },
                    ]}
                    onChange={(e) => setEmail(e.target.value)} 
                >
                    <Input />
                </Form.Item>

                <Form.Item
                    name="password"
                    label="Password"
                    rules={[
                    {
                        required: true,
                        message: 'Please input your password!',
                    },
                    ]}
                    onChange={(e) => setPassword(e.target.value)} 
                    hasFeedback
                >
                    <Input.Password />
                </Form.Item>

                <Form.Item
                    name="confirm"
                    label="Confirm Password"
                    dependencies={['password']}
                    hasFeedback
                    rules={[
                    {
                        required: true,
                        message: 'Please confirm your password!',
                    },
                    ({ getFieldValue }) => ({
                        validator(_, value) {
                        if (!value || getFieldValue('password') === value) {
                            return Promise.resolve();
                        }
                        return Promise.reject(new Error('The new password that you entered do not match!'));
                        },
                    }),
                    ]}
                >
                    <Input.Password />
                </Form.Item>

                <Form.Item
                    name="username"
                    label="username"
                    rules={[
                    {
                        required: true,
                        message: 'Please input your username!',
                        whitespace: true,
                    },
                    ]}
                    onChange={(e) => setUsername(e.target.value)} 
                >
                    <Input />
                </Form.Item>

                <Form.Item
                    name="fullname"
                    label="Full name"
                    tooltip="What do you want others to call you?"
                    rules={[
                    {
                        required: true,
                        message: 'Please input your full name!',
                        whitespace: true,
                    },
                    ]}
                    onChange={(e) => setFullname(e.target.value)} 
                >
                    <Input />
                </Form.Item>

                <Form.Item {...tailFormItemLayout}>
                    <Button type="primary" htmlType="submit">
                    Register
                    </Button>
                </Form.Item>
                </Form>
		</Layout>
		
	);
	};
export default RegisterPage;