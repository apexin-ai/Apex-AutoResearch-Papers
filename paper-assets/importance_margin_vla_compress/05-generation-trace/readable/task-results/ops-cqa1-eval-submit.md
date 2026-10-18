# ops cqa1 eval submit

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_cqa1_eval_submit_20260519T225647_result.json`
- **Structured JSON:** [`23aa06918cae424c0d7a.json`](../../sessions/23/23aa06918cae424c0d7a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

GPU 1 和 GPU 2 的 eval 都已成功启动。GPU 3 空闲。

对所有 checkpoint vs eval 的比对结果：

| Checkpoint | Eval 结果 | 状态 |
|---|---|---|
| m128_seed43 | ❌ | → GPU 1 eval 运行中 (PID 818806) |
| m16_seed43 | ❌ | → GPU 2 eval 运行中 (PID 819552) |
| m16_seed44 | ❌ | 训练中 (m16_seed44_v3, step 85.5K/100K, ~55min) |
| m32_seed43 | ✅ | |
| m32_seed44 | ✅ | |
| m64_seed43 | ✅ | |
| m64_seed44 | ✅ | |
| m96_seed43 | ✅ | |
| m96_seed44 | ✅ | |

**GPU 3 安排**：唯一缺 eval 的是 m16_seed44，但其训练 (m16_seed44_v3) 仍在 GPU 0 上运行 (step 85500/100000, ~4 sps)。预计约 55 分钟后完成。训练完成后可在 GPU 3 上提交 m16_seed44 的 eval。

### 汇总

| GPU | 任务 | PID | 状态 |
|---|---|---|---|
| 0 | train m16_seed44_v3 | 678106 | step 85.5K/100K, ~55min |
| 1 | eval m128_seed43 | 818806 | 已启动, 加载中 |
| 2 | eval m16_seed43 | 819552 | 已启动, 加载中 |
| 3 | 空闲 | — | 等 m16_seed44_v3 训练完成后提交 eval |

---
