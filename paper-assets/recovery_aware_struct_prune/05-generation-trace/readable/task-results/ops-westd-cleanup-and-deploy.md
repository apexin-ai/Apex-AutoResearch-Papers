# ops westd cleanup and deploy

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westd_cleanup_and_deploy_20260516T202648_result.json`
- **Structured JSON:** [`4c74a701b5c9aed96b8f.json`](../../sessions/4c/4c74a701b5c9aed96b8f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

cuda:0 已进入训练状态（85% util, 51GB 显存）。

## 完成报告

**已 Kill 进程：**
- PID 42301 (cuda:0, eval_grpo_rasp_rlvr_20) — 已不存在（可能先前已结束）
- PID 42096 (cuda:1, N=200 eval) — 已 kill
- PID 34234 (cuda:2, eval_grpo_rasp_25) — 已 kill

**保留进程确认正常：**
- cuda:1: PID 42590 (N=1319 eval) ✓
- cuda:2: PID 33921 (pass@k eval) ✓
- cuda:3: Phase B SFT 61% (1146/1870) ✓

**cuda:0 新部署：**
- tmux session `alpha_phaseB_cuda0`：α=2.0 SFT → eval → α=1.0 SFT → eval（链式执行）
- 当前状态：α=2.0 SFT 训练中（85% GPU util, 51GB 显存）

**α ablation 剩余状态：**
| α | 状态 |
|---|------|
| 0.0 | ✅ 完成 |
| 0.3 | SFT 完成，eval pending（cuda:3 Phase B 会处理） |
| 0.5 | cuda:3 Phase B 正在 SFT |
| 0.7 | 待 cuda:3 接力 |
| 1.0 | cuda:0 队列中（α=2.0 之后） |
| 2.0 | cuda:0 正在 SFT |

未处理 α：0.7（将由 cuda:3 Phase B 顺序覆盖）。所有 6 个 α 均有 GPU 在处理或已完成。

---
