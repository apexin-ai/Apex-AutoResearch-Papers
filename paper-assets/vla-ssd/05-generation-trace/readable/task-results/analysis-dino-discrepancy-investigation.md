# analysis dino discrepancy investigation

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_dino-discrepancy-investigation_20260515T133001_result.json`
- **Structured JSON:** [`567a86726d4bacf0ae12.json`](../../sessions/56/567a86726d4bacf0ae12.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据收集完毕，以下是根因分析。

---

## 根因分析：DINO per_task_mean_rho 从 0.554 跳到 0.9008

### 根因：`train_probes.py` 被整体重写，不只是 save_results

**关键证据：**

| 事件 | 时间 (CST) |
|------|-----------|
| DINO features 提取完成 | 15:11 |
| dinov2_baseline 旧结果生成（用**旧** train_probes.py） | ~15:15 |
| dinov2_baseline 注册到 registry | 19:05 |
| **当前** train_probes.py 文件创建（Birth） | **20:27** |
| train_probes.py 最后修改 | 21:10 |
| 旧结果备份到 temporal_distance_old_backup/ | 21:27 |
| 新结果生成（用**新** train_probes.py） | 21:28 |

`train_probes.py` 的 Birth 时间是 20:27，在旧 baseline 完成之后。**旧文件被完全替换，不存在了。** D003/D004 Worker 声称"只改了 save_results"不准确——整个脚本被重写。

### 两个因素共同导致 0.35+ 跳变

**因素 1：模型变强（贡献 ~0.07）**

| 指标 | 旧 | 新 |
|------|-----|-----|
| pooled ρ | 0.833 | 0.900 |
| val_loss | 0.0255 | 0.0160 |
| R² | 0.686 | 0.803 |
| epochs_trained | 9 | 15 |

同一数据、同一特征（.h5 文件时间戳一致），但新代码训练出更强的 probe。可能的架构变化（如 MLPProbe hidden_dim 128→256），但无法确证（旧代码已删）。

**因素 2：Simpson's Paradox 消除（贡献 ~0.28）**

| 指标 | 旧 | 新 |
|------|-----|-----|
| pooled ρ | 0.833 | 0.900 |
| per_task_mean_rho | 0.554 | 0.901 |
| 膨胀量 (pooled - per_task) | **+0.279** | **-0.001** |

旧模型较弱时，跨 task 方差严重膨胀 pooled ρ。新模型每个 task 都达到 ρ≈0.90，跨 task 膨胀消失。

### 旧 0.554 的来源

旧 backup 的 summary.json 和 layer_0.json **完全没有** per_task_rho 字段。旧代码不计算这个指标。Registry 中的 `per_task_rho_mean: 0.5542` 是事后另算的——对于旧的弱模型，这个值可能是正确的。

Registry 中 `per_task_n_pairs: 500` 是错误的（实际应为 5000 = 10 val_traj × 10 bins × 50 pairs/bin）。

### 哪个数字是正确的

**两个都可能对其各自的模型是正确的。** 但应采用新的 0.9008：
- 使用可审计的当前代码
- per_task_rho 在训练评估中直接计算（非事后补算）
- 与 OpenVLA 的 probe 训练使用完全相同的代码（从 mvp_probe 日志确认）

### 对 MVP 的影响

| 模型 | per_task_mean_rho | 来源 |
|------|------------------|------|
| DINO-V2 baseline | **0.901** | 当前结果 |
| OpenVLA trained (best layer) | ~0.956 | mvp_probe_trained.log |
| OpenVLA untrained (best layer) | ~0.933 | mvp_probe_untrained.log |

**DINO baseline 从 0.554 → 0.901 后，OpenVLA 的优势从 ~0.40 缩小到 ~0.05。** 而且 OpenVLA untrained（随机 LLM 权重）也达到 0.93，仅比 trained 低 0.02。

### 建议

1. **更新 registry** 的 dinov2_baseline 指标，标注旧 0.554 不可靠
2. **DINO_GATE_THRESHOLD 需要从 ~0.6 提升到 ~0.90**
3. **重新评估 MVP 叙事**：temporal distance probe 这个指标上，视觉 backbone 本身（DINO/OpenVLA vision encoder）就编码了很强的 temporal progress 信号。OpenVLA 的 LLM 部分对此贡献很小（trained 0.956 vs untrained 0.933）。这可能意味着需要更难的 probe 任务来体现 VLA 训练的价值

---
