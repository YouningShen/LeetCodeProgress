const usernames = ["user1", "user2", "user3"]; // Replace with your LeetCode usernames

async function getSolvedCount(username) {
  const res = await fetch(`https://leetcode.com/${username}`);
  const html = await res.text();

  const match = html.match(/"totalSolved":(\d+)/);
  const total = match ? parseInt(match[1]) : 0;

  return { username, total };
}

async function main() {
  const results = await Promise.all(usernames.map(getSolvedCount));
  const names = results.map(r => r.username);
  const totals = results.map(r => r.total);

  const data = [{
    x: names,
    y: totals,
    type: 'bar',
    marker: { color: 'teal' }
  }];

  const layout = {
    title: 'LeetCode Problems Solved',
    xaxis: { title: 'Username' },
    yaxis: { title: 'Total Solved' }
  };

  Plotly.newPlot('chart', data, layout);
}

main();
