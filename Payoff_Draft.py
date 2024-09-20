import Equity_Pricer
import IR_Pricer

class Payoff :
    def __init__(self,parameters,number_of_simulations):
        self.parameters= parameters
        self.number_of_simulations = number_of_simulations
        self.pricer_object = self.identify_asset_class_object()
    def identify_asset_class_object(self) :
        asset_class = self.parameters["Asset Class"]
        product_type = self.parameters["Product"]
        if asset_class == "Equity" :
            if product_type == "Call " :
                object = Equity_Pricer.Call_option(self.parameters,self.number_of_simulations)
            if product_type == "AutoCallable" :
                object = Equity_Pricer.AutoCallable(self.parameters,self.number_of_simulations)
        elif asset_class == "IR" :
            if product_type == "Cap" :
                object = IR_Pricer.Cap (self.parameters,self.number_of_simulations)
        return object
    def price (self) :
        return self.pricer_object.price()


