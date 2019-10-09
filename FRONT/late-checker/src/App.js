import React, { Fragment } from 'react'
import './App.css'
import VideoFeed from './Components/VideoFeed/VideoFeed'
import SearchBar from './Components/SearchBar/SearchBar'
import LastArrivalList from './Components/LastArrivalList/LastArrivalList'
import AdminBlock from './Components/AdminBlock/AdminBlock'
import styled from 'styled-components'

function App() {

	// * ---------- STYLE ---------- *
	const TitleOne = styled.h1`
		margin-top : 30px;
		font-size: 50px;
		line-height: 1;
		font-weight: bold;
		color: #013087;
		text-align: center;
`
	const MainContainer = styled.main`
		display: flex;
		flex-wrap: wrap;
		justify-content: center;
`


	return(
		<Fragment>
			<TitleOne>Late Checker</TitleOne>
			<MainContainer>
				<VideoFeed />
				<SearchBar />
				<LastArrivalList />
				<AdminBlock />
			</MainContainer>
		</Fragment>
	)}

export default App
