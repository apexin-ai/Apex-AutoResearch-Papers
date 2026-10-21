# ops fp16 status check

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_fp16-status-check_20260525T060342_result.json`
- **Structured JSON:** [`9f11097025fb96a20b97.json`](../../sessions/9f/9f11097025fb96a20b97.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验状态：已完成（部分失败）

进程已结束，结果文件于 `2026-05-25 08:03` 生成。

### 逐模型结果

| 模型 | 参数 | Benchmark | AWQ | FP16 | Delta (pp) | 备注 |
|------|------|-----------|-----|------|-----------|------|
| **Qwen2.5-14B-Instruct** | 14B | MMLU | 0.71 | — | — | FP16 下载失败 (4/13 files) |
| | | ARC | 0.84 | — | — | |
| **Qwen2.5-32B-Instruct** | 32B | MMLU | 0.74 | 0.78 | **+4.0** | ✓ 对比完成 |
| | | ARC | 0.93 | 0.93 | 0.0 | |
| **Llama-3.1-8B-Instruct** | 8B | MMLU | 0.52 | 0.57 | **+5.0** | ✓ 对比完成 |
| | | ARC | 0.78 | 0.73 | **-5.0** | AWQ 反超 FP16 |
| **Llama-3.1-70B-Instruct** | 70B | MMLU | 0.74 | skipped | — | FP16 需 ~140GB VRAM，超出单卡 98GB |
| | | ARC | 0.89 | skipped | — | |
| **Mistral-Large-2407** | 123B | MMLU | — | — | — | AWQ 下载中断 (connection reset) |
| | | ARC | — | — | — | |

### 总结

- **成功对比**: 2 个模型 (Qwen2.5-32B, Llama-3.1-8B)
- **AWQ-only**: 2 个模型 (Qwen2.5-14B FP16下载失败, Llama-3.1-70B VRAM不足)
- **完全失败**: 1 个模型 (Mistral-Large 下载中断)
- **MMLU 平均 AWQ 退化**: 3.5pp, 最大 5.0pp
- **结论**: AWQ 量化在 MMLU 上导致 >2pp 退化；ARC 上表现不一致 (Llama-8B 上 AWQ 反而更好)

### 问题

1. **Qwen2.5-14B FP16** — HF 下载部分文件失败，需重试
2. **Mistral-Large AWQ** — 大文件下载中断 (`peer closed connection`)，建议改用 ModelScope 或断点续传
3. **Llama-3.1-70B FP16** — 单卡放不下，需多卡或跳过

---
