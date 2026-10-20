# gpu exp 002 ner conll2003

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_gpu_exp_002_ner_conll2003_20260514T114609_result.json`
- **Structured JSON:** [`46ef7720d3796de82659.json`](../../sessions/46/46ef7720d3796de82659.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练已启动，当前状态：

**已完成：**
- CoNLL-2003 数据转换（14041 train / 3250 dev / 3453 test）
- LLaMA Factory 数据格式（train + dev）及 dataset_info.json 注册
- 训练配置 `conll2003_lora.yaml`（LoRA r=32, alpha=64, epochs=5, lr=2e-4）
- Export 配置 `export_config_conll2003.yaml`
- `sampling.py` 添加 CONLL2003_SCHEMA_HINT
- `run_mvp_pilot.py` 添加 conll2003 数据集支持
- 实验注册 registry (RUNNING)

**进行中：**
- Fine-tune 在 GPU 1 运行，step 70/4390，loss=0.107，预计 ~2h 后完成

**待完成：**
- Merge LoRA adapter
- NER pilot (N=8, T=0.7, logprobs)
- 结果分析 & registry 更新

4.5 分钟后自动轮询训练进度。

---
