#!/usr/bin/python3

from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

model = BayesianNetwork([("Burglary", "Alarm"), ("Earthquake", "Alarm"), ("Alarm", "JohnCalls"), ("Alarm", "MaryCalls")])

cpd_burglary = TabularCPD("Burglary", 2, [[0.001], [0.999]])
cpd_earthquake = TabularCPD("Earthquake", 2, [[0.002], [0.998]])
cpd_alarm = TabularCPD("Alarm", 2, [[0.95,0.94,0.29,0.001], [1-0.95,1-0.94,1-0.29,1-0.001]], ["Burglary", "Earthquake"], [2,2])
cpd_john = TabularCPD("JohnCalls", 2, [[0.90, 0.05], [1-0.90, 1-0.05]], ["Alarm"], [2])
cpd_mary = TabularCPD("MaryCalls", 2, [[0.70,0.01], [1-0.70,1-0.01]], ["Alarm"], [2])

model.add_cpds(cpd_burglary, cpd_earthquake, cpd_alarm, cpd_john, cpd_mary)
model.check_model()

# print(cpd_burglary)
# print(cpd_earthquake)
# print(cpd_alarm)
# print(cpd_john)
# print(cpd_mary)

infer = VariableElimination(model)
# prob = infer.query(["Burglary"], evidence={"JohnCalls": 0, "MaryCalls": 0})
# print(prob)

# prob = infer.query(["Alarm"], evidence={"JohnCalls": 0, "MaryCalls": 0, "Earthquake": 1, "Burglary": 1})
# print(prob)

prob = infer.query(variables=['Alarm'], evidence={'Burglary': 1, 'Earthquake': 1, 'JohnCalls': 0, 'MaryCalls': 0})
print(prob)
result = prob.values[0]
print('The probability that the alarm has sounded but neither a burglary nor an earthquake has occurred, and both John and Mary calls:', result)

