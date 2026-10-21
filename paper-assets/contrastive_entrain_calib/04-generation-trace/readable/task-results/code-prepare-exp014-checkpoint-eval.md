# code prepare exp014 checkpoint eval

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_prepare-exp014-checkpoint-eval_20260519T082049_result.json`
- **Structured JSON:** [`8c87d4545888ae29c2ce.json`](../../sessions/8c/8c87d4545888ae29c2ce.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本已就绪。汇报：

| 项目 | 路径 |
|------|------|
| **脚本** | `/root/contrastive_entrain_calib/eval/run_exp014_eval.sh` |
| **Checkpoint** | `/root/contrastive_entrain_calib/checkpoints/exp014_probe_baseline/checkpoint-3000/` |
| **Eval 数据** | `/root/contrastive_entrain_calib/data/sycon_eval_from_calib.jsonl` (362 samples) |
| **输出目录** | `/root/contrastive_entrain_calib/results/exp014_checkpoint3000_eval/` |

脚本使用 `--compare-base` 模式，会先跑 base Qwen3-8B 再跑 LoRA，输出含 delta 对比报告。NLI 模型 (`cross-encoder/nli-deberta-v3-base`) 已在本地缓存，无需联网。

**预估运行时间**：sycon_bench 362 samples，compare 模式需加载模型两次（base + LoRA），每轮多 turn 推理，单 GPU 预计 **40-60 分钟**。

GPU 3 空闲后直接 `bash /root/contrastive_entrain_calib/eval/run_exp014_eval.sh` 即可。

---
