# code gated crm design

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_gated-crm-design_20260514T174744_result.json`
- **Structured JSON:** [`b0b396aa814c81467358.json`](../../sessions/b0/b0b396aa814c81467358.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部验证通过。

### 产出总结

**1. `src/gated_crm.py`** — 完整实现
- MLP 结构与 CRM 完全一致（`net.{0,2,4}`），可直接加载现有 checkpoint
- 新增 per-DOF gating：使用 CGS 输出的 per_dof_stds（30D, uncertainty_features 的前 30 维）作为 gating 信号
- hard mode: `gate = (std > threshold).float()` — 二值门控
- soft mode: `gate = sigmoid((std - threshold) / temperature)` — 平滑过渡
- `delta = delta * gate` — 低 uncertainty 维度的 correction 被置零，pass-through base action

**2. `src/evaluate.py`** — 新增 `acr_gated` mode
- `--mode acr_gated` + `--gate_threshold` / `--gate_mode` / `--gate_temperature` 参数
- `select_action_gated_crm()` 函数：从 CGS 输出中提取 per_dof_stds 传给 GatedCRM
- 加载时使用 GatedCRM 替代 CRM，其余逻辑与 acr_vla 一致

**3. 验证结果**
- `import ok` ✓
- `load_state_dict ok`（兼容现有 checkpoint）✓
- forward + gating 逻辑正确（threshold=999 时 delta=0）✓
- `--help` 显示 `acr_gated` mode 及所有 gate 参数 ✓

**4. gate_threshold 推荐值**

CGS 的 per_dof_stds 是 6D pose 在 K=10 个 flow-matching samples 上的 Ledoit-Wolf 对角标准差。典型范围取决于 action scale，但经验上：
- **0.01–0.05**：保守值，大多数维度的 correction 会保留（只过滤极低 uncertainty）
- **0.05–0.15**：中等值，预期过滤 30-60% 的维度
- **0.15–0.30**：激进值，只在高 uncertainty 维度上修正

建议先在 eval 数据上统计 per_dof_stds 的分布（p25/p50/p75），用 **p50 附近作为起点**做 sweep。soft mode + temperature=0.05 可以避免 hard 门控的梯度不连续问题（如果后续要端到端 fine-tune gate）。

---
