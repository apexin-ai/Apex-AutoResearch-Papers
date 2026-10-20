# code diversity metrics

**The Embedding Alignment Gap: Why Diversity-Based Data Selection Accelerates Model Collapse in Iterative Self-Training** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_diversity_metrics_20260513T110418_result.json`
- **Structured JSON:** [`66872d233ea89f5e300f.json`](../../sessions/66/66872d233ea89f5e300f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

运行完成。CSV 已保存。以下是结果和关键发现：

## 结果表

| method | gen | self_bleu | distinct_1 | distinct_2 | distinct_3 | ttr |
|--------|-----|-----------|-----------|-----------|-----------|------|
| **rgds** | 0 | 0.0125 | 0.0688 | 0.3079 | 0.5281 | 0.0688 |
| rgds | 1 | 0.0122 | 0.0318 | 0.1329 | 0.2310 | 0.0318 |
| rgds | 2 | 0.0117 | 0.0225 | 0.0907 | 0.1576 | 0.0225 |
| rgds | 3 | 0.0097 | 0.0205 | 0.0784 | 0.1356 | 0.0205 |
| rgds | 4 | 0.0093 | 0.0192 | 0.0678 | 0.1131 | 0.0192 |
| rgds | 5 | 0.0085 | 0.0167 | 0.0585 | 0.0939 | 0.0167 |
| rgds | 6 | 0.0096 | 0.0148 | 0.0506 | 0.0802 | 0.0148 |
| rgds | 7 | 0.0107 | 0.0154 | 0.0527 | 0.0791 | 0.0154 |
| **external_only** | 0 | 0.0125 | 0.0688 | 0.3079 | 0.5281 | 0.0688 |
| external_only | 1 | 0.0110 | 0.0338 | 0.1339 | 0.2272 | 0.0338 |
| external_only | 2 | 0.0102 | 0.0243 | 0.0938 | 0.1582 | 0.0243 |
| external_only | 3 | 0.0086 | 0.0212 | 0.0796 | 0.1341 | 0.0212 |
| external_only | 4 | 0.0092 | 0.0186 | 0.0685 | 0.1145 | 0.0186 |
| external_only | 5 | 0.0086 | 0.0176 | 0.0677 | 0.1129 | 0.0176 |
| external_only | 6 | 0.0078 | 0.0166 | 0.0665 | 0.1127 | 0.0166 |
| external_only | 7 | 0.0078 | 0.0166 | 0.0669 | 0.1151 | 0.0166 |
| **uncurated** | 0 | 0.0125 | 0.0688 | 0.3079 | 0.5281 | 0.0688 |
| uncurated | 1 | 0.0112 | 0.0318 | 0.1300 | 0.2205 | 0.0318 |
| uncurated | 2 | 0.0098 | 0.0225 | 0.0873 | 0.1489 | 0.0225 |
| uncurated | 3 | 0.0093 | 0.0187 | 0.0715 | 0.1221 | 0.0187 |
| uncurated | 4 | 0.0089 | 0.0174 | 0.0661 | 0.1098 | 0.0174 |
| uncurated | 5 | 0.0088 | 0.0170 | 0.0647 | 0.1055 | 0.0170 |
| uncurated | 6 | 0.0085 | 0.0161 | 0.0638 | 0.1016 | 0.0161 |
| uncurated | 7 | 0.0077 | 0.0154 | 0.0616 | 0.1000 | 0.0154 |

## 关键发现

1. **所有方法多样性均随代数递减**——gen_0 相同（同一个 generator），之后 distinct-n 和 TTR 单调下降，符合 model collapse 的多样性丧失预期。

2. **三方法差异非常小**：
   - gen_7 时 distinct_3：rgds=0.079, external_only=0.115, uncurated=0.100
   - **external_only 在后期维持了最高多样性**（distinct-2/3 在 gen_5-7 停止下降趋于稳定）
   - rgds 在 gen_5 后多样性反而略低于 uncurated

3. **Self-BLEU 整体很低**（<0.013），说明生成文本之间重复度不高；三方法间差异微弱。

4. **external_only 多样性保持最好**——gen_6-7 的 distinct-2/3 稳定在 ~0.067/0.113，而 rgds 降到 ~0.051/0.080。这暗示外部参考信号对维持多样性有一定帮助。

脚本位于 `/root/div_cal_verify/compute_diversity_metrics.py`，CSV 保存在 `/root/autodl-tmp/div_cal_verify/diversity_metrics_seed42.csv`。

---
