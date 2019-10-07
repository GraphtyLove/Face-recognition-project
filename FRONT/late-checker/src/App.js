import React, {Fragment, useState} from 'react'
import './App.css'
import VideoFeed from './Components/VideoFeed/VideoFeed'
import SearchBar from './Components/SearchBar/SearchBar'
import LastArrivalList from './Components/LastArrivalList/LastArrivalList'
import styled from 'styled-components'

function App() {
	const TitleOne = styled.h1`
		margin-top : 0;
		font-size: 45px;
		line-height: 1;
		font-weight: normal;
		color: #013087;
		text-align: center;
`

	const [searchBarAnswer, setSearchBarAnswer] = useState([]);



	return(
		<Fragment>
			<TitleOne>Late Checker</TitleOne>
			<VideoFeed />
			<SearchBar searchBarAnswer={ setSearchBarAnswer } />
			<LastArrivalList  />
		</Fragment>
	)}

export default App
