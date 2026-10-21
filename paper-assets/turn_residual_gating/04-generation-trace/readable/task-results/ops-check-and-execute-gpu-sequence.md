# ops check and execute gpu sequence

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_and_execute_gpu_sequence_20260523T004244_result.json`
- **Structured JSON:** [`f4c0d687f72cd1a5cbd4.json`](../../sessions/f4/f4c0d687f72cd1a5cbd4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**情况 A：一切正常，自动过渡已触发，流水线正在运行。**

### 当前状态

| 项目 | 状态 |
|------|------|
| **tmux sessions** | `auto_transition` + `queue_runner` 均存活 |
| **GPU** | RTX PRO 6000 Blackwell, 88% util, 60383/97887 MiB, PID 56974 |
| **流水线进度** | [2/8] 完成 → [3/8] SS s123 训练中（刚启动 step 0） |

### PCGrad AR N=50 结果（已完成）

4 个方法的结果文件均存在于 `results/d048_ar_n50_existing/`：

| 方法 | β=0 GAR | β=3 GAR | β=5 GAR | β=5 PPL |
|------|---------|---------|---------|---------|
| **TG** | 0.0234 | 0.5300 | **0.6815** | 1.908 |
| **PCGrad** | 0.0180 | 0.5313 | 0.6615 | 1.761 |
| **UG** | 0.0268 | 0.5176 | 0.6566 | 1.723 |
| **LoRA-only** | — | — | — | — |

### 当前训练：[3/8] SS s123

- 08:43:07 启动，模型已加载，step 0 开始
- 配置：scheduled sampling, max_ratio=0.3, 3000 steps, grad_accum=8
- Gate 初始均值 0.8118，std 0.0277

无需手动干预，流水线自动串行执行中。

---
