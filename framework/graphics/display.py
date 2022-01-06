import win32api

def fetch_max_refreshrate() -> int:
    """Fetches the maximum refresh rate monitor's refresh rate as that's usually their main
    one. I also hate windows api."""

    res = []

    for idx, _ in enumerate(win32api.EnumDisplayMonitors()):
        disp_enum = win32api.EnumDisplayDevices(DevNum= idx)
        display = win32api.EnumDisplaySettings(disp_enum.DeviceName, -1)
        res.append(display.DisplayFrequency)
    
    return max(res)
