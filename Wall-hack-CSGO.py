import pymem
# These 3 offsets need to be updated after each CS:GO update
dwGlowObjectManager = 0x535A9D8    # Perhaps this is no longer up-to-date data
dwEntityList = 0x4DFFF14           # Perhaps this is no longer up-to-date data
m_iGlowIndex = 0x10488             # Perhaps this is no longer up-to-date data

pm = pymem.Pymem("csgo.exe")
client = pymem.process.module_from_name(pm.process_handle, "client.dll").lpBaseOfDll

def glowmodule():
    while True:
        glow = pm.read_int(client + dwGlowObjectManager)
        for i in range(0, 32):
            entity = pm.read_int(client + dwEntityList + i * 0x10)
            if entity:
                entity_glow =pm.read_int(entity + m_iGlowIndex)

                pm.write_float(glow + entity_glow * 0x38 + 0x8, float(0))
                pm.write_float(glow + entity_glow * 0x38 + 0xC, float(1))
                pm.write_float(glow + entity_glow * 0x38 + 0x10, float(0))
                pm.write_float(glow + entity_glow * 0x38 + 0x14, float(1))
                pm.write_int(glow + entity_glow * 0x38 + 0x28, 1)

glowmodule()