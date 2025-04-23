import streamlit as st
import re # Import the regular expression module

# Define the AES S-Box as a 2D list (hex strings)
# Based on the table provided in the image.
s_box = [
    ["63", "7C", "77", "7B", "F2", "6B", "6F", "C5", "30", "01", "67", "2B", "FE", "D7", "AB", "76"],
    ["CA", "82", "C9", "7D", "FA", "59", "47", "F0", "AD", "D4", "A2", "AF", "9C", "A4", "72", "C0"],
    ["B7", "FD", "93", "26", "36", "3F", "F7", "CC", "34", "A5", "E5", "F1", "71", "D8", "31", "15"],
    ["04", "C7", "23", "C3", "18", "96", "05", "9A", "07", "12", "80", "E2", "EB", "27", "B2", "75"],
    ["09", "83", "2C", "1A", "1B", "6E", "5A", "A0", "52", "3B", "D6", "B3", "29", "E3", "2F", "84"],
    ["53", "D1", "00", "ED", "20", "FC", "B1", "5B", "6A", "CB", "BE", "39", "4A", "4C", "58", "CF"],
    ["D0", "EF", "AA", "FB", "43", "4D", "33", "85", "45", "F9", "02", "7F", "50", "3C", "9F", "A8"],
    ["51", "A3", "40", "8F", "92", "9D", "38", "F5", "BC", "B6", "DA", "21", "10", "FF", "F3", "D2"],
    ["CD", "0C", "13", "EC", "5F", "97", "44", "17", "C4", "A7", "7E", "3D", "64", "5D", "19", "73"],
    ["60", "81", "4F", "DC", "22", "2A", "90", "88", "46", "EE", "B8", "14", "DE", "5E", "0B", "DB"],
    ["E0", "32", "3A", "0A", "49", "06", "24", "5C", "C2", "D3", "AC", "62", "91", "95", "E4", "79"],
    ["E7", "C8", "37", "6D", "8D", "D5", "4E", "A9", "6C", "56", "F4", "EA", "65", "7A", "AE", "08"],
    ["BA", "78", "25", "2E", "1C", "A6", "B4", "C6", "E8", "DD", "74", "1F", "4B", "BD", "8B", "8A"],
    ["8B", "8A", "70", "3E", "B5", "66", "48", "03", "F6", "0E", "61", "35", "57", "B9", "86", "C1"],
    ["1D", "9E", "E1", "F8", "98", "11", "69", "D9", "8E", "94", "9B", "1E", "87", "E9", "CE", "55"],
    ["28", "DF", "8C", "A1", "89", "0D", "BF", "E6", "42", "68", "41", "99", "2D", "0F", "B0", "54"]
]

def get_sbox_value(hex_input):
    """
    Looks up the S-Box value for a given 2-digit hex input.

    Args:
        hex_input (str): A two-digit hexadecimal string (e.g., "1A").

    Returns:
        str: The corresponding S-Box value (hex string), or None if input is invalid.
    """
    # Validate input: exactly 2 hex characters (case-insensitive)
    if not re.fullmatch(r"^[0-9a-fA-F]{2}$", hex_input):
        return None

    # Convert hex digits to integer indices
    try:
        row_index = int(hex_input[0], 16) # First digit for row
        col_index = int(hex_input[1], 16) # Second digit for column
    except ValueError:
        # Should not happen due to regex, but good practice
        return None

    # Perform the lookup
    return s_box[row_index][col_index]

# --- Streamlit App UI ---

st.set_page_config(layout="centered") # Center the content

st.title("AES S-Box Lookup Tool")
st.write("Enter a two-digit hexadecimal value (e.g., `00`, `1A`, `FF`) to find its corresponding AES S-Box substitution.")

# Input field for the hex value
hex_input = st.text_input("Enter Hex Value (2 digits):", max_chars=2, placeholder="e.g., 1A")

# Process the input when it's entered
if hex_input:
    # Convert to uppercase for consistency
    hex_input_upper = hex_input.upper()

    result = get_sbox_value(hex_input_upper)

    if result:
        st.success(f"Input: `{hex_input_upper}`  ->  S-Box Output: `{result}`")
        st.write(f"(Row: `{hex_input_upper[0]}`, Column: `{hex_input_upper[1]}`)")
    else:
        # Display error if input is not 2 valid hex digits
        st.error("Invalid input. Please enter exactly two hexadecimal characters (0-9, A-F).")
else:
    st.info("Waiting for input...")

st.markdown("---")
st.caption("The S-Box lookup table used is the standard one for AES.")

