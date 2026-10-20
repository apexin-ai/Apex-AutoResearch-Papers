# ssh verify v3 output and disk

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_verify_v3_output_and_disk_20260521T231029_result.json`
- **Structured JSON:** [`de6c15265d95486fb1f5.json`](../../sessions/de/de6c15265d95486fb1f5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

日志显示推理分两个阶段：
1. **vLLM 生成阶段**：301184/301184 completions — 已完成（耗时 ~1h44m）
2. **后处理/写出阶段**：12241/37648 prompts (32.5%)，ETA ~12 分钟

samples.jsonl 在后处理全部完成后才写入。当前进程仍在运行，预计 **约 12-15 分钟后完成**。

---

## 当前状态汇总

| 项目 | 状态 |
|------|------|
| **mf4v2_s42_v3** | 运行中 — vLLM 生成完毕，后处理 32.5%，预计 ~12 min 完成 |
| **samples.jsonl** | 尚未生成（后处理完毕后写入） |
| **MV recompute** | 待 samples.jsonl 生成后执行 |
| **磁盘** | `/root/autodl-tmp` 250G 用了 226G，剩余 **25G (91%)** |
| **GPU 进程** | VLLM::EngineCore (PID 76862)，占用 30562 MiB — 为 s42_v3 推理服务 |

需要等推理完成后再运行 recompute。要我过 15 分钟后再检查一次吗？

---
