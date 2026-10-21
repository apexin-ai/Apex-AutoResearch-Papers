# fix experiments tex review

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_experiments-tex-review_20260514T090242_result.json`
- **Structured JSON:** [`3353621512a60d34c133.json`](../../sessions/33/3353621512a60d34c133.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。改动汇总：

### 修改的文件

**paper/references.bib** — 新增 3 个 bib 条目：
- `deepseek2025r1`：DeepSeek-AI, "DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning", 2025, arXiv:2501.12948
- `qwen2.5`：An Yang et al., "Qwen2.5 Technical Report", 2024, arXiv:2412.15115
- `cobbe2021gsm8k`：Karl Cobbe et al., "Training Verifiers to Solve Math Word Problems", 2021, arXiv:2110.14168

**paper/experiments.tex**（从 `docs/paper/` 移入）— 4 处修改：

1. **Citation keys 统一**：
   - `\citep{ma2024llmpruner}` → `\citep{llmpruner2023}`
   - `\citep{wang2026graspune}` → `\citep{graspprune2026}`
   - `\citep{shao2024deepseekmath}` → `\citep{shao2024grpo}`
   - `deepseek2025r1`、`qwen2.5`、`cobbe2021gsm8k` 保留（已在 bib 中新建对应条目）

2. **文件路径**：从 `docs/paper/` 移到 `paper/`，与其他 .tex 文件一致。旧文件已删除。

3. **RASP 公式去重**：删除 `\begin{equation} S(h)=... \label{eq:rasp_score} \end{equation}` 独立公式块，改为行内引用 `(Eq.~\eqref{eq:score})`，指向 method.tex 中的 Eq. 4。

4. **Recoverability proxy 说明**：在 Correlation Analysis 段落补充 activation shift 代理指标的定义（$1 - \cos(\mathbf{a}^{\text{pre}}_h, \mathbf{a}^{\text{post}}_h)$）及合理性论证（feature disruption 与 accuracy degradation 正相关；可逐 structure 计算无需 recovery 训练）。

---
