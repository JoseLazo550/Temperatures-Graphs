from matplotlib import markers
import matplotlib.pyplot as plt
temperature_oax = {"January":21.8, "February":22.7, "March":24.6, "April":26.7, "May":25.8, "June":25.0, "July":24.8, 
        "August":24.2, "September":24.3,"October":23.2,"November":22.4, "December":20.3}

def plot_data(monthly_temperature):
    
    months = [month[:3] for month in monthly_temperature]
    temperatures = [monthly_temperature[temp] for temp in monthly_temperature]

    print(months)
    print(temperatures)
    #Create figure and axis
    figure, ax = plt.subplots()

    #Draw lines: (x,y,change colors,markers)
    ax.plot(months, temperatures, color = 'tab:blue', marker = "o")
    
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
    plot_data(temperature_oax)
    
if __name__ == "__main__":
    run()