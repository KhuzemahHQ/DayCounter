import re
import sys
from datetime import datetime

def parse_date(date_str):
    """
    Parses a date string with ordinal suffixes, e.g., '25th December 2022'.
    """
    # Remove ordinal suffixes (st, nd, rd, th) from the day
    date_str = re.sub(r'(\d+)(st|nd|rd|th)', r'\1', date_str)
    return datetime.strptime(date_str, "%d %B %Y")

def calculate_time_spent(text):
    """
    Parses the text and calculates the time spent in each location.
    """
    lines = text.strip().split('\n')
    
    events = []
    
    for line in lines:
        line = line.strip()
        # Skip empty lines or lines with specific addresses
        if not line or line.startswith('<'):
            continue
            
        # E.g. "First Landed in Canada: 25th December 2022"
        parts = line.split(':')
        if len(parts) == 2:
            location_part = parts[0].strip()
            date_part = parts[1].strip()
            
            # Extract the location by removing common prefixes
            location = location_part
            for prefix in ["First Landed in ", "Landed in ", "Returned to ", "Went to ", "Visited ", "Travelled to ", "Traveled to "]:
                if location.lower().startswith(prefix.lower()):
                    location = location[len(prefix):].strip()
                    break
                    
            date_obj = parse_date(date_part)
            
            events.append({'location': location, 'date': date_obj})
            
    # Calculate durations
    time_spent = {}
    
    for i in range(len(events)):
        location = events[i]['location']
        start_date = events[i]['date']
        
        # If there's a subsequent event, the end date for the current location is the start date of the next.
        if i + 1 < len(events):
            end_date = events[i+1]['date']
        else:
            # For the last event, we use the current date
            end_date = datetime.now()
            print(f"Note: Using current date ({end_date.strftime('%d %B %Y')}) as the end date for the last location ({location}).")
            
        duration = end_date - start_date
        
        if location not in time_spent:
            time_spent[location] = duration
        else:
            time_spent[location] += duration
            
    return time_spent

def main():
    if len(sys.argv) < 2:
        print("Usage: python day_counter.py <filename>")
        print("Defaulting to 'travel_history_sample.txt'...\n")
        filename = "travel_history_sample.txt"
    else:
        filename = sys.argv[1]
        
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return
        
    time_spent = calculate_time_spent(content)
    
    print("--- Time Spent in Each Location ---")
    for location, duration in time_spent.items():
        print(f"{location}: {duration.days} days")

if __name__ == "__main__":
    main()
