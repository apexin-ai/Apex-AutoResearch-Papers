# diag openpi official inference

**Meta-Brain: Perturbation-Diagnostic Routing of LoRA Experts for Parameter-E cient VLA Robustness** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_openpi_official_inference_20260516T124930_result.json`
- **Structured JSON:** [`8490734f9de92b5e9fe4.json`](../../sessions/84/8490734f9de92b5e9fe4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。下面是完整的诊断总结：

---

## 诊断结果

### 1. OpenPI 官方推理 — 可用 ✓
- 需要转换 checkpoint（strip `model.` prefix, remove norm buffers）
- 需要 monkey-patch 图像格式（openpi PyTorch 代码的 HWC/CHW 处理有 bug）
- 输出：`(50, 7)` actions，range `[-1.03, 1.83]`，合理的 delta 动作

### 2. 根因：MetaBrain 用了错误的 norm_stats

pi0_libero 训练时使用 `extra_delta_transform=True`，意味着动作被处理为 `raw_delta - state`。这导致两套不同的 norm_stats：

| 来源 | action_mean[3] (roll) | action_std[3] |
|------|----------------------|---------------|
| **norm_stats.json** (正确，delta 后) | -2.97 | 0.35 |
| **LeRobot buffer** (错误) | 0.0005 | 0.039 |

MetaBrain 用了 buffer stats 且不加 state 回去 → roll 维度输出 ~3.0 而非正确的 ~-0.06。

### 3. 修复已应用

修改 `_build_norm_stats()` 优先使用 JSON norm_stats + `use_delta=True`。验证后 roll 维度差异从 **3.16** 降到 **0.14**（剩余为随机噪声）。

### 4. 下一步
重新跑 MetaBrain LIBERO eval 验证非零成功率。

---
