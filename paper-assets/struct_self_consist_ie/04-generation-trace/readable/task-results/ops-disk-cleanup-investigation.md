# ops disk cleanup investigation

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_disk_cleanup_investigation_20260516T094423_result.json`
- **Structured JSON:** [`82402006606a4ecbc80d.json`](../../sessions/82/82402006606a4ecbc80d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

清理方案已保存到 `/root/autodl-tmp/struct_self_consist_ie/output/d112_disk_cleanup/cleanup_plan.md`。

**核心结论**：仅 Tier 1（删 4 个过时/中间目录）即可释放 ~41.3GB，满足 ≥32GB 目标：

| 路径 | 大小 | 原因 |
|------|------|------|
| `qwen3-8b-scierc-merged` | 16G | 旧 v1，已被 v2 取代 |
| `qwen3-8b-scierc-merged-v2-ckpt400` | 16G | v2 中间 ckpt，非最终版 |
| `qwen3-8b-scierc-lora` | 1.7G | 旧 v1 LoRA，已被 lora-v2 取代 |
| `qwen3-4b-conll2003-merged-ckpt4200` | 7.6G | 中间 ckpt，最终版已存在 |

ft_002_v2（`qwen3-8b-scierc-lora-v2` + `qwen3-8b-scierc-merged-v2`）及各 dataset 最新 LoRA 均保留。未执行任何删除操作，等待确认。

---
