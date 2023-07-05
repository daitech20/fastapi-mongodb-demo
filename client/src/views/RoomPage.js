import { Breadcrumb, Layout, Menu, theme, Dropdown, Space } from 'antd';
import { Card, Col, Row } from 'antd';
import { DownOutlined, SmileOutlined } from '@ant-design/icons';
import { useNavigate } from "react-router";
import { getUser, clearAuth } from "../Auth";
import { useEffect, useState } from 'react';

const { Header, Content } = Layout;
const { Meta } = Card;

const RoomPage = () => {
	const {
		token: { colorBgContainer },
	} = theme.useToken();
	const navigate = useNavigate();
	const user = getUser()

	const [ws, setWs] = useState([])
	// const [messages, setMessages] = useState([])
	// const [clients, setClients] = useState([]) 

	const handLogout = () => {
		clearAuth();
		return navigate("/login");
	}

	useEffect(() => {
		console.log("ok")
		const url = "ws://localhost:8008/ws/rooms/";
		let socket = new WebSocket(url + user.id);
		setWs(socket);

		ws.onmessage = function(event) {
			let userdata = JSON.parse(event.data)
			// setMessages((prevMessages) => [...prevMessages, userdata.message])
			// let client_ids = [...userdata.client_ids]
			// setClients(client_ids)
			console.log("vclss", userdata)
		}

		}, []);

	
	const items = [
		{
		  key: '1',
		  label: (
			<a target="_blank" rel="noopener noreferrer"onClick={handLogout} >
				Logout
			</a>
		  ),
		},
	]


	return (
		<Layout className="layout">
		<Header
			style={{
			display: 'flex',
			alignItems: 'center',
			}}
		>
			<div className="demo-logo" />
			<Dropdown
				menu={{
				items,
				}}
			>
				<Space>
					{ user.username }
					<DownOutlined />
				</Space>
			</Dropdown>
		</Header>
		<Content
			style={{
			padding: '0 50px',
			}}
		>
			<Breadcrumb
			style={{
				margin: '16px 0',
			}}
			>
			<Breadcrumb.Item>Home</Breadcrumb.Item>
			</Breadcrumb>
			<div
			className="site-layout-content"
			style={{
				background: colorBgContainer,
			}}
			>
		<Row gutter={16} justify="center">
			<Col span={4}>
			<Card
				hoverable
				style={{ width: 240 }}
				cover={<img alt="example" src="https://os.alipayobjects.com/rmsportal/QBnOOoLaAfKPirc.png" />}
			>
				<Meta title="Europe Street beat" description="www.instagram.com" />
			</Card>
			</Col>

			<Col span={4}>
			<Card
				hoverable
				style={{ width: 240 }}
				cover={<img alt="example" src="https://os.alipayobjects.com/rmsportal/QBnOOoLaAfKPirc.png" />}
			>
				<Meta title="Europe Street beat" description="www.instagram.com" />
			</Card>
			</Col>
			<Col span={4}>
			<Card
				hoverable
				style={{ width: 240 }}
				cover={<img alt="example" src="https://os.alipayobjects.com/rmsportal/QBnOOoLaAfKPirc.png" />}
			>
				<Meta title="Europe Street beat" description="www.instagram.com" />
			</Card>
			</Col>
		</Row>
			</div>
		</Content>
		</Layout>
	);
};
export default RoomPage;









{/* <Row gutter={16} justify="center">
    <Col span={4}>
        <Card
            hoverable
            style={{ width: 240 }}
            cover={<img alt="example" src="https://os.alipayobjects.com/rmsportal/QBnOOoLaAfKPirc.png" />}
        >
            <Meta title="Europe Street beat" description="www.instagram.com" />
        </Card>
    </Col>

    <Col span={4}>
        <Card
            hoverable
            style={{ width: 240 }}
            cover={<img alt="example" src="https://os.alipayobjects.com/rmsportal/QBnOOoLaAfKPirc.png" />}
        >
            <Meta title="Europe Street beat" description="www.instagram.com" />
        </Card>
    </Col>
    <Col span={4}>
        <Card
            hoverable
            style={{ width: 240 }}
            cover={<img alt="example" src="https://os.alipayobjects.com/rmsportal/QBnOOoLaAfKPirc.png" />}
        >
            <Meta title="Europe Street beat" description="www.instagram.com" />
        </Card>
    </Col>
</Row> */}