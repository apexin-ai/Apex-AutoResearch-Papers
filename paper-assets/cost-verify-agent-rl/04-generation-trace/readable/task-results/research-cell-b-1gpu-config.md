# research cell b 1gpu config

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_cell_b_1gpu_config_20260524T235538_result.json`
- **Structured JSON:** [`f8632404101d7da698d3.json`](../../sessions/f8/f8632404101d7da698d3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入 `artifacts/cell_b_1gpu_config_analysis.md`。核心结论：

**只需改 3 个参数**即可 1-GPU 等效训练：
1. `CUDA_VISIBLE_DEVICES: "0"` 
2. `n_gpus_per_node: 1`
3. `test_freq: 999`（关闭中间 validation）

**不需要调整 `gradient_accumulation` 或 `ppo_mini_batch_size`。** RAGEN 的 batch size 由 `env_groups × group_size = 128` 决定，FSDP 仅分片并行，all-reduce 保证梯度等效。已有先例（`_alfworld_hsweep_h10_1gpu.yaml`）验证了这一点。

GRPO K=8 也不受 GPU 数影响——它在 es_manager 数据生成层面控制。

98GB RTX PRO 6000 跑 Qwen3-4B 内存充裕（~60GB/98GB），预估 1-GPU 训练 15 steps 约 6-7 小时，比 2-GPU 仅慢 10-20%（瓶颈在 vLLM rollout，始终单卡）。

---
