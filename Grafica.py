from os import stat
from matplotlib import markers
import matplotlib.pyplot as plt

def plot_data(temperature_data, months):

    #Create figure and axis
    plt.rcParams["figure.figsize"] = (12, 8)
    figure, ax = plt.subplots()
    
    for state in temperature_data:
        print(state)
        temperatures = []
        for temp in temperature_data[state]:
             temperatures.append(temperature_data[state][temp]) 
           
        months_plot = [m[:3] for m in months]
        
        #Draw lines: (x,y,change colors,markers)
        ax.plot(months_plot, temperatures, marker = ".", label = state)
        print(months_plot)
        print(temperatures)
    
    ax.legend(loc = 'upper right')
    
    
    #Set title
    
    ax.set_title('Temperaturas', loc = 'center',
        fontdict = {'font':'Arial','fontsize':14, 'fontweight':'bold'})
    
    #Name Axis
    ax.set_ylabel("Temperatura en °C")
    ax.set_xlabel("Mes")
    
    #Save graphic
    #plt.savefig("TemperatureGraphic.png")
    
    #Show Gaphic
    plt.show()
    

def run():
    pass
    
if __name__ == "__main__":
    run()