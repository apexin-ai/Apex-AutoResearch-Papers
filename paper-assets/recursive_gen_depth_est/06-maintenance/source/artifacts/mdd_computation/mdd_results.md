# MDD (Maximum Discriminable Depth) Computation

## 定义

- **EDD_{T}** = max{d : AUC(d\_i, d\_{i+1}) >= T, for all i in 0..d-1} (连续 prefix 全部 >= T)
- **MDD_{T}** = max{d : AUC(d\_i, d\_{i+1}) >= T, for any i} (不要求连续，只要存在某对 >= T)
- **T = 0.70**
- MDD > EDD 仅在 AUC profile 非单调（中间有 dip 但后续恢复）时出现

## 数据来源

- 9-cell atlas: `edd_threshold_sensitivity.json` (与 `matrix_3x3_analysis.md` 附录一致)
- 深度扩展 (d3v4, d4v5): `results_summary.json` -> `supplementary.depth_extension_binary_pairwise` (plan_011 系列, nucleus 策略)

---

## 9-Cell Atlas 结果 (3 pairs: d0v1, d1v2, d2v3)

| Model | Strategy | d0v1 | d1v2 | d2v3 | EDD | MDD | Gap | 单调性 |
|-------|----------|------|------|------|-----|-----|-----|--------|
| Pythia-1.4B | nucleus p=0.95 | 0.998 | 0.861 | 0.801 | 3 | 3 | 0 | 单调递减 |
| Pythia-1.4B | temp t=0.9 | 0.997 | 0.833 | 0.793 | 3 | 3 | 0 | 单调递减 |
| Pythia-1.4B | top-k k=50 | 0.993 | 0.752 | **0.692** | **2** | **2** | 0 | 单调递减 |
| OLMo-1B | nucleus p=0.95 | 0.983 | 0.867 | 0.812 | 3 | 3 | 0 | 单调递减 |
| OLMo-1B | temp t=0.9 | 0.996 | 0.901 | 0.821 | 3 | 3 | 0 | 单调递减 |
| OLMo-1B | top-k k=50 | 0.993 | 0.831 | 0.736 | 3 | 3 | 0 | 单调递减 |
| GPT-2 XL | nucleus p=0.95 | 0.994 | 0.913 | 0.883 | 3 | 3 | 0 | 单调递减 |
| GPT-2 XL | temp t=0.9 | 0.996 | 0.937 | 0.882 | 3 | 3 | 0 | 单调递减 |
| GPT-2 XL | top-k k=50 | 0.991 | 0.813 | 0.753 | 3 | 3 | 0 | 单调递减 |

### 9-Cell 汇总

- **EDD=3**: 8/9 cells
- **EDD=2**: 1/9 cells (Pythia-1.4B top-k, d2v3=0.692 < 0.70)
- **MDD=EDD 对所有 cell**: Gap 全部为 0
- **所有 AUC profile 严格单调递减**: 无任何非单调 (U 型) pattern

---

## 深度扩展结果 (5 pairs: d0v1, d1v2, d2v3, d3v4, d4v5)

仅 nucleus 策略有扩展实验 (plan_011 系列)。d0v1 取自 9-cell atlas 对应 cell。

| Model | d0v1 | d1v2 | d2v3 | d3v4 | d4v5 | EDD | MDD | Gap | 单调性 |
|-------|------|------|------|------|------|-----|-----|-----|--------|
| Pythia-1.4B | 0.998 | 0.925 | 0.823 | 0.784 | **0.683** | 4 | 4 | 0 | 单调递减 |
| OLMo-1B | 0.983 | 0.968 | 0.843 | 0.765 | **0.684** | 4 | 4 | 0 | 单调递减 |
| GPT-2 XL | 0.994 | 0.966 | 0.919 | 0.750 | **0.681** | 4 | 4 | 0 | 单调递减 |

### 深度扩展汇总

- 所有 3 个模型 EDD=MDD=4 at T=0.70
- d4v5 AUC 在 0.681-0.684 范围，一致低于 T=0.70，是 depth signal 消失的边界
- 仍然严格单调递减，无 recovery

---

## 关键发现

### 1. MDD = EDD 在所有实验条件下成立

所有 12 个 profiles (9-cell + 3 depth extension) 的 AUC 衰减均严格单调递减。不存在 MDD > EDD 的情况。这意味着 depth signal 的衰减是纯单调的，不存在 "中间 dip 但深层恢复" 的 U 型 pattern。

### 2. 单调衰减的物理含义

递归生成每增加一层，consecutive-pair AUC 单调下降，反映了 distribution collapse 的累积性。每一轮递归 finetune 使模型输出分布更集中，深度间的统计差异随深度单调缩小。这与 downstream train loss 的单调递减一致 (d0: 2.558, d1: 1.920, d2: 1.286)。

### 3. depth signal 消失边界

- 9-cell atlas (d0-d3): 8/9 cells 在 T=0.70 仍可区分到 d3
- 深度扩展 (d0-d5): 所有模型在 d4v5 跌破 0.70 (0.681-0.684)，信号消失边界 = depth 4
- d4v5 AUC 的跨模型收敛 (range 仅 0.003) 暗示 depth 4-5 的分布差异接近 noise floor

### 4. 唯一非单调 profile 出现在 instruct model (不在 atlas 内)

Qwen2.5-1.5B-Instruct 的 profile (d0v1=0.653, d1v2=0.620, d2v3=0.664) 呈 U 型: d1v2 < d2v3。该 cell 的 EDD=0 (d0v1 < 0.70), MDD=0 (所有 pairs < 0.70)。但 d2v3 > d1v2 的非单调性表明 instruct tuning 可能引入不同于 base model 的 depth-signal 动态。此数据来源: `results_summary.json` -> `instruct_model`。

### 5. 交叉验证数据的 AUC 值系统性偏高

`edd_analysis_9cell.json` 中的 cross-validated AUC means 系统性高于 `edd_threshold_sensitivity.json` 的值 (例如 pythia_nucleus d1v2: 0.930 vs 0.861)。两个数据源的 EDD 结论一致 (在 T=0.70 下)，但 margin 不同。本报告使用 `edd_threshold_sensitivity.json` 值，与论文正文和 `matrix_3x3_analysis.md` 一致。

---

## 附录: 多阈值 MDD 对比

由于所有 profile 单调递减，MDD=EDD at all thresholds。以下为 EDD (= MDD) 在不同 T 下的 9-cell 分布:

| T | EDD=3 count | EDD=2 count | EDD=1 count | EDD=0 count |
|---|-------------|-------------|-------------|-------------|
| 0.65 | 9/9 | 0 | 0 | 0 |
| 0.70 | 8/9 | 1/9 | 0 | 0 |
| 0.75 | 7/9 | 2/9 | 0 | 0 |
| 0.80 | 5/9 | 4/9 | 0 | 0 |

Drop cells:
- T=0.70: Pythia top-k (d2v3=0.692)
- T=0.75: + OLMo top-k (d2v3=0.736)
- T=0.80: + Pythia temp (d2v3=0.793), GPT-2 XL top-k (d2v3=0.753)

Bottleneck pair 始终是 d2v3，d0v1 从不是 limiting factor (所有 cell > 0.98)。
