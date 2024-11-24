from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

data = {
    '일': ['8일', '9일', '10일', '11일', '12일', '13일', '14일', '15일', '16일', '17일', '18일', '19일', '20일', '21일'],
    '매출': [3418679, 3763679, 1876679, 2947679, 2412679, 1726679, 3814679, 3511679, 5176679, 2073679, 4401679, 4217679, 4450679, 4867679],
    '매입': [3440000, 4590000, 2050000, 2930000, 2360000, 1710000, 3500000, 3250000, 5740000, 2160000, 4530000, 4000000, 4350000, 4750000],
    '주': ['2주', '2주', '2주', '2주', '2주', '2주', '2주', '3주', '3주', '3주', '3주', '3주', '3주', '3주'],
}


df = pd.DataFrame(data)

colors = {
    'background': 'linear-gradient(135deg, #2C3E50, #4CA1AF)',
    'card': '#34495E',
    'text': '#ECF0F1',
    'accent': '#E74C3C',
    'secondary': '#3498DB',
    'tertiary': '#2ECC71',
    'quaternary': '#F1C40F',
    'quinary': '#9B59B6',
    'senary': '#1ABC9C',
    'septenary': '#E67E22',
    'octonary': '#BDC3C7',
    'nonary': '#7F8C8D',
    'denary': '#D35400',
    'undecenary': '#C0392B',
    'duodenary': '#8E44AD',
    'tridenary': '#16A085',
}
card_style = {
    'backgroundColor': colors['card'],
    'padding': '10px',
    'borderRadius': '5px',
    'boxShadow': '0px 1px 3px rgba(0,0,0,0.1)',
    'flex': '1',
    'transition': 'transform 0.2s',
    'hover': {
        'transform': 'scale(1.05)',
        'boxShadow': '0px 4px 8px rgba(0,0,0,0.2)'
    }
}
graph_style = {'showlegend': False, 'height': 300}

app = Dash(__name__)

def create_card(title, figure):
    return html.Div([
        html.H3(title, style={'color': colors['text'], 'fontSize': '18px', 'fontFamily': 'Arial, sans-serif'}),
        dcc.Graph(figure=figure.update_layout(**graph_style))
    ], style=card_style, className='card')

app.layout = html.Div(style={'background': colors['background'], 'padding': '10px'}, children=[
    html.Div([
        html.H1("세진육운 호카게", style={'color': colors['text'], 'textAlign': 'center', 'fontSize': '60px', 'marginBottom': '10px', 'fontFamily': 'Arial, sans-serif'}),
        html.P("차크라를 통한 데이터분석", style={'textAlign': 'center', 'color': colors['text'], 'fontSize': '20px', 'fontFamily': 'Arial, sans-serif'}),
    ], style={'marginBottom': '20px'}),

    html.Div([
        create_card("매출", px.area(df, x='일', y='매출', color_discrete_sequence=[colors['accent']], template="plotly_dark")),
        create_card("매입", px.bar(df, x='일', y='매입', color_discrete_sequence=[colors['secondary']], template="plotly_dark")),
        create_card("매출 vs 매입", px.bar(df, x='일', y=['매출', '매입'], barmode='group', color_discrete_sequence=[colors['tertiary'], colors['quaternary']], template="plotly_dark").update_layout(showlegend=True)),
        create_card("주별 매출", px.bar(df.groupby('주').sum().reset_index(), x='주', y='매출', color='주', title="주별 매출", color_discrete_sequence=px.colors.qualitative.Set3, template="plotly_dark")),
        create_card("매출 & 매입 추세", px.line(df, x='일', y=['매출', '매입'], markers=True, color_discrete_sequence=[colors['quinary'], colors['senary']], template="plotly_dark").update_layout(showlegend=True)),
        create_card("매출 vs 매입 차이", px.line(df, x='일', y=(df['매출'] - df['매입']), markers=True, color_discrete_sequence=[colors['septenary']], template="plotly_dark")),
        create_card("주별 매입", px.bar(df.groupby('주').sum().reset_index(), x='주', y='매입', color='주', title="주별 매입", color_discrete_sequence=px.colors.qualitative.Set3, template="plotly_dark")),
        create_card("매출 & 매입 분포", px.scatter(df, x='매출', y='매입', size='매출', color='일', template="plotly_dark").update_layout(showlegend=True)),
        create_card("월별 차이", px.line(df, x='일', y=(df['매출'] - df['매입']), markers=True, color_discrete_sequence=[colors['octonary']], template="plotly_dark")),
        create_card("트렌드 분석", px.area(df, x='일', y=['매출', '매입'], color_discrete_sequence=[colors['nonary'], colors['denary']], template="plotly_dark").update_layout(showlegend=True)),
        create_card("평균 매출", px.histogram(df, x='매출', nbins=10, color_discrete_sequence=[colors['undecenary']], template="plotly_dark")),
        create_card("평균 매입", px.histogram(df, x='매입', nbins=10, color_discrete_sequence=[colors['duodenary']], template="plotly_dark")),
        create_card("매출 분포", px.box(df, y='매출', color_discrete_sequence=[colors['tridenary']], template="plotly_dark")),
        create_card("매입 분포", px.box(df, y='매입', color_discrete_sequence=[colors['accent']], template="plotly_dark")),
        create_card("매출 히트맵", px.density_heatmap(df, x='일', y='매출', color_continuous_scale='Viridis', template="plotly_dark")),
        create_card("매입 히트맵", px.density_heatmap(df, x='일', y='매입', color_continuous_scale='Cividis', template="plotly_dark")),
    ], style={'display': 'grid', 'gridTemplateColumns': 'repeat(4, 1fr)', 'gap': '10px'}),

    html.Footer("© 2024 호카게 고용하. All rights reserved.", style={'textAlign': 'center', 'color': colors['text'], 'padding': '10px', 'fontFamily': 'Arial, sans-serif'})
])

if __name__ == "__main__":
    app.run_server(debug=True, host='0.0.0.0', port=10000)
