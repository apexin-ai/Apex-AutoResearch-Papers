# ops status check westd

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_status_check_westd_20260518T150934_result.json`
- **Structured JSON:** [`bd0a2c0a80b5d54436ec.json`](../../sessions/bd/bd0a2c0a80b5d54436ec.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## nvidia-smi 摘要
| GPU | 状态 | PID | 显存 | 利用率 | 温度 |
|-----|------|-----|------|--------|------|
| GPU0 | 刚启动(加载模型中) | 11457 | 0MiB | 0% | 31°C |
| GPU1 | 运行中 | 2261 | 30078MiB | 99% | 83°C |
| GPU2 | 运行中 | 2529 | 30078MiB | 96% | 75°C |
| GPU3 | 运行中 | 4229 | 17658MiB | 91% | 58°C |

## 各实验进度

**cuda:0 — E2 CKA-only Extended GRPO (grpo_cka_only_20_extended_300)**
- 状态: **刚启动** (23:10:10)，正在加载模型，尚未开始训练
- 从 checkpoint-100 恢复，目标 300 steps
- tmux session: `grpo_cka_only_20_extended_300` 未在 tmux ls 中出现（进程通过新 session 运行，PID 11457）

**cuda:1 — MATH-500 Standard GRPO Fair**
- 状态: **运行中** — **61/500** (12.2%)
- Acc@50: **0.3800**
- 已运行 ~2h10m，预估剩余 ~14h
- 模型: `grpo_stage2_standard_20_fair`

**cuda:2 — MATH-500 SFT CKA-only 20**
- 状态: **运行中** — **96/500** (19.2%)
- Acc@50: **0.3200**
- 已运行 ~2h09m，预估剩余 ~8-9h
- 模型: `sft_cka_only_20`

**cuda:3 — MATH-500 Dense Unpruned**
- 状态: **运行中** — **189/500** (37.8%)
- Acc@150: **0.7267**
- 已运行 ~1h49m，预估剩余 ~3-4h
- 模型: `DeepSeek-R1-Distill-Qwen-7B` (原始未剪枝)

## 磁盘
| 总容量 | 已用 | 可用 | 使用率 |
|--------|------|------|--------|
| 619G | 497G | 123G | 81% |

## 注意事项
- GPU1 温度 83°C 较高（满功率 600W），持续关注
- Dense unpruned 模型 Acc 0.7267 远高于两个剪枝模型（0.32-0.38），符合预期——剪枝模型的 GRPO 恢复效果需要看最终数字
- cuda:0 的 E2 训练刚提交，模型加载中，预计几分钟后开始出 step

---
