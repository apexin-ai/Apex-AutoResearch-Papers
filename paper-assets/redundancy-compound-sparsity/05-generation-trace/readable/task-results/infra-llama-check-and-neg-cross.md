# infra llama check and neg cross

**When Does KV Redundancy Predict MLP Sparsity? Architecture Dependence of Cross-Axis Signals in Reasoning Inference** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_llama-check-and-neg-cross_20260512T015202_result.json`
- **Structured JSON:** [`1f4464f1155e840421e8.json`](../../sessions/1f/1f4464f1155e840421e8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Dry-run 通过。

**结果汇总：**

1. **Llama 下载**：已完成。30GB，4 个 safetensors 文件齐全，tokenizer 验证通过（vocab=128256）。

2. **neg_cross_model_llama.py**：已写好并上传到 `/home/sonny/redundancy-compound-sparsity/results/neg_cross_model/neg_cross_model_llama.py`。Dry-run 通过：
   - 模型加载正常：32 layers, 8 KV heads, 14336 intermediate_size
   - Hook 注册和数据收集均工作（Pearson r=0.406, K-S test 有显著结果）
   - VRAM 使用可控，RTX 5090 (32GB) 足够
   - Dry-run 耗时 ~8s（含模型加载）

3. **GPU 状态**：当前空闲（0% utilization, 0MB used），kv-bench-001 未在运行。实际上现在可以立即提交 full run，但按指示不提交。

**运行命令**（GPU 可用时）：
```bash
cd /home/sonny/redundancy-compound-sparsity/results/neg_cross_model
nohup python neg_cross_model_llama.py > neg_cross_model.log 2>&1 &
```

---
