# TargetHeartRate
# This is a program to calculate target heart rate using the resting heart rate and age.
print("This is the Karvonen formula for Target Heart Rate.")
print("It uses your age and your resting heart rate.")
print("How old are you?")
age = int( input())

print("What is your resting heart rate?")
rhr = int( input())

Step1 = 206 - (0.88 * age)
Step2 = Step1 - rhr
THRl = Step2 * 0.65
THRh = Step2 * 0.85
THRlow = THRl + rhr
THRhigh = THRh + rhr

print("Your target heart rate range is from" + str(THRlow) + " to " + str(THRhigh) + "!")
