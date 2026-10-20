# code graspune adapt

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_graspune_adapt_20260515T035058_result.json`
- **Structured JSON:** [`d90140e05d22285802aa.json`](../../sessions/d9/d90140e05d22285802aa.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有验证通过。GPU 约束检查正常拦截非法 GPU ID。

---

## 报告

### Pipeline 状态：就绪

完整链路：
```
run_graspune.sh
  Phase 1: GRASPrune train.py (gate pruning, GSM8K calibration, 80% keep) 
           → pruned_state_dict.safetensors + meta.json
  Phase 2: convert_graspune_to_hf.py (rebuild → HF格式，含per-layer config)
           → model.safetensors + config.json + tokenizer
  Phase 3: eval_gsm8k.py (通过model_utils.load_pruned_model加载非均匀剪枝模型)
           → results/eval_pruned_graspune_20_greedy.json
```

### 修复内容

| 文件 | 修改 |
|------|------|
| `src/run_graspune.sh` | 添加 C001 GPU 约束验证；Phase 1/2 增加跳过逻辑（输出已存在时）；添加 Phase 3 eval 步骤；输出路径改到数据盘（C002）|
| `src/convert_graspune_to_hf.py` | 修复 `json.dump` 文件句柄泄漏 |
| `src/model_utils.py` | 新增（本地缺失），处理非均匀 per-layer 维度的模型加载 |

### 无 blocker

- GRASPrune 支持 `--model-family qwen` + DeepSeek-R1-Distill-Qwen-7B ✓
- 20% sparsity: `--keep-ratio 0.80` ✓
- GSM8K 校准: `--train-dataset gsm8k` ✓
- GQA 兼容: GRASPrune 在 KV group 粒度剪枝，`model_utils` 正确处理 per-layer num_heads/num_kv_heads ✓
- 所有 import 和语法验证通过 ✓

### 预估运行时间

- Phase 1 (GRASPrune pruning): ~30-45 min（4 epochs × 512 samples，7B 模型单卡）
- Phase 2 (Convert): ~3-5 min（CPU 上加载+保存）
- Phase 3 (GSM8K eval): ~2-3 hrs（1319 题，greedy，max 4096 tokens）
- **总计: ~3-4 小时**

---
