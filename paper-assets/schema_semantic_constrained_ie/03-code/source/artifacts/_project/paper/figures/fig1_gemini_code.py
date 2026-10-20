
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.patheffects as pe

# --- Configuration ---
FIG_SIZE = (14, 6)
DPI = 300

# Colors
BLUE = '#4A90D9'
ORANGE = '#E8833A'
GREEN = '#6BBF59'
YELLOW = '#FFD700'
LIGHT_GRAY = '#F0F0F0'  # For panel backgrounds
LIGHT_BLUE_BG = '#D9E8F5' # Light tint for grammar layer
LIGHT_ORANGE_BG = '#F5E0D9' # Light tint for semantic layer
TEXT_COLOR_DARK = 'dimgray'

# Font settings
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['DejaVu Sans', 'Arial'] # Prioritize DejaVu Sans, fallback to Arial

# Box styling
BOX_PAD = 0.3
BOX_RADIUS_PX = 10 # pixels for FancyBboxPatch rounding size
BOX_EDGECOLOR = 'black'
BOX_LINEWIDTH = 1.0

# Arrow styling
ARROW_LINEWIDTH = 1.5
ARROW_MUTATION_SCALE = 10 # Size of arrow head

# --- Helper Functions ---
def create_box(ax, xy, width, height, text, box_color='white