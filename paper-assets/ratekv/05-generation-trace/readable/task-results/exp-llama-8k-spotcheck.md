# exp llama 8k spotcheck

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_llama_8k_spotcheck_20260515T133243_result.json`
- **Structured JSON:** [`d7336e77911c6c335268.json`](../../sessions/d7/d7336e77911c6c335268.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验已启动并运行中。

**状态**：
- 脚本 `run_llama_8k_spotcheck.py` 已部署到 westd-37397
- tmux session `llama_8k_spotcheck` 在 cuda:0 上运行
- Profiles 已加载并合并（hires 2-bit + standard 4/8-bit）
- MCKP 求解完成：bit distribution {4: 253, 8: 1, 2: 2}（与 2K 结果一致）
- 模型已加载，WikiText-2 8K eval 进行中
- Registry: `llama_8k_spotcheck` → RUNNING

**配置**：
- 模型：Llama-3.1-8B（`/root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-8B`）
- k=2, budget=0.25, seq_len=8192, stride=8192
- 2K 参考：baseline=8.0922, MCKP=8.5042, uniform=8.4701（MCKP 改进 -9.01%，Spike 特征）

---
