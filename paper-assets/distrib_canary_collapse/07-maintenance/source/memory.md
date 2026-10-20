# Project Memory — distrib_canary_collapse

## Phase Transition Map (2026-05-23 综合)

### T=11 PermG Dose-Response (Pythia-410M, Wiki, fp32)
| α | s42 | s43 | s44 | 备注 |
|---|-----|-----|-----|------|
| 0.00 | 0/8 | 0/8 | 0/8 | FPR baseline (see FPR section) |
| 0.25 | 0/8 | — | — | blind zone |
| 0.45 | 0/8 | 0/8 | — | blind zone confirmed |
| 0.46 | 0/8 | running | — | blind zone |
| 0.48 | 0/8 | 0/8 | — | **2-seed: α_c > 0.48** |
| 0.50 | 6/8 | **6/8** | **6/8** | **3/3 seeds 一致！零 seed variance** |
| 0.52 | 3/8 | running | — | transition onset |
| 0.60 | 0/8 | — | — | sync-dip |
| 0.65 | 0/8 | — | — | sync-dip continues |
| 0.70 | 5/8 | — | — | dip recovery |
| 0.75 | 6/8 | — | — | detection regime |
| 1.00 | 6/8 | — | — | full replacement |

**α=0.50 Seed Consistency (Reviewer #114 修正)**：
s42=6/8, s43=**6/8**, s44=6/8。3/3 seeds 完全一致，**无 seed variance**。
- 之前报告的 s43=0/8 来自 `phase_diagram/t10_a050_s43_fp32` (start_gen=6 resume artifact)，已 invalidated
- Canonical 结果来自 `alpha_sweep/a050_s43_fp32` (full run gen_0-10)：PermG=6/8 fwd, 0/8 rev, K≥3=6/8
- ECE 是 s44 最强 canary（4/4 PermG FDR-sig），方向性完美（3 seed 均 0/8 reverse）

### FPR Analysis (α=0.0 null seeds, fp32) — 最终结果 D171
| seed | PermG_fwd | PermG_rev | 备注 |
|------|-----------|-----------|------|
| s42 | 0/8 | 0/8 | — |
| s43 | 0/8 | 0/8 | — |
| s44 | 0/8 | 0/8 | — |
| s45 | **2/8** | 0/8 | **D167: breaks zero-FPR** |
| s46 | 0/8 | 0/8 | — |
| s47 | 0/8 | 0/8 | — |
| s48 | 0/8 | 0/8 | — |

**最终 FPR**: 2/56 = 3.57%, Clopper-Pearson 95% CI [0.44%, 12.3%]（D171）。

### GPT-2m Cross-Architecture FPR (2026-05-24, D220)
| seed | PermG_fwd | PermG_rev | K≥3 consensus | 备注 |
|------|-----------|-----------|---------------|------|
| s42 | **6/6** ⚠️ | 0/6 | **0/6** ✓ | architecture-specific FPR inflation |
| s43 | 0/6 | 0/6 | 0/6 ✓ | clean |

**Director 决策 D220**:
- 不混入主文 410M FPR 数字（2 seeds 不够 robust）
- Appendix 新增 "Cross-Architecture FPR Sensitivity" 小节
- 主文 discussion/limitations 加一句：PermG 在 GPT-2m 上 FPR 50% vs 410M 11.1%，K≥3 consensus 仍 0%
- s42 6/6 FP 可能与 GPT-2m null 下 distinct_3 大幅衰减有关（0.84→0.53 趋势驱动伪信号）
- 强化两个 message: (a) method sensitivity 真实 (b) consensus 有附加价值

**Reviewer 补充写作指南（D220 附）**:
1. K≥3 措辞谨慎：s42 最高 2/5 票（naive+perm），离 K≥3 只差 1 票。用 "margin of safety, though narrow (max 2/5 votes in worst case)" 而非 overclaim
2. 加 null drift magnitude 对比表：GPT-2m entropy -20.5% vs 410M -5~6%, distinct_3 -35~37% vs -5%, gen0→1 Δentropy -0.60 vs -0.24。归因 architecture-specific null drift
3. 标注 "preliminary cross-architecture evidence requiring additional replication"
4. Defense: 若被问 "Pythia 是特例"，引 Table 7 跨架构 signal 实验——有 signal 时跨架构一致，FPR 差异来源于 null drift 幅度

### T=20 Predict-then-Verify (commit bad72cc)
- **α=0.25**: predicted 0/8, observed 3/8 → **blind zone = power issue, NOT fundamental** (D161)
- **α=0.45**: predicted 0/8, observed 5/8 → **blind zone = power issue, NOT fundamental**
- **α=0.50**: predicted 7/8, observed 6/8 → within CI
- **α=0.60**: predicted 3/8 CI[2,3], observed 0/8 → **sync-dip structural, outside CI**
- **α=0.75**: predicted 7/8, observed 6/8 → within CI [6,8]
- **α=1.00**: predicted 7/8, observed 6/8 → within CI [6,8]

### Sync-Dip Boundary Map
- α=0.52: PermG=3/8 (检测开始)
- α=0.55: 未测
- α=0.60: PermG=0/8 (dip, T=20 也是 0/8 — structural)
- α=0.65: PermG=0/8 (dip continues)
- α=0.70: PermG=5/8 (recovery)

Sync-dip 区间: [0.55, 0.65]，在 0.70 锐利恢复。T=20 也无法突破 → 不是功效问题。

### Sync-Dip Cross-Seed Validation (2026-05-22 更新)
| T | s42 | s43 | 双种子状态 |
|---|-----|-----|-----------|
| T=10 | 0/8 | 0/8 | ✅ confirmed (D148) |
| T=15 | 0/8 | 0/8 | ✅ confirmed (2026-05-22) |
| T=20 | 0/8 | **3/8** | ⚠️ seed-dependent dissolution (s43 部分恢复) |
| T=25 | 0/8→**5/8★** | — | Scenario A: sync-dip dissolves at T=25 (D188) |

s43 T=15 PermG=0/8 但 permg_robust=2/8 — 存在微弱信号但低于 d105 阈值。
T=20 s43=3/8 vs s42=0/8: sync-dip 开始出现 seed-dependent 裂缝。
T=25 v3(25 gens)=5/8 vs v2(13 gens)=0/8: 统计功效不足导致早期误判，sync-dip 在长训练后溶解。

### Phase Diagram T=5 (Pythia-410M, Wiki, fp32) — 完成 D173
| α | s42 | 备注 |
|---|-----|------|
| 0.45 | **0/8** ✅ | TY Granger 数值不稳定（6 点 VAR 病态）|
| 0.50 | **0/8** ✅ | — |
| 0.60 | **0/8** ✅ | — |
| 0.75 | **0/8** ✅ | — |

4/4 = 0/8，α_c(5)≥1.0 理论预测四点独立验证。T=5 行在论文中作为 anchor row（一句话）。
**T=5 统计功效限制**: 仅 6 数据点（gen 0-5），TY Granger VAR 模型病态（负 F-stat），threshold onset 无触发。检测全面依赖 PermG 和 diff_xcorr。

### Phase Diagram T=15 (Pythia-410M, Wiki, fp32) — 完成 D180
| α | s42 | s43 | 备注 |
|---|-----|-----|------|
| 0.45 | **6/8** ✅ | running | M063 修正（旧脚本报 8/8，d102 脚本确认 6/8）。0/8@T=10→6/8@T=15, step-function |
| 0.50 | **6/8** ✅ | — | — |
| 0.60 | **0/8** ✅ | **0/8** ✅ | sync-dip persists at T=15, **双种子确认** |
| 0.75 | **6/8** ✅ | — | — |

**关键洞察**: α=0.45 从 T=10 的 0/8 跳到 T=15 的 6/8，这是 Phase Diagram 中最锐利的 step-function 跃迁——不经过中间态。6/8 与其他可检测格一致，**6/8 ceiling 无例外**（M063 修正后确认，旧脚本的 8/8 是错误值）。

## Detection Lower Bound v2 (2026-05-21)
- **Joint model**: rate(α,T) = 0.70 / (1 + exp(-100·(α - α_c(T))))
- **α_c(T) = 0.193 + 75.68·T^(-2.41)**, R²=0.883
- α_c(T=10) = 0.487, α_c(T=15) ≈ 0.304, α_c(T=20) = 0.248, α_c(T=25) ≈ 0.232
- v1 错误: α=0.50 硬编码为 0/8 导致 α_c 偏高到 0.67。v2 从 JSON 读取修正。
- Sigmoid k=100 反映 sharp phase transition

## TE/MI Sync-Dip 机制 (2026-05-21, D162)
- 仅 2/8 对支持"高 MI 低 TE"假说 → 不能作为通用机制解释
- TE directionality 是最强发现: α 越高 forward-dominant pairs 越多 (4/8→8/8)
- 实际上是 confounded co-variation (同一 upstream force)，非独立因果关系
- 论文中 sync-dip 机制解释需要更保守的措辞

## 1.4B Scale Verification (2026-05-24 完成)

### Model Variant Note (D202 决策)
- **410M**: 全部使用 `EleutherAI/pythia-410m`（non-deduped），包括 s42/s43/s44
- **1.4B**: 全部使用 `EleutherAI/pythia-1.4b-deduped`
- 各 scale 内部一致可比。跨 scale 比较时用 "consistent across" 而非 "scale-invariant"
- 论文需在 Limitations 或 appendix 注脚中披露此差异

### T=10 Row Results (Pythia-1.4B-deduped, Wiki, fp32) — D102 5-method
| α | 410M PermG | 1.4B PermG (s42) | 1.4B K≥3 | 对比 |
|---|-----------|------------------|----------|------|
| 0.45 | 0/8 | **0/8** fwd, 0/8 rev | 1/8 | **below-threshold scale-consistent** ✅ |
| 0.50 | **6/8 (3/3 seeds)** | **4/8** fwd, 2/8 rev | 3/8 | 检测弱于 410M |
| 0.60 | 0/8(dip) | **4/8** fwd, 0/8 rev | 3/8 | **sync-dip 在 1.4B 消失！** |
| 0.75 | 6/8 | **5/8** fwd, 0/8 rev | 5/8 | Scenario B confirmed (onset shift) |

### 1.4B 6-pair D102 Complete Results (2026-05-24, mauve excluded → 6 pairs)

| α | T | Seed | PermG fwd | PermG rev | Robust ≥3/5 | 关键 |
|------|-----|------|-----------|-----------|-------------|------|
| 0.75 | 15 | s43 | 6/6 | 0/6 | **6/6** | 最强检测，perfect asymmetry |
| 0.75 | 10 | s44 | 6/6 | 0/6 | **6/6** | 3rd seed 完全一致 |
| 0.60 | 15 | s43 | 6/6 | 3/6 | **6/6** | sync-dip 消除确认 |
| 0.60 | 10 | s44 | 6/6 | 0/6 | **5/6** | sync-dip 消除（差 1 pair） |
| 0.50 | 15 | s43 | 3/6 | 0/6 | **3/6** | ece 通道 3/3 robust，entropy 全落 |
| 0.50 | 10 | s44 | 6/6 | 0/6 | **0/6** | ⚠️ PermG vs robust 分裂 |
| 0.45 | 15 | s43 | 5/6 | 3/6 | **3/6** | ece 通道 robust，T 增加挽救 |
| 0.45 | 10 | s44 | 0/6 | 0/6 | **0/6** | blind zone 3rd seed 确认 |

**关键发现**：
1. α=0.60 是 robust detection 可靠边界（T=10 已 5/6, T=15 达 6/6）
2. ece > entropy 灵敏度：α=0.45-0.50 transition zone 中 ece 始终更强
3. PermG 单方法 false positive 风险：T=10 α=0.50 s44 PermG 6/6 vs robust 0/6
4. Scenario B 完整确认：C1✅ C2✅ C3✅ C4✅

### Gap Pattern（完整，D206/D208）
| α range | Gap (1.4B - 410M) | 解读 |
|---------|-------------------|------|
| Onset (0.45-0.50) | **-3/8** (恒定) | entropy saturation → power loss |
| Sync-dip (0.60) | **+6/8** | 410M sync-dip 在 1.4B 消除 |
| Strong (0.75) | **0** | 完全匹配，无 attenuation |

## Invalidated Experiments
- **phase_diagram/t10_a050_s43_fp32** (19828): start_gen=6 resume artifact。PermG=0/8 是因为仅 5 代数据导致 Granger 检验失效，非真实检测失败。Canonical 结果见 alpha_sweep/a050_s43_fp32 (full run, PermG=6/8)。

## Key Decisions
- D079: fp32 是 ≤3B 模型的强制精度
- D148: α=0.60 clean PermG=0/8 fp32 — sync-dip confirmed real
- D157: GPT-2m failure is precision-dependent (fp32 6/8, bf16 0/8)
- D161: t20_a025 PermG=3/8 (positive surprise)
- D162: TE/MI sync-dip 仅 2/8 支持，不可作为通用机制
- D163: d37g/d37b 叙事约束: mechanistic 仅 2/5 指标单调
- D167: a000_s45 PermG FPR=2/8, 最终累积 2/56=3.57% (D171)
- D178: T=15 α=0.45 PermG=6/8（M063 修正确认，非 8/8）, step-function 最强证据
- D188: Scenario A confirmed — sync-dip dissolves at T=25 (5/8)
- D189: 1.4B 措辞约束 "consistent across" ≠ "scale-invariant"
- D192: γ-comparison 废弃，shape comparison 唯一路线
- D194: P_max 6/8 = mauve pair 结构，非信号饱和
- D202: 410M=non-deduped, 1.4B=deduped — 各 scale 内部一致，论文需披露
- D206: α-conditional scale effect
- D208: C4 4/4 PASS
- D209: C3 forward 4/4 robust, direction 2/4 (α≥0.60 bidirectional seed-specific)
- D212: Adopt Reviewer #160 framing
- D220: GPT-2m FPR 不入主文，放 appendix "Cross-Architecture FPR Sensitivity"；主文加一句 consensus 鲁棒性

## C4 First-Diff Monte Carlo
- Raw perm FPR inflates to 10-12% at φ=0.87; first-diff controls to ~5-6%
- Power loss: T=11 下 44-67%; T=21 强信号下 power=0.67-0.74（可接受）

## 1.4B Seed Variance Warning
- 1.4B Wiki α=1.0: s42 PermG=2/8, s43 PermG=6/8 — 不要从单 seed 下结论
- 1.4B Wiki α=0.50: s42 PermG=3/8 (negative, corrected from 0/8) — onset 可能随 scale 右移

## GPU Infrastructure
### westd-17855 (6× RTX PRO 6000 Blackwell 98GB)
- 工作目录: /root/autodl-tmp/distrib_canary_collapse/
- Python: /root/miniconda3/bin/python, conda base
- HF_HOME: /root/autodl-tmp/.hf_cache, TRANSFORMERS_OFFLINE=1
- 1.4B 模型路径: /root/autodl-tmp/.ms_cache/EleutherAI/pythia-1.4b-deduped

### westd-19828 (2× RTX PRO 6000 Blackwell 98GB)
- 同样 conda base, 同样项目路径
- 1.4B 模型路径: /root/autodl-tmp/.hf_cache/EleutherAI/pythia-1.4b-deduped

## GPT-2-medium Null Experiments (2026-05-24 诊断)
### westd-17855: null_gpt2m_s42_fp32 & null_gpt2m_s43_fp32
- **Cron 误判 false positive**：两个实验均正常完成（EXIT_CODE=0），cron 在实验运行期间 5 次轮询未找到 sentinel，自动标记 failed
- s42: all_metrics.json 4999B, sentinel 写入 15:42, ppl=17.27, mauve=0.0138
- s43: all_metrics.json 4974B, sentinel 写入 15:43, ppl=17.26, mauve=0.0128
- gen_0 到 gen_10 全部完成，输出目录完整
- **无需修复**，数据可直接使用
