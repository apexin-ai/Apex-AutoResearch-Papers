# research literature dream gaps

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_literature-dream-gaps_20260515T033623_result.json`
- **Structured JSON:** [`925aae3f01588541b8ba.json`](../../sessions/92/925aae3f01588541b8ba.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

literature_map.yaml 已更新。以下是变更摘要：

### 补全的 Dream 指出的 4 篇论文（已在文件中，补全了作者/详细信息）

| 论文 | 状态 | 补全内容 |
|------|------|---------|
| **FANG** | 真实论文 ✓ | 作者: Tao Yu 等 (CASIA), arXiv 2512.23014, 补全 key_finding 数据 |
| **FuncNet** | 真实论文 ✓ | 作者: Yiheng Liu 等 (西工大), arXiv 2508.05239 |
| **RestoreLCC** | 真实论文 ✓ | 作者: Zijian Feng 等 (NTU), NeurIPS 2025 Spotlight, arXiv 2510.21834 |
| **PAT** | 真实论文 ✓ | 作者: Yijiang Liu 等, AAAI 2025, arXiv 2408.14721 |

### 新增 CKA justification 文献（3 篇）

| ID | 论文 | 用途 |
|----|------|------|
| `kornblith_cka_2019` | Kornblith et al., ICML 2019 — CKA 原始论文 | **核心引用**: CKA 99.3% 层对应准确率 vs CCA 1.4% / SVCCA 45.4% |
| `raghu_svcca_2017` | Raghu et al., NeurIPS 2017 — SVCCA | CKA 的前身和对比 baseline |
| `klabunde_similarity_survey_2025` | Klabunde et al., ACM Computing Surveys 2025 | CKA 优势的综述级证据 |

### 新增 structured pruning + RL recovery 文献（3 篇）

| ID | 论文 | 关系 |
|----|------|------|
| `boiling_frog_2026` | Gradually Compacting LLMs (Zhao et al., Feb 2026) | 迭代 Prune-Tune Loop，用 SFT 恢复（我们用 RLVR 更优） |
| `think_prune_train_2025` | Think, Prune, Train, Improve (Costello et al., Stanford) | 剪 CoT trace 不剪权重，互补方向 |
| `fastforward_2025` | FastForward Pruning (arXiv Nov 2025) | RL 做稀疏度分配（不做恢复），可与我们的 CKA 选择结合 |

### 补全的其他条目
- `mipp_2024`: 补全 arxiv_id (2411.00147)、更新 venue 和 key_finding
- `self_healing_2025`: 补充 OpenReview ID (Cy8Qa4gAst)

### 搜不到精确匹配的论文
无 —— Dream 提到的 4 篇论文全部找到了真实匹配，不存在幻觉。

---
