# diagnose eval k07 and merge

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval_k07_and_merge_20260517T102501_result.json`
- **Structured JSON:** [`0f948b7d29e7f5a0ec82.json`](../../sessions/0f/0f948b7d29e7f5a0ec82.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总报告

### 1. eval_k07_zero_mask — 已完成

| 指标 | 值 |
|------|------|
| 状态 | **正常完成** (17:44 ~ 18:23，约 39 分钟) |
| Overall SR | **0/500 (0.0%)** |
| 95% Wilson CI | [0.0%, 0.76%] |
| 每个 Task SR | 全部 0% (10 个 task × 50 episodes，均 FAIL，mean_steps=280 即全部 timeout) |

结果文件保存为 `eval_results/libero_libero_object.json`（注意：不是 `eval_k07_zero_mask.json`，脚本用了默认命名）。

**结论**：zero_mask 在 k=0.7 下完全丧失执行能力，模型 30% 权重直接置零导致彻底崩溃。

---

### 2. eval_merge_k05 — 仍在运行中

| 指标 | 值 |
|------|------|
| 状态 | **运行中**（tmux session `eval_merge_k05` 存活，python 进程 PID 340300） |
| 当前进度 | Task 8/10, Episode 33/50 (已完成 ~7.6 个 task = ~76%) |
| 当前 SR | 所有已完成 task 均 0%（全部 FAIL） |
| 预计剩余 | ~2 个 task × 50 ep × ~5s/ep ≈ 8-10 分钟完成 |

**趋势**：和 zero_mask 一样，merge (alpha=1.0, k=0.5) 也是全 0%，剪枝后模型完全无法执行任务。

---

### 3. GPU 状态

| GPU | 型号 | 显存使用 | 利用率 | 状态 |
|-----|------|---------|--------|------|
| GPU 0 | RTX PRO 6000 Black (98GB) | 3266 MiB | 1% | eval_merge_k05 占用 |
| GPU 1 | RTX PRO 6000 Black (98GB) | 1 MiB | 0% | **完全空闲** |

**GPU 1 可用**，可以立即启动 P0 分析任务。

---
