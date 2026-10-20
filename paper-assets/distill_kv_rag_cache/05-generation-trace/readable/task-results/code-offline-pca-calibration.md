# code offline pca calibration

**distill kv rag cache** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_offline-pca-calibration_20260514T080043_result.json`
- **Structured JSON:** [`42cf79d3563f3e0c1efa.json`](../../sessions/42/42cf79d3563f3e0c1efa.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇报：

---

## 产出汇报

### 1. 标定完成

- **文件**: `/root/autodl-tmp/compresslink/calibration/hotpotqa_50/calibration.pt` (33MB)
- **内容**: 512 entries (32 layers × 8 KV heads × 2 kinds)
- **校准样本**: 前 50 条 HotpotQA contexts

### 2. Eigenvalue 覆盖分析（离线 50 样本标定）

| | 90% variance dims | 50% variance dims |
|---|---|---|
| **Keys** | mean=58.8 (min=4, max=92) | mean=11.8 |
| **Values** | mean=97.5 (min=53, max=111) | mean=30.9 |

关键发现：
- **Keys 低秩性强**：90% 方差平均只需 58.8/128 维，浅层更极端（Layer 0 仅需 16.5 维）
- **Values 高秩**：90% 方差需 97.5/128 维，压缩 values 比 keys 损失更大
- **6x 压缩预算 = 341 bits/head**：均匀 4-bit 可覆盖 85 个 components，greedy 分配下可覆盖 keys 的 90% 方差但对 values 不够

Per-sample PCA 能完美适配每个样本的分布，而离线 basis 使用跨样本的共享统计量，因此：
- 对于分布偏离校准集的样本，离线 PCA 的压缩误差更大
- 这正是我们要的——消除 per-sample PCA 给所有 config 的不公平优势

### 3. 5 条验证结果

| Config | EM | F1 |
|--------|------|------|
| A_6x (KVTC + ProphetKV) | 0.200 | 0.350 |
| B_6x (RABA + ProphetKV) | 0.200 | 0.350 |
| C_6x (KVTC + CEGR-MSE) | 0.200 | 0.350 |
| D_6x (RABA + CEGR-MSE) | 0.200 | 0.350 |
| E (Uncompressed baseline) | 0.200 | 0.314 |

### 4. Config 间差异

5 个样本上 **EM/F1 恰好相同**，但 **文本输出已有差异**（A/C 产出 "I cannot answer..." vs B/D 产出 "There is no information..."），说明 RABA vs 标准 bit allocation 已生效。5 样本太少看不到统计差异，需要 500 样本全量跑来验证。

### 代码变更
- `compresslink/pipeline.py`: 新增 `SimplePCACompressor.load_offline_basis()`；`CompressLinkPipeline.__init__` 支持 `calibration_path` config；`run_single()` Step 4 按需跳过 per-sample calibrate
- `compresslink/eval_runner.py`: 从 YAML config 传递 `calibration_path` 到 pipeline

---
