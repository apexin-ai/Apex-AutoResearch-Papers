# 全文数据真实性与可追溯性审计报告

**审计日期**: 2026-05-25
**审计范围**: `paper/sections/*.tex` 全部数值声明
**数据源**: `artifacts/raw_data_audit.md` (服务器原始数据 2026-05-23), `artifacts/epsilon_clipping_verification.json`, `artifacts/alternative_ews_comparison.json`, `artifacts/sigma_comparison_analysis.md`

---

## (a) 审计统计

| 类别 | 数量 |
|------|------|
| 审计数值总数 | ~420 |
| 已验证 ✓ (与源头数据一致) | ~350 |
| 无法本地验证 (需服务器数据) | ~55 |
| 发现问题 | 2 项 (1 项数据缺口, 1 项叙述不一致) |
| 轻微精度备注 (在可接受舍入范围内) | 5 项 |

### 验证覆盖率

| 论文组件 | 数值数 | 验证状态 |
|----------|--------|----------|
| Table 1 (tab:phase0) | 35 | ✅ 全部验证 |
| Table 3 (tab:phase_summary) | 37 | ✅ 全部验证 (r=0.2 见问题 #1) |
| Table 4 (tab:ews_main) | 7 | ✅ 全部验证 |
| Table 5 (tab:cross_arch) | 16 | ⚠️ 百分比已验证, 原始中间代值需服务器 |
| Appendix Table 6 (tab:pergen_variance, r=0) | 132 | ✅ 全部验证 |
| Appendix Table 7 (tab:pergen_variance_r02) | 110 | ⚠️ 声称 3 seeds, 仅找到 2 seeds 源数据 (见问题 #1) |
| Appendix Table 8 (tab:alpha_robustness) | 15 | ✅ 全部验证 |
| Appendix Table 9 (tab:ews_comparison) | 7 | ✅ 全部验证 |
| 正文内联数值 (~60 处) | ~60 | ✅/⚠️ 大部分验证, 部分需服务器 |

---

## (b) 问题清单

### 问题 #1: r=0.2 种子数不一致 [严重度: 中]

**现象**: 论文在两处声明 r=0.2 使用 3 seeds (42, 43, 44):
- Appendix Table 7 caption: "mean±s.d. across seeds 42, 43, 44"
- Table 3 caption: "$r{=}0.2$ the mean of three seeds (42, 43, 44)"

但 `raw_data_audit.md` (2026-05-23 从服务器提取) 仅包含 2 seeds:
- seed42: `phase1_fixed_mix_r02_seed42_results.json` (exp_011)
- seed43: `phase1_fixed_mix_r02_seed43_results.json` (exp_017)

**交叉验证**:
- 2-seed mean (raw): SLV=2467.74, r_eff=508.62, PPL=13.61
- Paper 值: SLV=2467.2, r_eff=508.1, PPL=13.54
- 差异: SLV 差 0.54, r_eff 差 0.52, PPL 差 0.07
- 这些差异与"存在第三个 seed 使均值偏移"一致 (推算 seed44 SLV≈2466.1, r_eff≈507.1, PPL≈13.39, 均合理)

**结论**: 很可能存在 seed44 的 r=0.2 实验数据在服务器上, 但 raw_data_audit 收集时遗漏。论文数值基于 3-seed 均值, 数值本身应正确, 但需要服务器确认。

**建议**: SSH 到 `rtx6000-diagprobe` 检查是否存在 `phase1_fixed_mix_r02_seed44*.json`。若存在, 补充到 raw_data_audit.md; 若不存在, 需修改论文中两处 caption 为 "2 seeds (42, 43)" 并重算所有 r=0.2 均值和标准差。

---

### 问题 #2: r=0.25 "dip" 度量基准不一致 [严重度: 低]

**现象**: §3.5 中两个相邻声明使用不同度量:

> "At $r{=}0.2$, SLV dips $-7.3$ points at Gen~2"

→ 验证: 3-seed mean Gen 2 SLV = 2359.4, baseline = 2366.7, **raw departure** = -7.3 ✓

> "At $r{=}0.25$, the same pattern holds with a weaker dip ($-2.1$)"

→ raw departure at Gen 2: 2363.41 - 2366.68 = **-3.27** (不是 -2.1)
→ EMA-smoothed (α=0.5) departure at Gen 2: **-2.17 ≈ -2.1** ✓
→ raw departure at Gen 1: 2364.54 - 2366.68 = **-2.14 ≈ -2.1** (也匹配)

后文则给出了正确的 raw maximum departure:
> "maximum SLV departure...shrinks continuously with $r$ ($-7.3$ at $r{=}0.2$, **$-3.3$** at $r{=}0.25$, $-1.5$ at $r{=}0.3$)"

→ -3.3 = 2363.41 - 2366.68 = -3.27 ✓

**结论**: 前后文自相一致 (后文 -3.3 正确), 但 "weaker dip (-2.1)" 与 "maximum departure (-3.3)" 使用了不同度量基准 (EMA vs raw), 而 r=0.2 的 -7.3 是 raw 度量。叙述上可能让仔细的 reviewer 困惑。

**建议**: 将 "weaker dip ($-2.1$)" 改为 "weaker dip ($-3.3$)" 以与 r=0.2 的 raw 度量保持一致, 并与后文 maximum departure 列表吻合。或在首次提及时注明度量基准 (EMA-smoothed)。

---

## 轻微精度备注 (均在可接受舍入范围内, 无需修改)

| # | 位置 | 论文值 | 精确计算值 | 差异 | 说明 |
|---|------|--------|-----------|------|------|
| 1 | §3.2 Phase I | CV < 1.3% | 1.297% | 边界 | 技术上是 "≤ 1.3%" 而非 "< 1.3%"; Gen 10 恰好是最大值 |
| 2 | §3.2 Cross-Scale | PPL +66% | 65.4% | 0.6pp | 依赖 PPL 输入精度 (8.1, 13.4 均为整数舍入) |
| 3 | §3.6 Cross-Arch | PPL +2028% | ~2023% | 5pp/2000pp | 取决于 PPL₀ 精度 (15.5 vs 15.47) |
| 4 | Table 5 ΔSLV | 6.9%, 7.0%, 17.9% | 6.97%, 7.11%, 18.0% | ≤0.1pp | SLV 在表中取整到整数, 百分比从未取整值计算 |
| 5 | Fig 1 caption | 104 points | 103.6 | 0.4 | 2572-2468=104 (取整后), 2571.6-2468.0=103.6 (精确) |

---

## 详细验证记录

### Abstract
| 声明 | 源 | 验证 |
|------|-----|------|
| "10 recursive generations of Pythia-410M" | setup | ✅ |
| "three seeds" | setup | ✅ |
| "HellaSwag drops 3.3 percentage points" (Gen 0→2) | .413-.380=.033=3.3pp | ✅ |
| "eight candidate indicators" | 8 in EWS table | ✅ |
| "<1 s" compute | methodology | ✅ |
| "five levels" mixing | r∈{0,0.2,0.25,0.3,0.5} | ✅ |
| "r_crit ∈ (0.25, 0.3]" | alpha_robustness table | ✅ |
| "GPT-2-medium (355M)" | model spec | ✅ |

### Table 1 (tab:phase0) — 全部 35 个值
| Gen | r_eff | SLV | PPL | HeSw | D-4 | σ₁ |
|-----|-------|-----|-----|------|-----|-----|
| 0 | 417.55 ✅ | 2366.68 ✅ | 9.55 ✅ | .413 ✅ | .738 ✅ | 1942.8 ✅ |
| 2 | 496.17 ✅ | 2467.98 ✅ | 13.56 ✅ | .380 ✅ | .505 ✅ | 718.7 ✅ |
| 5 | 479.77 ✅ | 2365.99 ✅ | 24.50 ✅ | .341 ✅ | .412 ✅ | 749.2 ✅ |
| 7 | 464.10 ✅ | 2293.24 ✅ | 37.82 ✅ | .319 ✅ | .375 ✅ | 788.4 ✅ |
| 10 | 438.05 ✅ | 2181.35 ✅ | 70.99 ✅ | .296 ✅ | .324 ✅ | 874.6 ✅ |

s.d. at Gen 10: r_eff ±4.8 ✅, SLV ±28.3 ✅, PPL ±5.6 ✅, HeSw ±.006 ✅, D-4 ±.15 ✅

**验证方法**: 逐 seed 重算 3-seed mean 和 sample s.d., 全部匹配。

### §3.2 Phase I 内联数值
| 声明 | 计算 | 验证 |
|------|------|------|
| r_eff +18.8% | (496.2-417.55)/417.55=18.83% | ✅ |
| SLV +4.3% | (2468.0-2366.7)/2366.7=4.28% | ✅ |
| σ₁ drops 1942.8→718.7 | raw data | ✅ |
| CV < 1.3% | max CV=28.3/2181.4=1.297% | ✅ (见备注 #1) |
| HellaSwag drops 8.0% | (.413-.380)/.413=7.99% | ✅ |
| D-4 falls 31.6% | (.738-.505)/.738=31.57% | ✅ |

### §3.2 Phase II
| 声明 | 计算 | 验证 |
|------|------|------|
| r_eff 496.2→493.6 | appendix Gen 2→3 | ✅ |
| SLV 2468→2440 | 2468.0→2440.4, rounds to 2440 | ✅ |
| SLV −1.1% vs r_eff −0.5% | (2468.0-2440.4)/2468.0=1.12%; (496.2-493.6)/496.2=0.52% | ✅ |

### §3.2 Phase III
| 声明 | 计算 | 验证 |
|------|------|------|
| decline −31.0/gen onset | (2468.0-2406.0)/2=31.0 | ✅ |
| decline −37.4/gen accel | (2406.0-2181.4)/6=37.43 | ✅ |
| 78% in Phase III | (2406.0-2181.4)/(2468.0-2181.4)=78.4% | ✅ |
| r_eff 438.1 (−11.7%) | (496.2-438.1)/496.2=11.71% | ✅ |
| SLV 2181.4 (−11.6%) | (2468.0-2181.4)/2468.0=11.61% | ✅ |
| PPL 71.0 (+643%) | (71.0-9.55)/9.55=643.5% | ✅ |
| σ₁ 1942.8→718.7→874.6 | appendix table | ✅ |

### §3.2 Cross-Scale Pilot (Pythia-1B)
| 声明 | 验证 |
|------|------|
| SLV 2835→2906 (+2.5%) | 71/2835=2.50% ✅ (计算验证, 原始数据需服务器) |
| SLV→2865 at Gen 3 | ⚠️ 需服务器 |
| r_eff peaks Gen 2 (580.9 vs 570.8) | ⚠️ 需服务器 |
| PPL 8.1→13.4 (+66%) | 计算得 65.4%, 见备注 #2 |

### §3.3 Adaptive Mixing
| 声明 | 计算 | 验证 |
|------|------|------|
| SLV peaks at 2468 | Gen 2 mean | ✅ |
| r=0.5 SLV→2572 | 2571.6→2572 | ✅ |
| Gen 1 dip Δ₁≈0.0005 | alpha_robustness r=0.5 α=0.5 = 0 (t≥2); Gen 1 值不在表中, 合理 | ✅ |
| Signal 40.4→3.8 | 0.0171×2366.7=40.5≈40.4; 0.0016×2366.7=3.8 | ✅ |
| 10× drop | 40.4/3.8=10.6≈10× | ✅ |
| Zero at r≥0.3 | alpha_robustness table | ✅ |
| PPL +58% at r=0.5 | (15.11-9.55)/9.55=58.2% | ✅ |
| D-4 falls to .152 | 2-seed mean=0.1521 | ✅ |

### §3.4 Alternative EWS (Table 4)
| 指标 | 论文 Rel Δ | 验证 |
|------|-----------|------|
| SLV | 11.8% | ✅ |
| RankMe | 4.7% | ✅ |
| Token ent. | 9.6% | ✅ |
| Stable rank | 14.0% | ✅ |
| Spec. norm | 8.0% | ✅ |
| Isotropy | 75% | ✅ |
| Raw PPL | 704% (seed 42) / 643% (3-seed) | ✅ |
| SLV SNR 2.5× RankMe | 11.8/4.7=2.51 | ✅ |

### §3.5 Trajectory Classification (Table 3)
| r | SLV | r_eff | PPL | D-4 | max_Δ_t | 验证 |
|---|-----|-------|-----|-----|---------|------|
| 0 | 2181.4 | 438.1 | 71.0 | .324 | --- | ✅ |
| 0.20 | 2467.2 | 508.1 | 13.54 | .324 | .0016 | ⚠️ 见问题 #1 |
| 0.25 | 2488.1 | 513.8 | 13.41 | .342 | .0005 | ✅ |
| 0.30 | 2508.2 | 521.1 | 13.34 | .295 | 0 | ✅ |
| 0.50 | 2571.6 | 553.5 | 15.11 | .152 | 0 | ✅ |

内联数值:
| 声明 | 计算 | 验证 |
|------|------|------|
| r=0.2 dip −7.3 at Gen 2 | 2359.4-2366.7=-7.3 (3-seed) | ✅ |
| r=0.2 recovery to 2467.2 (+4.3%) | (2467.2-2366.7)/2366.7=4.25% | ✅ |
| r=0.25 dip −2.1 | **见问题 #2** | ⚠️ |
| max departure −7.3/−3.3/−1.5 | raw Gen2/Gen2/Gen1 departures | ✅ |
| r=0.3 SLV 2508.2 (+6.0%) | (2508.2-2366.7)/2366.7=5.98% | ✅ |
| r=0.5 SLV 2572 (+8.7%) | (2571.6-2366.7)/2366.7=8.66% | ✅ |
| D-4 mean .324--.342 at r∈{0.2,0.25} | table values | ✅ |
| D-4 CV=3.9% vs SLV CV=0.12% at r=0.25 | D-4: 0.01337/0.3422=3.91%; SLV: 2.894/2488.1=0.116% | ✅ |
| D-4 s.d.≈0.17 | r=0.2 Gen10: .324±.171 | ✅ |
| D-4 s.d.=0.15 (r=0) | raw: 0.150 | ✅ |
| D-4 s.d.=0.155 (r=0.3) | raw: 0.1546 | ✅ |

### §3.6 Cross-Architecture (Table 5)
| 声明 | 验证 |
|------|------|
| SLV₀=689 | ⚠️ 需服务器 (与 r_eff=23 一致, epsilon_clipping 确认) |
| r=0 SLV peaks at 924 (+34.1%) | ⚠️ 需服务器 (计算: (924-689)/689=34.1%) |
| r=0 SLV=415 at Gen 9 (−55.1% from peak) | ⚠️ 需服务器 (计算: (924-415)/924=55.1%) |
| ΔSLV −39.8% (r=0) | (415-689)/689=−39.77% ✅ |
| ΔSLV +7.0% (r=0.25) | (738-689)/689=7.11%, 见备注 #4 |
| ΔSLV +6.9% (r=0.3) | (737-689)/689=6.97%, 见备注 #4 |
| ΔSLV +17.9% (r=1.0) | (813-689)/689=18.0%, 见备注 #4 |
| PPL 15.5→329 (+2028%) | 见备注 #3 |
| σ₁: 6598→1191→~1570 | ⚠️ 需服务器 |
| r_eff=23 vs Pythia 418 | epsilon_clipping: 23.09 ✅; Pythia: 417.55≈418 ✅ |
| r=1.0 PPL −27.4% | ⚠️ 需服务器 |
| r=0.25/0.3 Gen 0→1: SLV +7.5--8.5% | ⚠️ 需服务器 |

### Appendix
| 组件 | 验证 |
|------|------|
| Table 6 全部 132 值 (r=0 per-gen) | ✅ 逐值验证 |
| Table 7 (r=0.2 per-gen) | ⚠️ 声称 3 seeds, 仅 2 seeds 可验证 (见问题 #1) |
| Table 8 (alpha robustness) | ✅ |
| Table 9 (EWS comparison) | ✅ |
| Raw PPL 704% (seed 42) vs 643% (3-seed) footnote | ✅ (76.78-9.55)/9.55=703.7% |
| AdamW lr=5e-5, wd=0.01, warmup=5%, bs=32 | 训练配置, 需对照脚本 |
| Gradient clip=1.0 | 训练配置, 需对照脚本 |
| Temp=1.0, top-k=50, maxlen=512 | 生成配置, 需对照脚本 |
| RTX PRO 6000 (96 GB) | 硬件规格 ✅ |
| ~220 GPU-hours | ⚠️ 需服务器日志核实 |
| 15--26 single-GPU hours per pipeline | ⚠️ 需服务器日志核实 |

### 方法章节
| 声明 | 验证 |
|------|------|
| n=1000, d=1024, γ≈0.98 | ✅ |
| ε=10⁻¹⁰ | ✅ (epsilon_clipping) |
| Min σ=0.016 (GPT-2 Gen 10) | ✅ (epsilon_clipping: 0.0160) |
| 8 orders above ε | 0.016/1e-10=1.6e8 ✅ |
| SLV CV < 0.4% for n∈{250,5000} | ⚠️ 需服务器实验数据 |
| S̃₀=2366.68 | ✅ |

---

## (c) 建议修复方案

### 问题 #1: r=0.2 种子数
- **紧急**: SSH 到服务器检查 seed44 r=0.2 数据是否存在
- 若存在: 补充到 raw_data_audit.md, 验证论文数值
- 若不存在: 修改 Table 3 caption 和 Appendix Table 7 caption 为 "2 seeds (42, 43)", 重算均值和标准差 (差异约 SLV ±0.5, r_eff ±0.5, PPL ±0.07 — 结论不变)

### 问题 #2: r=0.25 dip 度量基准
- 建议将 "weaker dip ($-2.1$)" 改为 "weaker dip ($-3.3$)" 以与 r=0.2 的 raw departure 基准保持一致
- 或注明 "weaker EMA-smoothed dip ($-2.1$)" 明确度量基准
- 无论哪种方案, 后文 "maximum SLV departure...−3.3 at r=0.25" 不变

---

## (d) 需要 Director 决策的项

1. **r=0.2 seed 数**: 是否派 Worker SSH 到 rtx6000-diagprobe 验证 seed44 数据存在性? 若不存在需要改两处 caption。

2. **r=0.25 dip 措辞**: 是否修改为 -3.3 (统一度量基准) 或保留 -2.1 (EMA departure, 技术上正确但度量基准与前文不一致)?

3. **Cross-architecture 数据验证**: GPT-2-medium 中间代数据 (Gen 2 SLV=924, Gen 9 SLV=415, PPL=329, σ₁ trajectory) 仅在论文正文出现, 无本地 artifact。是否需要 SSH 验证? 这些数值支撑论文的核心 cross-arch claim。

4. **Pythia-1B pilot 数据**: SLV 2835→2906→2865, PPL 8.1→13.4, r_eff 580.9 等均无本地 artifact。是否需要 SSH 验证?

5. **Compute hours (~220 total)**: 无法从本地验证。是否需要从服务器 job 日志逐实验统计?

---

## 审计结论

论文中 **所有 Pythia-410M 相关数值 (r=0/0.25/0.3/0.5)** 均与服务器原始数据完全一致 (含标准差和衍生百分比), 未发现捏造或计算错误。

两个问题均为 **叙述层面** (caption seed 数声明, dip 度量基准), 不影响实验结论的正确性。

主要不确定性集中在 **GPT-2-medium 中间代数据和 Pythia-1B pilot 数据** — 这些值在论文中被引用但无本地 artifact 备份, 需要服务器验证以确认完整可追溯链。
