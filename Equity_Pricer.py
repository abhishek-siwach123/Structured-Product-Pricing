import numpy as np
class AutoCallable() :
    def __init__(self,parameters,number_of_simulations):
        self.parameters= parameters
        self.number_of_simulations = number_of_simulations
    def price (self) :
        return 100



class Call_option:
    def __init__(self, parameters, number_of_simulations):
        # Define required parameters
        required_params = [
            'Payoff Function',
            'Stock Price (S0)',
            'Strike Price (K)',
            'Volatility Type',
            'Volatility (σ)',
            'Stochastic Rate',
            'Risk-Free Rate (r)',
            'Maturity (T in years)'
        ]

        # Check for missing parameters
        for param in required_params:
            if param not in parameters:
                raise ValueError(f"Missing required parameter: {param}")

        # Extract and validate parameters
        self.payoff_function = parameters['Payoff Function']
        self.S0 = float(parameters['Stock Price (S0)'])
        self.K = float(parameters['Strike Price (K)'])
        self.sigma = float(parameters['Volatility (σ)'])
        self.r = float(parameters['Risk-Free Rate (r)'])
        self.T = float(parameters['Maturity (T in years)'])
        self.stochastic_rate = parameters['Stochastic Rate']

        # Validate that 'Volatility Type' and 'Stochastic Rate' are acceptable
        if parameters['Volatility Type'] != 'Constant':
            raise ValueError("Unsupported Volatility Type. Only 'Constant' is supported in this implementation.")
        if self.stochastic_rate == 'YES':
            raise NotImplementedError("Stochastic Rate 'YES' is not implemented in this example.")

        # Store the number of simulations
        self.number_of_simulations = number_of_simulations

    def price(self):
        # Validate payoff function
        if self.payoff_function != 'max(S-K,0)':
            raise ValueError("Unsupported Payoff Function. Only 'max(S-K,0)' is supported in this implementation.")

        # Monte Carlo simulation for call option pricing
        dt = self.T / self.number_of_simulations
        random_shocks = np.random.normal(0, 1, self.number_of_simulations)
        price_paths = np.zeros(self.number_of_simulations)

        # Simulate the stock price path
        for i in range(self.number_of_simulations):
            ST = self.S0 * np.exp(
                (self.r - 0.5 * self.sigma ** 2) * self.T +
                self.sigma * np.sqrt(self.T) * random_shocks[i]
            )
            price_paths[i] = ST

        # Calculate payoffs
        payoffs = np.maximum(price_paths - self.K, 0)

        # Calculate the average payoff and discount it to present value
        average_payoff = np.mean(payoffs)
        discounted_price = np.exp(-self.r * self.T) * average_payoff

        return discounted_price







        
