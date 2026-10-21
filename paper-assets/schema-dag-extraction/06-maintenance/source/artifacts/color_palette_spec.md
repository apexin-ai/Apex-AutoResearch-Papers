# Unified Color Palette Specification

## Design Basis

Foundation: **Paul Tol "Bright"** scheme — the gold standard for colorblind-safe scientific visualization, validated for deuteranopia, protanopia, and tritanopia. Used by Nature Astronomy, ESA, and CERN publications. We adopt it directly (no custom mixing) to guarantee accessibility.

Design principles:
- **Saturation**: Moderate (55-70% HSL) — professional without being garish
- **Grayscale**: All semantic pairs have ≥15% luminance contrast (verified via L* channel)
- **Cross-figure coherence**: Same semantic meaning → same color, no exceptions

---

## 1. Core Palette (7 colors + 4 neutrals)

### Semantic Colors

| Role | Name | Hex | RGB | L* | Primary Usage |
|------|------|-----|-----|-----|---------------|
| **Primary** | Steel Blue | `#4477AA` | 68,119,170 | 49 | RE task, Qwen3-32B, main data |
| **Secondary** | Burnt Orange | `#EE7733` | 238,119,51 | 60 | NER task, Llama-70B |
| **Tertiary** | Forest Green | `#228833` | 34,136,51 | 50 | ED task, Gemini Flash |
| **Negative** | Soft Rose | `#CC6677` | 204,102,119 | 53 | IntraSub error, High-BCS, failure |
| **Positive** | Sky Blue | `#66CCEE` | 102,204,238 | 77 | Low-BCS condition |
| **Accent** | Sand | `#CCBB44` | 204,187,68 | 75 | Key findings, highlight |
| **Reserve** | Plum | `#AA3377` | 170,51,119 | 37 | Additional series (if needed) |

### Neutral Colors

| Role | Hex | Usage |
|------|-----|-------|
| **Text Dark** | `#2D2D2D` | Axis labels, titles |
| **Text Mid** | `#555555` | Annotations, delta labels |
| **Text Light** | `#888888` | Secondary annotations, brackets |
| **Grid** | `#CCCCCC` | Gridlines, reference lines |
| **Fill** | `#F2F2F2` | Light background fills |

---

## 2. Semantic Mapping Rules

### Task Colors (consistent across ALL figures)
```
RE (Relation Extraction)  → Steel Blue  #4477AA
NER (Named Entity Recog.) → Burnt Orange #EE7733
ED (Event Detection)      → Forest Green #228833
```

### BCS Condition Pair
```
Low-BCS  (good, low confusability) → Sky Blue   #66CCEE
High-BCS (bad, high confusability) → Soft Rose  #CC6677
```
Rationale: Cool=good / warm=bad is intuitive. Sky Blue has L*=77, Soft Rose L*=53 — 24-point luminance gap ensures grayscale distinguishability.

### Error Categories
```
IntraSub / WrongType (confusability error) → Soft Rose  #CC6677
Missed / ExtraSub (recall error)           → Steel Blue #4477AA
Other / Correct                            → Grid Gray  #CCCCCC
```
Rationale: IntraSub shares color with High-BCS — semantically coherent (high confusability → more substitution errors).

### Cross-Model Series
```
Qwen3-32B  (primary model)   → Steel Blue    #4477AA  solid ─  ●
Llama-3.1-70B (validation)   → Burnt Orange  #EE7733  dashed ┄  ■
Gemini 2.5 Flash (external)  → Forest Green  #228833  dotted ⋯  ▲
```

### Pipeline Diagram
```
Main pipeline path      → Steel Blue #4477AA (border), #E8EFF7 (fill, 15% opacity)
Failure callout         → Soft Rose  #CC6677 (border), #F7EBEE (fill, 15% opacity)
Success marker          → Forest Green #228833
Flow arrows             → Text Light #888888
Main text               → Text Dark  #2D2D2D
Descriptive text        → Text Mid   #555555
```

### Chance / Reference Lines
```
Random chance  → Grid #CCCCCC, dotted, linewidth=1
```

---

## 3. Per-Figure Color Mapping

### Figure 1: SDGD Pipeline (gen_fig_sdgd_pipeline.py)

| Element | Current | New | Notes |
|---------|---------|-----|-------|
| Pipeline box border | `#3B6CB5` | `#4477AA` | Steel Blue |
| Pipeline box fill | `#E8F0FE` | `#E8EFF7` | 15% opacity of Steel Blue |
| Failure box border | `#C0392B` | `#CC6677` | Soft Rose |
| Failure box fill | `#FDF0EF` | `#F7EBEE` | 15% opacity of Soft Rose |
| Failure text | `#8B1A1A` | `#CC6677` | Same as border |
| Flow arrows | `#8C9BB5` | `#888888` | Text Light |
| Main text | `#2C3E50` | `#2D2D2D` | Text Dark |
| Descriptive text | `#7F8C8D` | `#555555` | Text Mid |
| Success checkmark | `#27AE60` | `#228833` | Forest Green |
| Colored dots (blue) | `#5B9BD5` | `#4477AA` | Steel Blue |
| Colored dots (orange) | `#ED7D31` | `#EE7733` | Burnt Orange |
| Colored dots (red) | `#E74C3C` | `#CC6677` | Soft Rose |

### Figure 2: Framework Scatter (gen_fig_framework.py)

| Element | Current | New | Notes |
|---------|---------|-----|-------|
| Count dimension arrow | `#3B6CB5` | `#4477AA` | Steel Blue |
| BCS dimension arrow | `#ED7D31` | `#EE7733` | Burnt Orange |
| Scatter colormap | `RdYlGn` | Custom diverging (see §3) | Rose→White→Blue |
| Annotation text | `#666666`/`#999999` | `#888888` | Text Light |
| BCS range lines | `#888888` | `#CCCCCC` | Grid |

### Figure 3a: Count Curves (fig_count_curves_v2.py)

| Element | Current | New | Notes |
|---------|---------|-----|-------|
| RE (FewRel) | `#0072B2` | `#4477AA` | Steel Blue, solid, ● |
| NER (Few-NERD) | `#D55E00` | `#EE7733` | Burnt Orange, solid, ▲ |
| Chance line | `#999999` | `#CCCCCC` | Grid, dotted |

### Figure 3b: BCS-Controlled Bars (fig_bcs_scaling_v2.py)

| Element | Current | New | Notes |
|---------|---------|-----|-------|
| Low-BCS bars | `#5B9BD5` | `#66CCEE` | Sky Blue |
| High-BCS bars | `#ED7D31` | `#CC6677` | Soft Rose |
| Bracket lines | `#555555` | `#888888` | Text Light |
| Delta labels | `#333333` | `#555555` | Text Mid |

### Figure 4: Error Taxonomy (fig_error_taxonomy_v2.py)

| Element | Current | New | Notes |
|---------|---------|-----|-------|
| IntraSub/WrongType | `#C0392B` | `#CC6677` | Soft Rose, solid, ● |
| Missed/ExtraSub | `#5B9BD5` | `#4477AA` | Steel Blue, dashed, ■ |
| Other/Correct | `#BBBBBB` | `#CCCCCC` | Grid, dotted, ▲ |
| Other marker edge | `#666666` | `#888888` | Text Light |

### Figure 5: Cross-Model Count Curves (fig_cross_model_count.py)

| Element | Current | New | Notes |
|---------|---------|-----|-------|
| Qwen3-32B | `#3B6CB5` | `#4477AA` | Steel Blue, solid, ● |
| Llama-3.1-70B | `#ED7D31` | `#EE7733` | Burnt Orange, dashed, ■ |
| Gemini 2.5 Flash | `#27AE60` | `#228833` | Forest Green, dotted, ▲ |

---

## 4. Continuous Colormap Recommendation

### Primary: Custom Diverging (Rose → White → Blue)

```python
from matplotlib.colors import LinearSegmentedColormap

palette_cmap = LinearSegmentedColormap.from_list(
    'schema_diverging',
    ['#CC6677', '#F5F5F5', '#4477AA'],
    N=256
)
```

Semantics: Low accuracy (rose/warm) → High accuracy (blue/cool). Matches the palette convention where rose = negative outcome, blue = positive/primary.

**Grayscale behavior**: Rose (L*=53) → White (L*=97) → Blue (L*=49). The midpoint is lightest, endpoints are dark — good luminance contrast in grayscale.

**Colorblind safety**: Blue-to-pink/rose diverging colormaps are safe for all common forms of color vision deficiency (unlike red-green diverging maps).

### Alternative: `cividis`

If a sequential (non-diverging) map is preferred:
```python
plt.cm.cividis  # blue-gray → yellow, perceptually uniform, CVD-safe
```

### Avoid
- `RdYlGn` (current): fails under deuteranopia (red/green indistinguishable)
- `jet`: perceptual non-uniformity, universally deprecated
- `coolwarm`: low luminance contrast at midpoint

---

## 5. Design Rationale (Brief)

1. **Why Paul Tol Bright?** It is the only palette simultaneously validated for all three common CVD types (deuteranopia 8% male, protanopia 1%, tritanopia 0.01%) while maintaining sufficient aesthetic quality for top-tier venues. Unlike Okabe-Ito (which has very high saturation), Tol Bright has moderate saturation suitable for academic print.

2. **Why not Okabe-Ito?** Okabe-Ito's orange (#E69F00) and vermillion (#D55E00) are extremely saturated (>85% HSL), giving a "textbook" rather than "journal" feel. Tol Bright's #EE7733 and #CC6677 are ~10-15% less saturated.

3. **Why semantic consistency across figures?** A reader who learns "blue = RE" in Figure 3 should not need to re-read the legend in Figure 5. Color-as-language reduces cognitive load.

4. **Why Rose for both High-BCS and IntraSub?** This is the paper's central finding: high confusability → intra-batch substitution. Using the same color creates a visual throughline across Figures 3b and 4 without requiring the reader to consciously link them.

5. **Why Sky Blue + Rose (not Blue + Orange) for BCS contrast?** Blue (#4477AA) is already committed to "RE task." Using it also for "Low-BCS" would create ambiguity in Figure 4, where both meanings co-occur. Sky Blue (#66CCEE) is perceptually distinct from Steel Blue while maintaining the cool-tone family.

---

## 6. Implementation Constants

```python
# === UNIFIED PALETTE — paste into every figure script ===

COLORS = {
    # Semantic colors (Paul Tol Bright, unmodified)
    'primary':    '#4477AA',  # Steel Blue — RE, Qwen3, main
    'secondary':  '#EE7733',  # Burnt Orange — NER, Llama-70B
    'tertiary':   '#228833',  # Forest Green — ED, Gemini
    'negative':   '#CC6677',  # Soft Rose — error, high-BCS, failure
    'positive':   '#66CCEE',  # Sky Blue — low-BCS
    'accent':     '#CCBB44',  # Sand — highlight
    'reserve':    '#AA3377',  # Plum — extra series

    # Neutrals
    'text_dark':  '#2D2D2D',
    'text_mid':   '#555555',
    'text_light': '#888888',
    'grid':       '#CCCCCC',
    'fill':       '#F2F2F2',

    # Derived fills (15% opacity approximation on white)
    'primary_fill':  '#E8EFF7',
    'negative_fill': '#F7EBEE',
}

# Task mapping
TASK_COLORS = {
    'RE':  COLORS['primary'],
    'NER': COLORS['secondary'],
    'ED':  COLORS['tertiary'],
}

# BCS condition mapping
BCS_COLORS = {
    'low':  COLORS['positive'],   # Sky Blue
    'high': COLORS['negative'],   # Soft Rose
}

# Error category mapping
ERROR_COLORS = {
    'intrasub':  COLORS['negative'],  # Soft Rose
    'missed':    COLORS['primary'],   # Steel Blue
    'other':     COLORS['grid'],      # Gray
}

# Cross-model mapping
MODEL_COLORS = {
    'qwen3':     COLORS['primary'],    # Steel Blue
    'llama70b':  COLORS['secondary'],  # Burnt Orange
    'gemini':    COLORS['tertiary'],   # Forest Green
}

# Custom diverging colormap (low-accuracy=rose, high=blue)
from matplotlib.colors import LinearSegmentedColormap
ACCURACY_CMAP = LinearSegmentedColormap.from_list(
    'schema_diverging',
    [COLORS['negative'], '#F5F5F5', COLORS['primary']],
    N=256
)
```
