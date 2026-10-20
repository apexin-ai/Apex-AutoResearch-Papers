# diagnose w5 llama constrained eval

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_w5_llama_constrained_eval_20260515T173641_result.json`
- **Structured JSON:** [`5b19c9a2818164670df7.json`](../../sessions/5b/5b19c9a2818164670df7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断报告

### 1. 崩溃原因
**FileNotFoundError**: `'data/scierc/test.json'` 不存在（`run_constrained_extraction.py:67` 的 `load_scierc_data`）。命令参数路径错误：
- `--data_path data/scierc/test.json` ❌ → 实际路径 `data/processed_data/test.json` ✓
- `--constraints_path data/scierc/ontology_constraints.json` ❌ → 实际路径 `ontology_constraints.json`（项目根目录）✓

注：`data/` 下只有 `docred/`、`processed_data/`、`sft/`，**没有 `scierc/` 子目录**。

### 2. GPU 状态
- **GPU 0**: PID **287677** 占 17160 MiB / 89% util。**不是僵尸**——是同 wave 的 unconstrained baseline (`w5_llama_lora_scierc_unconstrained`)，跑了 17:49 分钟还在进行
- **GPU 1**: 空闲（0 MiB / 0%），可用

### 3. Llama LoRA merged checkpoint 实际路径
- 符号链接: `/root/schema_semantic_constrained_ie/checkpoints/llama_lora_scierc_merged`
- 实指向: `/root/autodl-tmp/checkpoints/llama_lora_scierc_merged/`
- 完整: 4 shards safetensors (~15GB) + tokenizer.json + config.json + chat_template.jinja，齐全

### 4. type_mask_processor.py 是 clean 版本？
**是 clean 版本（在 `compiler/` 子目录下）**。证据：
- 字节数 15666 = `type_mask_processor_clean.py` 完全一致（cf_fallback 版本 20195 bytes / 490 lines）
- 行数 399 = clean 版本相同
- `grep -c fallback type_mask_processor.py` = **0**（cf_fallback 版本 27 处）
- mtime 01:19:09，比 .bak 新（说明有人手动从 clean 版恢复过）

### 5. 需要修复的内容
**代码无需改动**。只需修正提交命令的 `--data_path` 和 `--constraints_path`。磁盘 19G 空闲，无问题。

### 6. 推荐重新提交命令
```
bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/schema_semantic_constrained_ie && WANDB_MODE=disabled python3 run_constrained_extraction.py --mode full_s1 --dataset scierc --model_path checkpoints/llama_lora_scierc_merged --data_path data/processed_data/test.json --constraints_path ontology_constraints.json --output_path outputs/w5_llama_lora_scierc_constrained.jsonl --device cuda:0 --batch_size 1 --max_new_tokens 4096"
```

提交时指定物理 GPU 1（GPU 0 被 unconstrained 占用），`--device cuda:0` 保留以匹配 `CUDA_VISIBLE_DEVICES=1` 注入后的逻辑映射。

---
