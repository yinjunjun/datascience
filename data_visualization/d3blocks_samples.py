# Load d3blocks
from d3blocks import D3Blocks
#
# Initialize
d3 = D3Blocks()
#
# Create chart with defaults
# d3.particles('DATS 2102: Data Visualization')
#
# Create customized chart
d3.particles('DATS 2102',
                 filepath='./D3Blocks.html',
                 collision=0.05,
                 spacing=7,
                 figsize=[700, 170],
                 fontsize=130,
                 cmap='Turbo',
                 color_background='#ffffff')