import matplotlib.pyplot as plt 
time=[0, 1, 2, 3, 4 ,5] 
velocity=[0, 10, 20, 20, 30, 40]
plt.plot(time, velocity)
plt.title("🚲Bicycle speed over time🚲")
plt.xlabel("Time (hours)")
plt.ylabel("velocity(km/ph)")

plt.show()
