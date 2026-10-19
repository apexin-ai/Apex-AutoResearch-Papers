# fix crm spatial path

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_crm-spatial-path_20260521T212914_result.json`
- **Structured JSON:** [`8ff36e03937957522b8a.json`](../../sessions/8f/8ff36e03937957522b8a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 调查结果

### 1. spatial cache 状态：**完整，无需修复**

路径 `/root/autodl-tmp/crm_cache_pi05/spatial/` 实际存在且数据齐全：

| 文件 | 大小 | 修改时间 |
|------|------|---------|
| `obs_features.pt` | 494 MB | 2026-05-22 03:23:24 |
| `k_samples.pt` | 72 MB | 2026-05-22 03:23:30 |
| `expert_actions.pt` | 7.2 MB | 2026-05-22 03:23:31 |
| `manifest.json` | - | n_samples=60250, K=10, h_eff=5 |

外加 100+ 个 `partial_s*_*.pt` 分片文件。总大小 1006 MB。

manifest 与 object（69303 samples, K=10）规格一致，但 spatial manifest 少了 `num_shards` 字段（object 有 `num_shards: 10`），不过 consolidated 文件齐全，不影响训练加载。

### 2. 修复方案：**不需要**

原 `FileNotFoundError` 是 precompute 完成前触发的过期错误。precompute 已在 03:23 完成，spatial training 已重启并正常运行。

### 3. 当前训练进度（log 最后更新 05:30:57，正在写入）

**spatial** (`crm-train-pi05-spatial-full.log`):
- 当前 epoch 17/50（progressing through batch 750/1695）
- 最新完成: Epoch 16/50, train_loss=0.013585, val_loss=**0.007745**（持续下降，best）
- batch 数 = 1695（n_samples=60250）

**object** (`crm-train-pi05-object-full.log`):
- 当前 epoch 23/50（progressing through batch 600/1950）
- 最新完成: Epoch 22/50, train_loss=0.008599, val_loss=**0.004617**（best）
- batch 数 = 1950（n_samples=69303）

两个训练都在健康收敛，无需干预。

---
