# ops read gen length results

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_read_gen_length_results_20260517T055927_result.json`
- **Structured JSON:** [`f83f673a843408f1af5c.json`](../../sessions/f8/f83f673a843408f1af5c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## gen_length_ablation_001 实验结果

**配置**: Pythia-1.4B, nucleus sampling (top_p=0.95, temp=1.0), 1000 samples/depth, 5-fold CV RF (n_estimators=200), seed=42

---

### 各 Generation Length 的 4-Class Accuracy

| Length | 4-Class Acc | 95% CI | d1v2 AUC | Fold Accs |
|--------|------------|--------|-----------|-----------|
| 128 | 0.6835 | [0.6765, 0.6905] | 0.7543 | 0.685, 0.6963, 0.6763, 0.6875, 0.6725 |
| 256 | 0.7380 | [0.7248, 0.7512] | 0.8198 | 0.715, 0.7312, 0.7475, 0.7325, 0.7638 |
| 512 | 0.7782 | [0.768, 0.7885] | 0.8683 | 0.7825, 0.7963, 0.7837, 0.76, 0.7688 |

---

### Cross-Length Spread

- **Max - Min**: 0.7782 - 0.6835 = **9.47 pp**
- **结论**: Spread 9.47pp > 5pp threshold，generation length 显著影响 depth detection accuracy

### 与 Baseline (256-token) 比较

- 128 vs 256: -5.45 pp (CI 不重叠)
- 512 vs 256: +4.02 pp (CI 不重叠)
- 更长的生成文本提供更多统计特征信号，accuracy 单调递增

### 运行时间

33.1 分钟，exit_code=0

---
