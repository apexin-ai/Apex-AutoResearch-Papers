# code westd grasp baseline

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_westd-grasp-baseline_20260515T114735_result.json`
- **Structured JSON:** [`9144487636bd25d515c7.json`](../../sessions/91/9144487636bd25d515c7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

当前状况：

- **cuda:0 被占用**：RASP re-eval 正在运行（PID 25036，`eval_gsm8k.py --model_path pruned_rasp_20 --max_samples 100`），结果文件尚未生成
- **cuda:1 空闲**：0% util, 0 MiB
- **GRASPrune 外部仓库不存在**，但有原生实现 `run_grasp_prune.sh` + `grasp_scoring.py`（GraSP scoring → prune.py --mode standard）
- **模型路径需修正**：脚本写的 `/root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B`，实际是 `/root/autodl-tmp/models/DeepSeek-R1-Distill-Qwen-7B`
- **`run_grasp_prune.sh` 没有 eval 步骤**，prune 完需要手动跑 eval

用 cuda:1 启动 GraSP（两个 GPU 都属于本项目，C003），还是等 cuda:0 空出来？

---
