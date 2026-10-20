# verify 4b rsft adapters

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_verify_4b_rsft_adapters_20260521T173642_result.json`
- **Structured JSON:** [`61b2d029bbd1fd6dae6e.json`](../../sessions/61/61b2d029bbd1fd6dae6e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
rsft_output_qwen3_4b_k1 (Method A):  MISSING
rsft_output_qwen3_4b_bf16 (Method B): MISSING
rsft_output (old s42):               MISSING
rsft_output_r2b (old s42 variant):   MISSING
```

**实际存在的 4B RSFT adapter（命名不同）：**

| 路径 | base_model | LoRA config |
|------|-----------|-------------|
| `rsft_output_4b_sft_s44/` | Qwen3-4B | r=64, alpha=128, dropout=0.05, 7 target modules |
| `rsft_output_4b_sft_s44_bf16/` | Qwen3-4B | r=64, alpha=128, dropout=0.05, 7 target modules（同上） |

两个都是 s44 SFT base 的 RSFT。**没有找到任何 s42 base 的 4B RSFT adapter。**

**实验进度：**

| 实验 | PID | 运行时间 | 推理进度 |
|------|-----|---------|---------|
| s43 with-evi | 115868 | 1h41m | 65% (161/247) |
| s43 no-evi | 115948 | 1h41m | 72% (179/247) |
| s44 with-evi | 116928 | 1h31m | 66% (162/247) |
| s44 no-evi | 121951 | 3m35s | 2% (6/247)，刚启动 |

前三个预计再 40-60 分钟完成，s44 no-evi 刚开始，预计约 2 小时。

---
