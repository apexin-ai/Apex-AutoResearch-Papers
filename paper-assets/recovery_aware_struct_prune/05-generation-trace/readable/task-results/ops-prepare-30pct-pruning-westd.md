# ops prepare 30pct pruning westd

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_prepare_30pct_pruning_westd_20260517T173514_result.json`
- **Structured JSON:** [`9e4a4d6cef41b8922678.json`](../../sessions/9e/9e4a4d6cef41b8922678.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个 30% sparsity pruning 全部完成。

## 产出报告

| 项目 | 状态 |
|------|------|
| **脚本路径** | `/root/recovery_aware_struct_prune/src/prune.py` |
| **Base model** | `/root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B/` |
| **Importance scores** | `/root/autodl-tmp/recovery_aware_struct_prune/results/importance_scores_qwen_math.pt` |
| **CKA scores** | `/root/autodl-tmp/recovery_aware_struct_prune/results/cka_scores_qwen_math.pt` |

**prune.py 实际参数格式：**
```
--model_path, --importance_path, --cka_path, --mode (standard/rasp/rasp-rlvr), 
--sparsity, --alpha, --output_path, --seed, --dtype
```

**Pruning 结果：**

| 方法 | 输出目录 | 大小 | Actual Sparsity | MLP groups pruned |
|------|----------|------|-----------------|-------------------|
| RASP | `pruned_rasp_30/` | 11G | 28.63% | 300/784 |
| Standard | `pruned_standard_30/` | 11G | 28.63% | 300/784 |

两者均为纯 MLP 剪枝（0 attn GQA groups pruned），forward pass validation 通过。输出包含 `model.safetensors` + `config.json` + `pruning_metadata.pt` + tokenizer 文件，可直接加载 eval。

---
