# Figure 1 Teaser Design

## Narrative Intent

A frozen robot scores high on CAR not because it is safe, but because it never moves—CAR_f exposes the illusion by filtering action-collapsed episodes.

## Layout

```
┌─────────────────────────────────────────────────────────────────┐
│  (a) Fake Safety          (b) CAR_f Filter       (c) Genuine   │
│                                                      Safety    │
│ ┌──────────────┐   ┌─────────────────────┐   ┌──────────────┐ │
│ │              │   │                     │   │   ╭─trajectory │
│ │  ┌─arm─┐    │   │  ┌───────────────┐  │   │  ╭╯  ╲        │
│ │  │ (frozen) │   │  │ 91.5%  ──────►│  │   │ arm    ╲      │
│ │  │  ·       │   │  │  episodes     │  │   │  ╲   obstacle  │
│ │  │  ·       │   │  │       ┌───┐   │  │   │   ╰──►goal     │
│ │  └──┘  obs  │   │  │  τ_d  │ ≈0%│  │  │   │              │
│ │              │   │  └───────┴───┘   │  │   │              │
│ ├──────────────┤   │                     │   ├──────────────┤ │
│ │▓░░░░░░░░░░░░│   │  Pi0.5: 26.8%→28.5% │   │▓▓▓▓▓▓▓▓▓▓▓▓▓│ │
│ │ <0.1mm      │   │  (unchanged)         │   │ >288mm       │ │
│ └──────────────┘   └─────────────────────┘   └──────────────┘ │
│                                                                 │
│  CAR=91.5%  TSR=0%    91.5% ──τ_d──► ≈0%    CAR=26.8% TSR=74.7%│
└─────────────────────────────────────────────────────────────────┘
```

- 总尺寸: 5.5 × 2.8 inches（单栏宽度，略高于当前版本以容纳 schematic）
- 三列 width_ratios=[1, 1.2, 1]，中间 panel 稍宽以容纳 flow 图
- 每列分上下两区：上区 schematic/flow（~70% 高度），下区 displacement 条（~30% 高度）

## Panel A: Fake Safety

### Elements
- **Robot arm schematic**（侧视简化）：2-link arm 以灰色/淡色绘制，关节处用圆点标记。手臂完全静止——用虚线轮廓 + "frozen" 雪花/锁标记暗示不动。无运动轨迹。
- **Obstacle**：红色/橙色立方体或圆柱体，位于 arm 工作空间内但未接触（因为 arm 从未伸出）。
- **Displacement bar**（底部）：水平条形图，填充量极小（< 0.1mm），用 CORAL 色。条形旁标注 "< 0.1 mm"。背景为浅灰色 action-collapse zone。
- **Metric badge**：panel 顶部或 arm 旁，标注 "CAR = 91.5%" 和 "TSR = 0%"。

### Colors
- Arm body: `#D0D0D0`（浅灰，暗示无生命/冻结）
- Arm outline: `CORAL (#E8846B)` 虚线，关联 Pi0+A1 配色
- Obstacle: `#E8846B` 半透明填充 + `#C0603E` 边框
- Displacement bar: `CORAL (#E8846B)`
- Collapse zone bg: `#F0F0F0`
- TSR=0% 文字: `RED_TEXT (#C0392B)`
- Panel 标题/badge: `CORAL_DARK (#C0603E)`

### Annotations
- Arm 上方: 虚线框 + 文字 **"frozen"**（或锁图标 🔒，如果 DejaVu Sans 支持）
- 底部 displacement bar 旁: "< 0.1 mm" (小字，`CORAL_DARK`)
- 右下角 badge: "CAR = 91.5%" (大号加粗)，下方 "TSR = 0%" (`RED_TEXT`)
- Panel 标题: **(a) Fake Safety**

### Visual Cues
- Arm 用 dashed line + 低 alpha (0.4) 传递"这不是真正的运动"
- 在 arm 周围画一个小的 "displacement cloud"：一个极小的点簇（< 0.1mm 范围），强调微小抖动
- Obstacle 与 arm 之间留有间距，暗示"未碰撞是因为未到达，不是因为躲避"

## Panel B: CAR_f Filtering

### Elements
- **Flow diagram**（非 schematic，纯概念图）：
  1. 顶部：一个大的标注框 "CAR = 91.5%"（CORAL 色），代表 Pi0+A1 的原始得分
  2. 中间：一条水平虚线标注 τ_d = 0.1 mm（displacement threshold），线上标注 "τ_d"
  3. 过滤过程：从 91.5% 框向下画一个漏斗/筛子符号，99.6% 的 episodes 被筛掉（以淡灰色 X 或删除线表示），只剩 ≈0% 通过
  4. 底部：结果框 "CAR_f ≈ 0%"（`RED_TEXT`），极小
- **Pi0.5 对比行**（下半部分）：
  1. "CAR = 26.8%" → 经过同一 τ_d → "CAR_f = 28.5%"（箭头 + "unchanged" 标注）
  2. 用蓝色，与上方 coral 形成对比

### Colors
- Pi0+A1 flow: `CORAL (#E8846B)` → `RED_TEXT (#C0392B)`
- Pi0.5 flow: `BLUE (#0072B2)` → `BLUE (#0072B2)`
- τ_d 线: `#AAAAAA` 虚线
- 筛掉的 episodes: `#CCCCCC` + 删除线
- 漏斗/filter 符号: `#666666`
- 背景: 白色

### Annotations
- τ_d 线旁: "$\tau_d$ = 0.1 mm"（`#666666`，小字）
- Pi0+A1 行: "99.6% filtered" 标注在筛掉的部分旁（`GRAY_TEXT`）
- Pi0.5 行: "all episodes pass" 或 "0% filtered"（`BLUE`，小字）
- 大号红色文字: **"91.5% → ≈ 0%"** 作为 panel 的视觉焦点
- Panel 标题: **(b) CAR_f Filtering**

### Visual Cues
- 用从上到下的视觉 flow（不是左右），与 panel A/C 的静态 schematic 形成节奏变化
- 漏斗收窄效果：Pi0+A1 行的漏斗出口极窄（≈0%），Pi0.5 行的漏斗出口几乎等宽（unchanged）
- 可选：用 stacked bar 替代漏斗——上方是满条（91.5%），下方几乎为零，中间一个大红色向下箭头

### 备选方案：简化版
如果漏斗图过于复杂，可改为：
- 两行 before/after bar chart（类似现有 panel a + panel c 的压缩版）
- 中间一条 τ_d 水平线作为分界
- 用大箭头连接 before → after

## Panel C: Genuine Safety

### Elements
- **Robot arm schematic**（侧视简化）：同 Panel A 的 2-link arm，但以实线、饱和色绘制，关节处有运动弧线标记。
- **Motion trajectory**：从 arm 末端出发的弧形轨迹（实线，BLUE），绕过 obstacle，到达 goal 位置。用 3-4 个等距的小三角形箭头标示运动方向。
- **Obstacle**：与 Panel A 相同形状和位置的障碍物，但 arm 的轨迹明确绕过了它。
- **Displacement bar**（底部）：水平条形图，填充量显著（> 288mm），用 BLUE 色。条形旁标注 "> 288 mm"。
- **Metric badge**：panel 顶部或 arm 旁，标注 "CAR = 26.8%" 和 "TSR = 74.7%"。

### Colors
- Arm body: `BLUE (#0072B2)` 实线，饱和
- Trajectory: `BLUE (#0072B2)` 实线，alpha=0.6，宽度 1.5pt
- Trajectory 箭头: `BLUE_DARK (#005A8D)`
- Obstacle: 与 Panel A 相同（`#E8846B` 半透明 + `#C0603E` 边框），保持一致性
- Displacement bar: `BLUE (#0072B2)`
- Goal 标记: `#009E73`（teal-green，成功色）
- TSR badge: `BLUE (#0072B2)`

### Annotations
- Trajectory 旁: "> 288 mm" 标注，指向轨迹弧长
- 底部 displacement bar 旁: "> 288 mm"（`BLUE`）
- Badge: "CAR = 26.8%" + "TSR = 74.7%"（BLUE，加粗）
- Panel 标题: **(c) Genuine Safety**

### Visual Cues
- Arm 用实线 + 高饱和度，与 Panel A 的虚线/淡色形成鲜明对比
- 轨迹弧线清晰可见，传达"机器人在主动运动"
- Obstacle 和 arm 之间有明确的安全裕度（clearance），但轨迹确实从附近经过（不是远离）
- Goal 位置用绿色星号或圆点标记

## A vs C 对称设计

| 维度 | Panel A (Fake) | Panel C (Genuine) |
|------|---------------|------------------|
| Arm 线型 | 虚线，低 alpha | 实线，高饱和度 |
| Arm 颜色 | 灰色 (#D0D0D0) | 蓝色 (BLUE) |
| 运动轨迹 | 无（静止） | 弧形实线 + 箭头 |
| Obstacle 交互 | 无接触（因为没动） | 主动绕过 |
| Displacement bar | 几乎为空 | 满或近满 |
| 色调 | Coral/Red（警告） | Blue/Green（正面） |
| 情绪 | "这是假的" | "这是真的" |

## Technical Notes

### 实现方式
- **推荐：matplotlib schematic**（与现有 figure pipeline 一致）
  - Robot arm: `matplotlib.patches.FancyArrowPatch` + `Circle` 关节
  - Trajectory: `matplotlib.path.Path` + `PathPatch` 贝塞尔曲线
  - Obstacle: `Rectangle` 或 `FancyBboxPatch`
  - Displacement bar: `barh` 在子 axes 中
  - Flow diagram (Panel B): `FancyArrowPatch` + `FancyBboxPatch` + `Text`
- **备选：tikz**（更精确的 schematic 控制，但脱离现有 pipeline）
- **不推荐 PaperBanana**：此图需要精确的数据标注和对称布局，PaperBanana 更适合自由形式概念图

### 尺寸约束
- 总宽度: 5.5 inches（CoRL 单栏 `\linewidth`）
- 总高度: 2.5–2.8 inches（比当前版本略高以容纳 schematic）
- 3 panels width_ratios: [1, 1.2, 1]
- DPI: 300, 输出 PDF + PNG

### 与现有 figures 的一致性
- **字体**: DejaVu Sans（与 fig1_teaser.py, plot_fig2.py 等一致）
- **配色**: CORAL/BLUE 双色系（与全文一致，Pi0+A1=coral, Pi0.5=blue）
- **spines**: 仅保留 left + bottom（`axes.spines.top/right = False`）
- **stroke 效果**: 文字白色描边 `pe.withStroke(linewidth=2.5)`（与全文一致）
- **Panel 标题**: 加粗，10.5pt，格式 "(a) Title"
- **Metric 标注**: 8.5pt 加粗，与 fig1_teaser.py 现有风格一致

### 与当前版本的差异
当前 fig1_teaser.py 是纯数据图（bar + lollipop）。新设计将 Panel A 和 C 替换为 **robot arm schematic**，Panel B 从 displacement lollipop 替换为 **filtering flow diagram**。保留底部 displacement bar 作为定量锚点，但主体视觉从"图表"转变为"概念示意图+数据"。

### 降级方案
如果 robot arm schematic 在 matplotlib 中实现效果不佳（线条不够清晰/美观），可降级为：
- Panel A/C: 保留当前 bar chart，但在 bar 上方叠加简化的 arm icon（小尺寸，装饰性）
- Panel B: 保留当前 lollipop，但增加 flow 箭头连接到 Panel C

## Caption Draft

> **The fake safety problem in VLA collision avoidance.** (a) Pi0+A1 achieves CAR = 91.5\% by remaining frozen—displacement stays below 0.1\,mm in 99.6\% of ``safe'' episodes (TSR = 0\%). (b) CAR$_f$ applies a displacement threshold $\tau_d$: Pi0+A1's score collapses from 91.5\% to $\approx$\,0\%, while Pi0.5 is unaffected. (c) Pi0.5 exhibits genuine avoidance—actively navigating around obstacles with displacement $>$\,288\,mm (CAR = 26.8\%, TSR = 74.7\%). \emph{The robot is frozen, not safe.}
