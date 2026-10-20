# ops olmo scorer confound investigation

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_olmo_scorer_confound_investigation_20260520T125618_result.json`
- **Structured JSON:** [`557acdedf6bd4045d5ee.json`](../../sessions/55/557acdedf6bd4045d5ee.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

调查完成。以下是完整汇总。

---

## 调查报告：OLMo C4 scorer confound

### 1. exp-002 的 scorer 配置

没有 `exp_002_olmo_depth` 目录。论文中 OLMo C4 数据对应 `data/olmo_c4_cont/` 和 `results/olmo_c4_cont/`。

`olmo_c4_bootstrap_ci.py` 明确标注 **`scorer=OLMo-1B (self-scored)`**。`run_pipeline.py` 支持 `--scorer_path` 参数（默认 None = self-scoring），但没有日志记录原始调用参数。

### 2. 论文数字 vs 实际数据 — 严重不一致

**论文主表 (Table 2 / S4) OLMo 列：**
| Pair | AUC | 95% CI |
|------|-----|--------|
| 0v1 | 0.9970 | — |
| 1v2 | **0.6145** | [0.605, 0.625] |
| 2v3 | 0.5496 | [0.540, 0.560] |
| K* = **2** | | |

**实际存在的所有 OLMo 结果（全部今天 2026-05-20 生成）：**

| Source | Scorer | 0v1 | 1v2 | K* |
|--------|--------|-----|-----|-----|
| `olmo_c4_cont/pairwise_auc.json` | OLMo-1B (self) | 0.9986 | **0.507** | 1 |
| `exp_7b_scorer/olmo_c4__qwen1.5b` | Qwen-1.5B | 0.9819 | **0.4977** | 1 |
| `exp_7b_scorer/olmo_c4__qwen7b` | Qwen-7B | 0.9833 | **0.4965** | 1 |

**三种 scorer 一致给出 1v2 AUC ≈ 0.50（随机水平），K*=1。** 差距不是 11.7pp 而是 ~12pp，且没有任何现存数据支持论文的 0.6145。

### 3. 根因：数据今天被完整重生成，旧数据已丢失

所有 `data/olmo_c4_cont/` 文件均为今天新建：
- `depth_0.jsonl`: Born 12:43
- `depth_5.jsonl`: Born 13:48
- `features.csv`: Born 14:11
- `pairwise_auc.json`: Born 14:11

**论文中的 0.6145 来自一次更早的 pipeline 运行，其数据已被覆盖，没有任何备份或 artifact 保留。** 也没有 `olmo_c4_bootstrap_ci_10k.json` artifact 文件（脚本存在但 artifact 不存在）。

### 4. 验证：底层文本一致，不是 scorer 的问题

通过比较 `freq_kurtosis` 和 `freq_entropy`（白空格分词，scorer-agnostic）：三个 features.csv 中这些值**完全相同**，证明底层文本数据一致。`ttr`/`hapax` 的差异是因为它们使用 scorer 的 BPE tokenizer 计算。

所以这**不是 scorer confound** — 是**数据版本 confound**。当前 OLMo 生成的文本在 depth 1 和 2 之间没有可区分的信号，无论用什么 scorer。

### 5. 对 headline claim 的影响

论文当前声称：**"7/8 yield K\*=2"**（只有 Mistral-7B 例外）。

如果 OLMo 从 K\*=2 降为 K\*=1：
- 变为 **6/8 yield K\*=2**（OLMo + Mistral 为例外）
- 论文 Table S13 (Scorer Sensitivity) 中 `OLMo-1B / Self / K*=2` 也不成立
- "K\*≤2 across all configurations" 结论不变（K\*=1 < 2），但 "7/8 at K\*=2" 的 universality claim 被削弱

### 6. 建议行动

1. **找回原始数据**：检查 AutoDL 实例是否有快照/回收站；检查其他机器或 WandB 是否记录了原始运行
2. **如果无法找回**：用固定种子重跑 OLMo pipeline，对比多次运行的 1v2 AUC 稳定性
3. **确认 scorer 配置**：原始运行是否用了 `--scorer_path Qwen`？如果用 Qwen scorer 且得到 0.6145 但今天 Qwen scorer 只给 0.50，说明是文本本身的差异
4. **论文修正**：如果 OLMo K\*=2 不可复现，需要将论文改为 "6/8 yield K\*=2" 或移除 OLMo 列

---
