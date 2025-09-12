import dearpygui.dearpygui as dpg
import numpy as np
import pyaudio
import time
import json




WindowSize = (480, 600)
srOptions = [8000, 22500, 44100, 48000, 96000, 192000]
freq1 = [1209, 1336, 1477, 1633]
freq2 = [697, 770, 852, 941]
ButtonLabels = ["1","2","3","A","4","5","6","B","7","8","9", "C", "*", "0", "#", "D"]
p = pyaudio.PyAudio()
standardSettings = {
	"volumeValue": 80,
	"soundDurValue": 0.4,
	"pauseDurValue": 0.01,
	"srSelection": "41000",
	"expandedNumpadValue": False
} 

def generateSine(FreqPos):
    sine1 = np.sin(2 * np.pi * np.arange(int(dpg.get_value("srMenu"))*dpg.get_value("soundDurValue"))* freq1[FreqPos[0]]/int(dpg.get_value("srMenu"))).astype(np.float32)
    sine2 = np.sin(2 * np.pi * np.arange(int(dpg.get_value("srMenu"))*dpg.get_value("soundDurValue"))* freq2[FreqPos[1]]/int(dpg.get_value("srMenu"))).astype(np.float32)
    sineAdded = sine1 + sine2
    sineAdded = sineAdded / np.max(np.abs(sineAdded)) #normalisierung
    print(freq1[FreqPos[0]], freq2[FreqPos[1]])
    return sineAdded

def playAudio(output_bytes):
	stream = p.open(format=pyaudio.paFloat32, channels=1, rate=int(dpg.get_value("srMenu")), output=True)
	start_time = time.time()
	stream.write(output_bytes)

def buttonPress(sender, app_data, user_data): # sender und app_data sind benötigt, dass user_data richtig zugeordnet wird
	output = ((dpg.get_value("VolumeSettingSlider")/100) * generateSine(user_data)).tobytes()
	playAudio(output)

def addButtons(sender, app_data, user_data):
	if user_data == "checkboxValueChanged" and dpg.get_value("toggleExpandedNumpad") == True:
		dpg.delete_item("buttonTableSmall")
	elif user_data == "checkboxValueChanged" and dpg.get_value("toggleExpandedNumpad") == False:
		dpg.delete_item("buttonTableLarge")
	else:
		pass

	if dpg.get_value("expandedNumpadValue") == True:
		with dpg.table(header_row=False, tag="buttonTableLarge", parent="tabNumpad"):
			for i in range(4):
				dpg.add_table_column(tag=f"buttonTableLargeColum{i}")
			for i in range(0, 4):
				with dpg.table_row(tag=f"buttonTableLargeRow{i}"):
					for j in range(0, 4):
						dpg.add_button(label=f"{ButtonLabels[(3*i)+(j+i)]}", width=WindowSize[0]/5, height=WindowSize[1]/5, callback=buttonPress, user_data = [j,i])

	else:
		with dpg.table(header_row=False, tag="buttonTableSmall", parent="tabNumpad"):
			for i in range(3):
				dpg.add_table_column(tag=f"buttonTableSmallColum{i}")
			for i in range(0, 4):
				with dpg.table_row(tag=f"buttonTableSmallRow{i}"):
					for j in range(0, 3):
						dpg.add_button(label=f"{ButtonLabels[j+(4*i)]}", width=WindowSize[0]/3, height=WindowSize[1]/5, callback=buttonPress, user_data = [j,i])


try:
	with open("settings.json") as file:
		settingsDICT = json.loads(file.read())
		print("settings.json read")
except (FileNotFoundError):
	print("settings file not found, creating a new one :)")
	file = open("settings.json", "x")
	with open("settings.json", "w") as file:
		file.write(json.dumps(standardSettings))
	settingsDICT = standardSettings

dpg.create_context()

with dpg.value_registry():
    dpg.add_int_value(default_value=settingsDICT["volumeValue"], tag="volumeValue")
    dpg.add_float_value(default_value=settingsDICT["soundDurValue"], tag="soundDurValue")
    dpg.add_float_value(default_value=settingsDICT["pauseDurValue"], tag="pauseDurValue")
    dpg.add_bool_value(default_value=bool(settingsDICT["expandedNumpadValue"]), tag="expandedNumpadValue")

with dpg.window(tag="mainWindow"):
    with dpg.tab_bar(tag="tabBar") as tb:
        with dpg.tab(label="Numpad", tag="tabNumpad"):
        	addButtons(None, None, None)
        with dpg.tab(label="Settings", tag="tabSettings"):
        	dpg.add_slider_int(label="Volume", tag="VolumeSettingSlider", min_value=0, max_value=100, source="volumeValue")
        	dpg.add_slider_float(label="Sound Duration", tag="soundDurSlider", min_value=0.04, max_value=1, source="soundDurValue")
        	dpg.add_slider_float(label="Pause Duration", tag="pauseDurSlider", min_value=0.001, max_value=0.01, source="pauseDurValue")
        	dpg.add_combo(label="Sample Rate", tag="srMenu", items=srOptions, default_value=settingsDICT["srSelection"])
        	dpg.add_checkbox(label="Toggle expanded Numpad", tag="toggleExpandedNumpad", source="expandedNumpadValue", callback=addButtons, user_data="checkboxValueChanged")



dpg.setup_dearpygui()
dpg.create_viewport(width=WindowSize[0], height=WindowSize[1], title="An actual Phone?!")
dpg.show_viewport()
dpg.set_primary_window("mainWindow", True)
dpg.start_dearpygui()

settingsDICT = {
	"volumeValue": dpg.get_value("volumeValue"),
	"soundDurValue": dpg.get_value("soundDurValue"),
	"pauseDurValue": dpg.get_value("pauseDurValue"),
	"srSelection": dpg.get_value("srMenu"),
	"expandedNumpadValue": dpg.get_value("expandedNumpadValue")
}

with open("settings.json", "w") as file:
	file.write(json.dumps(settingsDICT))
	print("saved settings")

dpg.destroy_context()
