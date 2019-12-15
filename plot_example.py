from quickplot.plotter import quickplot

files = [
    {'filename': 'example_data1.xlsx', 'label': 'Sample 1', 'filetype': 'excel', 'x_column': 'A', 'y_column': 'C', 
    'norm_x': 1, 'norm_y': 1, 'add_x': 0, 'add_y': 0, 'skiprows': 250, 'skipfooter': 30},
    
    {'filename': 'example_data2.xlsx', 'label': 'Sample 2', 'filetype': 'excel', 'x_column': 'A', 'y_column': 'C',
    'norm_x': 1, 'norm_y': 1, 'add_x': 0, 'add_y': 0, 'skiprows': 250, 'skipfooter': 30},

    {'filename': 'example_data3.xlsx', 'label': 'Sample 3', 'filetype': 'excel', 'x_column': 'A', 'y_column': 'C',
    'norm_x': 1, 'norm_y': 1, 'add_x': 0, 'add_y': 0, 'skiprows': 250, 'skipfooter': 30},

    {'filename': 'example_data4.xlsx', 'label': 'Sample 4', 'filetype': 'excel', 'x_column': 'A', 'y_column': 'C',
    'norm_x': 1, 'norm_y': 1, 'add_x': 0, 'add_y': 0, 'skiprows': 250, 'skipfooter': 30}   
]

quickplot(files, title='Samples 1-4', xlabel='Temperature (C)', ylabel='Phase fraction austenite (%)', save_fig=False)