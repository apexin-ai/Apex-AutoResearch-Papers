# analyze exp 002 signals llama32 3B d000 gsm8k v2

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_exp_002_signals_llama32_3B_d000_gsm8k_v2_20260516T193756_result.json`
- **Structured JSON:** [`b20620505b415dd0e7eb.json`](../../sessions/b2/b20620505b415dd0e7eb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验已标记为 DONE/success。汇总：

| 文件 | 大小 | 样本数 |
|------|------|--------|
| signal_s1_embedding_gsm8k.json | 717K | 1319 |
| signal_s2_minkpp_gsm8k.json | 266K | 1319 |
| signal_s4_selfcritique_gsm8k.json | 311K | 1319 |
| signals_merged_gsm8k.json | 238K | 1319 |

3 个 signal（s1_embedding, s2_minkpp, s4_selfcritique）全部计算完成，1319 items，无失败或空文件。merged 文件格式正确，含 item_id、benchmark、三个 signal 字段。耗时约 20 分钟，0.33 GPU-hours。

---
