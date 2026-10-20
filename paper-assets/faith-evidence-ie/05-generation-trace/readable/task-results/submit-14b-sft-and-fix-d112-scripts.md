# submit 14b sft and fix d112 scripts

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_submit_14b_sft_and_fix_d112_scripts_20260519T040209_result.json`
- **Structured JSON:** [`f78260bbb69e01e70890.json`](../../sessions/f7/f78260bbb69e01e70890.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个任务完成。

### 任务 A：D112 step3/step4 脚本修复 ✅
- `step3_k1_filter_and_train.sh` 和 `step4_eval.sh` 均已在 `export HF_HOME=` 后加入 `HF_HUB_OFFLINE=1` 和 `TRANSFORMERS_OFFLINE=1`

### 任务 B：14B SFT 训练提交 ✅
- **exp_id**: `plan017_14b_sft`
- **GPU**: cuda:1 (14.6GB) + cuda:2 (11.9GB)，DeepSpeed ZeRO-3 + CPU offload
- **PID**: 611578, 611579
- **tmux**: `plan017_14b_sft`
- **总步数**: 144 步（3 epoch）
- **修复的问题**:
  1. 从脚本中移除了硬编码的 `CUDA_VISIBLE_DEVICES=2,3`
  2. 创建了 `deepspeed_zero3_14b.json`（14B 专用配置）
  3. 在 sft_trainer.py 中添加 `unset_hf_deepspeed_config()` 解决 ZeRO-3 init 与 "auto" config 值的冲突（模型先加载到 CPU，Trainer 再处理 ZeRO-3 分区）

**注意**: 脚本中 `max_length=4096`（任务说明提到 2048），保持原值未修改。如需调整请告知。

---
