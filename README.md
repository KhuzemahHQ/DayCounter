# DayCounter
Script that takes travel history data as input and outputs the total days spent in each location.

## Usage

To run the script, use Python from the command line and pass the path to your text file as an argument:

```bash
python day_counter.py <path_to_txt_file>
```

For example:
```bash
python day_counter.py travel_history_sample.txt
```

If no file is provided, it defaults to using `travel_history_sample.txt`.

## Input File Format

The script parses a text file line-by-line. To ensure your file is processed correctly, follow these formatting rules:

1. **Event Format**: Each travel event should be on a new line, formatted as:
   `[Prefix] Location Name: [Date]`
   
   Example: `Went to San Francisco: 5th February 2023`

2. **Accepted Prefixes**: The script recognizes the following prefixes before the location name:
   - `First Landed in `
   - `Landed in `
   - `Returned to `
   - `Went to `
   - `Visited `
   - `Travelled to `
   - `Traveled to `

3. **Date Format**: The date must follow a Day-Month-Year format (e.g., `25th December 2022`). Ordinal suffixes (`st`, `nd`, `rd`, `th`) are allowed and parsed correctly.

4. **Comments / Addresses**: You can include additional lines for context, such as a hotel name or address. If a line starts with a `<` character, the script will ignore it. Blank lines are also ignored.

### Example File

```text
First Landed in New York: 10th January 2023
<Times Square Hotel>

Went to San Francisco: 5th February 2023
<Silicon Valley Airbnb>

Returned to London: 20th March 2023
```
