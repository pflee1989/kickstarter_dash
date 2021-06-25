# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Imports from this application
from app import app

# 1 column layout
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## Insights
            
            The random forest classifier model, the one in this app, shows that the most important factors are the number
            
            of initial backers, the goal in usd and the pledged amount. The picture below shows that the key is to turn backers into
            
            sponsors. 

            """
        
        ), 
    
    
    html.Img(src='assets/pdp.png', className='img-fluid'),
    

    ],
)



       
layout = dbc.Row([column1])