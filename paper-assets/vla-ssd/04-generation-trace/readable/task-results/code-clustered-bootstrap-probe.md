# code clustered bootstrap probe

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_clustered_bootstrap_probe_20260522T140930_result.json`
- **Structured JSON:** [`cbc40a7ee763301e20d9.json`](../../sessions/cb/cbc40a7ee763301e20d9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Dry-run 结果汇报：

**`clustered_bootstrap_probe.py` — openvla / goal / trained (dry-run)**

| 参数 | 值 |
|------|-----|
| 样本数 | 20 (4 demos × 5 timesteps, 2 tasks) |
| Bootstrap | 100 iterations |
| 模式 | dry_run=true |

**核心指标：**

| 指标 | 值 |
|------|-----|
| Peak R² | **-0.7551** @ L28 |
| Exit R² | **-0.9913** @ L31 |
| Delta (peak - exit) | **0.2362** |
| 95% CI | [0.0, 1.4872] |
| Bootstrap delta mean/std | 0.1911 / 0.4205 |

**Per-layer R² 趋势：** 从 L0 (-2.36) 到 L6 (-0.95) 逐层改善，L7-L15 略有回落，L16 起再次改善，L28 达到 peak (-0.76)，随后 L29-L31 回落至 exit。

**解读：**
- 所有 R² 均为负值，这在 dry-run 的极小样本下（4 demos, 3/1 train/test split）是预期行为——Ridge probe 在如此少的数据上无法学到有意义的映射
- 关键验证点已全部通过：模型加载（含 transformers 5.x 兼容性修复）→ hidden state 提取 → demo-level 聚类分割 → 预计算 kernel 矩阵 → dual-form bootstrap → JSON 输出
- 正式运行（10 demos × 50 timesteps × 10 tasks = 5000 samples, 10000 bootstrap）预期 R² 将为正值

**脚本状态：** 已部署到 `westd-19183:/root/autodl-tmp/vla-ssd/scripts/clustered_bootstrap_probe.py`，本地 artifact 已同步更新。

---
