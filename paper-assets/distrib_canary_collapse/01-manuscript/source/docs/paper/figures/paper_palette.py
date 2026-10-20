"""Unified color palette for all paper figures.
Softened Okabe-Ito-derived colors, colorblind-friendly."""

# Method colors (consistent across all figures)
PERMG = '#4A90C4'       # soft blue (was #2166AC)
DIFFXCORR = '#E8A04C'   # soft orange (was #E08214)
NAIVEXCORR = '#CC5A5A'  # soft red (was #B2182B)
TODAYAM = '#4DAF7C'     # soft green (was #1B7837)
THRESHOLD = '#8B6BB0'   # soft purple (was #6A3D9A)

# Semantic colors
PRIMARY = PERMG
SECONDARY = NAIVEXCORR
ACCENT = DIFFXCORR

# Neutral
GRAY = '#999999'
LIGHT_BLUE = '#B8D4E8'  # (was #A6CEE3)
DARK_TEXT = '#333333'

# Method ordering for legends
METHOD_COLORS = {
    'Naive XCorr': NAIVEXCORR,
    'Diff. XCorr': DIFFXCORR,
    'Threshold (3σ)': THRESHOLD,
    'ThreshOnset': THRESHOLD,
    'Perm. Granger': PERMG,
    'PermG': PERMG,
    'Toda–Yamamoto': TODAYAM,
    'Toda-Yam.': TODAYAM,
    'Consensus': GRAY,
}

# Alpha-level colors for trajectory plots
ALPHA_COLORS = {
    0.00: LIGHT_BLUE,
    0.25: PERMG,
    0.50: DIFFXCORR,
    0.75: NAIVEXCORR,
}

# Intervention colors
BASELINE = GRAY
PREDICTIVE = PERMG
REACTIVE = NAIVEXCORR
INTERVENTION_THRESHOLD = DIFFXCORR

# Regime bands (dose-response)
REGIME_BANDS = {
    'blind': '#F4F6F9',
    'onset': '#EBF0F7',
    'sync_dip': '#FDF5EE',
    'detection': '#F0F5EF',
}
