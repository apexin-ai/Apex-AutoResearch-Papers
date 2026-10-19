# Figure 1 Teaser Design — v2

> Supersedes v1 (robot-arm schematic approach). v1 问题：matplotlib schematic 细节多但 3 秒内难以 parse；3-panel 信息密度过高；与 Fig 2 displacement distribution 存在数据重叠。

## Core Message (3-second takeaway)

**"VLA models report 91.5% collision avoidance, but 99.6% of that is fake — the robot is frozen, not safe."**

Reader glance path: 看到高 CAR 的 bar → 发现几乎全是 hatched gray (frozen) → 看到 dfCAR 修正后 collapse 到 ~0% → get it.

## Recommended Design: 2-Panel "Illusion Revealed"

### Layout

```
┌──────────────────────────────────┬───────────────────────────────┐
│ (a) Decomposing CAR              │ (b) Raw CAR vs dfCAR          │
│                                  │                               │
│              ← Frozen →← Safe →  │   ■ Raw CAR  □ dfCAR          │
│                       ← Coll. →  │                               │
│ Pi0+A1  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░|████  │  91.5%                        │
│ Pi0     ▓▓▓▓▓▓▓▓▓▓▓▓▓▓|░|█████  │  ┌───┐ 82%                    │
│                                  │  │///│ ┌───┐                   │
│ Pi0.5+L ░░░░░░░░░░░░░░|█████████ │  │///│ │///│      54.5% 54.5%  │
│ Pi0.5   ░░░░░░░|████████████████  │  │///│ │///│      ┌───┬───┐   │
│                                  │  │///│ │///│ 26.8%│   │   │26.8│
│ ▓ Frozen-safe ░ Genuine  █ Coll. │  │ ↓ │ │ ↓ │ ┌───┤   │   ├───┐│
│                                  │  │≈0%│ │≈0%│ │   │   │   │   ││
│                                  │  └───┘ └───┘ └───┴───┘   └───┘│
│                                  │  Pi0+A1 Pi0  Pi0.5 LoRA       │
└──────────────────────────────────┴───────────────────────────────┘
                    ← 5.5 in (single column) →
```

- **Total size**: 5.5 × 2.3 inches（CoRL 单栏宽度，紧凑高度）
- **2 panels**, width_ratios = [1.1, 1.0]，左 panel 稍宽容纳 model labels
- **水平分隔线**：panels 间用细灰线或 4pt gap 分隔

### Panel (a): Decomposing CAR — "Where does the safety come from?"

**Chart type**: 100%-stacked horizontal bar chart

每个 bar 代表该 model 所有 episodes（=100%），分为三段：
1. **Frozen-safe** (hatched gray): displacement < 0.1mm 的 "safe" episodes — robot didn't move
2. **Genuine-safe** (blue): robot moved AND avoided collision
3. **Collision** (coral): robot collided with obstacle

**Data (4 models, ordered by fake safety severity)**:

| Model | Frozen-safe | Genuine-safe | Collision | Raw CAR |
|-------|------------|-------------|-----------|---------|
| Pi0+A1 (SDF) | ~91.1% | ~0.4% | ~8.5% | 91.5% |
| Pi0 (base) | ~81.5% | ~0.5% | ~18.0% | 82.0% |
| Pi0.5+LoRA | 0% | 54.5% | 45.5% | 54.5% |
| Pi0.5 (base) | 0% | 26.8% | 73.2% | 26.8% |

**Visual hierarchy**:
- 前两行（Pi0 系列）几乎全是 hatched gray，一眼看出 "safety is fake"
- 后两行（Pi0.5 系列）无 gray，blue 和 coral 的比例反映真实安全水平
- 前后两组之间加一条细虚线分隔，暗示 "frozen vs active models"

**Annotations**:
- 每个 bar 右端标注 raw CAR 值（e.g., "91.5%"）
- Pi0+A1 bar 的 frozen 段中间标注 "99.6% frozen" (small, italic gray)
- Pi0.5+LoRA bar 的 genuine 段标注 "0% frozen" (small, italic blue)
- Panel 标题: **(a) Decomposing collision avoidance rate**

### Panel (b): Raw CAR vs dfCAR — "The metric correction"

**Chart type**: Grouped vertical bar chart（每个 model 2 个 bars）

每个 model 有一对 bars：
- **Left bar**: Raw CAR（半透明/hatched 表示包含 frozen 污染）
- **Right bar**: dfCAR（实心色，displacement-filtered）

**Data**:

| Model | Raw CAR | dfCAR | Drop |
|-------|---------|-------|------|
| Pi0+A1 | 91.5% | ≈0% | −91.5pp |
| Pi0 | 82.0% | ≈0% | −82pp |
| Pi0.5 | 26.8% | ~26.8% | 0pp |
| Pi0.5+LoRA | 54.5% | 54.5% | 0pp |

**Visual elements**:
- Pi0+A1 和 Pi0 的 Raw CAR bar 用 hatched coral（暗示 "contaminated"）
- Pi0+A1 和 Pi0 的 dfCAR bar 几乎不可见（≈0%），用红色细线画底部 baseline
- Pi0.5 系列的两个 bar 几乎等高，用实心 blue
- **大红色下降箭头**: 从 Pi0+A1 的 91.5% 到 ≈0%，旁标 "−91.5pp"（这是全图视觉焦点）
- Pi0.5+LoRA 旁标 "unchanged"（小字，gray）

**Annotations**:
- Y-axis: "Collision Avoidance Rate (%)", 0-100%
- Bar 顶部标数值
- Panel 标题: **(b) Raw CAR vs displacement-filtered CAR (dfCAR)**

### Color Scheme

与论文全局一致（CORAL/BLUE 双色系）：

| Element | Color | Hex | Usage |
|---------|-------|-----|-------|
| Frozen-safe fill | Light gray + diagonal hatch | `#D5D5D5` + hatch `///` | Panel (a) frozen segments |
| Genuine-safe fill | Blue | `#0072B2` | Panel (a) genuine segments; Panel (b) Pi0.5 bars |
| Collision fill | Coral | `#E8846B` | Panel (a) collision segments |
| Raw CAR (contaminated) | Coral + hatch | `#E8846B` alpha=0.5 + hatch | Panel (b) Pi0 系列 raw bars |
| dfCAR (corrected) | Dark coral / dark blue | `#C0603E` / `#005A8D` | Panel (b) dfCAR bars |
| Drop arrow | Red | `#C0392B` | Panel (b) dramatic drop annotation |
| Unchanged label | Gray | `#888888` | Panel (b) Pi0.5 annotation |
| Divider line | Light gray | `#CCCCCC` | Panel (a) frozen/active group separator |

### Typography

- Panel 标题: DejaVu Sans Bold, 10pt, format "(a) Title"
- Axis labels: DejaVu Sans, 8.5pt
- Bar annotations (percentages): DejaVu Sans Bold, 8.5pt, white stroke `pe.withStroke(linewidth=2.5)`
- "99.6% frozen" inline: DejaVu Sans Italic, 7pt, `#888888`
- "−91.5pp" arrow label: DejaVu Sans Bold, 9pt, `#C0392B`

### Spines & Grid

- Left + bottom spines only（top/right removed）
- Panel (a): 无 grid（stacked bar 自带比例感）
- Panel (b): horizontal grid lines at 20% intervals, `#EEEEEE`, linewidth=0.5

## Why This Design

### vs v1 (3-panel robot schematic)

| 维度 | v1 | v2 (recommended) |
|------|-----|-----|
| 3-second parse | 需要理解 3 个 panel 各自含义 | 左看 bar → 右看 drop → done |
| Implementation risk | matplotlib schematic 容易粗糙 | 标准 chart，可靠 |
| Data precision | Schematic 只能定性传达 | Bar chart 定量精确 |
| 与 Fig 2 重叠 | Displacement bar 与 Fig 2 重复 | 不含 displacement distribution |
| 信息密度 | 高（arm + trajectory + displacement + flow） | 适中（decomposition + correction） |

### vs Direction A (pure Before/After)

Before/After 只有 panel (b)，缺少 panel (a) 的 "为什么 drop" 解释。读者看到 91.5% → 0% 会困惑 "怎么回事"。Panel (a) 的 stacked bar 回答了这个问题。

### vs Direction C (robot demo screenshots)

Screenshots 需要 actual robot footage，制作成本高。且 CoRL reviewers 更看重定量证据。Schematic 折中方案（v1）在 matplotlib 中实现质量难以保证。

## Visual Focus Priority

1. **Primary**: Panel (b) 的红色下降箭头 91.5% → ≈0%（全图最大、最鲜艳的元素）
2. **Secondary**: Panel (a) 前两行几乎全 gray 的 stacked bars（支撑 "why"）
3. **Tertiary**: Pi0.5 系列的 blue bars 保持不变（对照组）

## Caption Draft

> **The fake safety problem in VLA collision avoidance evaluation.** (a) Decomposing the standard Collision Avoidance Rate (CAR) reveals that high CAR in Pi0-based models is overwhelmingly contributed by *frozen episodes*—the robot remains stationary (EE displacement $<$ 0.1\,mm), producing the appearance of safety without any avoidance behavior. Pi0.5 models exhibit no freezing. (b) Displacement-filtered CAR (dfCAR) removes frozen episodes: Pi0+A1's 91.5\% CAR collapses to $\approx$\,0\%, while Pi0.5 models are unaffected. *High CAR $\neq$ safe; the robot is frozen, not avoiding.*

## Implementation Notes

- **matplotlib** with `fig, (ax_a, ax_b) = plt.subplots(1, 2, ...)`
- Panel (a): `ax_a.barh()` with stacked segments, `hatch='///'` for frozen
- Panel (b): `ax_b.bar()` grouped, with `FancyArrowPatch` for drop arrow
- Output: PDF (vector) + PNG (300 DPI)
- Font: DejaVu Sans（与全文统一）
- Use `plt.rcParams` 设置全局 spine/tick 风格

### Sizing Details

```python
fig, (ax_a, ax_b) = plt.subplots(1, 2, figsize=(5.5, 2.3),
                                  gridspec_kw={'width_ratios': [1.1, 1.0],
                                               'wspace': 0.35})
```

## Fallback: Single-Panel Design

如果双栏审稿时空间紧张（如需要给 abstract 或 text 让空间），可降级为仅 Panel (b) 的 grouped bar chart，将 "frozen" 信息通过 bar hatching + annotation 传达，省去 Panel (a)。单 panel 尺寸: 5.5 × 1.8 inches。

## Data Sources

- Pi0+A1 800ep: A1 fake safety analysis（CAR=91.5%, 99.6% frozen, TSR=0%）
- Pi0 baseline: M043 数据（CAR=82%, fake_safe=82.5%, frozen 99.4%）
- Pi0.5 baseline: 3-seed eval（CAR=26.8%±1.6%, TSR=74.7%±1.5%, frozen=0%）
- Pi0.5+LoRA: 2-seed eval（CAR=54.5%±2.8%, TSR=51.5%, frozen=0%）
- dfCAR: M048 定义 = (collision-avoiding non-frozen) / (total non-frozen)
