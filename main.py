from string_utils import StringUtils
import js2py
import time
import datetime
import pytz
from main import AngelOneAPI, MultiIndexSignalGenerator

def main():
    # Configuration
    API_KEY = "LFIyC3E1"
    CLIENT_ID = "N305936"
    MPIN = "7582"
    TOTP = "NO3EEE64RFWJCEO7I3YLWYVVA4"

    # Initialize API
    angel_api = AngelOneAPI(API_KEY, CLIENT_ID, MPIN, TOTP)

    if not angel_api.login():
        print("Failed to login to Angel One API")
        return

    # Initialize multi-index signal generator
    signal_generator = MultiIndexSignalGenerator(angel_api)

    print("🚀 Multi-Index Signal Generator Started!")
    print("📊 Covering: NIFTY, Bank NIFTY, FINNIFTY, SENSEX")
    print("⏰ Checking for signals every 3 minutes...")
    print("-" * 60)

    last_signal_time = 0

    while True:
        try:
            current_time = time.time()

            if current_time - last_signal_time > 180:  # 3 minutes
                all_signals = signal_generator.generate_all_signals()

                if all_signals:
                    print("=" * 80)
                    print(f"📊 GENERATED {len(all_signals)} SIGNALS:")
                    for index, signal in all_signals.items():
                        print(f"🎯 {index}: {signal['confidence']:.1f}% confidence - {signal['signal_type']} {signal['strike']} {signal['option_type']}")
                    print("=" * 80)
                    last_signal_time = current_time
                else:
                    ist = pytz.timezone('Asia/Kolkata')
                    current_time_str = datetime.datetime.now(ist).strftime('%H:%M:%S')
                    print(f"⏳ {current_time_str} IST - Waiting for high-confidence signals...")

            time.sleep(30)

        except KeyboardInterrupt:
            print("\n👋 Multi-index signal generator stopped!")
            break
        except Exception as e:
            print(f"❌ Error: {e}")

if __name__ == "__main__":
    main())
