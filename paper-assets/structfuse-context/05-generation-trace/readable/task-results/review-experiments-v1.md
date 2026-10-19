# review experiments v1

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_review_experiments-v1_20260515T134308_result.json`
- **Structured JSON:** [`d4dada7e1a22d2efdf65.json`](../../sessions/d4/d4dada7e1a22d2efdf65.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All data collected. Here's the review:

---

## 审查结果: NEEDS_REVISION

### 问题清单 (按严重程度)

**1. [CRITICAL] Seed 方差远大于 treatment effect，统计力不足**

唯一完成的配对比较 (Qwen embedding_s43 vs random_s43) treatment effect = +0.52pp，而 random 策略内部的跨 seed 方差高达 4.82pp（s44=0.6009 vs s42=0.5527）。Treatment effect 仅为 seed 方差的 ~1/9。草稿声称将报告 "bootstrap 95% confidence intervals for all pairwise comparisons"，但 n=3 seeds 在这个方差水平下 CI 几乎必然跨零。

草稿 §4.3.2 提到了 s44 异常但未量化这个比值，也未讨论对 Claim 1 ("reliable improvement") 的影响。reviewer 会立刻指出：你声称的 "reliable" improvement 在统计上无法与噪声区分。

**建议**: 在 §4.3.2 显式报告 treatment effect vs seed variance 的比值。在 Discussion 中坦诚讨论统计力限制。考虑是否需要增加 seed 数量（paper_framing 的 contingency plan 应提前考虑这一场景）。

---

**2. [MAJOR] StarCoder random_s43 数据已就绪但草稿仍为 placeholder**

Registry 显示 `m2_full_starcoder_resumed` 的 `random_s43` 已完成 (best_R@1=0.4912, early_stopped step 2500)，但 Table 1 StarCoder 面板中 random_s43 仍为 X.XX。同时 `random_s44` 的 eval@500 R@1=0.4848 也已可用（虽然未完成，不应填入正式表格）。

**建议**: 更新 StarCoder random_s43 = 0.4912。

---

**3. [MAJOR] 数据管道数字 14,288 已被 D042 标记为待重算**

§4.1 声称 "14,288 yield resolvable positive files"。decisions.yaml D042 明确指出 "数据管道数字（15133/15897/14288）存在多处不一致，根因是 M1 reextract v2 尚未完成，完成后全链路重算一次统一"。我通过 plan_018 metrics 交叉验证 14,288 = 各 seed 的 train+val 之和（s42: 11,308+2,980=14,288; s43: 11,236+3,052=14,288; s44: 11,264+3,024=14,288），当前数值本身一致。但 M1v2 完成后（ETA 今晚 22:00 CST）若重建训练数据，此数字可能变化。

**建议**: 确认当前 M2 训练数据是否基于 pre-M1v2 数据。如果是，明确说明；如果 M1v2 数据将用于后续训练，标记为 provisional。

---

**4. [MAJOR] Claim 3（CodeQL 可扩展性）在实验章节无专属小节**

paper_framing 列出 Claim 3: "Scope-bounded inter-procedural data-flow analysis via CodeQL provides a practical pipeline"，关键证据 (0% timeout, 78% Z%, 123/131 repos) 来自 plan_006_scalability。但 §4 中仅在 §4.1 Dataset 段落提及了部分数字，没有 dedicated analysis。plan_006 的 tier-wise scalability 数据（small/medium/large/xlarge）完全未出现。

**建议**: 增加 §4.3.x "Structural Extraction Scalability" 小节，或在 §4.1 扩展报告 plan_006 关键指标。

---

**5. [MAJOR] BM25 baseline (§4.3.4) 和 Pool Size Sensitivity (§4.3.6) 完全是 placeholder**

plan_018 Phase 2（GPU 训练）仍为 QUEUED，plan_019 未启动。Dream 审稿三档一致认定缺 BM25 baseline 是 "#1 structural gap"。这两个小节的完成对论文可投稿性是 blocking dependency。

**状态确认**: Phase 1 (CPU mining) 已完成，BM25 数据已就绪。这不是草稿问题而是实验进度问题，但草稿应明确标注 blocking 依赖。

---

**6. [MAJOR] 无统计检验规范**

§4.1 Seeds 段落说 "We report bootstrap 95% confidence intervals for all pairwise comparisons"，但未指定 bootstrap 方法细节（resample unit 是什么？seed-level resampling n=3 还是 instance-level？bootstrap iterations 数量？）。n=3 seeds 的 seed-level bootstrap CI 几乎无统计意义。如果用 instance-level bootstrap（在 val set ~3K instances 上），需要说明 instance 间非独立性（同 repo 的 instances 相关）。

**建议**: 明确 bootstrap 的 resampling unit 和方法。如果是 seed-level，坦诚承认 n=3 的限制。

---

**7. [MINOR] 训练/验证集大小应报告精确范围**

§4.1 写 "~11,300 training and ~3,000 validation"。实际各 seed 不同: train 11,236–11,308, val 2,980–3,052。建议改为 "11,236–11,308 training and 2,980–3,052 validation instances (varying by seed due to stratified splitting)"。

---

**8. [MINOR] RepoBench-R 引用 placeholder**

§4.4 Limitations: `\cite{[TBD: key]}` 需补充。RepoBench 原始论文: Liu et al., 2023.

---

**9. [MINOR] §4.3.5 neg_difficulty 分析与训练结果的桥接缺失**

neg_difficulty table 数据完整且经 registry 验证全部正确（3 位小数均匹配）。但该分析旨在解释 strategy × encoder interaction，而 interaction 的训练证据（dataflow 结果）全部是 placeholder。当前该节是 self-contained 的 pretrained-space 分析，但与 §4.2 的因果连接完全依赖于尚未产出的 dataflow 训练数据。

**建议**: 在 §4.3.5 开头增加一句前向引用，明确该分析的解释力取决于 §4.2 的完整结果。

---

**10. [MINOR] margin compression 百分比方向性表述可能误导**

§4.3.5: "embedding-distance mining reduces Qwen's margin by 77% (0.074→0.017) versus 65% for StarCoder (0.194→0.067)"。数学正确（(0.074-0.017)/0.074=77%），但 "reduces margin" 的表述暗示这是坏事。在 hard negative mining 语境下，更小的 margin = 更难的 negatives = 更强的训练信号。建议改为更中性的表述，如 "compresses the margin"。

---

### 数字准确性审计

| 草稿数字 | Registry 来源 | 状态 |
|---|---|---|
| 44,173 instances | m1_extraction: 50,869-6,696 skip = 44,173 | ✅ |
| 123 repositories | m1_extraction: repos_with_output=123 | ✅ |
| 15,897 (36.0%) | m1_extraction: 15,133+764=15,897, rate=0.36 | ✅ |
| 14,288 | plan_018: 各 seed train+val=14,288 | ✅ (D042 待确认) |
| ~11,300 train / ~3,000 val | plan_018: 11,236-11,308 / 2,980-3,052 | ✅ (约数) |
| Qwen random s42=0.5527 | m2_full_qwen: random_s42 best_R@1=0.5527 | ✅ |
| Qwen random s43=0.5554 | m2_full_qwen: random_s43 best_R@1=0.5554 | ✅ |
| Qwen random s44=0.6009 | m2_full_qwen_continued: random_s44 best_R@1=0.6009 | ✅ |
| Qwen embed s43=0.5606 | m2_full_qwen_continued: embedding_s43 best_R@1=0.5606 | ✅ |
| StarCoder random s42=0.4604 | m2_full_starcoder: random_s42 best_R@1=0.4604 | ✅ |
| neg_difficulty 全表 (12 cells) | neg_difficulty_analysis: qwen_2048 + starcoder_2048 | ✅ (全部匹配) |
| pos_sim Qwen=0.986 | 0.9855 → 0.986 (3dp rounding) | ✅ |
| pos_sim StarCoder=0.798 | 0.7985 → 0.799 (草稿写0.799, framing写0.798) | ⚠️ 微小不一致 |
| margin ratio 2.6–4.1× | registry sc_qwen_margin_ratio_2048: 2.61–4.07 | ✅ |

pos_sim StarCoder: §4.1 写 "0.798"，§4.3.5 Table 写 "0.799"。Registry 值 0.7985 四舍五入到 3dp = 0.799。§4.1 的 0.798 不准确。

---

### 修改建议（优先级排序）

1. **[必须]** 在 §4.3.2 或 Discussion 中量化 seed variance vs treatment effect，讨论统计力。这决定了 Claim 1 的 "reliable" 措辞是否站得住脚。
2. **[必须]** 更新 StarCoder random_s43 = 0.4912。
3. **[必须]** 确认 14,288 在 M1v2 完成后是否仍有效，或标记为 provisional。
4. **[强烈建议]** 为 Claim 3 增加 scalability analysis 小节。
5. **[强烈建议]** 明确 bootstrap CI 方法论（resampling unit, 是否 cluster by repo）。
6. **[建议]** 统一 StarCoder pos_sim: §4.1 的 0.798 → 0.799。
7. **[建议]** 精确化 train/val 数量描述。

---
