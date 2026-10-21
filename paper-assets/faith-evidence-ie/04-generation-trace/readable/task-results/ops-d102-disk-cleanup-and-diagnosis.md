# ops d102 disk cleanup and diagnosis

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_d102_disk_cleanup_and_diagnosis_20260518T071841_result.json`
- **Structured JSON:** [`007c573074a32e0732a8.json`](../../sessions/00/007c573074a32e0732a8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

### 1. 磁盘清理
- **释放 ~130GB**（250G → 120G used），当前可用 **131GB (48%)**
- 删除内容：GRPO 全部 (~4G)、旧 RSFT mvp2/k=3 系列 (~115G)、合并模型 (~8G)、损坏 ckpt (~0.6G)

### 2. D102 Checkpoint 状态

| 实验 | 输出目录 | 最后完好 ckpt | 进度 | epoch | loss |
|---|---|---|---|---|---|
| 8B s42 | rsft_output_qwen3_8b_k1 | **checkpoint-250** | 250/1134 (22%) | 0.66 | 0.485 |
| 8B s43 | rsft_output_qwen3_8b_k1_s43 | **checkpoint-250** | 250/1134 (22%) | 0.66 | 0.523 |
| 1.7B s42 | rsft_output_qwen3_1_7b_k1 | **checkpoint-250** | 250/567 (44%) | 1.32 | 0.564 |
| LLaMA 8B s42 | rsft_output_llama_3_1_8b_k1 | **checkpoint-250** | 250/1107 (23%) | 0.68 | 0.488 |

全部在 step 300 因磁盘满崩溃（EXIT_CODE=1）。1.7b 的 checkpoint-300 已损坏并删除。

### 3. GPU 状态
4 张 GPU 全部空闲（0% 利用率，0 MiB 显存占用）。

### 4. 推荐：全部 resume from checkpoint-250
- 4 个实验都有完好的 checkpoint-250，可直接 `--resume_from_checkpoint checkpoint-250`
- 4 张 GPU 空闲，可并行启动全部 4 个训练
- 131GB 可用空间足够完成剩余训练（每个实验最多再产生 ~10G checkpoint）

---
