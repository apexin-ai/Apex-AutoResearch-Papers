# code qwen retrain chain

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_qwen-retrain-chain_20260518T165823_result.json`
- **Structured JSON:** [`464cdaebeb36c21394dd.json`](../../sessions/46/464cdaebeb36c21394dd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Dry-run 通过。全部验证完成。

---

## 报告

### 1. Qwen2.5-1.5B 确认可用
- 路径: `/root/autodl-tmp/.hf_cache/Qwen/Qwen2___5-1___5B`
- 模型大小: 2.9G (model.safetensors)
- 参数量: 1,543,714,304
- Tokenizer vocab: 151,643

### 2. LoRA target modules 确认
- `q_proj, k_proj, v_proj` 均存在于 `model.layers.*.self_attn.*`
- `detect_lora_targets()` 自动检测通过
- Trainable: 2,981,888 / 1,546,696,192 (0.19%)

### 3. 修改后脚本路径
- 服务器: `/root/autodl-tmp/gen-depth-contamination/scripts/exp_qwen_retrain_chain.py`
- 本地: `scripts/exp_qwen_retrain_chain.py`

### 4. 提交命令
```
bash -c "cd /root/autodl-tmp/gen-depth-contamination && source /root/miniconda3/bin/activate && CUDA_VISIBLE_DEVICES=0 HF_HOME=/root/autodl-tmp/.hf_cache python scripts/exp_qwen_retrain_chain.py"
```

### 5. 注意事项
- `torch_dtype` 参数在新版 transformers 中已 deprecated，建议改为 `dtype`，但不影响运行
- torch 2.8.0 版本的 cpp extensions 警告可忽略
- Qwen2.5 自带 tokenizer 无 pad_token，脚本已处理（fallback 到 eos_token）
- 数据目录 `data/exp_qwen_retrain_chain/depth_0.jsonl` 已就绪 (5000 docs)
- Self-scoring: generator 和 scorer 都是同一个 Qwen2.5-1.5B

---
