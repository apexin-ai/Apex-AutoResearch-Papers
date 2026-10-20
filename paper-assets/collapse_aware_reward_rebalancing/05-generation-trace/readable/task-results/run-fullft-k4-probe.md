# run fullft k4 probe

**Does Reward Curation Kill Diversity? Systematic Evidence of Surprising Resilience in Iterative Self-Training** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_run_fullft_k4_probe_20260516T155107_result.json`
- **Structured JSON:** [`392635d58df8ac1ab41f.json`](../../sessions/39/392635d58df8ac1ab41f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

进程正常运行。Full-FT K=4 Probe 已在 cuda:1 上启动：

- **exp_id**: `carr_fullft_k4_probe_01`
- **日志**: `~/runs/collapse_aware_reward_rebalancing/carr_fullft_k4_probe_01.log`
- 已确认模型加载成功、数据集读取正常、正在生成第 0 代 candidates（16/2000）

修改总结：
- `train_sft.py`：添加 `config.USE_LORA` 条件分支，Full-FT 模式跳过 peft，直接训练所有参数并保存完整模型；LoRA 模式行为不变
- `run_quick_probe_fullft.py`：设置 `USE_LORA=False`, `LR=5e-6`, `BATCH_SIZE=2`, `GRAD_ACCUM=4`，输出到 `outputs_fullft_k4/`

---
