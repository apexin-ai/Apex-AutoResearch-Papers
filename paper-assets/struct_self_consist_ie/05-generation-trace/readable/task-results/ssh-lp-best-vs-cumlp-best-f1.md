# ssh lp best vs cumlp best f1

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_lp_best_vs_cumlp_best_f1_20260522T013119_result.json`
- **Structured JSON:** [`ab53226c8b9024aa0c1e.json`](../../sessions/ab/ab53226c8b9024aa0c1e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果清晰：

```
Instances evaluated: 32565

Overall: LP-best mean F1 = 0.7614, cumLP-best mean F1 = 0.7151 (差 +4.62pp)
Disagreement subset (n=3550): LP-best = 0.6429, cumLP-best = 0.2187 (差 +42.42pp)
Wilcoxon p-value (overall): 0.000000
Wilcoxon p-value (disagreement): 0.000000
Winner: mean_LP
```

**Token CV 分层表格：**

| Bucket | n | LP-best F1 | cumLP-best F1 | diff | p |
|--------|---|-----------|--------------|------|---|
| low (CV≤0.05) | 7123 | 0.7554 | 0.7556 | -0.01pp | 0.77 |
| mid (0.05&lt;CV≤0.10) | 3572 | 0.8174 | 0.8159 | +0.15pp | 0.052 |
| high-mid (0.10&lt;CV≤0.20) | 5649 | 0.7883 | 0.7878 | +0.05pp | 0.14 |
| high (CV>0.20) | 16221 | 0.7423 | 0.6499 | **+9.24pp** | 0.0000 |

**关键发现：**

1. **mean_LP 全面优于 cumulative_LP**，+4.62pp（p ≈ 0）
2. 在 rank-1 不同的 3550 个 instances 上，差距达 **+42.42pp**——cumLP 选出的 sample F1 仅 0.22，几乎选错
3. 差异完全集中在 **high CV (>0.20)** 桶：+9.24pp。低/中 CV 桶两者几乎无差别（因为 ranking 本身就一致）
4. 这验证了之前的 token CV 分析：token 长度变异大时 cumulative LP 偏向长序列，选出的 sample 质量显著更差

脚本已保存在服务器 `code/lp_best_vs_cumlp_best.py`，结果在 `output/lp_best_vs_cumlp_best_results.txt`。

---
