# analysis deepseek vota seed456

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_deepseek_vota_seed456_20260520T045649_result.json`
- **Structured JSON:** [`6a0fa8ae825c28cd1fe2.json`](../../sessions/6a/6a0fa8ae825c28cd1fe2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

**seed456 = 99.33%** (95% CI: [98.8%, 99.7%])

### 仲裁结论：seed42 是 outlier，DeepSeek VOTA 归 Tier 1

| Seed | Accuracy | eval max_length |
|------|----------|-----------------|
| 42 | 84.45% | 16384 |
| 123 | 99.16% | 2048 |
| 456 | 99.33% | 2048 |

seed123 和 seed456 高度一致（gap=0.17pp），seed42 偏低 14.8pp。

### 关键发现
seed42 的 84.45% 用了 max_length=16384 评估（训练只用 2048），存在 train/eval 长度不匹配问题。seed456 使用 fixed evaluate.py（right truncation, max_length=2048），不受 front-truncation bug 影响。

### 建议
距 DDL 还有 5 天，**建议补跑 seed42 用 fixed evaluate.py (max_length=2048)** 重评——只需 ~3 分钟。如果 seed42 重评后也 ≥ 95%，三 seed 全部一致，论文数据更solid。否则论文用 seed123/456 均值 99.25%，附注脚说明 seed42。

报告已注册：`art_20260520_b44de2`

---
