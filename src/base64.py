import argparse
import string

# Base62 Encoding Function
def encode_base62(num):
    BASE62 = string.ascii_uppercase + string.ascii_lowercase + string.digits
    base62_str = ""
    
    while num > 0:
        num, remainder = divmod(num, 62)
        base62_str = BASE62[remainder] + base62_str
    
    return base62_str or BASE62[0]

if __name__ == "__main__":
    # Setup argument parser
    parser = argparse.ArgumentParser(description="Encode an event ID to Base62")
    parser.add_argument("event_id", type=int, help="The event ID to encode in Base62")
    
    # Parse arguments
    args = parser.parse_args()
    
    # Encode event_id
    short_code = encode_base62(args.event_id)
    print(short_code)
