# run exp012 llama 8b r2 exp2

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_run_exp012_llama_8b_r2_exp2_20260515T195454_result.json`
- **Structured JSON:** [`3d799adaf61236447df3.json`](../../sessions/3d/3d799adaf61236447df3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据和 embeddings 加载成功（1000 samples, 64 types）。正在构建 batch configs，随后会启动 vLLM 加载模型。

任务已完成：

- **vLLM 残留进程已 kill**，GPU 内存已释放（0 / 97887 MiB）
- **exp2-only 脚本已创建**：`scripts/run_exp012_llama8b_r2_exp2only.sh`，gpu_memory_utilization 降为 0.80
- **训练任务已提交**：PID 321037，tmux session `exp012_llama_8b_r2_exp2`，日志 `~/runs/schema-dag-extraction/exp012_llama_8b_r2_exp2.log`
- 数据已加载（1000 samples），vLLM 模型即将加载

上次卡死位置：count_12/random/0 的 998/1000。如果再次卡在同一位置需要排查。

---
