# research asymmetric diagnostic

**When Debiasing Hurts: An Exact Bias Identity for LLM-Annotated Treatment Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_asymmetric-diagnostic_20260523T071457_result.json`
- **Structured JSON:** [`93430791c96084d513f0.json`](../../sessions/93/93430791c96084d513f0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

**核心发现：对 K_Z=2（二值标签），非对称诊断与对称诊断代数等价，无法改善。**

### 证明

对一般非对称混淆矩阵 (FPR_s ≠ FNR_s)，CATE bias 的关键量是：

```
B_s[1,1] - B_s[1,0] = -2·δ_s / (1 - 2π̄)
```

其中 δ_s = π_s - π̄，π_s = (FPR_s + FNR_s)/2。FPR 和 FNR 的不对称性在行差中完全抵消。因此：

```
|B_s[1,1] - B_s[1,0]| / (FPR_s + FNR_s) ≡ |δ_s| / ((1-2π̄)·π_s)  （恒等式）
```

### AUC 对比

| 条件 | 对称 | 旧非对称 \|B[0,1]\| | 新比率 | 新原始值 |
|------|------|---------------------|--------|----------|
| 全部子组 (n=56) | 0.6571 | 0.6041 | 0.6571 | 0.6816 |
| τ_s > 0 (n=40) | **1.0000** | 0.8857 | **1.0000** | **1.0000** |

### AUC=0.63 的真正原因

不是对称假设导致的。τ_s=0 的子组（两个 bias 都≈0）的 ground truth 完全由 MC 噪声决定，拉低了整体 AUC。排除这些子组后，所有诊断都达到 AUC=1.0。

### 结论

- 对称假设 A2 (FPR=FNR) **对 Proposition 3 的诊断不是限制**——非对称公式恒等于对称公式
- 旧 exp028 用 |B_s[0,1]|（仅 FNR 偏差）是错误的，但正确的非对称公式也只能回到对称结果
- 若要在论文中表述：Remark 1 的一般形式虽然对逐项 bias 更精确，但对 CATE 诊断而言，信息量与对称版完全相同

输出文件：`results/exp_asym_diag_v2.csv`、`results/exp_asym_diag_v2_summary.csv`、`results/exp_asym_diag_v2_analysis.md`

---
