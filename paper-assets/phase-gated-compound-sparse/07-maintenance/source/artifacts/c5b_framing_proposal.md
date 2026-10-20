# C5b Framing 调整提案

> 日期: 2026-05-14 | 状态: 待 Director 审批 | 关联: D052, D053

## 1. 现状

**原 Claim**: C5b — Phase-aware mitigation recovers compound degradation  
**实验设计**: oracle + heuristic (token position ratio as phase proxy) on s025/s030, gate: >30% recovery  
**结果**: FAILED — 进程反复崩溃（5次），无有效数据产出。Registry 无条目。

## 2. 分析

这不是 hypothesis 被否定，而是 **pilot 实现层面的失败**（进程崩溃，非统计结论）。

但重做 C5b 的 ROI 极低：
- **时间约束**: 截稿 2026-05-25（11天），C2 n=500 和 C3 LLaMA 仍在运行，GPU 和人力已满载
- **调试成本**: 进程崩溃5次意味着代码/环境问题非 trivial，排查+重跑至少 1-2 天
- **论文定位**: Empirical finding paper（D015），非 method paper。Mitigation 从未进入论文主体结构（§1-§8 已完成，无 C5b 对应 section）
- **边际价值**: C1-C6 核心 claims 全部独立于 C5b。C5b 成功仅增强 RC3（practical impact）的防御，而 RC3 已有合理应对——"本文是 finding paper，throughput 不是 claim 的一部分"

## 3. 建议：降为 §8 Future Work

将 C5b mitigation 降为 §8 Future Work 中的 open question：

> *"Phase-aware sparsity allocation — dynamically adjusting KV cache budgets based on detected reasoning phase — is a promising but unvalidated direction for mitigating compound severity. Our pilot exploration of oracle and heuristic (token position ratio) allocators did not yield conclusive results within the scope of this work. Whether phase-gated controllers can recover the compound degradation documented in §5 remains an open question for future investigation."*

## 4. 对论文各章节影响评估

| Section | 影响 | 操作 |
|---------|------|------|
| §1 Introduction | 无 | C5b 未在 contributions 中列出 |
| §2 Related Work | 无 | ThinKV/R-KV 引用独立于 C5b |
| §3 Background | 无 | 公式和 II 定义不涉及 mitigation |
| §4 Methodology | 无 | 实验设计不包含 mitigation 实验 |
| §5 Results | 无 | 5.1-5.5 全部是现象描述，无 mitigation 结果 |
| §6 Analysis | 无 | Discrimination collapse 是机制解释 |
| §7 Discussion | **微调** | 将 "phase-gated controller 作为 future direction" 的措辞从暗示可行调整为明确标记为 unvalidated |
| §8 Conclusion | **微调** | 添加 1-2 句 future work 提及 phase-aware allocation |
| paper_framing.md | **更新** | C5b status 从 planned 改为 deferred_to_future_work |
| Claims table | **更新** | C5b 行删除或标注 deferred |

**净影响**: 仅 §7/§8 需约 2-3 句修改。核心 claims (C1-C6) 和论文主体结构完全不受影响。

## 5. 三种 Narrative 备选方案

### 方案 A（推荐）: Future Work Open Question
- C5b 降为 §8 的 open question
- §7 Discussion 保留 "phase-gated controller" 概念但标注 unvalidated
- 措辞："promising but unvalidated direction"
- **优势**: 诚实、不 overclaim、保持论文 finding paper 定位一致性
- **风险**: Reviewer 可能追问 "为什么不做 mitigation"——用 RC3 现有应对（finding paper 定位）防御

### 方案 B: 完全删除 C5b
- 从 Claims table 和论文中完全移除 C5b
- §7/§8 不提及 mitigation 可能性
- **优势**: 最简洁，消除任何 overclaim 嫌疑
- **风险**: 削弱论文的 forward-looking vision，审稿人可能问 "so what's the practical implication?"

### 方案 C: 重做 C5b（不推荐）
- 投入 1-2 天调试+重跑 pilot
- 若成功，加入 §7 作为 preliminary mitigation validation
- **优势**: 最强的论文完整性
- **风险**: 挤占 C2 n=500 / C3 LLaMA 分析时间，可能再次失败，11天 deadline 下 ROI 极低

## 6. 推荐决策

**采纳方案 A**。理由：
1. 论文定位（empirical finding paper）从不依赖 mitigation validation
2. C1-C6 核心 claims 的证据链完整，C5b 缺失不构成逻辑缺口
3. §8 Future Work 中的 open question 措辞既诚实又保留学术价值
4. 11天 deadline 下，将精力集中在 C2 n=500 数据分析和 C3 LLaMA 论文整合上 ROI 更高
5. 审稿人对 finding paper 不做 mitigation 的质疑（RC3）已有成熟应对策略

## 7. 需要 Director 确认

- [ ] 是否采纳方案 A（降为 Future Work）
- [ ] §7 Discussion 中 "phase-gated controller" 的具体措辞
- [ ] Claims table 中 C5b 行的处理方式（标注 deferred vs 删除）
