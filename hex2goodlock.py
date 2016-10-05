import os
import sys
import colorsys

# Decided to use built in adb binary or now
useSystemADB = True
hasADB = os.popen("which adb").readline().strip()
if sys.platform == "darwin" and not hasADB:
    useSystemADB = False

# Setting start of command
commandStart = "adb "
if not useSystemADB:
    commandStart = "./mac-tools/adb "

# Getting color from command line
inputHex = sys.argv[1]

print("Input Hex: " + inputHex)

# Converting from hex string to decimal values
rgb = (int(inputHex[1:3],16), int(inputHex[3:5], 16), int(inputHex[5:7], 16))

# Converting to correct color space
hsv = colorsys.rgb_to_hsv(rgb[0]/255, rgb[1]/255, rgb[2]/255)

# Finding Location on screen
hueLocation        = round(924 + (hsv[0] * 466))
saturationLocation = round(249 + (hsv[1] * 562))
valueLocation      = round(924 + ((1 - hsv[2]) * 466))

print("Hue Screen Location: %spx" % hueLocation)
print("Saturation Screen Location: %spx" % saturationLocation)
print("Value Screen Location: %spx" % valueLocation)

command = commandStart + "shell input tap 850 %s && adb shell input tap %s %s" % (hueLocation, saturationLocation, valueLocation)

print(command)
os.system(command)
