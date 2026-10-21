# ops fetch nve audit detail

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_fetch-nve-audit-detail_20260518T225936_result.json`
- **Structured JSON:** [`219420434664c41ca863.json`](../../sessions/21/219420434664c41ca863.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部数据已获取。以下是完整汇总。

---

## nve_audit_results.txt 完整内容

### Baselines

**Walker baseline (= exp_009d_baseline_walker_s1):**

| step | ve_ratio |
|------|----------|
| 35000 | 0.241219 |
| 45000 | 0.331018 |
| 55000 | 0.403526 |
| 65000 | 0.562928 |
| 75000 | 0.719429 |
| 85000 | 0.700652 |
| 95000 | 0.632013 |
| 105000 | 0.656413 |

**Cheetah baseline (avg 023a+023b):**

| step | avg | 023a | 023b |
|------|-----|------|------|
| 35000 | 0.109623 | 0.112012 | 0.107234 |
| 45000 | 0.196562 | 0.238781 | 0.154343 |
| 55000 | 0.342713 | 0.311536 | 0.373890 |
| 65000 | 0.385000 | 0.362932 | 0.407069 |
| 75000 | 0.408752 | 0.424438 | 0.393065 |
| 85000 | 0.614197 | 0.601288 | 0.627105 |
| 95000 | 0.509839 | 0.533528 | 0.486151 |
| 105000 | 0.650991 | 0.742791 | 0.559192 |

### Summary Table

```
exp_id         logdir                                     paper  peakNVE  pk_step  nve105K  ve105K   paper_matches      note
008d_s1        exp_008d_civo_trigger_s1                    4.12   2.0933   45000     ---      ---     MISMATCH
008d_s3        exp_008d_civo_trigger_s3                    1.53   1.5279  105000   1.5279   1.0029   peakNVE,nve@105K
008d_s4        exp_008d_civo_trigger_s4                    3.03   4.6150  105000   4.6150   3.0294   ve@105K,ve@105000   Reviewer=4.62x
009b           exp_009b_008d_walker_s2                     1.62   1.6190   45000   0.3825   0.2511   peakNVE
008a_orig      exp_008a_fixed_dt2_no_subsample             0.93   0.9322   55000   0.5882   0.3861   peakNVE
008a_s1        exp_008a_unexposed_s1                       0.43   0.8348   55000   0.6552   0.4301   ve@105K,ve@105000   Reviewer=0.83x
008a_s2        exp_008a_unexposed_s2                       0.51   0.8908   45000   0.5070   0.3328   nve@105K,nve@105000
008e_v3_s1     exp_008e_v3_walker_s1                       0.94   0.9411   35000   0.8020   0.5264   peakNVE
008e_v3_s2     exp_008e_v3_walker_s2                       3.78   3.7801  105000   3.7801   2.4813   peakNVE,nve@105K
008e_v3_s3     exp_008e_v3_s3                              4.02   4.0147  105000   4.0147   2.6353   peakNVE,nve@105K
008e_v3_s4     exp_008e_v3_s4                              0.99   0.9915   95000   0.9273   0.6087   peakNVE
008f           exp_008f_no_dt_embed_subsample_on_h8        0.97   0.9701   55000   0.2974   0.1952   peakNVE
015b           exp_015b_frozen_dt_emb                      1.45   1.4539   55000   0.4194   0.2753   peakNVE             paper_final=0.55x
006            NOT FOUND                                   4.83     ---     ---      ---      ---     ---                 tried:['exp_006_variable_dt']
009c           exp_009c_008f_walker_s2                     1.14   1.1425  105000   1.1425   0.7499   peakNVE,nve@105K
009c_s3        exp_009c_no_dt_emb_s3                       0.52   1.0409   95000   0.5874   0.3856   MISMATCH
008f_s3        exp_008f_s3_no_dt_embed_walker               N/A   0.8509   95000   0.7177   0.4711   ???
010b           exp_010b_cheetah_civo_trigger               8.27   8.2672   65000   1.0549   0.6867   peakNVE
010b_s0        exp_010b_cheetah_civo_trigger_s0           70.64  108.517  105000  108.517  70.6437   peakNVE(=nve@105K)
```

---

## 完整 NVE 轨迹

### 1. exp_008a_unexposed_s1 (paper=0.43)
```
step    cfg_ve     bl_ve      NVE       eval_ret    val_mean
35000   0.161955   0.241219   0.671403   394.15      63.84
45000   0.260919   0.331018   0.788231   414.32     108.10
55000   0.336888   0.403526   0.834861   441.48     148.73  ← peak
65000   0.363766   0.562928   0.646203   491.74     178.88
75000   0.445171   0.719429   0.618784   452.34     201.37
85000   0.399346   0.700652   0.569963   546.82     218.37
95000   0.383609   0.632013   0.606963   628.57     241.13
105000  0.430113   0.656413   0.655247   630.91     271.36
```
**Peak NVE=0.835 @55K → @105K NVE=0.655.** Paper 报 0.43（不匹配任何）。审计匹配 ve@105K=0.430。

### 2. exp_008a_unexposed_s2 (paper=0.51)
```
step    cfg_ve     bl_ve      NVE       eval_ret    val_mean
35000   0.185071   0.241219   0.767230   431.61      79.88
45000   0.294924   0.331018   0.890961   430.81     127.06  ← peak
55000   0.272634   0.403526   0.675630   607.53     165.63
65000   0.305329   0.562928   0.542394   653.75     199.61
75000   0.425042   0.719429   0.590804   534.43     227.16
85000   0.405179   0.700652   0.578289   605.35     245.28
95000   0.335673   0.632013   0.531117   819.42     275.06
105000  0.332825   0.656413   0.507036   899.45     299.36
```
**Peak NVE=0.891 @45K → @105K NVE=0.507.** Paper 报 0.51 ≈ nve@105K。

### 3. exp_008d_civo_trigger_s1 (paper=4.12) — 仅 2 个数据点，提前终止
```
step    cfg_ve     bl_ve      NVE       eval_ret    val_mean
35000   0.411346   0.241219   1.705282   146.34      60.20
45000   0.692906   0.331018   2.093258   140.76      97.53  ← peak & last
```
**只训到 ~50K。Peak NVE=2.09。Paper 报 4.12 完全不匹配。MISMATCH。**

### 4. exp_008d_subsample_on_h8（可能是 "008d_trained_embed"）— 仅 3 个数据点
```
step    cfg_ve     bl_ve      NVE       eval_ret    val_mean
35000   0.411346   0.241219   1.705282   146.34      60.20
45000   0.692906   0.331018   2.093258   140.76      97.53
55000   1.666256   0.403526   4.129242    82.75     137.88  ← peak & last
```
**训到 ~55K 终止。与 008d_s1 的 35K/45K 数据完全相同（同一 run 不同 checkpoint？）。NVE 在 55K 达到 4.13 后终止。**

### 5. exp_008a_cheetah_unexposed_s0 (paper=0.49)
```
step    cfg_ve     bl_ve      NVE       eval_ret    val_mean
35000   0.118242   0.109623   1.078626   372.21      44.01
45000   0.199926   0.196562   1.017113   383.03      76.58
55000   0.264310   0.342713   0.771229   402.76     106.45
65000   0.267427   0.385000   0.694616   479.54     128.24
75000   0.301932   0.408752   0.738669   482.10     145.56
85000   0.314284   0.614197   0.511699   485.29     152.52
95000   0.326093   0.509839   0.639600   496.45     161.89
105000  0.319304   0.650991   0.490489   532.35     169.98
```
**Peak NVE=1.079 @35K → @105K NVE=0.490.** Paper 报 0.49 ≈ nve@105K。趋势平稳下降。

### 6. exp_008a_cheetah_unexposed_s1 (paper=0.48)
```
step    cfg_ve     bl_ve      NVE       eval_ret    val_mean
35000   0.141479   0.109623   1.290594   177.41      25.10
45000   0.151485   0.196562   0.770671   282.01      42.72
55000   0.161370   0.342713   0.470860   389.36      62.83
65000   0.192415   0.385000   0.499779   429.57      82.66
75000   0.269688   0.408752   0.659785   393.89     106.23
85000   0.246628   0.614197   0.401545   512.32     126.35
95000   0.277117   0.509839   0.543538   519.03     143.83
105000  0.311204   0.650991   0.478046   504.38     156.97
```
**Peak NVE=1.291 @35K → @105K NVE=0.478.** Paper 报 0.48 ≈ nve@105K。

### 7. exp_009c_no_dt_emb_s3 (paper=0.52)
```
step    cfg_ve     bl_ve      NVE       eval_ret    val_mean
35000   0.130946   0.241219   0.542853   196.53      25.74
45000   0.136610   0.331018   0.412697   337.17      46.06
55000   0.152749   0.403526   0.378536   456.10      69.67
65000   0.218442   0.562928   0.388046   457.74     100.00
75000   0.396915   0.719429   0.551709   304.59     120.90
85000   0.469931   0.700652   0.670705   268.30     126.08
95000   0.657821   0.632013   1.040835   187.34     123.24  ← peak
105000  0.385583   0.656413   0.587409   311.92     120.27
```
**Peak NVE=1.041 @95K → @105K NVE=0.587.** Paper 报 0.52（不匹配 peak 也不匹配 @105K）。审计标记 MISMATCH。

### 8. exp_015b_frozen_dt_emb (paper=1.45)
```
step    cfg_ve     bl_ve      NVE       eval_ret    val_mean
35000   0.194810   0.241219   0.807607   201.64      39.28
45000   0.417604   0.331018   1.261575   122.34      51.09
55000   0.586697   0.403526   1.453926   105.81      62.08  ← peak
65000   0.368331   0.562928   0.654313   160.31      59.05
75000   0.754102   0.719429   1.048196    80.00      60.33
85000   0.327497   0.700652   0.467418   183.48      60.09
95000   0.248928   0.632013   0.393866   238.38      59.34
105000  0.275277   0.656413   0.419365   204.20      56.21
```
**Peak NVE=1.454 @55K → @105K NVE=0.419.** Paper 报 1.45 = peakNVE。final NVE@105K=0.42 (paper_final=0.55x 也不完全匹配)。值得注意：value_mean 从 62→56 基本持平但 eval_return 剧烈波动导致 NVE 不稳定。

---

## 目录检查

**exp_006:** logdir 中不存在任何 `006` 相关目录。完全缺失。

**exp_008d 相关目录:**
```
exp_008d_civo_trigger_s1      (67 lines, 训到~50K, 2个eval点)
exp_008d_civo_trigger_s3      (完整)
exp_008d_civo_trigger_s4      (完整)
exp_008d_subsample_on_h8      (70 lines, 训到~55K, 3个eval点)
```
没有名为 `exp_008d_trained_embed` 的目录。`exp_008d_subsample_on_h8` 是最接近的候选（且其 35K/45K 数据与 008d_s1 完全一致）。

**其他审计相关文件:**
- `nve_audit.py` — 审计脚本 v1
- `nve_audit_v2.py` — 审计脚本 v2
- `nve_threshold_analysis.py` — 阈值分析脚本
- 无 `nve_audit_detailed.txt` 或其他额外输出文件

---
