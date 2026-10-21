# exp olmo seed43 001

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_olmo_seed43_001_20260518T151655_result.json`
- **Structured JSON:** [`91fda0aec3647b1b3ef6.json`](../../sessions/91/91fda0aec3647b1b3ef6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验已提交并注册为 RUNNING。

**总结：**
- `olmo_seed43_001` 已在 gpu-6000pro-2 cuda:1 上启动（tmux session: `olmo_seed43`, PID 903688）
- 脚本：`scripts/run_olmo_seed43.sh`，8 步全流程（3 轮 LoRA finetune + 3 轮生成 + 特征提取 + RF eval）
- 参数：OLMo-1B-hf, seed=43, nucleus p=0.95, 5000 samples/depth, d0-d3
- LoRA target modules: `q_proj,k_proj,v_proj`（OLMo 特有，区别于 Pythia 的 `query_key_value`）
- Step 1 LoRA finetune 已在执行中
- 预计 ~2h 完成，日志在 `results/olmo_seed43/pipeline.log`

---
