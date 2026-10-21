# harvest westd41074 xvla attention results

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_harvest_westd41074_xvla_attention_results_20260522T155701_result.json`
- **Structured JSON:** [`21e6423cec56e66cf3c2.json`](../../sessions/21/21e6423cec56e66cf3c2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部数据已收集。汇报如下：

---

## X-VLA Long 结果

| 实验 | SR | Tokens | CI 95% | 文件路径 |
|------|-----|--------|--------|---------|
| baseline (k=1.0) | **92.5%** | 50→50 | [88.0%, 95.4%] | `results/xvla_long_baseline.json` |
| L2norm k=0.95 | **47.0%** | 50→47 | [40.2%, 53.9%] | `results/xvla_long_l2norm_k095.json` |
| L2norm k=0.9 | **27.5%** | 50→45 | [21.8%, 34.1%] | `results/xvla_long_l2norm_k09.json` |

X-VLA Long 对 token pruning 极其敏感：仅去掉 5% tokens（3个）就从 92.5% 暴跌到 47%。

## Attention Pruning k=0.95 Object (π0.5)

- **SR: 98.4%** (492/500)
- 文件: `eval_results/pi05_attention_k0.95_libero_object_seed42.json`
- 768 vision tokens → keep 690 (230/256 per image, 2-layer probe)
- Attention k=0.9 Object 仍在运行中（当前到 T3，~98.7%）

## GPU 冲突审查

**确认 bug**: `eval_pi05_pruning_libero.py` line 151 `DEVICE = "cuda:0"` 硬编码。`args.gpu` 仅用于 line 155 日志打印，从未用于设备分配。

**受影响实验**（指定 `--gpu 1` 但实际跑在 cuda:0）：

| 实验 | 声称 GPU | 实际 GPU | 启动时间 |
|------|---------|---------|---------|
| baseline_object_s42 | 1 | 0 | 05-21 11:31 |
| baseline_object_s42_official | 1 | 0 | 05-21 13:18 |
| diag_5ep | 1 | 0 | 05-21 11:21 |
| l2norm_k03_object_s42 | 1 | 0 | 05-21 15:43 |
| l2norm_k05_goal_s42 | 1 | 0 | 05-22 23:46 |
| random_k05_object_s43 | 1 | 0 | 05-21 17:54 |
| random_k07_object_s42 | 1 | 0 | 05-21 17:51 |
| random_k09_s43 | 1 | 0 | 05-22 01:53 |

**OOM 事件**: 无（所有日志无 "CUDA out of memory" 或 "RuntimeError"）

**结果可信度: 高** — 推理任务无梯度状态，GPU 共享不影响计算正确性，只影响速度。无 OOM 说明显存充足。两个模型共享 cuda:0 做 inference 不会产生数值差异。

---
