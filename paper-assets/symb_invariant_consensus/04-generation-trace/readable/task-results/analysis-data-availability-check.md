# analysis data availability check

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_data-availability-check_20260518T095819_result.json`
- **Structured JSON:** [`415ae678c41744420410.json`](../../sessions/41/415ae678c41744420410.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 报告

### exp-001 traces 数据: **不可用**

原始数据在已回收的 westd-32608 上，路径为 `results/sica_expanded_14b.json`。westd-25068 的 `results/` 目录为空，无 intermediates 目录，无大 JSON 文件。

本地仅存元数据（非原始 traces）：
- `artifacts/sica_expanded_14b/data/sica_expanded_14b_config.txt` — 实验配置（K=12, 804题, temp=0.7）
- `artifacts/sica_expanded_14b/report/exp001_analysis_summary.txt` — 汇总指标（SICA 76.49% vs SC 76.24%）
- `artifacts/exp-001/data/f2_per_problem_metadata.txt` — 307 条 multi-candidate 问题元数据（指向 westd-32608 上的 CSV）

**结论：原始 K=12 traces 数据已随 westd-32608 回收丢失，需重新生成。**

### 模型可用性（westd-25068）

| 模型 | 状态 |
|------|------|
| Qwen2.5-14B-Instruct | **下载中**（权重在 `._____temp/`，8个 shard 已部分下载，总计 ~569MB，完整应 ~28GB） |
| Qwen2.5-72B-Instruct | 已下载（39GB） |
| LLaMA-3.1-8B-Instruct | **未下载** |
| Mistral-7B-Instruct-v0.3 | **未下载** |

### 建议下一步

1. 等 Qwen-14B 下载完成后，重跑 exp-001（K=12, 804题）生成 traces，这次加 `--save-intermediates` 并将结果同步到本地备份
2. LLaMA-8B 和 Mistral-7B 需要额外下载（cross-model extraction 依赖）

---
