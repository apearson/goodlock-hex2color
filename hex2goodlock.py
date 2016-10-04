import os
import sys
import colorsys

# Getting color from command lin
color = sys.argv[1];

print("Printing screen locations for: " + color)

# Converting to correct color space
hsv = colorsys.rgb_to_hsv(37/255, 50/255, 55/255)

# Finding Location on screen
hueLocation = round(924 + (hsv[0] * 466))

saturationLocation = round(249 + (hsv[1] * 562))

valueLocation = round(924 + ((1 - hsv[2]) * 466))

print("Hue Screen Location: %spx" % hueLocation)
print("Saturation Screen Location: %spx" % saturationLocation)
print("Value Screen Location: %spx" % valueLocation)

command = "adb shell input tap 850 %s && adb shell input tap %s %s" % (hueLocation, saturationLocation, valueLocation)

os.system(command)
