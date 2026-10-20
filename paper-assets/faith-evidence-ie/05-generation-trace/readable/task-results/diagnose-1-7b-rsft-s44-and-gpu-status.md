# diagnose 1 7b rsft s44 and gpu status

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_1_7b_rsft_s44_and_gpu_status_20260519T034324_result.json`
- **Structured JSON:** [`24162587c60b285842e7.json`](../../sessions/24/24162587c60b285842e7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练完成，`should_training_stop: true`，max_steps=567 全部完成。

## 诊断结论

### 1. plan019_1_7b_rsft_s44：**SUCCESS（正常完成，cron 误判）**

- PID 602749 已正常退出（非 crash）
- 训练完成全部 567 steps（3 epochs），`should_training_stop: true`
- 最终 loss=0.5539，token_accuracy=0.8707，epoch=2.963
- Checkpoint 路径：`/root/autodl-tmp/rsft_output_qwen3_1_7b_k1_s44/`
  - `adapter_model.safetensors` (279MB)，写入时间 11:29
  - checkpoint-550, checkpoint-567
- 无 tmux session 残留（正常退出后已关闭）
- 日志文件 `/root/runs/faith-evidence-ie/plan019_1_7b_rsft_s44.log` 不存在（可能 tmux 未配置 logging 或命名不同）

### 2. 全卡 GPU 状态

| GPU | 显存占用 | 利用率 | PID | 实验 |
|-----|---------|--------|-----|------|
| 0 | 1501/32607 MiB | 41% | 604576 | D112 CED scoring (`rsft_score_filter`, rsft_scored_4b_sft_s44) |
| 1 | 0 MiB | 0% | - | **空闲** |
| 2 | 0 MiB | 0% | - | **空闲** |
| 3 | 18891/32607 MiB | 70% | 598911 | 8B RSFT s44 eval (`rsft_8b_k1_s44_eval`) |

### 3. D112 step 2 (PID 604576)：正常运行中
- 进度：8000/24216 records scored
- 任务：`rsft_score_filter` 对 `rsft_generations_4b_sft_s44` 做 CED 打分
- GPU 0，显存 1.5GB

### 4. 额外发现
- GPU 3 上 PID 598911 是 8B RSFT s44 的 eval 推理，占用 18.9GB，正常运行
- GPU 1 和 GPU 2 均空闲，可用于新任务

---
