# ops pre launch validation

**Shifting the Cross-Lingual Calibration Pareto Frontier: Probe-Based Calibration Transfer via CaCLR** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_pre-launch-validation_20260521T073614_result.json`
- **Structured JSON:** [`6a2dfeac94552dec360a.json`](../../sessions/6a/6a2dfeac94552dec360a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有信息收集完毕。汇总如下：

---

## P0 预启动检查结果

### 1. GlobalMMLU 数据

**状态: 部分可用 — 缺 te (Telugu)**

HF cache 路径: `/root/autodl-tmp/.hf_cache/datasets/CohereForAI___global-mmlu/`

已缓存 18 种语言: ar, bn, de, es, fr, hi, id, ja, ko, nl, pl, pt, ru, sw, tr, uk, vi, zh

English 从 `cais/mmlu` 加载（已缓存于 `/root/autodl-tmp/.hf_cache/hub/datasets--cais--mmlu`）

**缺失: te (Telugu)** — 脚本运行时会自动从 HF 下载，但建议提前下载避免运行时延迟。

### 2. 模型下载

| 模型 | 已下载 | 目标 | 进度 | 活跃下载 |
|------|--------|------|------|----------|
| Llama4 Scout W4A16 | 46GB (8/14 shards) | ~66GB | ~70% | **无** — 下载似乎中断，缺 shard 00004, 00009, 00011-00014 |
| Qwen3-235B GPTQ-Int4 | 39GB (5/32 shards) | ~125GB | ~31% | **有** (PID 53359, `huggingface_hub.snapshot_download`) |

**Llama4 需要恢复下载。** Qwen3 正在下载中，按当前速率（~200KB/s AutoDL 代理）预计还需较长时间；如果网速稳定在 ~5MB/s 则约 5-6 小时。

### 3. 代码 sync

| 修复项 | 状态 |
|--------|------|
| Fix 1: LANGS_20 用 `"te"` 非 `"th"` | ✅ 行55: `"te"` 在列表中 |
| Fix 2: solver=`"liblinear"` | ✅ 行209, 无 `lbfgs` 残留 |
| Fix 3: global split indices (`train_indices`) | ✅ 行421, metadata 中保存 |
| Fix 4: `n_control` default=10 | ✅ 行436: `default=10` |
| Fix 5: final layer inclusion | ✅ 行272-273: `compute_layer_indices` 自动 append `n_layers-1` |
| 脚本完整性 | ✅ `extract_activations.py`, `train_probes.py`, `run_p0.sh` 全部存在 |

**代码全部到位，无问题。**

### 4. 磁盘空间

| 分区 | 总量 | 已用 | 可用 | 使用率 |
|------|------|------|------|--------|
| /root/autodl-tmp | 350GB | 172GB | 179GB | 50% |
| /root (系统) | 30GB | 1.4GB | 29GB | 5% |

Llama4 剩余 ~20GB + Qwen3 剩余 ~86GB = ~106GB，可用 179GB，**空间充足**。

---

**需要行动的两项:**
1. 恢复 Llama4 Scout 下载（6 个 shard 缺失，无活跃下载进程）
2. 可选：提前下载 GlobalMMLU te (Telugu) 数据集到缓存

是否现在处理这两项？

---
