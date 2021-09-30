from matplotlib import markers
import matplotlib.pyplot as plt


def run():
    temperature_oax = {"January":21.8, "February":22.7, "March":24.6, "April":26.7, "May":25.8, "June":25.0, "July":24.8, 
        "August":24.2, "September":24.3,"October":23.2,"November":22.4, "December":20.3}
    
    months = [month[:3] for month in temperature_oax]
    temperatures = [temperature_oax[temp] for temp in temperature_oax]

    #Create figure and axis
    figure, ax = plt.subplots()

    #Draw lines: (x,y,change colors,markers)
    ax.plot(months, temperatures, color = 'tab:red', marker = "o")
    
    #Set title
    ax.set_title('Temperatures in Oaxaca troughout 2020', loc = 'center',
        fontdict = {'font':'courier','fontsize':14, 'fontweight':'bold'})
    
    #Name Axis
    ax.set_ylabel("Temperature in °C")
    ax.set_xlabel("Months")
    
    #Save graphic
    #plt.savefig("TemperatureGraphic.png")
    
    #Show Gaphic
    plt.show()
    
    
if __name__ == "__main__":
    run()