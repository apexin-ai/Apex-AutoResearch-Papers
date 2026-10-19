# ops disk cleanup investigation

**error diag dpo recovery** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_disk-cleanup-investigation_20260512T161452_result.json`
- **Structured JSON:** [`7d9963b5f5db8e6c72b7.json`](../../sessions/7d/7d9963b5f5db8e6c72b7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。以下是磁盘使用全景和清理建议。

---

## 磁盘使用全景（169G / 169G = 100%）

| 路径 | 大小 | 说明 |
|------|------|------|
| `structfuse/checkpoints/` | **100G** | 9组 p2b 训练 checkpoint（另一个项目） |
| `structfuse/models/` | **5.8G** | Qwen2.5-Coder-3B（structfuse 专用） |
| `structfuse/` 其余 | **~1G** | 日志、脚本、数据 |
| `.hf_cache/Qwen3-8B` | **19G** | Qwen3-8B 全精度缓存 |
| `.hf_cache/Qwen3-14B-AWQ` | **9.4G** | Qwen3-14B-AWQ 缓存 |
| `.hf_cache/models--openai-community--gpt2` | **4.9G** | GPT-2（可疑，GPT-2 不该这么大） |
| `.hf_cache/models--gpt2` | **3.5G** | GPT-2 另一份缓存 |
| `.hf_cache/SWE-bench___swe-smith` | **4.9G** | SWE-smith 数据集缓存 |
| `models/Qwen/Qwen2___5-7B-Instruct` | **15G** | ModelScope 下载的 Qwen2.5-7B（另有 552M 重复拷贝） |
| `alfworld_data/` | **2.2G** | ALFWorld 环境数据 |
| `mvp_results/` | **1.7G** | structfuse MVP 评测结果 |
| `gpt2-small/` | **526M** | GPT-2 small 权重 |
| 其余 | ~1G | repos, mvp_data, error_diag_dpo_recovery 等 |

---

## 清理建议

### 可以安全删除（共 ~136G）

| 项 | 大小 | 理由 |
|----|------|------|
| `structfuse/checkpoints/` 已完成的 runs | **~96G** | 5个已完成的 checkpoint（p2b_embedding_distance_s42/s123, p2b_random_s42/s123/s456 各 24G/7G）。**注意：p2b_dataflow_aware_s456 正在训练中（PID 248524），不能删。** |
| `.hf_cache/models--gpt2` + `.hf_cache/models--openai-community--gpt2` | **8.4G** | GPT-2 缓存，当前项目不需要 |
| `.hf_cache/SWE-bench___swe-smith` | **4.9G** | SWE-smith 数据集，属于 structfuse，非本项目 |
| `gpt2-small/` | **526M** | 独立 GPT-2 副本 |
| `mvp_results/` | **1.7G** | structfuse MVP 评测产出 |
| `structfuse/dryrun_repos/` | **554M** | dry run 临时克隆的 repos |
| `error_diag_dpo_recovery/data/trajectories_v3/` + `trajectories_v3_test/` | **400K** | 有毒轨迹数据（v1/v2 已不存在，v3 还在） |
| `models/Qwen2.5-7B-Instruct/`（552M 的那份） | **552M** | 重复拷贝，15G 主拷贝在 `models/Qwen/` |

### 需要确认

| 项 | 大小 | 问题 |
|----|------|------|
| **`structfuse/` 整个目录** | **107G** | 这是另一个项目。当前有训练进程在跑（PID 248524, GPU:4），还有 `run_mvp.py`（PID 98594, GPU:5）。**如果 structfuse 实验已不需要，删掉整个目录可回收 107G。** 但需等运行中的进程结束或手动 kill。 |
| **`models/Qwen/Qwen2___5-7B-Instruct`** | **15G** | democalib DPO 训练（PID 170853）正在使用。训练完成后如果不再需要可删除。 |
| **`.hf_cache/Qwen3-8B`** | **19G** | 项目需要的模型（4-bit），但缓存的是全精度。确认是否还需要。 |
| **`.hf_cache/Qwen3-14B-AWQ`** | **9.4G** | 项目需要的模型。保留。 |
| **`alfworld_data/`** | **2.2G** | error_diag_dpo_recovery 的环境数据，可能仍需要。 |

### 推荐优先级

1. **先删 GPT-2 相关**（3 项共 ~9.4G）— 无进程使用，纯冗余
2. **删 structfuse 已完成 checkpoints**（~96G）— 回收最多空间。需确认哪些 seed 的结果已保存到 wandb/评估完毕
3. **删 SWE-smith 缓存 + mvp_results**（~6.6G）— structfuse 专用
4. **考虑清理 structfuse 整体**（需等进程结束）

请确认哪些可以执行删除。

---
