import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
from . import style as st

def quickplot(files, title=None, xlabel='x', ylabel='y', xmin=None, xmax=None, ymin=None, ymax=None, save_fig=False):
    """ Reads data from a set of files defined in the list files and plots the data accordingly"""

    # Define plot
    plt.style.use(st.style_template)
    fig, ax = plt.subplots(figsize=st.figsize)
    
    # Read files, currently only excel
    for file, style in zip(files, st.linestyles):
        usecols = file['x_column'] + ',' + file['y_column']
        df = pd.read_excel(file['filename'], header=None, usecols=usecols, skiprows=file['skiprows'], skipfooter=file['skipfooter'])
        df = df.div([file['norm_x'], file['norm_y']], axis='columns')  
        df = df.add([file['add_x'], file['add_y']], axis='columns')  
        ax.plot(df[0], df[1], style, label=file['label'], linewidth=st.linewidth)
        
    ax.set_title(title, fontsize=st.title_size)
    ax.set_xlim(left=xmin, right=xmax)
    ax.set_ylim(bottom=ymin, top=ymax)
    ax.set_xlabel(xlabel, fontsize=st.xy_label_size)
    ax.set_ylabel(ylabel, fontsize=st.xy_label_size)
    ax.tick_params(labelsize=st.tick_size)
    ax.grid(st.grid)
    ax.legend(loc=st.legend_location)

    plt.show()

    if save_fig == True:
        fig.savefig(st.filename, transparent=st.transparent, dpi=st.resolution)