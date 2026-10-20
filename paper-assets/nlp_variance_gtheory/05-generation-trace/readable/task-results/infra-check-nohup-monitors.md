# infra check nohup monitors

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_check_nohup_monitors_20260521T153923_result.json`
- **Structured JSON:** [`1e455acf9ba9990c8fb1.json`](../../sessions/1e/1e455acf9ba9990c8fb1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两台服务器状态确认完毕。

## 结果汇总

### westd-32570 — `math_then_new_models.sh`
| 项目 | 值 |
|------|-----|
| PID | 174350 (wrapper) → 174351 (script) |
| PPID | **1 (init)** — nohup 正确 |
| TTY | `?` (已脱离终端) |
| 状态 | **正常，无需修复** |

**MATH 最新进度** (23:57): llama=95%, mistral=94%, qwen=68%, gemma=47%，5 个推理进程并行运行。

---

### westd-15695 — `auto_chain.sh`
| 项目 | 值 |
|------|-----|
| PID | 26843 (`prepare_and_chain.sh`) → 27326 (`auto_chain.sh`) |
| PPID | 26843 → **1 (init)** — nohup 正确 |
| TTY | `?` (已脱离终端) |
| 状态 | **正常，无需修复** |

**推理进度**:
- Yi MMLU: **完成** (86400 行)
- OLMo MMLU: **完成** (50MB)
- OLMo ARC: **完成** (86400 行, 50.9MB)
- OLMo GSM8K: **进行中** (1.9MB, auto_chain 正在跑，GPU 利用率 98%)

`wait_yi_and_chain.log` 里有一个 `httpx.ConnectTimeout` SSL 错误（HF 下载超时），但不影响当前推理 — auto_chain 已经在正常推理 OLMo GSM8K。

---

**结论：两台服务器的 monitor 脚本均以 nohup 方式运行（顶层 PPID=1, TTY=?），SSH 断开不会影响。无需修复。**

---
