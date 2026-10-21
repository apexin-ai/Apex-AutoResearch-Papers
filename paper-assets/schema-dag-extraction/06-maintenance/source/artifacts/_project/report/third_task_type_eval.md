# 第三任务类型评估：是否需要 Relation Extraction 强化 task-agnostic claim

## 1. 边际收益判断

### 当前覆盖：2 个任务类型够不够？

**不够，但有变通方案。**

顶会标准参考：
- InstructUIE (ACL 2023 Findings) 评估了 NER/RE/EE 三大任务，覆盖 32 个数据集
- RUIE-Bench (ACL 2025) 同样覆盖 NER/RE/EE 三类
- USM (AAAI 2024) 覆盖 NER/RE/EE

**声称 "task-agnostic" 的 IE 论文几乎都评估 NER + RE + EE 三类。** 只有 NER + ED 会被 reviewer 质疑：两者都是 sequence labeling（给 span 分配单个 label），结构高度同构。RE 是 pair classification（判断两个 entity 之间的关系），输入/输出结构根本不同。

不过，本文的 claim 不是 "our framework works on any IE task"，而是 "confusability-aware decomposition is task-agnostic"。这意味着核心证据是 **confusability 现象在不同 IE 任务上都存在**，而非 SDGD 在所有任务上都跑过。如果实验计划中已有 ACE05（含 NER/RE/EE 三层）和 MAVEN（168 event types），加上 Few-NERD（66 entity types），已涉及 3 种 IE 子任务的 schema。

**关键风险**：审稿人可能问 "confusability 在 RE 上的表现如何？pair-wise relation types 的 confusability structure 和 span-level types 一样吗？" 如果完全没有 RE 数据，这个问题无法回答。

### 加第三个任务类型的边际收益 vs 时间成本

| 维度 | 不加 RE | 加 RE |
|------|---------|-------|
| task-agnostic 说服力 | 中等（NER+ED 结构类似，reviewer 可质疑） | 强（覆盖 span-labeling + pair-classification） |
| 实验时间 | 省 ~8h | 需额外 ~8h（数据准备 2h + 实验 5h + 分析 1h） |
| 论文篇幅 | 够 | 增加 ~0.5 页（一个表 + 1 段分析） |
| 被 reject 的概率 | 较高（"task-agnostic claim not supported"） | 较低 |

**10 天的时间约束下，8h 是可承受的。** 实验计划中 exp-005 (DocRED) 已被规划为 P1，只需将其提升为 P0。

## 2. 候选 RE 数据集

| 数据集 | Types | 公开可下载 | 数据量 | 适合度 | 备注 |
|--------|-------|-----------|--------|--------|------|
| **FewRel** | 100 | **Yes** (GitHub + HuggingFace) | 70K sentences | **最优** | 100 types 提供足够的 confusability 分析空间；sentence-level RE，处理简单 |
| **DocRED** | 96 | **Yes** (GitHub + HuggingFace) | 5K docs | **次优** | 文档级 RE 增加 pipeline 复杂度；但 96 types 充足 |
| Re-TACRED | 40 | **需 LDC** ($25) | 106K | 不推荐 | 需购买 TACRED base；40 types 偏少 |
| TACRED | 42 | **需 LDC** ($25) | 106K | 不推荐 | 同上 |
| SemEval 2010 T8 | 19 | Yes (多源) | 10K | 不推荐 | 19 types 太少，confusability 分析空间不足 |

数据集可用性确认来源：
- FewRel: [GitHub](https://github.com/thunlp/FewRel) / [HuggingFace](https://huggingface.co/datasets/thunlp/few_rel)
- DocRED: [GitHub](https://github.com/thunlp/DocRED) / [HuggingFace](https://huggingface.co/datasets/thunlp/docred)

## 3. 推荐

### 结论：**推荐加 RE，选 FewRel**

**理由**：
1. **FewRel (100 types) > DocRED (96 types)** 在本项目场景下更优：
   - Sentence-level RE，无需文档级上下文处理，数据准备和实验代码改动最小
   - 100 types 的 confusability structure 分析空间充足（与 Few-NERD 66 types、MAVEN 168 types 形成梯度）
   - 数据格式简单（JSON，每条带 head/tail entity + relation label），可直接复用现有 BCS 计算 pipeline
   - 70K 样本量足够做 count curve + BCS correlation 分析

2. **DocRED 作为备选**但有额外复杂度：
   - 文档级 RE 需要先做 entity pair enumeration，增加 pipeline 代码量
   - 实验计划中 exp-005 已规划了 DocRED，可保持不变作为 P1 补充

3. **替代方案（如果时间实在不够）**：在论文中用 ACE05 的 RE 子任务（7 relation types）做一个 mini confusability analysis，作为 "preliminary evidence"。但 7 types 说服力弱。

### 时间成本估算

| 步骤 | 时间 |
|------|------|
| FewRel 数据下载 + 预处理（转换为统一格式） | 1-2h |
| BCS 矩阵计算（100 types） | 0.5h |
| Count curve 实验（5 count levels × 5 random samples） | 3-4h GPU |
| BCS correlation 分析 + 可视化 | 1h |
| **总计** | **~6-8h** |

### 执行建议

将 FewRel 实验插入为 **exp-005b**（P0），与原 exp-005 (DocRED, P1) 并行规划。优先完成 FewRel，DocRED 视剩余时间决定。
