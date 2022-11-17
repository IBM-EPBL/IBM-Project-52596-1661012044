from __future__ import print_function

try:
    
    from PIL import Image, ImageDraw, ImageFont
    from optparse import OptionParser
    import requests
    from bs4 import BeautifulSoup
    import sys
    import time
    import numpy as np
    import warnings
        
    warnings.filterwarnings(action="ignore",message="CHECK PYTHON VERSION")
    warnings.filterwarnings(action="ignore",message="ALREADY IMPORTED",category=UserWarning)
    warnings.filterwarnings(action="ignore",category=DeprecationWarning)
    
except KeyboardInterrupt:
    
    Message_Error = "ACCESS NOT POSSIBLE"
    sys.exit(f"{Message_Error} - MISSING MODULES! PLEASE CHECK YOUR LIBRARIES AND TRY AGAIN!")
