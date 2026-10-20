# research libero para check

**afford invar** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_libero-para-check_20260519T170856_result.json`
- **Structured JSON:** [`63032fb4fd227cbb3652.json`](../../sessions/63/63032fb4fd227cbb3652.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

信息收集完毕。以下是完整报告。

---

## LIBERO-Para 可用性验证报告

### 1. 代码/数据: **完全可用**

| 资源 | 链接 | 状态 |
|------|------|------|
| GitHub repo | [cau-hai-lab/LIBERO-Para](https://github.com/cau-hai-lab/LIBERO-Para) | 公开，含评估脚本+PRIDE代码 |
| HuggingFace 数据集 | [HAI-Lab/LIBERO-Para](https://huggingface.co/datasets/HAI-Lab/LIBERO-Para) | 公开，12.1MB |
| 数据格式 | BDDL 文件 + `metrics/libero_para_metadata.csv` | 可直接用于 LIBERO 评估 |

**数据规模**: 4,092 条 paraphrase 指令，来自 10 个 LIBERO-Goal 原始任务，43 种变体类型（3 Object × 10 Action + 组合）。

**生成方法**: Gemini 2.5 Pro 生成，axis-wise 独立生成 action/object paraphrase → LLM 验证 → 合并 → 人工验证（5% 抽检，Gwet's AC1=0.854，99.51% meaning-preserving）。

### 2. PRIDE Metric: **有代码 + 公式**

代码位置: `metrics/` 目录，含 `PRIDE_metric_playground.ipynb` 交互笔记本和 `analyze_results.py`。

**公式**:
```
PD(O, P) = 1 - (α · SK(O, P) + (1-α) · ST(T_O, T_P))

PRIDE = PD   if success
        0    if failure
```
- **SK**: keyword similarity，content word 的 cosine similarity
- **ST**: structural similarity，dependency tree edit distance
- **α**: 默认 0.5
- PRIDE 越高越好，给困难 paraphrase 更多权重

### 3. OpenVLA-OFT Baseline PRIDE 分数: **有**

| Model | Params | SR (%) | PRIDE | Overestimation (%) |
|-------|--------|--------|-------|---------------------|
| VLA-Adapter | 0.6B | 46.3 | 36.1 | 22.0 |
| π0.5 (expert-only) | 3.3B | 39.1 | 32.0 | 18.2 |
| X-VLA | 0.9B | 62.1 | 52.7 | 15.1 |
| **OpenVLA-OFT_mixed** | **7.5B** | **63.7** | **56.3** | **11.6** |
| **OpenVLA-OFT_goal** | **7.5B** | **64.7** | **58.8** | **9.1** |
| π0.5 | 3.3B | 71.4 | 65.4 | 8.4 |
| Xiaomi-Robotics-0 | 4.7B | 76.0 | 69.2 | 8.9 |

原始 LIBERO-Goal SR → Para SR 退化：OFT_goal 97.9% → 64.7% (−33.2pp)，OFT_mixed 96.1% → 63.7% (−32.4pp)。

### 4. 关键限制

**LIBERO-Para 仅覆盖 LIBERO-Goal**（10 个任务），不含 Spatial/Object/Long 套件。论文原文："LIBERO-Para is constructed on top of LIBERO-Goal, a setting in which linguistic understanding is essential."

### 5. 对 Phase 0.5 的影响

- **不需要自行跑 OFT baseline** — 论文已提供 OFT_goal 和 OFT_mixed 的 PRIDE 分数
- **可直接复用** LIBERO-Para 的 paraphrase 数据和 PRIDE 评估代码
- **局限**: 如需在 Spatial/Object/Long 上评估 paraphrase robustness，需自行扩展 paraphrase 数据（可参考其 Gemini 2.5 Pro 生成 pipeline）
- 核心发现（80-96% 失败来自 planning-level trajectory divergence）与我们的 affordance invariance 方向高度相关

Sources:
- [arXiv 2603.28301](https://arxiv.org/abs/2603.28301)
- [GitHub: cau-hai-lab/LIBERO-Para](https://github.com/cau-hai-lab/LIBERO-Para)
- [HuggingFace: HAI-Lab/LIBERO-Para](https://huggingface.co/datasets/HAI-Lab/LIBERO-Para)
- [Project Page](https://cau-hai-lab.github.io/LIBERO-Para/)

---
