# diag occ data dummy investigation

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_occ_data_dummy_investigation_20260520T114944_result.json`
- **Structured JSON:** [`0253e9942297e68f75e8.json`](../../sessions/02/0253e9942297e68f75e8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

证据完全确凿了。

## 结论：occ_data_dummy 是**随机合成数据**，不是真实 MuJoCo BEV 数据

### 证据

| 指标 | occ_data_dummy 实际值 | 真实数据预期值 | 随机 Bernoulli(0.15) 预期值 |
|------|----------------------|---------------|---------------------------|
| **Overall occ rate** | 0.1500（精确一致） | ~30-50%（因场景而异） | 0.15 |
| **水平相邻像素差异率** | 0.2569 | 低（连续区域） | 0.255 (= 2×0.15×0.85) |
| **垂直相邻像素差异率** | 0.2453 | 低 | 0.255 |
| **同 task 不同 demo IoU** | 0.071 | 高（同一场景布局） | ~0.081 |
| **不同 task IoU** | 0.088 | 低（不同场景） | ~0.081 |
| **BEV 可视化** | 随机散点噪声 | 桌面/机器人/物体的连续区域 | 噪声 |
| **时间一致性** | t0 vs t1 变化 990 cells ≈ t0 vs t100 变化 1059 cells | 相邻帧变化少，远帧变化多 | 均匀随机 |

所有统计量精确匹配 `np.random.random() < 0.15` 的理论值，无空间结构、无时间一致性、无场景差异。

### 建议

- **不能用 occ_data_dummy 启动 occ_s0 训练**——用随机标签训练 occ head 只会学到噪声
- 必须等 `occ_data/` 的真实 MuJoCo 提取完成（当前 ~1% 完成，预估 20-30h）
- Part 2 dry-run **跳过**，因为前提不满足

---
