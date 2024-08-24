#climate change project

import numpy
from matplotlib.pyplot import *
import simmod


def plot_carbon_emissions():
  years, emissions = numpy.loadtxt('emissions/historical_ghgs.csv',
                                   usecols=(0, 1),
                                   delimiter=',',
                                   skiprows=1,
                                   unpack=True)

  plot(years, emissions, 'r-',
       label='Carbon')  # Plot c vs cyear using a red line.

  legend(loc='upper left')  # Add a legend to the graph.
  title("Historical Carbon Emissions")  # Set the title for the plot.
  xlabel("Year")  # Label the x axis.
  ylabel("Carbon Emissions (pg)")  # Label the y axis.
  grid(True)  # Turn on the grid lines.
  show()  # Make the graph show up in the notebook.


def plot_methane_emissions():
  years, emissions = numpy.loadtxt('emissions/historical_ghgs.csv',
                                   usecols=(0, 2),
                                   delimiter=',',
                                   skiprows=1,
                                   unpack=True)

  plot(years, emissions, 'r-',
       label='Methane')  # Plot c vs cyear using a red line.

  legend(loc='upper left')  # Add a legend to the graph.
  title("Historical Methane Emissions")  # Set the title for the plot.
  xlabel("Year")  # Label the x axis.
  ylabel("Methane Emissions (pg)")  # Label the y axis.
  grid(True)  # Turn on the grid lines.
  show()  # Make the graph show up in the notebook.


def plot_carbon_rcps():
  years, emissions = numpy.loadtxt('emissions/rcp_2.6_data.csv',
                                   usecols=(0, 7),
                                   delimiter=',',
                                   skiprows=1,
                                   unpack=True)

  plot(years, emissions, 'Green',
       label='RCP2.6')  # Plot c vs cyear using a red line.

  years, emissions = numpy.loadtxt('emissions/rcp_4.5_data.csv',
                                   usecols=(0, 7),
                                   delimiter=',',
                                   skiprows=1,
                                   unpack=True)

  plot(years, emissions, 'BlueViolet',
       label='RCP4.5')  # Plot c vs cyear using a red line.

  years, emissions = numpy.loadtxt('emissions/rcp_6.0_data.csv',
                                   usecols=(0, 7),
                                   delimiter=',',
                                   skiprows=1,
                                   unpack=True)

  plot(years, emissions, 'Gold',
       label='RCP6.0')  # Plot c vs cyear using a red line.

  years, emissions = numpy.loadtxt('emissions/rcp_8.5_data.csv',
                                   usecols=(0, 7),
                                   delimiter=',',
                                   skiprows=1,
                                   unpack=True)

  plot(years, emissions, 'Red',
       label='RCP8.5')  # Plot c vs cyear using a red line.

  legend(loc='upper left')  # Add a legend to the graph.
  title("Representative Concentration Pathways")  # Set the title for the plot.
  xlabel("Year")  # Label the x axis.
  ylabel("CO2 Concentration")  # Label the y axis.
  grid(True)  # Turn on the grid lines.
  show()  # Make the graph show up in the notebook.


def simulate_rcp_2_6():
  simmod.run_simmod(1900, 2100, '2.6', 3, 'results/rcp_2.6.csv')

def plot_rcp_2_6():
  years, emissions = numpy.loadtxt('results/rcp_2.6.csv',
     usecols=(2, 30),
     delimiter=',',
     skiprows=1,
     unpack=True)

  plot(years, emissions, 'r-',
  label='Temperature Change')  # Plot c vs cyear using a red line.

  legend(loc='upper left')  # Add a legend to the graph.
  title("RCP_2.6 Temperature Change")  # Set the title for the plot.
  xlabel("Year")  # Label the x axis.
  ylabel("Temperature Change (C)")  # Label the y axis.
  grid(True)  # Turn on the grid lines.
  show()  # Make the graph show up in the notebook.

def simulate_all_rcps():
  simmod.run_simmod(1900, 2100, '2.6', 3, 'results/rcp_2.6.csv')

  simmod.run_simmod(1900, 2100, '4.5', 3, 'results/rcp_4.5.csv')

  simmod.run_simmod(1900, 2100, '6.0', 3, 'results/rcp_6.0.csv')

  simmod.run_simmod(1900, 2100, '8.5', 3, 'results/rcp_8.5.csv')

def plot_all_rcps():
  years, emissions = numpy.loadtxt('results/rcp_2.6.csv',
     usecols=(2, 30),
     delimiter=',',
     skiprows=1,
     unpack=True)

  plot(years, emissions, 'Green',
  label='RCP2.6')  # Plot c vs cyear using a red line.

  years, emissions = numpy.loadtxt('results/rcp_4.5.csv',
     usecols=(2, 30),
     delimiter=',',
     skiprows=1,
     unpack=True)

  plot(years, emissions, 'BlueViolet',
  label='RCP4.5')  # Plot c vs cyear using a red line.

  years, emissions = numpy.loadtxt('results/rcp_6.0.csv',
     usecols=(2, 30),
     delimiter=',',
     skiprows=1,
     unpack=True)

  plot(years, emissions, 'Gold',
  label='RCP6.0')  # Plot c vs cyear using a red line.

  years, emissions = numpy.loadtxt('results/rcp_8.5.csv',
     usecols=(2, 30),
     delimiter=',',
     skiprows=1,
     unpack=True)

  plot(years, emissions, 'Red',
  label='RCP8.5')  # Plot c vs cyear using a red line.

  legend(loc='upper left')  # Add a legend to the graph.
  title("All RCP Temperature Changes")  # Set the title for the plot.
  xlabel("Year")  # Label the x axis.
  ylabel("Temperature Change (C)")  # Label the y axis.
  grid(True)  # Turn on the grid lines.
  show()  # Make the graph show up in the notebook.
  
#plot_carbon_emissions()
#plot_methane_emissions()
#plot_carbon_rcps()
#simulate_rcp_2_6()
#plot_rcp_2_6()
#simulate_all_rcps()
plot_all_rcps()
