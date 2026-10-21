# code verify analysis script

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_verify-analysis-script_20260515T175541_result.json`
- **Structured JSON:** [`9b918045986308e2b753.json`](../../sessions/9b/9b918045986308e2b753.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

验证完成，汇总如下：

## analyze_goal_probes.py 就绪性报告

### 1. 脚本可运行：PASS
- 文件存在，7168 bytes，2026-05-16 01:32 更新

### 2. Gate 阈值：全部 PASS
| Gate | 期望值 | 脚本默认值 | 状态 |
|------|--------|-----------|------|
| Sanity-GC | DINO acc ≤ 0.25 | `--sanity_gate 0.25` | PASS |
| G1-GC | trained acc > 0.40 | `--acc_gate 0.40` | PASS |
| G2-GC | Δ(trained-DINO) > 0.25 | `--gap_gate 0.25` | PASS |
| G3-GC | Δ(trained-untrained) > 0.10 | `--g3_gate 0.10` | PASS |

### 3. 输入目录状态
| 实验 | 目录 | 状态 |
|------|------|------|
| trained | `trained_libero_goal/goal_classification/` | 已完成，33 层 JSON + summary.json ✓ |
| untrained | `untrained_libero_goal/` | **不存在** — 还没跑 |
| dinov2 | `dinov2_libero_goal/goal_classification/` | 进行中，仅 layer_0 + summary |

### 4. 参数确认
脚本接受 `--trained_dir` / `--untrained_dir` / `--dino_dir`，与预期调用方式匹配。`untrained_dir` 和 `dino_dir` 为 optional（`default=None`），缺失时对应 gate 会 SKIP 而非报错。

### 5. 注意事项
- `load_summary()` 期望路径为 `{dir}/goal_classification/summary.json`，三组实验的目录结构均匹配此模式
- untrained 实验目录尚未创建，需要在实验启动前确保路径一致
- dinov2 正在运行中，目前只完成了 layer 0

**结论：脚本就绪，三组实验完成后可直接运行。**

---
