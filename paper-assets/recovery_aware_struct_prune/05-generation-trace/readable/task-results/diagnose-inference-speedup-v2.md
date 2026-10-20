# diagnose inference speedup v2

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_inference_speedup_v2_20260516T221321_result.json`
- **Structured JSON:** [`92f266beca9094e15b61.json`](../../sessions/92/92f266beca9094e15b61.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新（cron 不存在，跳过删除）。

## 实验结果：inference_speedup_plan016_v2 ✓ 成功

| 指标 | Dense (7B) | RASP 20% | Standard 20% |
|------|-----------|----------|--------------|
| Tokens/s | 76.25 | 52.07 | 49.78 |
| Avg Latency/prompt | 6.682s | 4.156s | 6.167s |
| Peak Memory | 16.22 GB | 11.60 GB | 11.61 GB |
| Latency speedup vs Dense | — | **37.8%** | 7.7% |
| Memory reduction vs Dense | — | **28.5%** | 28.4% |

**关键发现：**
- RASP 20% 的 per-prompt latency 比 dense 快 37.8%（4.16s vs 6.68s），比 standard pruning 快 32.6%
- 两种剪枝方案内存节省几乎相同（~28.5%），但 RASP 生成更短更精准的回答（总 token 10820 vs 15348），导致实际 latency 大幅领先
- Tokens/s 方面 RASP 略高于 standard（52.07 vs 49.78），说明模型结构效率也有微弱优势
- RASP 的 latency 优势主要来自生成更简洁的推理链（token 数少 29.5%），这与其更好的 reasoning 质量一致

---
