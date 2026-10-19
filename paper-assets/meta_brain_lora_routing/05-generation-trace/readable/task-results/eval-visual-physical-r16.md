# eval visual physical r16

**Meta-Brain: Perturbation-Diagnostic Routing of LoRA Experts for Parameter-E cient VLA Robustness** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_visual_physical_r16_20260516T070121_result.json`
- **Structured JSON:** [`16a8f3a178316996bc3c.json`](../../sessions/16/16a8f3a178316996bc3c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个评估任务已成功提交并运行中：

| 实验 | tmux session | PID | 命令 |
|------|-------------|-----|------|
| `eval_visual_r16` | `eval_visual_r16` | **408926** | `CUDA_VISIBLE_DEVICES=1 python phase1/evaluate_libero_plus.py --lora_visual_dir .../lora_visual_r16/final/ --routing par --gpu 0 --num_episodes 50 --seeds 42` |
| `eval_physical_r16` | `eval_physical_r16` | **408929** | `CUDA_VISIBLE_DEVICES=1 python phase1/evaluate_libero_plus.py --lora_physical_dir .../lora_physical_r16/final/ --routing par --gpu 0 --num_episodes 50 --seeds 42` |

注意：两个任务同时在 GPU 1 上启动了（都设了 `CUDA_VISIBLE_DEVICES=1`），可能会争抢显存。如果 OOM，需要改为串行执行。日志分别在：
- `/root/meta_brain_lora_routing/phase1/outputs/eval_visual_r16.log`
- `/root/meta_brain_lora_routing/phase1/outputs/eval_physical_r16.log`

---
