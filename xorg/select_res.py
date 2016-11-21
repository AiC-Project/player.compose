"""
Choose an adequate xorg resolution to hold a window
"""

class Resolution:
    __slots__ = ["width", "height"]
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return '%sx%s' % (self.width, self.height)

RESOLUTIONS = [
    Resolution(800, 480),
    Resolution(800, 562),
    Resolution(800, 600),
    Resolution(1024, 600),
    Resolution(1024, 768),
    Resolution(1280, 1024),
    Resolution(1280, 682),
    Resolution(1280, 720),
    Resolution(1280, 762),
    Resolution(1280, 768),
    Resolution(1280, 800),
    Resolution(1280, 800),
    Resolution(1360, 768),
    Resolution(1440, 900),
    Resolution(1600, 1200),
    Resolution(1600, 900),
    Resolution(1680, 1050),
    Resolution(1920, 1080),
    Resolution(1920, 1200),
    Resolution(1920, 1440),
    Resolution(2048, 1536),
    Resolution(2048, 2048),
    Resolution(2560, 1440),
    Resolution(2560, 1600),
    Resolution(3288, 1080),
    Resolution(3600, 1200),
    Resolution(3840, 1080),
    Resolution(3840, 2048),
    Resolution(3840, 2560),
    Resolution(3840, 2880),
    Resolution(4800, 1200),
    Resolution(5120, 3200),
    Resolution(5280, 1080),
    Resolution(5280, 1200),
    Resolution(5496, 1200),
    Resolution(8192, 4096),
    Resolution(16384, 8192),
    Resolution(32768, 16384),
    Resolution(32768, 32768),
]

def main():
    import os
    max_dim = int(os.getenv("AIC_PLAYER_MAX_DIMENSION", "800"))
    for resol in RESOLUTIONS:
        if max_dim <= resol.height and max_dim <= resol.width:
            print(resol)
            break
    else: # default
        print(RESOLUTIONS[-1])

if __name__ == "__main__":
    main()

