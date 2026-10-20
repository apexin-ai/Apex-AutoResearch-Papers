# ops verify selfbleu pythia data

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_verify_selfbleu_pythia_data_20260521T122556_result.json`
- **Structured JSON:** [`3fdc27450f2782d47c06.json`](../../sessions/3f/3fdc27450f2782d47c06.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

调查完成。以下是完整报告。

---

## 核查结果：Table 32 Pythia-1.4B 数据确认为 greedy 数据混入

### 1. 根因

`scripts/exp_14d_ablation_detail.py` 第 30 行硬编码了 Pythia 的数据路径：

```python
"Pythia": Path("/root/autodl-tmp/gen-depth-contamination/data_exp020_pythia_greedy/features.csv"),
```

其他三个模型使用的是 nucleus/continuation 模式数据：
- Qwen-base → `data_exp016_qwen_base`
- LLaMA-8B → `data/exp_018_llama8b`
- Mistral-7B → `data_exp019_mistral7b`

### 2. 证据链

| 来源 | 1v2 AUC | 说明 |
|------|---------|------|
| `results_exp020_pythia_greedy/summary.txt` | **0.8838** | greedy decoding 原始结果 |
| `artifacts/exp_14d_ablation_detail.json` → Pythia 15D | **0.884** | selfbleu ablation 输出 (= Table 32) |
| Table 32 (appendix_extended.tex:254) | **.8840** [.878,.890] | 论文中的值 |
| Table S10 (appendix.tex:413) Greedy 列 | **.8838** | 论文中 greedy decoding 表 (完全吻合) |
| Table S10 Nuc p=0.9 列 | **.6770** | 正确的 nucleus 值 |
| `results_exp020_pythia_nuc09/summary.txt` | **0.677** | nucleus p=0.9 原始结果 |
| Table 2 (experiments_c1.tex:25) | **.6539** [.645,.663] | 主表中 Pythia 的值 |

### 3. 各模型行状态

| 模型 | Table 32 值 | 数据来源 | generation mode | 状态 |
|------|------------|---------|----------------|------|
| Qwen-base | .6288 | `data_exp016_qwen_base` | nucleus/continuation | **正确** |
| **Pythia-1.4B** | **.8840** | **`data_exp020_pythia_greedy`** | **greedy** | **错误** |
| LLaMA-8B | .6075 | `data/exp_018_llama8b` | nucleus | **正确** |
| Mistral-7B | .5902 | `data_exp019_mistral7b` | nucleus | **正确** |

### 4. 正确值

**已有的 nucleus 数据**：`data_exp020_pythia_nuc09/features.csv`（30000 条，包含 self_bleu 列）。基于该数据的 raw 5-fold AUC = 0.677。

**但需注意**：Table 2 中 Pythia C4 值为 .6539，与 nuc09 的 0.677 不一致。目前 `data/exp_pythia14b_c4_rerun/` 正在生成中（只有 depth 0-3 的 jsonl，尚无 features.csv）。Table 2 的 .6539 可能来自已覆盖或不同配置的数据。

### 5. 结论

- **确认 greedy 数据混入**：Table 32 Pythia 行使用了 greedy decoding 数据
- **结论是否受影响**：ablation 结论（removing self_bleu doesn't change K\*）在 nucleus 下仍成立（K\*=2 不变），但 AUC 数值需要修正
- **修复方式**：**需要重跑** `exp_14d_ablation_detail.py`，将 Pythia 路径改为正确的 nucleus sampling features（待 `exp_pythia14b_c4_rerun` 完成并生成 features.csv，或使用 `data_exp020_pythia_nuc09/features.csv`）
- **其他模型行无问题**

---
