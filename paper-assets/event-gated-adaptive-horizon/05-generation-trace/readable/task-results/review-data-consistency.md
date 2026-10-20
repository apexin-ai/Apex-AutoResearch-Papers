# review data consistency

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_review_data-consistency_20260524T021301_result.json`
- **Structured JSON:** [`2080d66a6113864ea228.json`](../../sessions/20/2080d66a6113864ea228.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审计完成。以下是全部发现：

---

## 不一致报告

### [不一致 #1] exp\_058 NVE 值错误
```
文件: docs/paper/sections/appendix.tex 行 75
论文中的值: 0.23×
Registry/实际值: nve_peak = 0.78 @ 45K
```
Registry note 明确记录 "NVE=0.78× (raw 0.231 / baseline 0.296 @45K)"。论文误用了原始 ve_ratio (0.231) 而非 NVE (0.78)。
**修正建议**: 将 `0.23$\times$` 改为 `0.78$\times$`

---

### [不一致 #2] Abstract vs Introduction 退化范围不一致
```
文件: docs/paper/sections/abstract_body.tex 行 1
论文中的值: "14--30\% of baseline"

文件: docs/paper/sections/introduction.tex 行 6
论文中的值: "14--19\% of baseline"
```
实际数据：fixed dt=2 → 14.5%, fixed dt=4 → 19.3%, learned gate → 10.8%。Introduction 的 14-19% 覆盖 dt=2 和 dt=4。Abstract 的 30% 可能来自 CIVO factorial 中 self-correcting seed (009b: 267.9/915.7 = 29.3%)，但这不属于"variable-rate configuration"的同一范畴。
**修正建议**: 统一为 `11--19\%`（含 learned gate）或 `14--19\%`（仅 fixed-dt），并在 abstract 修正

---

### [不一致 #3] analysis.tex 行 8 种子数与 NVE 范围不匹配
```
文件: docs/paper/sections/analysis.tex 行 8
论文中的值: "sustained CIVO (4/4 trained, NVE 1.53--108×)"
```
"4/4" 是 Walker 种子数，但 NVE 范围 1.53--108× 跨越了 Walker (1.53--4.62×) 和 Cheetah (8.27--108.52×)。
**修正建议**: 改为 `(6/6 trained locomotion, NVE $1.53$--$108\times$)` 或保持 4/4 但缩窄范围为 `NVE $1.53$--$4.62\times$`

---

### [不一致 #4] exp\_047 缺失于 Complete Results 表
```
文件: docs/paper/sections/appendix.tex tab:complete_results (行 14-93)
论文中的值: exp_047 未出现
Registry/实际值: exp_047_frozen_dt_emb_walker_s1, NVE=1.71×, eval_peak=408.79@125K, eval_final=144.22@215K
```
exp\_047 在 three-way table (行 320) 和脚注 (行 325) 中被引用，但在 complete results 表中缺失。其他 frozen Walker 种子 (042, 015b, 057) 都有列出。
**修正建议**: 在 042 和 057 之间添加一行：`047 & Frozen emb (s1) & frz$^b$ & ON & 8 & 144.2 @215K & 1.71$\times$ & Transient (self-corr.)`

---

### [不一致 #5] NVE 原始值表中 008d 四舍五入不一致
```
文件: docs/paper/sections/appendix.tex 行 132
论文中的值: 4.13 (NVE raw values table)

文件: docs/paper/sections/appendix.tex 行 26 (及全文其他位置)
论文中的值: 4.12×
```
Complete results 表、main Table 1、post-CIVO 表、dual critic 表全部使用 4.12×，唯独 NVE raw values 表写成 4.13。
**修正建议**: 统一为 `4.12`

---

### [不一致 #6] exp\_022b NVE — Registry 值陈旧
```
文件: docs/paper/sections/appendix.tex 行 40
论文中的值: 0.63×
Registry 值: nve_peak = 1.22
```
Registry 记录的 ve\_ratio\_peak=0.218，ve\_ratio\_105K=0.075。论文使用 4-seed mean baseline 归一化得到 0.63×，而 registry 似乎使用单种子 baseline 得到 1.22。论文的归一化规范 (4-seed mean) 是明确声明的 (appendix 行 267)，论文值 0.63 可能正确。
**修正建议**: 更新 registry 中 exp\_022b 的 nve\_peak 为与论文一致的 0.63（使用 4-seed 归一化）

---

## 一致性确认

以下检查点全部一致：

| 检查项 | 论文 | Registry | 状态 |
|--------|------|----------|------|
| 6/6 locomotion CIVO | Walker 4/4 + Cheetah 2/2 | ✓ | 一致 |
| 0/5 manipulation dt-emb-dep CIVO | Stack 0/2 + Peg 0/2 + Pick 0/1 | ✓ | 一致 |
| Walker frozen s0 NVE | 0.19× | 0.194 | 一致 |
| Walker frozen s1 NVE | 1.71× | 1.71 | 一致 |
| Walker frozen s2 NVE | 1.88× | 1.88 | 一致 |
| Cheetah frozen s0 NVE | 1.35× | 1.35 | 一致 |
| PegInsertion s1 trained peak | 3.08× | ve_ratio_peak=3.08 | 一致 |
| PegInsertion s1 frozen peak | 11.32× | ve_ratio_peak=11.321 | 一致 |
| Detector TPR/FPR | 5/5, 2/9 | N/A (14 runs) | 论文内一致 |
| Baseline s1 eval@105K | 915.7 | N/A | 一致 |
| Baseline s1 eval@505K | 970.4 | N/A | 一致 |
| LOEO mean AUROC | 0.981 | N/A | 论文内一致 |
| 022b eval@105K | 300.7 | 300.7 | 一致 |
| 058 eval@215K | 80.46 | 80.46 | 一致 |
| Frozen intervention 5/7 prevention | 7 seeds (W5+C2) | ✓ | 一致 |
| PickCube frozen peak | 8.81× @ 62.5K | exp\_054 (metrics empty but paper cites) | 无法验证 |

---

## 附注：陈旧 Artifact 文件（不影响论文）

- `artifacts/analysis/detector_table.tex`: TPR=3/3, FPR=2/7（旧版 10-run），论文已更新为 5/5, 2/9（14-run）
- `artifacts/_project/paper/nve_sensitivity_table*.tex`: AUROC=0.933（旧版），论文已更新为 0.958
- exp\_053, exp\_054 registry metrics 为空，无法从 registry 交叉验证

**总结**: 6 个不一致（#1 exp\_058 NVE 最严重，直接影响数值准确性），14+ 个检查点一致。

---
