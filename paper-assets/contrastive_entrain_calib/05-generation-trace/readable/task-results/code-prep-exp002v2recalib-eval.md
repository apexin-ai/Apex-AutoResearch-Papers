# code prep exp002v2recalib eval

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_prep-exp002v2recalib-eval_20260519T103312_result.json`
- **Structured JSON:** [`8def4094940a4de25b87.json`](../../sessions/8d/8def4094940a4de25b87.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本已创建并通过语法检查。

**汇总：**

- 脚本路径：`/root/contrastive_entrain_calib/eval/run_exp002v2recalib_unified_eval.sh`
- Checkpoint 目录：`/root/contrastive_entrain_calib/checkpoints/exp002v2_dcgrpo_cosine/`（当前有 checkpoint-500 和 checkpoint-1000，训练在 step ~1089/8000，save_steps=500）
- LoRA 确认：checkpoint-500 内有 `adapter_model.safetensors`
- Calibration 数据：`/root/mvp_v2_1_expanded/data/calibration_v2_1_expanded.jsonl`
- 输出目录：`/root/contrastive_entrain_calib/results/exp002v2recalib_unified_eval/`
- 覆盖 checkpoint 500~8000（每 500 步），自动跳过不存在和已评估的 checkpoint
- 运行方式：`CUDA_VISIBLE_DEVICES=0 bash eval/run_exp002v2recalib_unified_eval.sh`

---
