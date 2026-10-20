# review exp015 code preaudit

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_review_exp015_code_preaudit_20260513T232844_result.json`
- **Structured JSON:** [`f3f1cf98e4c66e2de0cd.json`](../../sessions/f3/f3f1cf98e4c66e2de0cd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部检查完成。以下是预审报告：

---

## exp-015 Neural Probe 预审报告

### 检查结果总览

| 检查项 | 状态 | 说明 |
|--------|------|------|
| 代码完整性 | ✅ | 400 行，无 TODO/FIXME/placeholder |
| Dry-run 输出 | ✅ | JSON 格式完整，K\*=2 与 lgbm 一致 |
| 模型路径 | ✅ | model.safetensors (3GB) + tokenizer 均在位 |
| 数据路径 | ✅ | data_exp017_qwen_cont/ 6×5000 samples，格式匹配 |
| LightGBM baseline | ✅ | results_exp017_qwen_cont/pairwise_auc.json 存在，格式匹配 |
| 依赖包 | ✅ | sklearn=1.8.0, transformers=4.57.6, torch=2.10.0+cu128 |
| GPU 内存 | ✅ | 峰值 ~5GB（模型 3GB + hidden_states ~1.5GB + misc），远低于 24GB |

### 问题清单

**无阻塞性问题。** 代码可直接提交运行。

一个可选优化（非阻塞）：`output_hidden_states=True` 会保留全部 29 层 hidden states（~1.1GB），但只用最后一层。可改为通过 `model.model(**inputs).last_hidden_state` 避免多余内存占用，但当前 24GB 完全够用，不影响运行。

### GPU 内存估算明细

| 组件 | 内存 |
|------|------|
| Qwen2.5-1.5B fp16 weights | ~3.0 GB |
| 29 层 hidden states (batch=24, seq=512, dim=1536) | ~1.1 GB |
| Forward pass activations (per layer) | ~0.2 GB |
| MLP probe (embedding 阶段后 LLM 释放) | <10 MB |
| Embeddings numpy (CPU RAM) | ~184 MB |
| **Peak** | **~5 GB** |

### 提交命令

```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/gen-depth-contamination && python scripts/run_exp015_neural_probe.py
```

默认参数全部正确，无需额外指定：
- `--model_path`: `/root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-1.5B-Instruct/Qwen/Qwen2.5-1.5B-Instruct`
- `--data_dir`: `data_exp017_qwen_cont`（有对应 lgbm baseline）
- `--max_depth 5`, `--embed_batch_size 24`, `--device cuda:0`
- `--output`: `artifacts/exp015_neural_probe_results.json`

预估运行时间：10-15 分钟（embedding ~3min + 5-fold MLP ~7min）。

---
