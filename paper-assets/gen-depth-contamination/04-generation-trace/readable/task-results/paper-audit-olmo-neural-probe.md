# paper audit olmo neural probe

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_audit_olmo_neural_probe_20260523T114922_result.json`
- **Structured JSON:** [`1cad318d08a022e53187.json`](../../sessions/1c/1cad318d08a022e53187.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Now I have the complete picture. Here's the summary:

---

## Neural Probe AUC 验证结果

### OLMo

**两套结果来源不同：**

| 来源 | Probe 模型 | 数据 | 1v2 | 2v3 | K* |
|------|-----------|------|-----|-----|----|
| **原始 exp_015 v4** (westc-26893) | Qwen2.5-1.5B (cross-model) | `data_exp002_olmo` | 0.657 | 0.589 | 2 |
| **OLMo rerun** (cqa1-22115) | OLMo-1B (self-probe) | `data/exp_olmo1b_c4_rerun` | 0.5054 | 0.5056 | 1 |

**论文 Table 3 使用的是 rerun 值（K\*=1），这是正确的。** Registry 中的旧值（K\*=2, 1v2=0.657）来自原始跨模型 probe，已被 rerun 替代。

服务器原始文件路径：`/root/autodl-tmp/gen-depth-contamination/results/exp015_olmo_rerun/neural_probe_results.json`

OLMo rerun 全部 pairwise AUC：
| Pair | AUC | 95% CI | p-value |
|------|-----|--------|---------|
| 0v1 | 0.9773 | [0.9747, 0.9795] | <0.002 |
| 1v2 | 0.5054 | [0.4954, 0.5148] | 0.176 |
| 2v3 | 0.5056 | [0.4966, 0.5157] | 0.142 |
| 3v4 | 0.5032 | [0.4941, 0.5133] | 0.262 |
| 4v5 | 0.4999 | [0.4913, 0.5073] | 0.514 |

### Qwen 和 Pythia

原始结果文件在旧服务器 westc-26893 (`artifacts/exp015_neural_probe_results.json`)，已不可访问。仅有 checkpoint 记录的rounded值：

| 模型 | Probe 模型 | 0v1 | 1v2 | 2v3 | 3v4 | 4v5 | K* |
|------|-----------|-----|-----|-----|-----|-----|----|
| **Qwen-cont** | Qwen2.5-1.5B (self) | 0.988 | 0.702 | 0.616 | 0.590 | 0.566 | 3 |
| **Pythia-1.4B** | Qwen2.5-1.5B (cross) | 0.966 | 0.676 | 0.596 | 0.555 | 0.532 | 2 |

论文中更精确的值（Qwen 2v3=0.6159, Pythia 2v3=0.5963）与 checkpoint 的 rounded 值一致，**K\* 正确**。

### 方法论注意

Table 3 混用了不同 probe 设置：
- **Qwen**: Qwen 自身做 probe（self-model），K\*=3
- **Pythia**: Qwen 做 probe（cross-model），K\*=2
- **OLMo**: OLMo 自身做 probe（self-model，rerun），K\*=1

Qwen/Pythia 未在新数据上做 rerun，也没有用各自模型做 self-probe。

---
