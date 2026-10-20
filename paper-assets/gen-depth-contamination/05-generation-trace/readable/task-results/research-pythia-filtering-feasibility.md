# research pythia filtering feasibility

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_pythia_filtering_feasibility_20260520T215735_result.json`
- **Structured JSON:** [`6ba1cea3a08786b29ee5.json`](../../sessions/6b/6ba1cea3a08786b29ee5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据全部收集完毕。以下是汇总：

---

## 可行性评估：Pythia-1.4B Filtering Cross-Model Replication

### 可行性: YES — 实验已经跑完，无需新计算

### 1. 数据状态

| 资源 | 状态 |
|------|------|
| Pythia depth chain (arxiv, depth 0-5) | `exp_025_pythia_arxiv/` ✅ 6个jsonl + features.csv |
| Pythia depth chain (wiki, depth 0-5) | `exp_wiki_pythia/` ✅ |
| Pythia depth chain (code, depth 0-5) | `exp_code_pythia1b4/` ✅ |
| Pythia C4 features | `exp_7b_scorer_ablation/pythia_c4__qwen1.5b/features.csv` ✅ |
| OBD classifier results | `results/exp_025_pythia_arxiv/` ✅ (pairwise_auc, jsd, ordinal, feature_importance) |

### 2. Filtering + 下游 eval: 已完成

`results/exp_025_pythia_filtering/` 包含 **3 conditions × 3 seeds = 9 runs**，全部有 `eval_results.json`：

| Condition | Seed 42 | Seed 123 | Seed 456 | **Mean** |
|-----------|---------|----------|----------|----------|
| **no_filter** | MMLU=25.68 / HS=52.53 | 25.69 / 52.43 | 25.53 / 52.58 | **MMLU=25.63 / HS=52.51** |
| **binary_ours** | 25.88 / 52.52 | 25.80 / 52.49 | 25.87 / 52.51 | **MMLU=25.85 / HS=52.51** |
| **graduated_a09** | 25.65 / 52.55 | 25.82 / 52.40 | 25.53 / 52.58 | **MMLU=25.67 / HS=52.51** |

### 3. 结果解读

- binary filtering 在 MMLU 上有 +0.22pp 的微弱改善，HellaSwag 基本持平
- graduated filtering 与 no_filter 无显著差异
- Pythia-1.4B 的 MMLU ~25.8% 接近随机水平（4选1 = 25%），信噪比极低，filtering 效果难以显现
- HellaSwag ~52.5% 在三组间完全一致

### 4. 需要的步骤

**零 GPU 时间。** 唯一需要做的是：
1. 将 `exp_025_pythia_filtering` 结果整理进论文表格
2. 在 Section 对应位置添加 Pythia-1.4B 行
3. 在讨论中说明：cross-model replication 在 Pythia 上模式一致（filtering 不降性能），但因基线模型能力较弱（near-random MMLU），filtering 带来的改善幅度小于 Qwen-1.5B

### 5. 建议

**启动。** 数据已全部就绪，只需写作。但要注意 framing：Pythia-1.4B 的 near-random MMLU 使得 filtering 信号微弱，应该诚实讨论这一点，将其定位为 "filtering 保持无害性 + cross-model generalization 的验证" 而非 "filtering 在所有模型上都带来显著提升"。如果还需要更强的 cross-model evidence，考虑用已有的 wiki/code 域 Pythia 数据做额外 OBD 分类器评估（已有 features.csv，只需跑分类器，几分钟 CPU 时间）。

---
