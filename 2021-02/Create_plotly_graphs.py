import plotly.express as px
import plotly
import plotly.graph_objs as go
import pandas as pd
import numpy as np
from tqdm import tqdm
import os

print(os.path.abspath(os.path.relpath("/2021-02/Probe 1_2021-02-15/")))

path = "/accel-datalogger/2021-02/Probe 1_2021-02-15/"

files = os.listdir(path)
csvfiles = [f for f in files if f.endswith(".CSV")]

for f in tqdm(csvfiles):
    df = pd.read_csv(path+f, names=['MinSec', 'accX', 'accY', 'accZ', 'gyroX', 'gyroY', 'gyroZ'])
    df['MinSec'] = df['MinSec'] + '_' + df.index.astype(str)
    df['norm'] = np.sqrt(df['accX']**2 + df['accY']**2 + df['accZ']**2)
    fig = px.line(df, x='MinSec', y=["accX", "accY", "accZ", "norm"])
    fig.write_html(path+f[:-4] + ".html")
