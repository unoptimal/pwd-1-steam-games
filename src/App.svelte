<script>
	import { onMount } from "svelte";
	import Genres from "./Genres.svelte";
	import * as d3 from "d3";
	
	let data;
	let genre_data;
	
	onMount(async () => {
	  data = await d3.json('/genre_data.json')
	  genre_data = data.filter(d => d.genres);
	});
  </script>
  
  <div>
	<h1>Playing with Data #1: Steam Games</h1>
	<p><i>Source data can be found <a href="https://github.com/leinstay/steamdb">here</a>, and source code <a href='https://github.com/unoptimal/pwd-1-steam-games'>here</a><div class=""></div></i></p>
	<p><i>by <a href='http://unoptimal.com/'>unoptimal</a></i></p>

	<p>What's the distribution of genres of Steam games (as of December 2022)? Let's find out.</p>
    <p>I've excluded one entry from initial dataset since the genres were in Russian.</p>
    <p>Also, it's worthing noting that many games have multiple genres.</p>

	{#if genre_data}
		<Genres {genre_data} />
	{:else}
		<p>Loading data...</p>
	{/if}
</div>

