# infra check server status

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_check_server_status_20260516T034913_result.json`
- **Structured JSON:** [`aa459aea5830f06c8f35.json`](../../sessions/aa/aa459aea5830f06c8f35.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

save_project_file 不支持该文件名，已写入 artifacts 目录。

---

## 汇总

### PID 状态
- **PID 194814** (lm_eval_teal_30pct, cuda:0): **已结束**，结果已收取
- **PID 195242** (lm_eval_mistral_kl_50pct, cuda:1): **运行中** 53 分钟，GSM8K generate_until **71%** (941/1319)，预计 **~17min 后完成**

### GPU 可用性
| GPU | VRAM | 利用率 | 状态 |
|-----|------|--------|------|
| cuda:0 | 18.3/97.9 GB | 0% | **立即可用** |
| cuda:1 | 62.1/97.9 GB | 95% | ~17min 后释放 |

### 已完成 Eval 对比（vs Mistral dense baseline）

| 方法 | Sparsity | ARC-c | WinoGrande | MMLU | GSM8K |
|------|----------|-------|------------|------|-------|
| **Mistral dense** | 0% | **0.6024** | **0.7869** | **0.6244** | **0.3654** |
| Vanilla TEAL | 30% | 0.3933 | 0.6559 | 0.3598 | 0.0925 |
| KL distill (kl_30pct) | 30% | 0.3575 | 0.6756 | 0.2874 | 0.0781 |
| Vanilla TEAL | 50% | 0.2491 | 0.5556 | 0.2856 | 0.0190 |
| **Mistral KL 50%** | 50% | *running...* | — | — | — |

Mistral KL 50% 的结果是本次最关键的数据点，大约 17 分钟后可收取。文件已保存至 `artifacts/server_status_check.md`。

---
