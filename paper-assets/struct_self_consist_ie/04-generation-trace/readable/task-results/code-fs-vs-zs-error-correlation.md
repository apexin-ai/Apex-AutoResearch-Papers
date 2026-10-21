# code fs vs zs error correlation

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fs-vs-zs-error-correlation_20260520T013711_result.json`
- **Structured JSON:** [`1c18bae718b391f1fd31.json`](../../sessions/1c/1c18bae718b391f1fd31.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果总结

**"Demonstration-induced error correlation" 假说未被数据支持。**

### SciERC (551 instances)

| Metric | FS | ZS | p-value |
|--------|----|----|---------|
| Mean pairwise error Jaccard | 0.454 ± 0.301 | 0.452 ± 0.296 | 0.844 (n.s.) |
| Mean entity entropy | 0.483 ± 0.261 | 0.485 ± 0.257 | 0.807 (n.s.) |

FS 和 ZS 的 error overlap 几乎完全相同，effect size 极小 (r=0.008)。

### CoNLL (3453 instances)

| Metric | FS | ZS | p-value |
|--------|----|----|---------|
| Mean pairwise error Jaccard | 0.103 ± 0.233 | 0.104 ± 0.238 | 0.638 (n.s.) |
| Mean entity entropy | 0.209 ± 0.286 | 0.184 ± 0.281 | **5.0e-10** |

Jaccard 同样无显著差异。**entity entropy 显著但方向与假说相反**：FS entropy (0.209) > ZS entropy (0.184)，意味着 FS 的 entity 预测反而**更分散**而非更集中。不过 effect size 小 (r=0.106)。

### 关键发现

1. **Error overlap（核心指标）在两个数据集上 FS≈ZS，假说不成立**——demonstrations 并未导致 8 个 sample 犯更相似的 entity 错误
2. CoNLL 中 2380/3453 instances 的所有 pair 都无 error（median Jaccard=0），说明 CoNLL 上模型在大部分 instance 上表现一致良好
3. SciERC 的高 Jaccard (~0.45) 和高 entropy (~0.48) 反映的是任务本身的难度（entity boundary/type ambiguity），而非 FS 特有的问题

SciERC FS construction 失效可能需要从其他角度解释（如 entity recall 下降导致 construction pool 缺乏多样性，而非 error 本身的 correlation）。

---
