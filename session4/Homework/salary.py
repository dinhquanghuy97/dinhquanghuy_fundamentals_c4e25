p1 ={
    "name": "Huy",
    "salary per hour": 25,
    "Hour": 20,
}

p2 ={
    "name": "Quan",
    "salary per hour": 25,
    "Hour": 25,
}

p3 ={
    "name": "Duc",
    "salary per hour": 30,
    "Hour": 40,
}

h_sal = p1["salary per hour"]*p1["Hour"]
q_sal = p2["salary per hour"]*p2["Hour"]
d_sal = p2["salary per hour"]*p2["Hour"]

sal = {
    "Huy": h_sal,
    "Quan": q_sal,
    "Duc": d_sal
}
print(sal)
total =h_sal+q_sal+d_sal
print("total salary: ",total)