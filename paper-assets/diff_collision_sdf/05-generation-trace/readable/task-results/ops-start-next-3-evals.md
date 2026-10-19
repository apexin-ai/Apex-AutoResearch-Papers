# ops start next 3 evals

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_start_next_3_evals_20260525T125144_result.json`
- **Structured JSON:** [`00f15d42c8513b722e35.json`](../../sessions/00/00f15d42c8513b722e35.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

3 个 eval 都在加载模型阶段（"Creating PI0Pytorch model and injecting LoRA..."），正常——加载完权重后才会占 GPU 显存。

## 结果

| GPU | 任务 | PID | 状态 |
|-----|------|-----|------|
| cuda:0 | spatial_bowl 训练 | - | 27GB 占用，100% 利用率 |
| cuda:1 | eval s2_l01 30K | 260018 | 模型加载中 |
| cuda:2 | eval s0_l005 30K | 260019 | 模型加载中 |
| cuda:3 | eval s0_l01 30K | 260020 | 模型加载中 |

**JSON 覆写修复**：使用 `--output_path` 指定唯一路径（`--seed` 统一为 0 不影响 eval 行为），3 个输出互不干扰：
- `/root/autodl-tmp/eval_results/eval_s2_l01_30k.json`
- `/root/autodl-tmp/eval_results/eval_s0_l005_30k.json`
- `/root/autodl-tmp/eval_results/eval_s0_l01_30k.json`

同时用 `CUDA_VISIBLE_DEVICES` 隔离 GPU（脚本内 `--gpu 0` 映射到可见的唯一卡），比直接 `--gpu N` 更可靠。

---
