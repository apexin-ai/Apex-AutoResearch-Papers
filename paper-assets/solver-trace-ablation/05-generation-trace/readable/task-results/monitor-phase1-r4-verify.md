# monitor phase1 r4 verify

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_phase1-r4-verify_20260513T203157_result.json`
- **Structured JSON:** [`d2a971afba7db970a66e.json`](../../sessions/d2/d2a971afba7db970a66e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Phase 1 r4 训练状态报告

### 进程状态
| 实验 | PID | 状态 | 运行时间 |
|------|-----|------|---------|
| exec-only-r4 | 70716 (子进程 70721) | **存活** | 3min 45s |
| exec-sta-r4 | 70797 (子进程 70802) | **存活** | 3min 43s |

### GPU 隔离
| GPU | 型号 | 进程 PID | 显存占用 | GPU 利用率 |
|-----|------|----------|---------|-----------|
| cuda:0 | RTX PRO 6000 Black (98GB) | 70721 (exec-only) | **80,676 MiB / 97,887 MiB (82%)** | 91% |
| cuda:1 | RTX PRO 6000 Black (98GB) | 70802 (exec-sta) | **80,676 MiB / 97,887 MiB (82%)** | 89% |

GPU 隔离正常，各占一块卡，无交叉。

### 训练进度
两个实验均已完成 **24/100 steps**（24%），运行约 3 分 46 秒，平均 ~9.4s/step。

**exec-only reward 趋势**: 0.25 → 0.00 → 0.50 → 0.125 → ... → 1.00 (step 23) → 0.50 (step 24)
**exec-sta reward 趋势**: 0.25 → 0.00 → 0.50 → 0.125 → ... → 1.00 (step 23) → 0.3125 (step 24)

parse_rate 始终 1.000，模型输出格式没问题。两个实验在 step 24 开始出现 isr 差异（exec-only: 0.125, exec-sta: 0.125），reward 也开始分化（0.50 vs 0.3125），符合预期——两个 reward 函数开始产生不同信号。

### 输出文件
reward_log.jsonl 已生成，位于 `/root/autodl-tmp/outputs/grpo_exec_only/` 和 `/root/autodl-tmp/outputs/grpo_exec_sta/`（注意路径不含 `phase1_` 和 `_r4`）。

### 异常
- 无报错、无 OOM、无 CUDA error
- 唯一 warning 是 vLLM 版本兼容性提示（0.18.1 vs 支持的 0.11-0.17），不影响训练
- 预计总训练时间约 15-16 分钟（100 steps × ~9.4s/step）

---
