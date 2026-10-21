# ops migration final verify

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_migration-final-verify_20260520T122010_result.json`
- **Structured JSON:** [`6d2f17c771e5da3a1965.json`](../../sessions/6d/6d2f17c771e5da3a1965.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有数据已收集完毕，编制验证报告。

## autodl-rtx6000 (目标)
- **总大小**: 20G
- **子目录明细**:

| 目录 | 大小 |
|------|------|
| checkpoints/ | 18G |
| results/ | 1.8G |
| data/ | 1.2G |
| paper/ | 11M |
| logs/ | 9.7M |
| artifacts/ | 6.3M |
| scripts/ | 1.9M |
| src/ | 784K |
| results_filtered/ | 92K |
| baselines/ | 40K |

## westd-48862 (源)
- **总大小**: 2.9G
- **子目录明细**:

| 目录 | 大小 |
|------|------|
| checkpoints/ | 2.2G |
| data/ | 403M |
| results/ | 322M |
| scripts/ | 316K |
| logs/ | 8.0K |

## 逐目录验证

| westd-48862 目录 | autodl-rtx6000 状态 | 详情 |
|---|---|---|
| **data/** (43 files, 12 subdirs) | **全部存在** | downstream/, pythia_temp09/, olmo/, gpt2xl/, qwen25_14b/, 6个 temp/topk 变体, depth_0-3.jsonl, features_all.jsonl 全部匹配 |
| **scripts/** (27 files) | **全部存在** | rtx6000 有 140+ 脚本（超集），westd 的 27 个全部包含 |
| **logs/** (1 file) | **全部存在** | detectgpt_baseline.log 已确认 |
| **checkpoints/downstream_v2/** (68 files) | **全部存在** | d0_only, d1_only, d2_only, mixed_all 结构完全一致 |
| **checkpoints/qwen25_14b/** (51 files) | **全部存在** | lora_depth_0/1/2 + checkpoint-939 结构完全一致 |
| **checkpoints/accumulation_v2/** (90 files) | **全部存在** | mix25 + mix50, lora_d1/d2/d3 结构完全一致 |
| **results/** 16个子目录 + 13个根文件 | **全部存在** | learned_estimator, downstream_benchmark_001, detectgpt_baseline, accumulation, accumulation_v2, mink_prob_baseline, deberta_pilot, feature_ablation, 9个 bino_features.npz 等全部确认 |

## 验证结论

- **westd-48862 的全部文件已在 autodl-rtx6000 上确认存在**
- **缺失文件: 无**
- autodl-rtx6000 是严格超集（20G vs 2.9G），包含 westd-48862 没有的目录：paper/, artifacts/, baselines/, src/, results_filtered/, __pycache__/
- westd-48862 可安全关闭

---
