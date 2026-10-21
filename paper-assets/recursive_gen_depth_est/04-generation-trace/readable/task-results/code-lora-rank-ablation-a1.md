# code lora rank ablation a1

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_lora_rank_ablation_a1_20260516T174023_result.json`
- **Structured JSON:** [`203d73e4add4a64a626b.json`](../../sessions/20/203d73e4add4a64a626b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验已正常启动，rank=4 阶段正在加载模型。

**总结：**
- 修改了 `scripts/lora_finetune.py`，新增 `--lora_rank` / `--lora_alpha` CLI 参数
- 创建了 `scripts/run_lora_rank_ablation.sh`（循环 rank∈{4,16,64}，每个跑完整 pipeline：LoRA finetune×3 → generate×3 → feature extraction）
- ���建了 `scripts/eval_lora_rank_ablation.py`（5-fold CV + summary.json 输出）
- 已提交到 cuda:0，exp_id=`lora_rank_ablation_001`，预计 ~3h 完成
- 结果将写入 `/root/autodl-tmp/recursive_gen_depth_est/results/lora_rank_ablation/summary.json`

---
