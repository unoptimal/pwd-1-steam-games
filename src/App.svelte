<script>
	import Genres from "./Genres.svelte";
	import genre_data from "../public/genre_data.json";
  </script>
  
  <div>
	<h1>Playing with Data #1: Steam Games</h1>
	<p><i>Source data can be found <a href="https://github.com/leinstay/steamdb">here</a>, and source code <a href='https://github.com/unoptimal/pwd-1-steam-games'>here</a>.</i></p>
	<p><i>by <a href='http://unoptimal.com/'>unoptimal</a></i></p>

	<p>What's the distribution of genres of Steam games (as of December 2022)? Let's find out.</p>
    <li>I've excluded one entry from initial dataset since the genres were in Russian.</li>
	<li>Also, it's worthing noting that many games have multiple genres.</li>

	{#if genre_data}
		<Genres {genre_data} />
	{:else}
		<p>Loading data...if it loads for a while then something is broken.</p>
	{/if}
</div>

