# research pride formula verify

**afford invar** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_pride-formula-verify_20260519T232737_result.json`
- **Structured JSON:** [`6b6b3b1c97e8ac4f5ed4.json`](../../sessions/6b/6b6b3b1c97e8ac4f5ed4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## PRIDE 指标验证报告

### 论文原始定义 (arXiv:2603.28301)

**PD (Paraphrase Distance):**
```
PD = 1 - (α·S_K + (1-α)·S_T),  α=0.5
```

- **S_K** (Keyword Similarity): 对原始指令的 content words (NOUN/VERB/ADJ/ADV) 用 Sentence-BERT (all-MiniLM-L6-v2) 编码，每个原始词与所有 paraphrase 词取 max cosine similarity，再取平均：`S_K = (1/n) Σ max_j cos(e(o_i), e(p_j))`
- **S_T** (Structural Similarity): 依赖解析树的 Zhang-Shasha tree edit distance (TED)，节点标签为 (dep, POS)：`S_T = 1 - TED(T_O, T_P) / (|T_O| + |T_P|)`

**PRIDE 聚合公式（关键）:**
```
PRIDE(α) = Σ(success_i × PD_i) / Σ(PD_i) × 100
```

即 **PD 加权成功率**——成功 episode 的 PD 之和除以所有 episode 的 PD 之和，乘 100。Higher = better。

### 与我们当前实现的对比

| 要素 | 论文定义 | 我们 memory.md 记录 | 一致？ |
|------|---------|-------------------|--------|
| PD 公式 | `1 - (α·SK + (1-α)·ST)` | `1 - (α·SK + (1-α)·ST)` | **一致** |
| α 默认值 | 0.5 | 0.5 | **一致** |
| PRIDE 聚合 | `Σ(success×PD) / Σ(PD) × 100` | memory.md 未记录聚合公式 | **需确认** |
| 方向 | Higher = more robust | 未明确 | **需确认** |
| OFT_goal PRIDE | 58.8 | 58.8 | **一致** |
| OFT_mixed PRIDE | 56.3 | 56.3 | **一致** |

### 关键发现

1. **PD 单 episode 公式正确**——与论文 Eq.3 完全一致。

2. **PRIDE 不是简单的 per-episode PD 值**。论文 HTML (Eq.4) 简写为 "PRIDE = PD if success, 0 if failure"，但代码实现的聚合是 **加权比率**：`Σ(success_i × PD_i) / Σ(PD_i) × 100`。这不是简单平均，而是 PD 加权的成功率。更难的 paraphrase（PD 大）在分母中权重更大，成功则在分子中贡献更多。

3. **我们的 eval_pride.py 尚未实现**（项目中无 .py 文件包含 PRIDE 计算）。ROADMAP.md 已标注此为待办项。

4. **实现时需注意**：论文官方代码使用 `paraphrased_instruction` 字段匹配 pre-computed SK/ST CSV，而非实时计算。可直接复用论文的 `libero_para_metadata.csv`。

### 结论

PD 公式和 baseline 数值与论文完全一致，无需修改。实现 eval_pride.py 时需用 **加权比率公式** `Σ(success×PD)/Σ(PD)×100`，不能简单取均值。

Sources:
- [LIBERO-Para Paper (HTML)](https://arxiv.org/html/2603.28301v1)
- [LIBERO-Para Paper (Abstract)](https://arxiv.org/abs/2603.28301)
- [LIBERO-Para GitHub](https://github.com/cau-hai-lab/LIBERO-Para)
- [LIBERO-Para Project Page](https://cau-hai-lab.github.io/LIBERO-Para/)

---
