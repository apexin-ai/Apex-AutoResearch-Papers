# infra westd32570 start internlm deepseek now

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_westd32570_start_internlm_deepseek_now_20260521T163905_result.json`
- **Structured JSON:** [`d5429f5ba8faa39807b0.json`](../../sessions/d5/d5429f5ba8faa39807b0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All running and producing output. Summary:

### 状态报告

**GPU 利用率** — 4/4 GPU 全负载运行:
| GPU | 任务 | PID | VRAM | Util |
|-----|------|-----|------|------|
| 0 | Qwen MATH | 166536 | 88.5 GB | 97% |
| 1 | **InternLM MMLU** | 177670 | 88.0 GB | 97% |
| 2 | Gemma MATH | 167468 | 88.4 GB | 82% |
| 3 | **DeepSeek MMLU** | 178495 | 87.9 GB | 97% |

**InternLM/DeepSeek 初始进度** — MMLU 推理已开始，正在逐条件处理（200 items/condition，~5s/condition）:
- InternLM: condition 5771 处理中，141/200 correct
- DeepSeek: condition 7202 处理中，107/200 correct

**Chain 脚本已部署** — 每条链按 mmlu → arc → hellaswag → gsm8k → math 顺序自动接力，跳过已完成的 benchmark。

**Qwen/Gemma MATH 进度**:
- Qwen: 50,800 / 57,600 = **88%**
- Gemma: 36,000 / 57,600 = **63%**

**Monitor 已 kill** — `math_then_new_models.sh`（PID 174350/174351）已终止，避免与手动启动冲突。`auto_start_new_models.sh` 不会被触发。

---
