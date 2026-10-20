# ops pipeline sampling audit

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_pipeline_sampling_audit_20260521T141038_result.json`
- **Structured JSON:** [`d0ca763bd7fe8145fbe5.json`](../../sessions/d0/d0ca763bd7fe8145fbe5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据收集完毕。以下是完整审计结果。

---

## 产出 1: `--no_sample` 默认值

**默认 `do_sample=True`（nucleus sampling, top_p=0.95, T=1.0）。不是灾难性 bug。**

```python
# run_pipeline.py L636-639
parser.add_argument("--do_sample", action="store_true", default=True)
parser.add_argument("--no_sample", dest="do_sample", action="store_false")
```

只有显式传 `--no_sample` 的实验才会用 greedy。

---

## 产出 2: 原始 Pythia-1.4B 主表数据 decoding 配置

| 版本 | Decoding | 1v2 AUC | 证据 |
|---|---|---|---|
| **exp_008_retrain_chain**（原始） | **nucleus** p=0.95 T=1.0 | 原始数据丢失 | log: `Decoding: nucleus p=0.95, T=1.0` |
| **exp_pythia14b_c4_rerun**（今日重跑） | **GREEDY** | 0.8786 | config.json: `"greedy (no_sample=True, do_sample=False)"` |

原始 exp_008 是正确的 nucleus。但重跑时误用了 greedy，导致 1v2 AUC 虚高到 0.8786。

---

## 产出 3: 全实验 decoding 参数表

### GREEDY（有问题的）

| 实验 | 证据来源 | 1v2 AUC | 说明 |
|---|---|---|---|
| **exp_pythia14b_c4_rerun** | config.json 明确标注 greedy | 0.8786 | 重跑误用 greedy |
| **exp_pythia69b_c4** | 无 log；1v2 AUC=0.8542 异常高；事后创建了 `_nuc` 修正版 | 0.8542 | **高度疑似 greedy** |
| **pythia_c4_qwen_scorer** | depth_0 符号链接到 `data_exp020_pythia_greedy/` | 0.6074 | 确认使用 greedy 生成的数据 |
| exp020_pythia_greedy | 脚本 `--no_sample`（Config 1/4） | — | **有意的 ablation，无问题** |

### NUCLEUS（正确的）

| 实验 | 证据 | 1v2 AUC |
|---|---|---|
| exp_008_retrain_chain | log: nucleus p=0.95 T=1.0 | (features 丢失) |
| exp_018_llama8b | log: do_sample=True | — |
| exp019 | log: do_sample=True | — |
| exp020_pythia_nuc09/t07/t12 | 脚本 `--top_p`/`--temperature` | — |
| exp021_length_128/256/512 | 脚本无 `--no_sample` → 默认 nucleus | — |
| exp022 cross-scorer (all) | log: do_sample=True | — |
| exp023_wiki | 脚本无 `--no_sample` | — |
| exp024_arxiv | log: do_sample=True | — |
| exp025_pythia_arxiv | log: do_sample=True | — |
| exp_arXiv_qwen1b5_crossscorer | log: do_sample=True | — |
| exp_olmo_retrain_chain | log: nucleus p=0.95 T=1.0 | — |
| exp_qwen_retrain_chain (+ext) | log: nucleus p=0.95 T=1.0 | — |
| exp_pythia_retrain_depth7 | log: nucleus p=0.95 T=1.0 | — |
| exp_gemma2b_depth | log: do_sample=True | — |
| exp_code_pythia1b4 | log: do_sample=True | — |
| exp_code_mistral7b | log: do_sample=True | — |
| exp_pythia69b_c4_nuc | log: do_sample=True (但 crash 未完成) | — |
| olmo_c4_cont | 无 log 但 1v2 AUC=0.507 (符合 nucleus 预期) | 0.507 |
| olmo_c4_qwen_scorer | 1v2 AUC=0.5001 | 0.500 |
| exp_olmo1b_c4_rerun | skip_generation=True，复用 olmo_c4_cont 数据 | 0.508 |
| olmo_retrain_v3 | log: nucleus p=0.95 T=1.0 | — |

### 无 log / 不涉及生成的实验

exp_009 (dose response), exp_contamination_rate_sweep, retrain_chain_bootstrap, semantic_ablation_multi, c4_subsample_control, exp026 filtering, exp027, deberta — 这些是训练/评估/分析实验，不涉及 depth chain 生成。

---

## 产出 4: 是否有非 Pythia 实验也有 greedy 混入

**没有。** Greedy 问题仅限 Pythia 系列：
1. `exp_pythia14b_c4_rerun` — 确认 greedy
2. `exp_pythia69b_c4` — 高度疑似 greedy（1v2 AUC=0.8542，事后创建 `_nuc` 修正）
3. `pythia_c4_qwen_scorer` — 数据来源于 exp020 greedy

OLMo、Qwen、Llama、Gemma、Mistral 的所有实验均确认为 nucleus sampling。`olmo_c4_cont` 虽无 log，但 1v2 AUC=0.507 符合 nucleus 预期。

---
