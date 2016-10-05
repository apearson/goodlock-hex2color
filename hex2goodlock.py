import os
import sys
import colorsys
import matplotlib.colors as colors

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
rgb = colors.hex2color(sys.argv[1])

# print("Printing screen locations for: " + sys.argv[1])

# Converting to correct color space
hsv = colorsys.rgb_to_hsv(rgb[0], rgb[1], rgb[2])

# Finding Location on screen
hueLocation        = round(924 + (hsv[0] * 466))
saturationLocation = round(249 + (hsv[1] * 562))
valueLocation      = round(924 + ((1 - hsv[2]) * 466))

# print("Hue Screen Location: %spx" % hueLocation)
# print("Saturation Screen Location: %spx" % saturationLocation)
# print("Value Screen Location: %spx" % valueLocation)

command = commandStart + "shell input tap 850 %s && adb shell input tap %s %s" % (hueLocation, saturationLocation, valueLocation)

print(command)
# os.system(command)
