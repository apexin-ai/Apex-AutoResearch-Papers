# analysis ckpt10 eval result

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_ckpt10-eval-result_20260514T191250_result.json`
- **Structured JSON:** [`11e0fb961e0e68bcc637.json`](../../sessions/11/11e0fb961e0e68bcc637.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Cron 已不存在（可能已被其他 worker 清除或未在本 session 创建）。

## 对比简表

| 指标 | SFT baseline | ckpt-10 | ckpt-50 | 趋势 |
|------|-------------|---------|---------|------|
| **rel_f1** | **0.4057** | 0.0030 | 0.1563 | ckpt-10 最差，ckpt-50 稍恢复但仍远低于 SFT |
| rel_precision | — | 0.0031 | — | — |
| rel_recall | — | 0.0028 | — | — |
| **evi_f1** | **0.7979** | 0.7200 | 0.5643 | ckpt-10 > ckpt-50，两者都低于 SFT |
| evi_precision | — | 0.6429 | — | — |
| evi_recall | — | 0.8182 | — | — |
| **edcr** | **0.7118** | 0.9983 | 0.8858 | GRPO 越早越"保守"（几乎全引 distractor） |
| n_parseable | — | 984/985 | — | 格式正常 |
| n_truncated | — | 24 | — | — |

**结论**: ckpt-10 的 rel_f1=0.003 是灾难性的（仅 34 TP / 10839 predictions），比 ckpt-50 还差一个数量级。edcr=0.998 说明模型几乎把所有 citation 都指向 distractor。GRPO (ced_kl001_r4) 从第 10 步起就严重损害 relation 抽取能力，随训练推进 relation 略有恢复但远未达 SFT 水平。该配置确认 negative。

---
