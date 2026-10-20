# ops eval script prep

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_eval-script-prep_20260514T225839_result.json`
- **Structured JSON:** [`ee1b5bb697cdf8d95da0.json`](../../sessions/ee/ee1b5bb697cdf8d95da0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总

| 项目 | 状态 |
|------|------|
| **checkpoint-80** | 存在，完整（adapter_model.safetensors 252MB + tokenizer + optimizer） |
| **checkpoint-100** | 存在，完整（同上，保存于 06:43） |
| **eval 脚本** | **已创建** — `eval_lr5e6_ckpt80.sh`（GPU 2）、`eval_lr5e6_ckpt100.sh`（GPU 3） |
| **训练进度** | 最新 checkpoint 为 step 100，目录中有 checkpoint-20/40/60/80/100，训练仍在进行中（4 张 GPU 均有负载） |
| **GPU 占用** | GPU 0: 13.6/32.6G (62%) · GPU 1: 9.7/32.6G (87%) · GPU 2: 11.2/32.6G (71%) · GPU 3: 9.7/32.6G (73%) |

脚本基于 ckpt-60 模板创建，output_dir 分别为 `eval_results/lr5e6_r1_ckpt80` 和 `lr5e6_r1_ckpt100`，其余参数一致。4 张 GPU 当前都在被训练占用，eval 需要等训练完成或在训练间隙执行。

---
