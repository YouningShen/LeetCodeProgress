# dashboard.py
import plotly.graph_objects as go

def create_bar_chart(user_stats: list):
    usernames = [u['username'] for u in user_stats]
    totals = [int(u['total_solved']) for u in user_stats]

    fig = go.Figure(go.Bar(x=usernames, y=totals, marker_color='skyblue'))
    fig.update_layout(
        title="LeetCode Problems Solved",
        xaxis_title="User",
        yaxis_title="Total Solved",
        template="plotly_white"
    )
    return fig.to_html(full_html=False)
