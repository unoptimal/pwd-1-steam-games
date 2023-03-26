<script>
    import { onMount } from 'svelte';
    import Chart from 'chart.js/auto';    
    export let genre_data;
    
    let genre_counts = {};
    let small_genres = {}; 

    for (let i = 0; i < genre_data.length; i++) {
        let genres = genre_data[i].genres.split(',');
        for (let j = 0; j < genres.length; j++) {
            let category = genres[j].trim();
            if (category in genre_counts) {
                genre_counts[category] += 1;
            } else {
                genre_counts[category] = 1;
            }
        }
    }

    let total_count = 0;
    const MIN_COUNT = 4000; 
    Object.keys(genre_counts).forEach((key) => {
        let count = genre_counts[key];
        if (count < MIN_COUNT) {
            small_genres[key] = count;
            delete genre_counts[key];
        } else {
            total_count += count;
        }
    });
    genre_counts['Other'] = Object.values(small_genres).reduce((a, b) => a + b, 0);
    small_genres = Object.entries(small_genres).sort((a, b) => b[1] - a[1]);

    let chart;

    const options = {
        plugins: {
            tooltip: {
                callbacks: {
                    label: function(context) {
                        let label = context.label || '';
                        let value = context.parsed || 0;
                        let total = context.dataset.data.reduce((acc, val) => acc + val, 0);
                        let percent = total > 0 ? (value / total) * 100 : 0;
                        return label + ': ' + value + ' (' + percent.toFixed(2) + '%)'
                    }
                }
            }
        },
    };
   

    onMount(() => {
        const ctx = document.getElementById('myChart').getContext('2d');

        chart = new Chart(ctx, {
            type: 'pie',
            data: {
                labels: Object.keys(genre_counts),
                datasets: [{
                    data: Object.values(genre_counts),
                    backgroundColor: [
                        '#FF6384',
                        '#36A2EB',
                        '#FFCE56',
                        '#8B008B',
                        '#008080',
                        '#FF8C00',
                        '#FFD700',
                        '#90EE90',
                        '#9400D3',
                        '#FA8072',
                        '#00CED1',
                        '#1E90FF',
                        '#FFE4C4',
                        '#CD5C5C',
                        '#8FBC8F',
                        '#4B0082',
                        '#7B68EE',
                        '#00FA9A',
                        '#FF00FF'
                    ]
                }]
            },
            options: options
        });
    });

    function destroyChart() {
        chart.destroy();
    }
</script>

    <div class='container'>
        <canvas id="myChart"></canvas>
    
        
        {#if small_genres.length > 0}
            <p>The following categories have less than {MIN_COUNT} entries and are not shown on the chart (clumped into the Other category):</p>
            <ul>
                {#each small_genres as [key, value]}
                    <li>{key}: {value}</li>
                {/each}
            </ul>
        {/if}
    </div>

    <p>I was surprised to see that Indie games was leading the pack over the likes of Action or Casual. Though I suppose this can be attributed to indie games often being smaller scale.</p>
    <p>I also thought there would be way more Free to Play games, but that's evidently not the case.</p>

    <style>

        canvas {

            max-width: 500px;
            max-height: 500px;
            width: 100%;
            height: auto;
        }


    </style>
