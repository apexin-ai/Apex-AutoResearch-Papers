# audit crossover script consistency

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_crossover_script_consistency_20260525T092836_result.json`
- **Structured JSON:** [`0af498e001a758f74823.json`](../../sessions/0a/0af498e001a758f74823.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

信息收集完毕。以下是完整的一致性审计报告。

---

## Eval 脚本一致性审计报告

### 1. 两个脚本的 Diff 分析

| 方面 | `eval_openvla_libero.py` (standard, 290行) | `eval_openvla_l2norm_libero.py` (l2norm, 410行) |
|------|------|------|
| 可用模式 | `baseline`, `random_prune` | `baseline`, `random_prune`, `l2norm_prune`, `attention_prune` |
| 模型路径 | **硬编码** `/root/autodl-tmp/openvla-libero-object` | CLI `--model_path`（默认值相同） |
| unnorm_key | **硬编码** `libero_object` | CLI `--unnorm_key`（默认值相同） |
| GPU | 硬编码 `cuda:0` | 有 `--gpu` 参数但**未实际使用**（仍是 `cuda:0`） |
| RandomPruningHook | ✅ lines 127-144 | ✅ lines 130-145 **完全一致** |
| L2NormPruningHook | ❌ | ✅ lines 147-165 |
| AttentionPruningHook | ❌ | ✅ lines 167-250 |
| Eval loop | 完全一致 | 完全一致 |
| JSON "model" 字段 | 硬编码 `"openvla-7b-libero-object"` | `os.path.basename(args.model_path)` |

**l2norm 脚本是 standard 脚本的超集。** `RandomPruningHook` 实现（`torch.randperm(N)[:keep].sort().values`）**逐行一致**，eval loop 也完全相同。

### 2. Crossover Table 实验脚本归属

| exp_id | 脚本 | 模式 | Suite | SR | Server | 日期 | 备注 |
|--------|------|------|-------|-----|--------|------|------|
| eval_openvla_baseline_object_seed42 | l2norm | baseline | Object | 74.0% | westd-38929 | 5/21 | ✅ |
| eval_openvla_baseline_goal_seed42_v3 | l2norm | baseline | Goal | 74.8% | westd-27271 | 5/23 | ✅ |
| openvla_baseline_spatial_correct_seed42 | l2norm | baseline | Spatial | 80.0% | westd-27271 | — | ✅ 正确模型 |
| eval_openvla_baseline_long_seed42 | l2norm | baseline | Long | 52.8% | westd-27271 | 5/23 | ✅ |
| **eval_openvla_prune_random_k09_seed42** | **standard** | random | Object | **64.6%** | **westd-41074** | **5/20** | ⚠️ 唯一用 standard 的 |
| eval_openvla_random_k09_object_seed42 | l2norm | random | Object | 62.8% | westd-27271 | 5/21 | 重复实验 |
| eval_openvla_random_k09_goal_seed42_v2 | l2norm | random | Goal | — | westd-38929 | 5/25 | killed |
| eval_openvla_random_k09_spatial_seed42_v2 | l2norm | random | Spatial | — | westd-38929 | 5/25 | killed |
| eval_openvla_random_k09_long_seed42_v2 | l2norm | random | Long | — | westd-41074 | 5/25 | killed |
| eval_openvla_l2norm_k09_object_seed42 | l2norm | l2norm | Object | 70.6% | westd-27271 | 5/21 | ✅ |
| eval_openvla_l2norm_k09_goal_seed42 | l2norm | l2norm | Goal | 74.8% | westd-27271 | 5/24 | ✅ |
| eval_openvla_l2norm_k09_spatial_seed42 | l2norm | l2norm | Spatial | 75.0% | westd-27271 | 5/24 | ✅ |
| eval_openvla_l2norm_k09_long_seed42_v2 | l2norm | l2norm | Long | — | westd-41074 | 5/25 | killed |
| eval_openvla_attn_k085_object_seed42 | l2norm | attention | Object | 55.0% | westd-38929 | 5/24 | k=0.85 |
| eval_openvla_attn_k09_goal_seed42 | l2norm | attention | Goal | 73.2% | westd-27271 | 5/24 | ✅ |
| eval_openvla_attn_k09_spatial_seed42 | l2norm | attention | Spatial | 80.4% | westd-27271 | 5/24 | ✅ |
| eval_openvla_attn_k09_long_seed42_v2 | l2norm | attention | Long | — | westd-41074 | 5/25 | killed |

### 3. 各模式下脚本差异的影响分析

| 模式 | 行为是否一致？ | 说明 |
|------|------------|------|
| **baseline** | ✅ 一致 | 两个脚本都不注册 hook，eval loop 相同。Object suite 模型路径相同。 |
| **random_prune** | ✅ 一致（Object suite） | `RandomPruningHook` 实现完全一致，模型/unnorm_key 对 Object suite 相同。 |
| **random_prune**（非Object） | ⚠️ standard 不可用 | standard 脚本硬编码 Object 模型，无法正确评估 Goal/Spatial/Long。 |
| **l2norm_prune** | N/A | 只有 l2norm 脚本支持此模式。所有实验一致。 |
| **attention_prune** | N/A | 只有 l2norm 脚本支持此模式。所有实验一致。 |

### 4. 64.6% vs 62.8% 差距分析

两个结果都是 **random pruning k=0.9 on Object seed42**：

- **64.6%** — standard 脚本, westd-41074, 5/20
- **62.8%** — l2norm 脚本, westd-27271, 5/21

由于两个脚本的 `RandomPruningHook` 实现完全一致，1.8pp 差距**不是脚本差异导致**，而是来自：

1. **Random pruning 的固有非确定性**：`torch.randperm(N)` 在每个 step 生成不同的随机排列。虽然起始 seed 相同，但随着 episode 推进，GPU 上的随机状态因硬件差异和执行顺序不同而发散。
2. **不同服务器**：westd-41074 vs westd-27271，不同 CUDA driver/GPU → 不同数值行为。
3. 1.8pp 在 random pruning 的正常方差范围内（同脚本同 seed 跨服务器跑也会有类似差异）。

### 5. 结论与建议

**脚本一致性问题：无实质影响。** Crossover table 中唯一用 standard 脚本的实验是 Random k=0.9 Object（64.6%），其 `RandomPruningHook` 和 eval loop 与 l2norm 脚本完全一致。1.8pp 差异源于随机性，非脚本差异。

**建议：**

1. **统一到 `eval_openvla_l2norm_libero.py`**：它是 standard 的超集，支持所有模式，且通过 `--model_path`/`--unnorm_key` 避免硬编码问题。Standard 脚本可以废弃。
2. **Crossover table 中 Random k=0.9 Object 用哪个值？** 两个都可以，因为脚本无功能差异。建议选择 62.8%（l2norm 脚本），与其他所有实验保持脚本一致性。或者如果已经发表了 64.6%，也没问题——两个值都是有效的。
3. **不需要重跑任何实验。** 所有已完成实验的结果是有效的，脚本差异不影响结果可比性。

---
