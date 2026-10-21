# research lalonde dataset screening

**When Debiasing Hurts: An Exact Bias Identity for LLM-Annotated Treatment Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_lalonde-dataset-screening_20260524T123858_result.json`
- **Structured JSON:** [`d900baf5eaffd299533c.json`](../../sessions/d9/d900baf5eaffd299533c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入 `artifacts/lalonde_dataset_candidates.md`。

**核心结论**：

- **方案 A（首选）**：**Hangartner et al. (2021) 共情反言论 Twitter 实验**。N=1,350，有匿名化推文文本（Harvard Dataverse DVN/ARZ9PU），RCT 设计，Z 可定义为"显式 vs. 隐式仇恨言论"，LLM 分类误差在不同推文特征子群间天然异质。可行性 4.5/5。

- **方案 B（备选）**：**Hainmueller et al. (2014) 移民 Conjoint 实验**。N=13,960，R 包 `cjoint` 即装即用，ground truth Z 100% 已知，但需要额外步骤将结构化属性转化为自然语言文本。可行性 4/5。

**推荐策略**：先下载验证方案 A 的文本质量；如果文本被过度匿名化或 N 不足，退回方案 B。两个方案可并行准备。

---
