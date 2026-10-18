# diag eval openvla attn k085 long seed42 v3

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_eval_openvla_attn_k085_long_seed42_v3_20260525T133130_result.json`
- **Structured JSON:** [`1781c40d2c42314a82ac.json`](../../sessions/17/1781c40d2c42314a82ac.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

- **失败原因: 实验并未失败，已正常完成**
- **错误类型: 非错误（误报）**
- **错误详情:**
  - 实验于 `2026-05-25 21:20` 正常结束，耗时 511.2 分钟
  - Overall SR: **0.4580** (229/500)，10 个 task 全部跑完，每个 50 episodes
  - 结果已保存至 `/root/autodl-tmp/importance_margin_vla_compress/eval_results/openvla_l2norm_prune_k085_10.json`
  - **无 W&B metrics 的原因**: 脚本未集成 W&B logging，只保存了本地 JSON
- **GPU 状态:**
  - GPU 0: 15938/97887 MiB (69%) — attn_k09 运行中
  - GPU 1: 1/97887 MiB (0%) — attn_k085 已完成，空闲
  - GPU 2: 15938/97887 MiB (67%) — random_k09 运行中
  - GPU 3: 15938/97887 MiB (84%) — l2norm_k09 运行中
- **磁盘状态:** `/root/autodl-tmp` **99% 已满**（247G/250G，仅剩 3.2G）⚠️ 风险
- **其他 3 个 Long v3 实验**: 全部正常运行中，均在 Task 10/10 的后半段

### 发现两个 Bug：

1. **结果文件命名错误**: mode 是 `attention_prune`，但文件名保存为 `openvla_l2norm_prune_k085_10.json`（硬编码了 `l2norm_prune`）
2. **k_ratio 未记录**: JSON 中 `"k_ratio": null`，实际应为 0.85

### 建议修复：

1. 不需要重跑实验——结果有效，手动修正 JSON 文件名和 k_ratio 字段即可
2. **紧急**: 磁盘仅剩 3.2G，其他 3 个实验完成后保存结果可能失败。建议清理旧日志或不需要的文件
3. 修复 `eval_openvla_l2norm_libero.py` 中结果文件命名逻辑，使其使用实际 mode 而非硬编码 `l2norm_prune`

---
