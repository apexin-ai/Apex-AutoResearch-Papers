# code random reweight baseline

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_random_reweight_baseline_20260516T061055_result.json`
- **Structured JSON:** [`0f8e9fac8471e8999887.json`](../../sessions/0f/0f8e9fac8471e8999887.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

**结果：脚本已就绪，无需新建。**

现有代码已完整支持 random reweight baseline：

- **训练代码**：`/root/provenance_weight_training/training/pretrain_weighted.py`（line 174）已实现 `--weighting_method random`
  - 每 batch 从 U(0,2) 独立采样权重
  - 归一化到 mean=1
  - 不使用 q_score 信息
- **启动脚本**：`/root/provenance_weight_training/scripts/run_random_reweight_seed42.sh`
  - 参数与 adaptive_v2_seed42 一致（batch_size=4, grad_accum=4, lr=5e-5, seed=42, 200M tokens → 6103 steps, Qwen3-0.6B, bf16）
  - 输出到 `output/models/random_reweight_seed42`
  - wandb run name: `random_reweight_seed42`

**启动命令**（正式训练时）：
```bash
cd /root/provenance_weight_training && bash scripts/run_random_reweight_seed42.sh
```

Dry-run 验证通过：3 步训练正常，random 权重 ESS 在 2.6~3.8 间（batch size=4 的合理范围），weighted_loss 与 unweighted_loss 有差异，符合预期。

---
