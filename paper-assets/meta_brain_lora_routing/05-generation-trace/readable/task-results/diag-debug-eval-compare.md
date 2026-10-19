# diag debug eval compare

**Meta-Brain: Perturbation-Diagnostic Routing of LoRA Experts for Parameter-E cient VLA Robustness** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_debug_eval_compare_20260516T124213_result.json`
- **Structured JSON:** [`26bd2d3c5eea1546b15c.json`](../../sessions/26/26bd2d3c5eea1546b15c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果已出。openpi 官方推理失败了——checkpoint 格式与 openpi 的 `safetensors.torch.load_model` 不兼容。

## 完整诊断报告

### MetaBrain 推理（成功）

| 项目 | 值 |
|------|-----|
| Shape | `(50, 7)` — 50步 action horizon，7维 |
| Range | `[-1.0173, 1.0569]`，mean=0.0284 |
| NaN | 无 |

**首步 action[0]:**
```
[ 0.1698, -0.1323, 0.5482, 0.4313, -0.0788, -0.0355, 1.0395 ]
```

**各维统计:**
| dim | min | max | mean | std |
|-----|-------|-------|-------|-------|
| 0 | -0.0601 | 0.1973 | 0.0595 | 0.0789 |
| 1 | -0.2007 | 0.1015 | 0.0058 | 0.0798 |
| 2 | -0.2486 | 0.7758 | 0.2355 | 0.2631 |
| 3 | -0.1333 | 0.4313 | 0.0909 | 0.1595 |
| 4 | -0.7727 | 0.5323 | -0.0689 | 0.3413 |
| 5 | -0.1504 | 0.0744 | 0.0055 | 0.0519 |
| 6 | -1.0173 | 1.0569 | -0.1298 | 0.9629 |

### openpi 官方推理（失败）

`policy_config.create_trained_policy()` 在 `safetensors.torch.load_model()` 崩溃：

**根因：checkpoint 格式不匹配。** 该 checkpoint 是 LeRobot 格式（key 带 `model.` 前缀），而 openpi 的 `load_pytorch` 直接用 `safetensors.torch.load_model` 加载，期望无前缀的 key。

具体错误：
- **Missing keys** (openpi 期望但 checkpoint 没有)：`action_in_proj.weight`, `paligemma_with_expert.gemma_expert.model.layers.*.weight` 等 — 这些是无前缀格式
- **Unexpected keys** (checkpoint 有但 openpi 不期望)：`model.action_in_proj.weight`, `model.paligemma_with_expert.*.weight` — 全部带 `model.` 前缀，以及额外的 `normalize_inputs.*`, `normalize_targets.*`, `unnormalize_outputs.*` buffers

**关键诊断结论：**

1. MetaBrain 的 `meta_brain_assembly.py` 正确处理了 LeRobot 格式（`stripped model. prefix from 777 keys, extracted 6 norm buffers`），而 openpi 官方的 `load_pytorch` 没有这个 strip 逻辑
2. MetaBrain 单独推理正常工作，输出范围合理
3. 无法通过 openpi 官方路径加载同一 checkpoint 做对比——需要修改 openpi 的加载逻辑或使用 openpi 原生格式的 checkpoint

---
