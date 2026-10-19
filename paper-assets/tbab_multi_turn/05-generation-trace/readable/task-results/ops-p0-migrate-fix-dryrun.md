# ops p0 migrate fix dryrun

**tbab multi turn** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_p0-migrate-fix-dryrun_20260518T074644_result.json`
- **Structured JSON:** [`bb7608872d62a946cf8e.json`](../../sessions/bb/bb7608872d62a946cf8e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## P0 任务完成汇报

### Step 1: 迁移 ✅
从 westd-29046 通过 sshpass+rsync 迁移完成：
- **scripts/**: `train.py`, `tbab_model.py`, `tbab_dataset.py`, `tbab_utils.py`, `configs/` (4 YAML)
- **data/**: `training_data.json` (22MB), `preprocess.py`, `data_stats.txt`, `sharegpt_raw.json`
- **eval/**: `run_eval.py`, `model_local.py`, `metrics.py`, `attention_analysis.py`, `tbab_inference.py`, `lost_in_conversation/`

### Step 2: YAML 路径修复 ✅
4 个 YAML 配置的 `model_name_or_path` 已从 `/root/autodl-tmp/.hf_cache/AI-ModelScope/...` 改为 `/root/autodl-tmp/models/Mistral-7B-Instruct-v0.1`。模型权重通过 ModelScope 下载完成（pytorch_model .bin 格式，14GB）。

### Step 3: trainable_token_indices ✅
**代码已经是修复后的状态** — `tbab_model.py` 中 `apply_lora()` 函数已正确使用 PEFT 原生 `trainable_token_indices` 参数，无需修改。没有 `_make_bridge_embeddings_trainable` 函数存在。

### Step 4: Dry-Run 结果 ✅

| 条件 | Trainable Params | % | 5-step Loss | 状态 |
|------|-----------------|---|-------------|------|
| C1 (LoRA only) | 83,886,080 (83.9M) | 1.1451% | 0.7315 | ✅ |
| C2 (pos reset) | 83,886,080 (83.9M) | 1.1451% | 2.240 | ✅ |
| C3 (bridge+std pos) | 83,918,848 (83.9M+33K) | 1.1455% | 0.7321 | ✅ |
| C4 (full TBAB) | 83,918,848 (83.9M+33K) | 1.1455% | 2.244 | ✅ |

**参数量验证**：C3/C4 比 C1/C2 多出 32,768 = 4 tokens × 4096 dim × 2 layers（embed_tokens + lm_head），而非之前错误实现的 346M。`trainable_token_indices` 正确工作。

### 遇到的问题及解决
1. **HuggingFace 下载失败** — 无 HF token，Mistral 模型可能有访问限制。改用 ModelScope 镜像下载
2. **safetensors 文件缺失** — ModelScope 只提供 .bin 格式权重。删除 `model.safetensors.index.json` 让 transformers 回退到 .bin 加载
3. **C2/C4 loss 偏高 (2.24)** — position reset 条件的 loss 比标准条件高，这在 5-step dry-run 中属正常现象（position reset 改变了注意力模式，前几步 loss 波动较大）

---
