import plotly.graph_objects as go

def plot_vol_surface_html(K_list, T_list, surface):
    fig = go.Figure(data=[go.Surface(z=surface, x=K_list, y=T_list)])
    fig.update_layout(
        title='Volatility Surface',
        scene=dict(
            xaxis_title='Strike Price',
            yaxis_title='Time to Maturity',
            zaxis_title='Implied Volatility'
        ),
        autosize=True
    )
    return fig.to_html(full_html=False)
