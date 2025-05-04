// Function to initialize chart with error handling
function initChart(url, chartId, configFn) {
    fetch(url, { mode: 'cors' })
      .then(response => {
        if (!response.ok) throw new Error(`Fetch failed: ${response.status} ${response.statusText}`);
        return response.json();
      })
      .then(data => {
        console.log(`Data for ${chartId}:`, data); // Debug data
        const chart = echarts.init(document.getElementById(chartId));
        chart.setOption(configFn(data));
      })
      .catch(error => {
        console.error(`Error loading ${chartId}:`, error);
        document.getElementById(chartId).innerHTML = `Error loading chart: ${error.message}`;
      });
  }
  
  // Line Chart (SQLite)
  initChart('http://localhost:8000/api/line/data', 'line-chart', data => ({
    title: { text: 'Line Chart', left: 'center' },
    legend: { data: ['Value'], top: 'bottom' },
    xAxis: {
      type: 'category',
      data: data.map(item => item.date),
      name: 'Date',
      nameLocation: 'center',
      nameGap: 30
    },
    yAxis: {
      type: 'value',
      name: 'Value',
      nameLocation: 'center',
      nameGap: 40
    },
    series: [{
      name: 'Value',
      type: 'line',
      data: data.map(item => item.value)
    }],
    tooltip: { trigger: 'axis' }
  }));
  
  // Graph Chart (Neo4j)
  initChart('http://localhost:8000/api/graph/data', 'graph-chart', data => ({
    title: { text: 'Graph Chart', left: 'center' },
    legend: {
      data: [...new Set(data.flatMap(item => [item.source, item.target]))],
      top: 'bottom'
    },
    series: [{
      type: 'graph',
      layout: 'force',
      data: [...new Set(data.flatMap(item => [item.source, item.target]))].map(name => ({ name })),
      links: data.map(item => ({ source: item.source, target: item.target, value: item.weight })),
      roam: true,
      label: { show: true },
      edgeSymbol: ['none', 'arrow'],
      lineStyle: { width: 2 }
    }],
    tooltip: { trigger: 'item' }
  }));
  
  // Hotspot Map (MongoDB)
  initChart('http://localhost:8000/api/hotspot/data', 'hotspot-chart', data => ({
    title: { text: 'Hotspot Map', left: 'center' },
    legend: { data: ['Hotspot'], top: 'bottom' },
    visualMap: {
      min: 0,
      max: 100,
      inRange: { color: ['#d94e5d', '#50a3ba'] },
      show: true,
      left: 'left',
      top: 'top'
    },
    xAxis: {
      type: 'value',
      min: 0,
      max: 100,
      name: 'X Coordinate',
      nameLocation: 'center',
      nameGap: 30
    },
    yAxis: {
      type: 'value',
      min: 0,
      max: 100,
      name: 'Y Coordinate',
      nameLocation: 'center',
      nameGap: 40
    },
    series: [{
      name: 'Hotspot',
      type: 'scatter',
      data: data.map(item => [item.x, item.y, item.value]),
      symbolSize: val => val[2] / 2
    }],
    tooltip: { trigger: 'item' }
  }));