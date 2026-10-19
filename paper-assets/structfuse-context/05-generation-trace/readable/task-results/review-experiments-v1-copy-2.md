# review experiments v1

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_review_experiments-v1_20260515T140139_result.json`
- **Structured JSON:** [`1f821f3c9323c2bce7c6.json`](../../sessions/1f/1f821f3c9323c2bce7c6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All data collected. Let me compile the review.

---

## 审查结果: NEEDS_REVISION

### 问题清单 (按严重程度)

**1. [CRITICAL] 草稿 >70% 是 TBD 占位符，不具备审查实质内容的条件**

18 个 M2 runs 仅完成 ~6 个（Qwen: random×3 + embed_s43 done, embed_s44 running; StarCoder: random_s42 done, random_s43 done, random_s44 running）。Main Results 两张表中仅填入 4 个 Qwen 值和 1 个 StarCoder 值。所有 mean、CI、delta 均为 X.XX。Claim 1 的核心证据（embedding > random across seeds and encoders）目前只有 1 个完整 seed 比较（Qwen s43: 0.5606 vs 0.5554, Δ+0.52pp）。**无法对 claim-evidence 对齐做出实质判断。**

建议：M2 全部完成后重新提交审查。当前版本仅作为结构模板评估。

**2. [CRITICAL] Claim 3（CodeQL scalability）在 Experiments 中完全缺失**

plan_006 在 registry 中标记为 DONE，有详细 metrics（0% timeout, 78% Z%, 123/131 repos），但 experiments_v1.md 没有任何对应的 subsection 或 table。Claim 3 是 paper_framing.md 的三个 core claims 之一，实验章节必须有对应证据。

建议：添加 §4.3.x "Structural Extraction Scalability" subsection，报告 timeout rate, Z% by repo tier, coverage。

**3. [CRITICAL] Seed 44 outlier 未做统计处理，存在 inflate mean 的风险**

Qwen random_s44 R@1=0.6009，比 s42/s43（0.5527/0.5554）高出 ~4.5pp。3-seed mean 会被严重拉高。如果 embedding_s44 也偶然较高（当前 eval@500 R@1=0.5942），mean delta 可能完全由 seed variance 驱动而非策略效应。草稿 §4.3.2 承认了这一点但全部 TBD。

建议：报告 median 和 leave-one-out 分析作为 primary robustness check。若排除 s44 后 embedding > random 仍成立，才能支撑 "reliable"。D051 已经要求 mean ± std，但 std 可能比 treatment effect 还大。

**4. [MAJOR] 缺少 plan_005 分层分析 subsection**

ROADMAP D053 已将 plan_005 升级为 P0（Claim 2 唯一定量支撑），experiment_plan.yaml 列出 5 维分层分析，但 experiments_v1.md 没有对应 subsection。Claim 2（dataflow × geometry interaction）在草稿中仅靠 §4.3.5 neg difficulty 的 pretrained-space 分析支撑，没有 training R@1 分层数据。

建议：添加 §4.3.x "Stratified Analysis" subsection。

**5. [MAJOR] "zero additional computational cost" claim 未提供计量支撑**

Claim 1 反复说 "zero additional computational cost over random sampling"，但草稿从未量化各策略的 mining time。Embedding-distance mining 需要先跑一遍 encoder forward pass 计算所有文件的 embedding，这不是零成本。

建议：报告各策略的 mining wall-clock time（random: 0, BM25: X min, embedding: X min, dataflow: X min CodeQL + X min BM25）。如果 embedding mining 的一次性成本远小于训练时间，可以说 "negligible additional cost"，但不能说 "zero"。

**6. [MAJOR] 数字一致性问题：StarCoder pos_sim 文本 vs 表格不一致**

§4.1 line 7: "StarCoder maintains healthy separation (0.798)"
Table 5 line 161: StarCoder random pos_sim = 0.799

Registry ground truth: 0.7985。两者都是合理的四舍五入，但同一篇论文中不一致会引发 reviewer 质疑。

建议：统一为 0.80 或 0.799。

**7. [MAJOR] §4.3.5 interpretive language 过强**

- Line 171: "embedding-distance negatives occupy **precisely the region** where the encoder is most uncertain" — "precisely" 暗示精确定位，实际是宽泛的 distributional pattern
- Line 171: "providing **maximal** gradient signal" — 未经证明。gradient signal 没有被测量

建议：改为 "negatives drawn from the high-similarity tail of the pretrained distribution, where the encoder has least separation" 和 "providing stronger gradient signal"。

**8. [MAJOR] BM25 overlap 87.1% 未讨论**

plan_018 Phase 1 数据显示 BM25 vs embedding negatives 的 overlap = 87.1%。这意味着两种策略在 87% 的 negative 选择上完全一致，策略差异主要来自 13% 的不同。这对 "different strategies explore different dimensions of difficulty" 的叙事是严重挑战。草稿未提及此 finding。

建议：在 §4.3.4 或 §4.4 Discussion 中报告 overlap 率，讨论其对策略区分度的 implication。特别是 small repos（<50 files）overlap 更高（66.8% top-7 Jaccard），说明策略差异仅在大 repo 中有意义。

**9. [MINOR] s42 regime 不一致未充分说明**

s42 跑 3 epochs 无 early stopping，s43/s44 跑 2 epochs 有 early stopping。脚注提到是为了 "overfitting diagnostic curve"，但这意味着 s42 的 best_by_R@1 checkpoint 搜索范围比其他 seed 大 50%（4242 vs 2816 steps），引入 checkpoint selection bias。

建议：在 §4.3.1 或 Limitations 中明确说明这一 confound。D047 已标记需要 s42 重跑（2-epoch regime），建议优先执行。

**10. [MINOR] Pool 构造细节缺失**

§4.1 说 "Pool-based retrieval with pool size 50 (1 positive + 49 negatives)" 但未说明 49 个 negatives 如何从 repo 中采样。是随机？按距离？同 repo 内？跨 repo？

建议：补充 pool 构造协议。

**11. [MINOR] 无 pretrained baseline（zero-shot retrieval）**

所有策略都是 contrastive fine-tuning 后的结果。缺少 pretrained encoder 直接做 retrieval 的 baseline，无法说明 fine-tuning 本身的价值。

建议：添加 "Pretrained (no fine-tuning)" 行到 Table 1/2。

**12. [MINOR] §4.4 Limitations 用 plan 编号**

Line 190: "Sensitivity to pool size at evaluation time will be reported in §4.3.6 (pending plan_019 completion)" — plan_019 是内部编号，不应出现在论文中。

建议：删除所有 plan_NNN 引用。

### 修改建议

1. **等 M2 完成**后填入所有数字，重新提交审查
2. **添加 3 个缺失 subsection**: CodeQL scalability (Claim 3), Stratified analysis (Claim 2), Pretrained baseline
3. **量化 mining cost**: 一个表格比较各策略的 data preparation wall-clock time
4. **统一数字精度**: 全文采用一致的小数位数规则（建议 3 位）
5. **弱化 interpretive language**: §4.3.5 中的 "precisely"/"maximal" → "approximately"/"stronger"
6. **报告 BM25-embedding overlap**: 在 Discussion 中讨论策略重叠率的 implication
7. **处理 s44 outlier**: 报告 median + leave-one-out + 排除 s44 后的 robustness check
8. **清理 plan 编号**: 论文中不应出现内部 tracking ID

### 审稿攻击面预演

| 攻击点 | 严重度 | 预期 reviewer 措辞 | 防御准备 |
|--------|--------|-------------------|----------|
| **Effect size 仅 +0.52pp**（s43）| 致命 | "The improvement is within noise range. Is this practically meaningful?" | 需 3-seed mean + CI 证明显著性；若 CI 跨零则 Claim 1 需大幅 reframe |
| **Seed 44 outlier** | 高 | "Seed 44 inflates your means. Report median or exclude it." | Leave-one-out table showing ranking holds; per-seed val difficulty check (D050) |
| **Pool=50 太小** | 高 | "Real repos have hundreds of files. Does your finding hold at pool=200+?" | plan_019 必须完成并报告 |
| **只有 2 个 encoder** | 中 | "n=2 is anecdotal. You need ≥3 for any geometry interaction claim." | 已在 Claim 2 用 "exploratory observation" 降级，但 reviewer 可能仍嫌不够 |
| **36% structural coverage → 64% fallback** | 中 | "Your dataflow strategy is really 36% dataflow + 64% embedding. You're testing a diluted mixture." | plan_005 分层分析必须显示 dataflow-rich 子集有更大差异 |
| **无 downstream task** | 高 | "R@1 improvement doesn't mean anything if it doesn't help fix bugs." | plan_003 SWE-bench 必须完成 |
| **BM25 训练 baseline 缺失** | 高 | "You claim CoCoHaNeRe's BM25-proxy caused harm but don't train with BM25 negatives yourself." | plan_018 Phase 2 必须完成 |
| **"Zero cost" 未证明** | 中 | "Embedding mining requires a forward pass over the corpus. That's not zero cost." | 量化 mining time 并改措辞为 "negligible" |

**最危险场景**: 3-seed Qwen mean embedding-random delta < 1pp 且 CI 跨零。此时 Claim 1 的 "reliable improvement" 不成立，需要启动 D052 Scenario C/D 应急方案。当前唯一完成的 seed (s43) delta 仅 +0.52pp，这个风险是真实存在的。

---
