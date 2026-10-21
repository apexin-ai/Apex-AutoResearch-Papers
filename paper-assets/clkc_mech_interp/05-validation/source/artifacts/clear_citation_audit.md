# CLEAR Citation Audit Report

> 审计日期: 2026-05-22

## 验证结论: ✅ 真实存在

CLEAR (Zhao et al. 2026) 是真实论文，非 AI 幻觉引用。

## 论文完整信息

| 字段 | 内容 |
|------|------|
| 标题 | When Abundance Conceals Weakness: Knowledge Conflict in Multilingual Models |
| 作者 | Jiaqi Zhao, Qiang Huang, Haodong Chen, Xiaoxing You, Jun Yu |
| 提交日期 | 2026-01-11 |
| arXiv | [2601.07041](https://arxiv.org/abs/2601.07041) |
| 会议/期刊 | arXiv preprint (截至审计日期，未确认正式发表venue) |
| 缩写含义 | CLEAR = Cross-Lingual knowlEdge conflict evAluation fRamework |

## 论文实际内容

CLEAR 是一个系统性评估框架，研究多语言 LLM 如何处理跨语言知识冲突：
- 覆盖 **10 种类型学多样性语言**，评估 **6 个代表性 LLM**
- 使用 ConflictQA 和 ConflictingQA 的多语言版本
- 将冲突解决分解为 4 个递进场景

**核心发现（task-dependent pattern）**:
1. **推理密集型任务**: 语言资源丰富度 (resource abundance) 主导冲突解决，高资源语言有更强说服力
2. **实体中心事实冲突**: 语言亲缘性 (linguistic affinity) 而非资源规模决定冲突解决，低资源但语言学亲近的语言可胜过高资源但距离远的语言

## ⚠️ 引用准确性问题

paper_framing.md 当前描述:
> "CLEAR 发现的 '语言相似性决定冲突解决'"

**问题**: 这是对 CLEAR 发现的不完整简化。CLEAR 的关键贡献恰恰是发现冲突解决机制是 **task-dependent** 的——linguistic affinity 仅在 entity-centric factual conflicts 中起决定作用。在 reasoning-intensive tasks 中，resource abundance 才是主导因素。

**建议修正**: 论文叙事中引用 CLEAR 时应准确呈现其 task-dependent 发现，而非笼统说"语言相似性决定冲突解决"。我们的 probing 实验使用的是 ConflictQA（entity-centric factual QA），因此可以说"CLEAR 发现在 entity-centric factual conflicts 中，linguistic affinity 而非 resource abundance 决定冲突解决"。

## 搜索证据

以下 4 组搜索查询均指向同一论文 arXiv:2601.07041:
1. `CLEAR cross-lingual knowledge conflict LLM benchmark` → 首条结果
2. `"CLEAR" "Zhao" 2026 cross-lingual knowledge conflict` → 首条结果
3. `CLEAR benchmark cross-lingual knowledge conflict multilingual` → 首条结果
4. `Zhao et al 2026 knowledge conflict LLM cross-lingual` → 首条结果

## 相关真实论文（供交叉引用）

| 论文 | arXiv | 相关性 |
|------|-------|--------|
| CLM-Bench: Cross-lingual Misalignment of LLMs in Knowledge Editing | [2601.17397](https://arxiv.org/abs/2601.17397) | 跨语言知识编辑错位 |
| ECLeKTic: Evaluating Cross-lingual Knowledge Transfer in LLMs | Google Research Blog | 跨语言知识迁移评估 |
| LiveCLKTBench: Reliable Evaluation of Cross-Lingual Knowledge Transfer | [2511.14774](https://arxiv.org/abs/2511.14774) | 跨语言知识迁移基准 |
| Knowledge Conflicts for LLMs: A Survey (EMNLP 2024) | [2403.08319](https://arxiv.org/abs/2403.08319) | 知识冲突综述 |
| Analysing the Residual Stream under Knowledge Conflicts | [2410.16090](https://arxiv.org/abs/2410.16090) | 残差流+知识冲突（方法论最近） |
| Crosslingual Capabilities and Knowledge Barriers in Multilingual LLMs | [2406.16135](https://arxiv.org/abs/2406.16135) | 跨语言能力与知识壁垒 |
| Beneath the Surface of Consistency: Cross-lingual Knowledge Representation Sharing | [2408.10646](https://arxiv.org/abs/2408.10646) | 跨语言知识表征共享 |
