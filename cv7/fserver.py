from xmlrpc.server import SimpleXMLRPCServer

class Forecast(object):
    """
    Reprezentuje predpoved. V instancnich promennych jsou reprezentovany hodnoty
    predpovedi.
    """

    def __init__(self, description, wind_force, temperature):
        """
        Konstuktor predpovedi. Instancni promenne reprezentuji predana data.
        """
        self.description=description
        self.wind_force=wind_force
        self.temperature=temperature

    def get_list(self):
        """
        Vraci trojici reprezentujici predpoved.
        """
        return list(self.description,self.wind_force,self.temperature)


    def __str__(self):
        return "description: {0} wind force: {1} temperature: {2}".format(self.description,self.wind_force,self.temperature)

class ForecastCalendar(object):
    """
    Reprezentuje predpovedi pro nekolik dni. Data predpovedi jsou ulozena ve
    slovniku. Klicem je datum, hodnotou pak instance trody Forecast. Vkladani
    predpovedi metodou update_forecast je chraneno heslem, ktere je predano v
    konstruktoru. Startovaci data jsou tezz predana v konstruktoru.
    """
    
    def __init__(self, initial_values, password):
        """
        Konstruktor kalendare predpovedi. Instancni promenne reprezentuji predana data.
        """
        self.initial_values=initial_values
        self.password=password


    def get_forecast(self, date):
        """
        Vrati predpoved pro zadane datum jako retezec. V pripade, ze pro dane
        datum neexistuje predpoved. Vrati se retezec "No focecast".
        """
        # ret=str(self.initial_values[date])
        # return ret if ret not null else return "No forecast"
        try:
            return str(self.initial_values[date])
        except:
            return "No forecast"

    def update_forecast(self, password, date, description, wind_force, temperature):
        """
        Aktualizuje predpoved pro zadane datum. Akce je chranena heslem. Pokud
        heslo nesouhlasi s heslem, ktere je zadano v konstruktoru, neni mozno
        aktualizovat predpoved. v takovm priapde metoda vrati retezec "No
        update". Metoda muze aktualizovat stavajici predpoved nebo pridat novou.
        """
        fore=Forecast(description,wind_force,temperature)
        if password == self.password:
            self.initial_values[date]=fore
            return "Updated!"
        else: return "No update"
        
def main():

    # TODO Pridat do initial_state data predpovedi tak, aby je mohl klient
    # precist.
    fore1=Forecast("raining","big force","big temperature")
    fore2 = Forecast("not raining", 15, 20)

    initial_state = {"2012-11-05" : fore1, "2012-11-06": fore2}

    fcalendar = ForecastCalendar(initial_state, password = "master-of-weather")

    server_address = ('localhost', 10001)
    server = SimpleXMLRPCServer(server_address)
    server.register_instance(fcalendar)
    server.register_introspection_functions()
    print("Starting Weather XML-RPC server, use <Ctrl-C> to stop")
    server.serve_forever()

if __name__ == "__main__":
    main()
