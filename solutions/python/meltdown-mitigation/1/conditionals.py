"""Functions to prevent a nuclear meltdown."""


def is_criticality_balanced(temperature, neutrons_emitted):
   if temperature < 800:
       if neutrons_emitted > 500:
           if temperature * neutrons_emitted < 500000:
               return True
   return False

def reactor_efficiency(voltage, current, theoretical_max_power):
    generated_power = voltage * current
    efficiency = (generated_power / theoretical_max_power) * 100

    if efficiency >= 80:
        return 'green'
    elif efficiency >= 60:
        return 'orange'
    elif efficiency >= 30:
        return 'red'
    else:
        return 'black'
        

def fail_safe(temperature, neutrons_produced_per_second, threshold):
    hold = temperature * neutrons_produced_per_second

    if hold > threshold * 1.1:
        return 'DANGER'
    elif hold > threshold * 0.9:
        return 'NORMAL'
    else:
        return 'LOW'    
