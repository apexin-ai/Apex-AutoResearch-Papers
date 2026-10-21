# ops openvla eval check

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_openvla_eval_check_20260517T193154_result.json`
- **Structured JSON:** [`f62abd2d560ed55fd0fd.json`](../../sessions/f6/f62abd2d560ed55fd0fd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇总

### Baseline（已完成）
**Overall SR: 74.0% (370/500)**

| Task | SR |
|------|-----|
| alphabet soup | 78% |
| cream cheese | 80% |
| salad dressing | 82% |
| bbq sauce | 46% |
| ketchup | **96%** |
| tomato sauce | 78% |
| butter | 58% |
| milk | 72% |
| chocolate pudding | 68% |
| orange juice | 82% |

耗时 226 分钟。结果文件：`/root/autodl-tmp/importance_margin_vla_compress/eval_results/openvla_baseline_object.json`

### Random Prune k=0.5（正在运行）
刚启动不久（03:30 开始，Task 1/10 还没有 episode 输出）。进程 PID 697608 仍在 GPU 0 上运行（15.9 GB VRAM, 64% util）。

按 baseline 的速度（226 min / 500 eps ≈ 2.2 eps/min），pruning 条件预计也需要 ~226 分钟（~3.8 小时），大约在 **07:15-07:30 UTC** 完成。

### 状态
- Baseline: 完成，SR=74%
- Pruning: 正在运行，Task 1/10 刚开始，预计还需 ~3.5 小时
- 无需手动干预，脚本会自动保存结果到 `eval_results/openvla_random_prune_k05_object.json`（推测路径）

---
