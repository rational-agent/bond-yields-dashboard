# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
app = Dash(__name__)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
bond_yields = pd.read_csv("yields.csv")
bond_yields["time"] = bond_yields["time"] / 1_000
bond_yields["time"] = bond_yields["time"].astype(int)
bond_yields["time"] = pd.to_datetime(bond_yields["time"], unit='s')
bond_yields.rename(columns={"time": "datetime"}, inplace=True)
bond_yields.sort_values(by="datetime", ascending=True, inplace=True)

# australian_yields = px.line(bond_yields, x="datetime", y=[i for i in bond_yields.columns if 'AU' in i], title='Australian Government Bonds term')
# belgian_yields = px.line(bond_yields, x="datetime", y=[i for i in bond_yields.columns if 'BE' in i], title='Belgian Government Bonds term')
# canadian_yields = px.line(bond_yields, x="datetime", y=[i for i in bond_yields.columns if 'CA' in i], title='Canadian Government Bonds term')
# chinese_yields = px.line(bond_yields, x="datetime", y=[i for i in bond_yields.columns if 'CN' in i], title='Chinese Government Bonds term')
# danish_yields = px.line(bond_yields, x="datetime", y=[i for i in bond_yields.columns if 'DK' in i], title='Danish Government Bonds term')
# french_yields = px.line(bond_yields, x="datetime", y=[i for i in bond_yields.columns if 'FR' in i], title='French Government Bonds term')
# german_yields = px.line(bond_yields, x="datetime", y=[i for i in bond_yields.columns if 'DE' in i], title='German Government Bonds term')
# greek_yields = px.line(bond_yields, x="datetime", y=[i for i in bond_yields.columns if 'GR' in i], title='Greek Government Bonds term')
# hongkong_yields = px.line(bond_yields, x="datetime", y=[i for i in bond_yields.columns if 'HK' in i], title='HongKong Government Bonds term')
# indian_yields = px.line(bond_yields, x="datetime", y=[i for i in bond_yields.columns if 'IN' in i], title='Indian Government Bonds term')
# indonesian_yields = px.line(bond_yields, x="datetime", y=[i for i in bond_yields.columns if 'ID' in i], title='Indonesian Government Bonds term')
irish_yields = px.line(bond_yields, x="datetime", y=[i for i in bond_yields.columns if 'IE' in i], title='Irish Government Bonds term')
# italian_yields = px.line(bond_yields, x="datetime", y=[i for i in bond_yields.columns if 'IT' in i], title='Italian Government Bonds term')
# japanese_yields = px.line(bond_yields, x="datetime", y=[i for i in bond_yields.columns if 'JP' in i], title='Japanese Government Bonds term')
# korean_yields = px.line(bond_yields, x="datetime", y=[i for i in bond_yields.columns if 'KR' in i], title='Korean Government Bonds term')
# malay_yields = px.line(bond_yields, x="datetime", y=[i for i in bond_yields.columns if 'MY' in i], title='Malay Government Bonds term')
# dutch_yields = px.line(bond_yields, x="datetime", y=[i for i in bond_yields.columns if 'NL' in i], title='Dutch Government Bonds term')
# new_zealand_yields = px.line(bond_yields, x="datetime", y=[i for i in bond_yields.columns if 'NZ' in i], title='New Zealand Government Bonds term')
# norwegian_yields = px.line(bond_yields, x="datetime", y=[i for i in bond_yields.columns if 'NO' in i], title='Norwegian Government Bonds term')
# polish_yields = px.line(bond_yields, x="datetime", y=[i for i in bond_yields.columns if 'PL' in i], title='Polish Government Bonds term')
portuguese_yields = px.line(bond_yields, x="datetime", y=[i for i in bond_yields.columns if 'PT' in i], title='Portuguese Government Bonds term')
# singaporean_yields = px.line(bond_yields, x="datetime", y=[i for i in bond_yields.columns if 'SG' in i], title='Singaporean Government Bonds term')
# south_african_yields = px.line(bond_yields, x="datetime", y=[i for i in bond_yields.columns if 'ZA' in i], title='South-African Government Bonds term')
# spanish_yields = px.line(bond_yields, x="datetime", y=[i for i in bond_yields.columns if 'ES' in i], title='Spanish Government Bonds term')
# swedish_yields = px.line(bond_yields, x="datetime", y=[i for i in bond_yields.columns if 'SE' in i], title='Swedish Government Bonds term')
# taiwan_yields = px.line(bond_yields, x="datetime", y=[i for i in bond_yields.columns if 'TW' in i], title='Taiwan Government Bonds term')
# thai_yields = px.line(bond_yields, x="datetime", y=[i for i in bond_yields.columns if 'TH' in i], title='Thai Government Bonds term')
# turkish_yields = px.line(bond_yields, x="datetime", y=[i for i in bond_yields.columns if 'TR' in i], title='Turkish Government Bonds term')
# british_yields = px.line(bond_yields, x="datetime", y=[i for i in bond_yields.columns if 'GB' in i], title='British Government Bonds term')
# us_yields = px.line(bond_yields, x="datetime", y=[i for i in bond_yields.columns if 'US' in i], title='American Government Bonds term')

app.layout = html.Div(children=[
    html.H1(children='Government Bonds'),
    html.Div(children='''
        The dataset contains government bond prices and yields of 30 countries from 6 world regions.
    '''),
    # dcc.Graph(id='australian_yields-graph', figure=australian_yields),
    # dcc.Graph(id='belgian_yields-graph', figure=belgian_yields),
    # dcc.Graph(id='canadian_yields-graph', figure=canadian_yields),
    # dcc.Graph(id='danish_yields-graph', figure=danish_yields),
    # dcc.Graph(id='french_yields-graph', figure=french_yields),
    # dcc.Graph(id='german_yields-graph', figure=german_yields),
    # dcc.Graph(id='greek_yields-graph', figure=greek_yields),
    # dcc.Graph(id='hongkong_yields-graph', figure=hongkong_yields),
    # dcc.Graph(id='indian_yields-graph', figure=indian_yields),
    # dcc.Graph(id='indonesian_yields-graph', figure=indonesian_yields),
    dcc.Graph(id='irish_yields-graph', figure=irish_yields),
    # dcc.Graph(id='italian_yields-graph', figure=italian_yields),
    # dcc.Graph(id='japanese_yields-graph', figure=japanese_yields),
    # dcc.Graph(id='korean_yields-graph', figure=korean_yields),
    # dcc.Graph(id='malay_yields-graph', figure=malay_yields),
    # dcc.Graph(id='new_zealand_yields-graph', figure=new_zealand_yields),
    # dcc.Graph(id='norwegian_yields-graph', figure=norwegian_yields),
    # dcc.Graph(id='polish_yields-graph', figure=polish_yields),
    dcc.Graph(id='portuguese_yields-graph', figure=portuguese_yields),
    # dcc.Graph(id='singaporean_yields-graph', figure=singaporean_yields),
    # dcc.Graph(id='south_african_yields-graph', figure=south_african_yields),
    # dcc.Graph(id='spanish_yields-graph', figure=spanish_yields),
    # dcc.Graph(id='swedish_yields-graph', figure=swedish_yields),
    # dcc.Graph(id='taiwan_yields-graph', figure=taiwan_yields),
    # dcc.Graph(id='thai_yields-graph', figure=thai_yields),
    # dcc.Graph(id='turkish_yields-graph', figure=turkish_yields),
    # dcc.Graph(id='british_yields-graph', figure=british_yields),
    # dcc.Graph(id='us_yields-graph', figure=us_yields)
])

if __name__ == '__main__':
    app.run_server(debug=True)
