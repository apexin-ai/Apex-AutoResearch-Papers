# analysis qwen14b gsm8k s123 check

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_qwen14b_gsm8k_s123_check_20260523T150847_result.json`
- **Structured JSON:** [`0a94e327af38ec386f97.json`](../../sessions/0a/0a94e327af38ec386f97.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果文件不在 westd-34887 上（实验跑在 41718 且该服务器当前不可达）。但 checkpoint 记录里已有 metrics。让我再确认 s42/s456 的 GSM8K 样本数作为对比。

## 报告

### qwen14b_kl30_s123_gsm8k

| 项目 | 值 |
|------|-----|
| **结果文件** | `results/benchmark/qwen14b_kl30_s123_gsm8k/results.json`（仅存在于 westd-41718，当前不可达） |
| **westd-34887 上** | 无此文件，也无日志 |
| **conclusion** | killed |
| **checkpoint 记录的 metrics** | exact_match=0.3442, strict=0.3434, actual_sparsity=0.297 |
| **评估样本数** | **无法直接确认**（results.json 在 41718 上，无法读取 sample_len 字段） |
| **运行服务器** | westd-41718 cuda:1 |
| **运行时间** | 2026-05-19 18:23 → 20:52（约 2.5h） |

### 对比：s42 和 s456

| seed | sample_len | exact_match | 运行时间 | 服务器 |
|------|-----------|-------------|---------|--------|
| s42 | **1319** (完整) | 0.3548 | 2026-05-22 | westd-34887 |
| s456 | **1319** (完整) | 0.2608 | 2026-05-20 | westd-34887 |

### 结论

1. **s123 的 GSM8K 评估大概率是完整的**：checkpoint 记录了 metrics（exact_match=0.3442），说明评估脚本正常完成并写出了 results.json。"killed" 可能是后续状态管理标记，不是评估中途中断。
2. **但无法 100% 确认 sample_len=1319**，因为 results.json 在 westd-41718 上，该服务器当前不在可用列表中。
3. **如需确认**：要么将 westd-41718 加回 SSH 可用列表，要么从 41718 手动将 `results/benchmark/qwen14b_kl30_s123_gsm8k/results.json` 同步到 34887。

---
