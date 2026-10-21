# code prompted generation

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_prompted_generation_20260517T084602_result.json`
- **Structured JSON:** [`9e93c6742cb49c7551fd.json`](../../sessions/9e/9e93c6742cb49c7551fd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

plan_016 已全部执行完毕：

- **脚本**: `scripts/prompted_generation_eval.py` (560行) 已部署到 gpu-6000pro-2
- **实验 ID**: `prompted_gen_gpt2xl_001`, status=RUNNING, parent=cross_model_gpt2xl_001
- **GPU**: cuda:1, PID 695547
- **流程**: 50 topic prompts × 100 samples/prompt = 5000/depth, 4 depths → Pythia-1.4B 特征提取 → RF 5-fold CV
- **日志**: `logs/prompted_gen_gpt2xl_001.log`
- **预计耗时**: 3-6h (generation + 3x LoRA fine-tune + feature extraction + classification)

---
