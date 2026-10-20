# exp mvp 001 check

**Why Calibration Fails: A Taxonomy of Failure Modes in Dialect-Aware LLM User Simulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_mvp-001-check_20260512T124453_result.json`
- **Structured JSON:** [`bc6f091b297955cc1afc.json`](../../sessions/bc/bc6f091b297955cc1afc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇报如下：

## mvp-001 实验状态：失败（部分完成）

### 1. 最终状态
**Phase 1（Uncalibrated baseline）在 task 10 处崩溃。Phase 2（aave_target calibrated）未执行。**

实验完成了 task 0-10（共 11 个），计划跑 0-20（共 20 个）。在启动 task 10 的 user simulation 时，vLLM 服务端连接断开，抛出 `openai.APIConnectionError: Connection error`，进程直接退出。

### 2. 崩溃原因
vLLM 服务在实验运行过程中挂掉（可能被其他进程抢占 GPU 内存——当前服务器上有 2 个 alfworld python 进程各占 100% CPU，另有 2 个 `collect_trajectories.py` 在跑，加上 vLLM 共 3 个 GPU 用户）。实验代码没有 connection retry 逻辑，一次连接失败即整体崩溃。

### 3. Trace 数据
- 大 JSON（`range_0-20`）: 11 条 trace（task 0-10），作为 checkpoint 已保存
- `mvp_results.json`: 包含早期 quick_test 的结果（仅 2-3 traces per condition），非最终实验结果
- Reward 分布（11 traces）: task 0=1.0, 1=0.0, 2=0.0, 3=1.0, 4=0.0, 5=0.0, 6=1.0, 7=0.0, 8=0.0, 9=0.0, 10=0.0 → **3/11 成功（27.3%）**

### 4. mvp_results.json 指标（早期小规模测试，非最终结果）
| Condition | Traces | Task Completion | Mean Question Rate | Mean Politeness Rate |
|-----------|--------|----------------|--------------------|---------------------|
| uncalibrated_baseline | 2 | 33.3% | 0.65 | 0.45 |
| aave_target | 3 | 0.0% | 0.74 | 0.66 |
| Gate H1 | — | **PASS** | — | — |
| Gate H2 | — | **FAIL** (calibration 反向) | — | — |
| Gate H3 | — | **FAIL** (completion retention 不足) | — | — |

### 5. vLLM 当前状态
**已重新启动**（PID 96388, 20:43 启动，CUDA_VISIBLE_DEVICES=2），服务就绪，但没有实验进程在调用它。无 `full_experiment_restart.log`，说明重启后未重新启动实验。

---
