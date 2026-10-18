# audit pruning method consistency

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_pruning-method-consistency_20260520T075045_result.json`
- **Structured JSON:** [`fddc55e386b686dc052e.json`](../../sessions/fd/fddc55e386b686dc052e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审计完成。以下是完整结果。

---

## 跨模型 Pruning 方法一致性审计结果

### 核心结论：**pruning analysis（曲线生成）方法一致，全部使用 L2_norm_zero_out**

之前的 D100 决策已部分确认此结论，本次审计扩展覆盖了 X-VLA。

---

### 详细审计表

| 模型 | 脚本路径 | Pruning 方法 | 重要性指标 | 证据 |
|------|---------|-------------|-----------|------|
| **π0** | `artifacts/pi0_token_importance.py` | **L2_norm_zero_out** | L2 norm | L258-265: `mask = torch.zeros(1, n_real_vis, 1)` → `mask.scatter_(1, topk_idx.unsqueeze(-1), 1.0)` → `prefix_embs[:,:n_real_vis,:] * mask`。JSON 明确标注 `"pruning_method": "L2_norm_zero_out"`。输出 shape 不变。 |
| **OpenVLA-OFT** | `analyze_openvla_oft.py` (westd-38929) | **L2_norm_zero_out** | L2 norm | L207-213 `ProjectorHook.__call__`: `mask = torch.zeros(B, N, ...)` → `mask.scatter_(1, topk_idx, 1.0)` → `output = output * mask.unsqueeze(-1)`。JSON 标注 `"pruning_method": "L2_norm_zeroing"`。输出 shape 不变。 |
| **X-VLA** | `analyze_xvla_token_importance.py` (westd-41074) | **L2_norm_zero_out** | L2 norm | Worker log 中代码：`mask = torch.zeros_like(importance, dtype=torch.bool)` → `mask.scatter_(1, top_idx, True)` → `vlm_p = vlm_feat * vlm_mask.unsqueeze(-1).float()`。输出 shape 不变。 |
| **SmolVLA (IMM)** | `eval_pruning_sweep.py` → `imm/token_selection.py` | **ACIS + zero_out** | ACIS (learned) | `MarginAwareTokenSelector._hard_forward()`: `selected = tokens * binary_mask.unsqueeze(-1)`。输出 shape 不变。注意：重要性指标是 ACIS（学习的打分器），非 L2 norm。 |

---

### 评估脚本（不同于 curve 分析脚本）

这些是实际 task success rate 评估脚本，使用 **true_removal**：

| 模型 | 评估脚本 | 方法 | 关键代码 |
|------|---------|------|---------|
| OpenVLA | `eval_openvla_acis_prune.py` | **true_removal** | L224: `pruned_vision = vision_features[:, topk_sorted[0], :]` — index select 缩短 sequence |
| X-VLA | `eval_xvla_pruning_libero.py` | **true_removal** | L100-103: `features.gather(1, indices_sorted.unsqueeze(-1).expand(...))` — gather 缩短 sequence |
| SmolVLA | `geometric_prior_pruning.py` | **true_removal** (default) | L160: `tokens[:, kept, :]` — boolean indexing 缩短 sequence |

---

### 关键区分

**Reviewer 的担忧指向的是两类不同脚本**：

1. **Pruning curve 分析脚本**（生成论文中跨模型压缩曲线）→ **全部一致使用 zero_out**，跨模型对比有效
2. **Pruning eval 脚本**（实际评估 task success rate）→ 使用 **true_removal**，这是合理的，因为实际部署时确实需要减少 token 数量

### 已知问题（D100 已记录）

- **OpenVLA-OFT pruning curve 无效**：`openvla_oft_pruning_curve.json` 所有 k_ratio 输出完全相同值 (0.274493)，因为脚本 hook 注入的位置在 `model.generate()` 的 autoregressive 路径上不生效。OFT entropy 数据有效，pruning curve 需修复重跑。

### 结论

**不存在方法不一致问题。** 跨模型 pruning sensitivity curve（论文核心图表数据）全部使用相同的 L2_norm_zero_out 方法（SmolVLA 的重要性指标是 ACIS 而非 L2 norm，但 masking 方式一致）。评估脚本使用 true_removal 是预期行为，不影响跨模型对比的有效性。

---
