# ssh confirm v73 lora completion

**action cond info bottleneck** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_confirm_v73_lora_completion_20260518T022007_result.json`
- **Structured JSON:** [`b8de3f5801473ebff254.json`](../../sessions/b8/b8de3f5801473ebff254.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇总

### 1. checkpoint-20000 ✅ 存在
- 文件：`checkpoint.pt` (909 MB)，时间 May 18 10:05

### 2. 训练日志 ✅ 正常完成
- 20000 步全部跑完，耗时 3.2h
- 最终 step: loss=0.2602, task=0.1472, ib=0.5411, scorer_mean=0.344
- `EXIT_CODE=0`

### 3. Probe A+B ✅ 已由 watch 脚本自动触发并完成

**Probe A (fixed image, swap instruction):**
| Pair | cos | l2 |
|------|-----|-----|
| bbq_sauce vs black_bowl_cookie | 0.8644 | 3.52 |
| bbq_sauce vs black_bowl_drawer | 0.7652 | 3.89 |
| black_bowl_cookie vs black_bowl_drawer | 0.9387 | 2.06 |

- cos ∈ [0.765, 0.939], bit_identical=False for all pairs
- **结论：scorer 是 language-condition-dependent**（cos < 0.95 判定依赖语言）

**Probe B (natural cross-task obs):**
| Pair | cos | l2 |
|------|-----|-----|
| bbq_sauce vs black_bowl_cookie | 0.6031 | 2.97 |
| bbq_sauce vs black_bowl_drawer | 0.5619 | 3.06 |
| black_bowl_cookie vs black_bowl_drawer | 0.7283 | 2.45 |

- cos ∈ [0.562, 0.728]
- **结论：importance maps 是 task-dependent**（cos < 0.8）

### 4. GPU 状态
- GPU 0: 空闲 (1 MiB, 0%)
- GPU 1: 进程 PID 759167 占用 2201 MiB (1% util) — connector-only eval 正在跑

### 5. Connector-only eval
- 正在运行 rollout（步数 31/280），success_rate 目前 0%，还在早期阶段

---
