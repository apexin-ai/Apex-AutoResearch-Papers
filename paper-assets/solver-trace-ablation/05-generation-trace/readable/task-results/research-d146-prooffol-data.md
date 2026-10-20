# research d146 prooffol data

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_d146-prooffol-data_20260519T135905_result.json`
- **Structured JSON:** [`871ac94c309b1d51c73e.json`](../../sessions/87/871ac94c309b1d51c73e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。报告如下：

---

## ProofFOL 数据准备报告

### 1. 来源
- **论文**: [Strategies for Improving NL-to-FOL Translation with LLMs](https://arxiv.org/abs/2409.16461) (arXiv:2409.16461)
- **GitHub**: `https://github.com/RamyaKeerthy/Translation-NL2FOL`
- **数据文件**: `data/train/proof_train_fol.json`

### 2. 原始数据集
- 总条数：**10,424**（train），600（test）
- 字段：`id`, `input`, `label`, `output`
- `output` 字段包含结构化 FOL：`Predicates` + `Premise_FOL-` + `Conclusion_FOL-`，每条 FOL 后跟 `::: NL` 对齐说明
- 成功解析：**10,332**（92 条因 FOL 解析为空被跳过，0.9%）

### 3. 与 FOLIO 格式兼容性
- 字段完全对齐：`id`, `context`, `question`, `answer`, `fol_premises`, `fol_conclusion`, `depth` — **零差异**
- FOL 符号风格一致（`∀`, `∃`, `∧`, `→`, `¬`），与 FOLIO 使用相同 Unicode
- 区别：ProofFOL 的 FOL 是 GPT-4o 生成 + Prover9 验证的银标准数据；谓词更简单（`Blue(x)`, `Rough(x)` 等 ProofWriter 风格），不如 FOLIO 的真实世界谓词复杂

### 4. 生成文件
| 文件 | 路径 | 条数 |
|------|------|------|
| 训练集 | `/root/solver-trace-ablation/data/prooffol_train_500.jsonl` | 500 |
| 评估集 | `/root/solver-trace-ablation/data/prooffol_eval_100.jsonl` | 100 |

### 5. Sanity check 结果
- ID 前缀：全部 `prooffol_*`，无 `folio_` 污染
- 空 `fol_premises`：0
- 空 `fol_conclusion`：0
- Train/Eval ID 重叠：0
- 标签分布（train_500）：true=180, unknown=176, false=144（较均衡）
- Depth 分布（全集）：d2=1978, d3=867, d4=3919, d5=3528, d6/7/8=40
- seed=42 可复现

### 6. 注意事项
- ProofFOL 来自 ProofWriter，谓词语义简单（颜色/属性），推理链较长（depth 4-5 为主），与 FOLIO 的真实世界知识推理有风格差异——这正是跨数据集验证的意义
- FOL 是 GPT-4o 银标准翻译，非人工标注，但经 Prover9 正确性验证过滤

---
