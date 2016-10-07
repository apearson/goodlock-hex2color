import os
import sys
import colorsys

# Getting color from command line
inputHex = sys.argv[1]

print("Input Hex: " + inputHex)

# Converting from hex string to decimal values
print("Parsing hex to rgb")
rgb = (int(inputHex[1:3],16), int(inputHex[3:5], 16), int(inputHex[5:7], 16))

# Converting to correct color space
print("Converting rgb into hsv space")
hsv = colorsys.rgb_to_hsv(rgb[0]/255, rgb[1]/255, rgb[2]/255)

# Figuring out if in standard display mode or condensed
print("Querying device for screen density")
densityOutput = os.popen("adb shell wm density").read()

# Screen Settings
print("Parsing screen density")
if "Override density: 560" in densityOutput:
    print("Display Mode: Condensed")
    HueAreaStart = (826, 924)  # X, Y
    HueAreaSize = (69 ,466) # Width, Height
    SVAreaStart = (249,924) # X, Y
    SVAreaSize = (562,466) # Width, Height
elif "Physical density: 640" in densityOutput:
    print("Display Mode: Standard")
    HueAreaStart = (852, 871)  # X, Y
    HueAreaSize = (19 ,534) # Width, Height
    SVAreaStart = (182,871) # X, Y
    SVAreaSize = (655,534) # Width, Height
else:
    sys.exit("Display Density Not Supported!")

# Finding Location on screen
print('Finding correct screen locations')

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

print("Creating command for device")
command = "adb shell input tap %s %s && adb shell input tap %s %s" % (hueLocationMiddle, hueLocation, saturationLocation, valueLocation)

print(command)

print("Running command on device")
os.system(command)
