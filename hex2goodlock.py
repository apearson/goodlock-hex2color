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

print("HSV")
print(hsv)

# Figuring out if in standard display mode or condensed
displayMode = len(os.popen("adb shell wm density").readlines());

# Screen Settings
if displayMode == 1:
    print('Display Mode: Standard')
    HueAreaStart = (852, 871)  # X, Y
    HueAreaSize = (19 ,534) # Width, Height
    SVAreaStart = (182,872) # X, Y
    SVAreaSize = (655,533) # Width, Height
else:
    print('Display Mode: Condensed')
    HueAreaStart = (826, 924)  # X, Y
    HueAreaSize = (69 ,466) # Width, Height
    SVAreaStart = (249,924) # X, Y
    SVAreaSize = (562,466) # Width, Height

# Finding Location on screen

# Hue Bar on right side
hueLocationMiddle  = round((HueAreaStart[0] + (HueAreaStart[0] + HueAreaSize[0])) / 2)
hueLocation        = round(HueAreaStart[1] + (hsv[0] * HueAreaSize[1]))

# Saturation and Value Area on left side
# Saturation is x while Value is y
saturationLocation = round(SVAreaStart[0]  + (hsv[1] * SVAreaSize[0]))
valueLocation      = round(SVAreaStart[1]  + ((1 - hsv[2]) * SVAreaSize[1]))

#Debug statements
print("Hue Screen Location: %sx%s" % (hueLocationMiddle, hueLocation))
print("Saturation Screen Location: %spx" % saturationLocation)
print("Value Screen Location: %spx" % valueLocation)


command = commandStart + "shell input tap %s %s && adb shell input tap %s %s" % (hueLocationMiddle, hueLocation, saturationLocation, valueLocation)

print(command)
os.system(command)
