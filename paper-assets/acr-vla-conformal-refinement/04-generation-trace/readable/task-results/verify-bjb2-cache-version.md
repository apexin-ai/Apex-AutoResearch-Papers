# verify bjb2 cache version

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_verify_bjb2-cache-version_20260514T181621_result.json`
- **Structured JSON:** [`f2f1adecbce8b4c23bdb.json`](../../sessions/f2/f2f1adecbce8b4c23bdb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

关键发现：本地 SmolVLA 模型 Birth 是 May 13 20:00，而 cache 创建于 May 13 15:17-15:43。cache 是用**不同的模型**生成的。

## 结论

### 1. bjb2 `/root/autodl-tmp/crm_cache/` 版本

**无法从计算验证确定 v4/v5**，原因：
- 6D 和 8D state 产生的 obs_features 几乎完全相同（cosine 0.99999），差异可忽略
- cache 与当前 SmolVLA 模型输出的 cosine 只有 ~0.65（因为 cache 是用不同模型生成的——可能是 `lerobot/smolvla_base`，而当前用的是 `/root/autodl-tmp/models/smolvla_libero/`）

**间接证据倾向 v4**：
- 路径 `crm_cache/`（无版本后缀），bjb1 的 v5 cache 明确命名为 `crm_cache_v5/`
- bjb2 上不存在 `crm_cache_v5/`

### 2. 3 个训练进程状态

全部存活（运行约 12 小时），当前 epoch ~41/50：
| PID | input_mode | cache_dir | output_dir |
|-----|-----------|-----------|------------|
| 181668 | full (perdof) | `/root/autodl-tmp/crm_cache/` | `crm_v3/perdof/` |
| 181896 | scalar_unc | `/root/autodl-tmp/crm_cache/` | `crm_v3/scalar_unc/` |
| 181973 | obs_only | `/root/autodl-tmp/crm_cache/` | `crm_v3/obs_only/` |

### 3. 更大的问题

**不管 v4 还是 v5，cache 和当前模型不匹配**：cache 的 obs_features 是用旧版 SmolVLA（可能是 `lerobot/smolvla_base`，May 13 15:43 之前）生成的，而当前本地模型（`smolvla_libero/`）是 May 13 20:00 才创建。eval 时 CRM 接收的 obs_features 来自当前模型，与训练时的 cache 分布不同（cosine 仅 0.65）。

### 4. 建议

- 这 3 个训练可以**让它们跑完**（快到 epoch 50 了），但 eval 时需注意 cache-model mismatch
- 如果要保证 eval 质量，需要用当前模型重新 precompute cache（建议命名为 `crm_cache_v5/`，使用 8D state）
- 是否 kill 取决于你对 cache-model mismatch 的容忍度——如果只是消融实验对比 input_mode，同一个 cache 下的相对比较仍然有效

---
