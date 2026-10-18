# research demo subgroup codebase discovery

**When Debiasing Hurts: An Exact Bias Identity for LLM-Annotated Treatment Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_demo-subgroup-codebase-discovery_20260524T040730_result.json`
- **Structured JSON:** [`38dc0f502273d9f6c98e.json`](../../sessions/38/38dc0f502273d9f6c98e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入 `/home/ubuntu/ec_hte_llm_annotation/results/demo_subgroup_discovery.md`。

核心发现：

**数据方面：**
- **UC Berkeley Hate Speech** (`data/exp004_raw.parquet`, 135K行 × 143列) 是最有价值的资源——同时有 annotator demographics（race/gender/age/education/ideology/income 等 40+ 列）和 target demographics（race/gender/religion 等 30+ 列），且已有 GPT-4.1 的 LLM 标注
- **CivilComments** 有 3 个 LLM 的标注（GPT-4o/4o-mini/3.5-turbo，6443条），但当前 CSV 缺少原始 identity columns（male/female/black/white/muslim 等 24 列）——需要从 HuggingFace 重新 join
- **Stance Detection** 已有 5 个 topic subgroup 的 CM，但无 demographic 维度

**代码方面：**
- EC-HTE 全套 pipeline 已有：`diff_in_means`, `get_counts`, `build_mixing_matrix`, `invert_mixing_safe`, MLE/EB/Gibbs CM estimation
- 关键入口在 `exp001_hb_synthetic.py`（centered HB）和 `exp023_civil_comments_semisynthetic_v3.py`（non-centered HB）
- `exp_civilcomments_demographic.py` 有 per-subgroup CM 计算和 semi-synthetic simulation 的完整 pipeline，可直接复用

**最大缺口：**
1. UCB 数据的 annotator demographics 从未用于 subgrouping（exp004 只用了 platform × text_length）
2. CivilComments 的 24 个 identity columns 未 join 到现有 LLM 标注数据
3. 尚无 per-annotator-demographic confusion matrix 的计算

**推荐路线：** UCB Hate Speech + annotator demographics 是最佳方案，数据已在本地，只需重新处理 raw parquet 按 annotator demographics 分组。

---
