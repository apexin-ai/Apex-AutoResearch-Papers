# infra post restart gpu check

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_post-restart-gpu-check_20260523T034405_result.json`
- **Structured JSON:** [`ce4a62be2024e3cc5643.json`](../../sessions/ce/ce4a62be2024e3cc5643.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部信息到手。汇总如下：

---

## 实验状态汇总

### westd-16639

| GPU | 实验 | 状态 | 进度 | ETA |
|-----|------|------|------|-----|
| 0 | Qwen2.5-14B PW seed123 (rerun) | **运行中** | 399/600 | — |
| 1 | LLaMA-8B PW seed123 | **运行中** | 361/600 | ~5.1h |
| 2 | — | **空闲** | — | — |
| 3 | Qwen2.5-14B PW seed456 (rerun) | **运行中** | 418/600 | ~3.5h |

**旧的部分结果**（重启前保存，现在正在被重跑覆盖）：

| 实验 | n | SC% | SICA% | Δ(SICA-SC) |
|------|---|-----|-------|------------|
| qwen25_pw_seed456 | 415 | 74.22 | 73.25 | -0.96 |
| qwen25_pw_seed123 | 397 | 74.06 | 72.54 | -1.51 |
| llama8b_pw_seed123 | 359 | 72.42 | 63.79 | -8.64 |

### westd-14391

| GPU | 实验 | 状态 | 进度 | ETA |
|-----|------|------|------|-----|
| 0 | LLaMA-8B PW seed42 | **运行中** | 498/600 | ~1.6h |

旧部分结果：SC=72.93%, SICA=67.47%, Δ=-5.45% (n=495)

---

### 问题

1. **Qwen PW seed789 失败** — vLLM 启动失败（Mistral 端口 8005 RuntimeError），导致实验脚本 Connection error。`qwen25_pw_seed789/` 目录为空。
2. **GPU 2 空闲** — 可以用来跑 seed789 或其他实验。

### 初步趋势（基于部分数据，仅供参考）

- Qwen2.5-14B 在 PW 上 Δ(SICA-SC) 约 -1% 到 -1.5%，SICA 略低于 SC
- LLaMA-8B 在 PW 上 SICA 下降更大（Δ 约 -5% ~ -9%），表明 LLaMA 的约束提取质量更弱

等重跑完成后会有完整 n=600 的结果。需要我在 GPU 2 上启动 seed789 吗？

---
