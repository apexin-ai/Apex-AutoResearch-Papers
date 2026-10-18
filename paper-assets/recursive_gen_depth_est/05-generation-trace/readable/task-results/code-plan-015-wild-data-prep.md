# code plan 015 wild data prep

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan_015_wild_data_prep_20260516T045647_result.json`
- **Structured JSON:** [`b4d3e8a5d9134706830d.json`](../../sessions/b4/b4d3e8a5d9134706830d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

准备完成。汇报：

## 完成状态

**1. 数据下载** ✓
| 数据源 | 来源 | 样本数 | 路径 |
|--------|------|--------|------|
| RedPajama | `togethercomputer/RedPajama-Data-V2` (CC 2023-06 en_head) | 5000 | `data/wild_data/redpajama.jsonl` |
| Dolma | `allenai/dolma` v1.6 sample (olmo-data.org) | 5000 | `data/wild_data/dolma.jsonl` |

**2. 脚本路径和运行命令**
- Python: `/root/autodl-tmp/recursive_gen_depth_est/plan_015_wild_data_v4.py`
- Shell: `/root/autodl-tmp/recursive_gen_depth_est/scripts/run_wild_data_plan015.sh`
- 运行: `bash scripts/run_wild_data_plan015.sh`（全量）或 `bash scripts/run_wild_data_plan015.sh --dry_run`（测试）

**3. Dry-run 结果** ✓ 通过
- 两个数据源均从缓存加载
- RF 训练正常（features_all.jsonl, 20000 samples）
- Pythia-1.4B 加载到 cuda:1（通过 CUDA_VISIBLE_DEVICES=1）
- Feature extraction + classification 正常输出

**4. 预估全量运行时间**
- v3 在同一服务器上 5000 FineWeb 样本耗时 77s（feature extraction）
- 本次 2×5000 = 10000 样本，预估 **~3-5 分钟**（含模型加载和 RF 训练）

---
