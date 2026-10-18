# gpu yi15 9b full pipeline

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_gpu_yi15_9b_full_pipeline_20260514T140307_result.json`
- **Structured JSON:** [`923644e5fde1b0c34fae.json`](../../sessions/92/923644e5fde1b0c34fae.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

架构确认:
- `model_type: llama` (LlamaForCausalLM)
- `num_attention_heads: 32, num_key_value_heads: 4` → GQA 8:1
- `num_hidden_layers: 48`
- `hidden_size: 4096`

完全符合预期，标准 Llama 架构，现有 profiler/eval 代码直接兼容。

下载仍在进行 (~4 shards, 当前 shard 2/4 的 3%)。预计还需 2-3 小时（736kB/s）。下载完成后可直接提交任务：

```
模型路径: /root/autodl-tmp/.hf_cache/01ai/Yi-1___5-9B
脚本已部署: /root/ratekv/run_yi15_full_pipeline.py
```

等下载完成后提交命令：

```bash
bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/ratekv && CUDA_VISIBLE_DEVICES=1 python -u run_yi15_full_pipeline.py --model /root/autodl-tmp/.hf_cache/01ai/Yi-1___5-9B --gpu cuda:0 2>&1 | tee yi15_full.log"
```

注意：`CUDA_VISIBLE_DEVICES=1` 让物理 cuda:1 映射为 cuda:0，所以脚本里用 `--gpu cuda:0`。

要我现在轮询等待下载完成再提交，还是你稍后手动触发？

---
