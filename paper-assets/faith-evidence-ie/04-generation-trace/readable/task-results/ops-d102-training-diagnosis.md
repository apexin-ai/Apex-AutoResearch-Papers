# ops d102 training diagnosis

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_d102_training_diagnosis_20260518T071617_result.json`
- **Structured JSON:** [`b3ffc6335a254481aa61.json`](../../sessions/b3/b3ffc6335a254481aa61.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

### 根因：磁盘空间 100% 满

`/root/autodl-tmp` 250G 全部用完（Avail=140K），4 个任务全部在 **step 300 保存 checkpoint 时因磁盘满而崩溃**。

### 各实验状态

| 实验 | 进度 | Epoch | 错误 | 最新完整 checkpoint |
|---|---|---|---|---|
| **d102_8b_rsft_k1_s42** | 300/1134 (26%) | 0.80 | `No space left on device` | checkpoint-250 |
| **d102_8b_rsft_k1_s43** | 300/1134 (26%) | 0.80 | `No space left on device` | checkpoint-250 |
| **d102_1_7b_rsft_k1_s42** | 300/567 (53%) | 1.59 | `iostream error` (磁盘满导致写入损坏) | checkpoint-250 或 300（需验证完整性）|
| **d102_llama_rsft_k1_s42** | 300/1107 (27%) | 0.81 | `No space left on device` | checkpoint-250 |

### GPU 状态
4 张 RTX 5090 全部空闲（0% 利用率，0 MiB 显存）。

### 磁盘空间分布（rsft_output 目录）
旧实验输出占大量空间，仅 `rsft_output_*` 就有 ~140G：
- 旧的 k3 实验输出（`rsft_output_qwen3_8b`, `rsft_output_llama_3_1_8b_seed43` 等）各 4-11G
- D102 新实验的部分 checkpoint 也占了 ~34G

### 需要的操作
1. **清理旧实验输出**释放磁盘空间——确认哪些旧的 `rsft_output_*` 可以删除
2. 考虑删除 checkpoint-300 的损坏文件
3. 清空后可从 checkpoint-250 resume 或重新训练

需要我列出哪些旧目录可以安全删除吗？

---
