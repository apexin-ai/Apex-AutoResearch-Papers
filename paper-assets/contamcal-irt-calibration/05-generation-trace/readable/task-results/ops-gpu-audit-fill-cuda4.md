# ops gpu audit fill cuda4

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu_audit_fill_cuda4_20260516T193737_result.json`
- **Structured JSON:** [`c17959ddffab32dffeef.json`](../../sessions/c1/c17959ddffab32dffeef.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## GPU 审计报告

| GPU | 状态 | PID | 实验 | Util | 显存 |
|-----|------|-----|------|------|------|
| cuda:0 | RUNNING | 825638 | eval_llama32_3B_d005_s42 | 83% | 8072/24564 MiB |
| cuda:1 | RUNNING | 830115 | signals_llama32_3B_d000_mmlu | 62% | 7077/24564 MiB |
| cuda:2 | **FREE** | — | ⚠️ PID 839655 已死亡 | 0% | 0 MiB |
| cuda:3 | RUNNING | 822390 | eval_llama32_3B_d025_s42 | 86% | 8313/24564 MiB |
| cuda:4 | **STARTED** | 842929 | signals_llama32_3B_d005_mmlu | — | loading... |
| cuda:5 | RUNNING | 831033 | eval_llama32_3B_d100_s42 | 81% | 8304/24564 MiB |

### cuda:4 已启动
**Llama-3.2-3B_d005_s42 signals (mmlu, all signals)** — 进度：S1 embedding encoding 中 (~22 it/s, 12500 batches)

### 任务选择逻辑
C007 优先项全部完成（0.5B s123 ✓, 1.5B s123 ✓, d100_a32_s123 ✓），转入 Llama-3.2-3B 系列 signals 计算。d000 mmlu 正在 cuda:1 跑，选了 d005 mmlu 作为下一个。

### 异常
- **cuda:2 空闲**：PID 839655（registry 中的 signals_llama32_3B_d000_gsm8k_v2）已死亡，但 d000 gsm8k signals 文件完整（s1/s2/s4/merged 全部存在），不影响结果。该 registry 条目不在 RUNNING 列表中。
- cuda:2 可用于下一个任务分配。

---
