import requests
import json
import time
import datetime
from typing import Dict, List, Optional
import pandas as pd
import numpy as np
import pyotp

# [AngelOneAPI and TechnicalAnalysis classes omitted for brevity]

class NIFTYSignalGenerator:
    # ... (class code here)

def main():
    # Configuration - Add your Angel One credentials
    API_KEY = "LFIyC3E1"  # Add your API key
    CLIENT_ID = "N305936"  # Add your client ID
    MPIN = "7582"  # Add your 4-digit MPIN (replace with your actual MPIN)
    TOTP = "NO3EEE64RFWJCEO7I3YLWYVVA4"  # Add your TOTP

    if API_KEY == "YOUR_API_KEY" or MPIN == "YOUR_MPIN":
        print("⚠️  Please add your Angel One credentials in the main() function")
        print("You need to set:")
        print("- API_KEY")
        print("- CLIENT_ID") 
        print("- MPIN (4-digit Mobile PIN)")
        print("- TOTP")
        return

    # Initialize API
    angel_api = AngelOneAPI(API_KEY, CLIENT_ID, MPIN, TOTP)

    # Login
    if not angel_api.login():
        print("Failed to login to Angel One API")
        return

    # Initialize signal generator
    signal_generator = NIFTYSignalGenerator(angel_api)

    print("🚀 NIFTY Live Signal Generator Started!")
    print("⏰ Checking for signals every 30 seconds...")
    print("💡 Signals will be generated based on technical analysis")
    print("-" * 50)

    last_signal_time = 0

    while True:
        try:
            current_time = time.time()

            # Generate signal every 5 minutes to avoid spam
            if current_time - last_signal_time > 300:  # 5 minutes
                signal = signal_generator.generate_signal()

                if signal:
                    print(signal)
                    print("-" * 50)
                    last_signal_time = current_time
                else:
                    print(f"⏳ {datetime.datetime.now().strftime('%H:%M:%S')} - No clear signal detected")

            time.sleep(30)  # Check every 30 seconds

        except KeyboardInterrupt:
            print("\n👋 Signal generator stopped!")
            break
        except Exception as e:
            print(f"❌ Error: {e}")
            time.sleep(60)  # Wait 1 minute before retry

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))  # Use port from environment variable or fallback to 5000
    main()
