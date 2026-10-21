# Memory — trace-verdict-study

## Full_trace 3-Seed 统计结论 (2026-05-23)

3-seed mean accuracy = **80.61% ± 1.09%** (seed42=81.76%, seed123=79.58%, seed456=80.50%)。
方差（std=1.09pp）介于 exception_only（0.20pp）和 no_trace（2.31pp）之间。

**信号强度→方差单调关系**：exception_only (0.20%) < full_trace (1.09%) < no_trace (2.31%)。诊断信号越强，种子间方差越小。full_trace 的中间方差符合其 "包含诊断信号但被稀释" 的定位。

## No_trace 3-Seed 统计结论 (2026-05-23)

3-seed mean accuracy = **76.42% ± 2.31%** (seed42=75.13%, seed123=79.08%, seed456=75.04%)。
方差（std=2.31pp）显著高于 exception_only 3-seed（std=0.20pp），符合预期：弱学习信号→模型对初始化更敏感。

对比 exception_only 3-seed mean = 99.22% ± 0.20%，差距 = **22.80pp**。
这是 Two-Pathway Model 最核心的定量对比：explicit pathway (diagnostic tokens) vs implicit pathway (terminal state only)。

## Gradient Masking 3-Seed 统计结论 (2026-05-22)

3-seed mean accuracy = **99.22% ± 0.20%** (seed42=98.99%, seed123=99.33%, seed456=99.33%)。
exception_only baseline = 99.83%。full_trace = 81.76%。

**Decomposition**：
- Gradient dilution 解释 ~0.6pp 退化（99.83% → 99.22%），占 ~3%
- Content quality 解释 ~17.5pp 退化（99.22% → 81.76%），占 ~97%

这是 MF-2 最核心的定量证据：full_trace 性能差主要因为缺乏诊断信息（content），而非训练信号被非诊断 token 稀释（gradient dilution）。

## Exception 子组件消融完整结果 (2026-05-22)

三个子组件均独立达到 Tier 1（>99%），排序：
- exc_type_only: 100%（eval_loss ~0.01）
- exc_stacktrace_only: 99.83%（eval_loss ~0.05）
- exc_message_only: 99.50%（eval_loss **0.58**）

**关键洞察**：exc_message_only 的 eval_loss 远高于另两个（10-60x），但 verdict accuracy 仍达 99.5%。模型对 message 文本的 token-level 预测不确定性高，但 verdict 分类的决策边界仍然清晰。exception type 是最浓缩的诊断信号。

## Cross-dataset Generalization 关键发现 (2026-05-22)

HE→MBPP：
- exception_only: 99.41%（同数据集 99.83%，仅降 0.4pp）
- no_trace: 70.56%（同数据集 75.13%，降 4.6pp）
- **exception_only_nomarker: 95.46%**（vs 带标记 99.41%，降 3.95pp）

MBPP→HE：
- exception_only: 100%（完美迁移）
- no_trace: 67.99%（大幅退化）

**结论**：exception trace SFT 教会模型可迁移的代码推理能力。这是 MF-2 (near-tautological) 的核心反驳证据。

**Nomarker 跨域发现**：格式标记在跨数据集场景贡献 ~4pp（同分布仅 ~2pp），可能因为格式标记在陌生代码模式下提供额外结构线索。但 95.46% 仍远高于 no_trace（70.56%），exception 语义内容仍解释 >90% 的跨域泛化。

## Round 15 统计实验摘要 (2026-05-22)

- MF-3 Holm-Bonferroni: 80 pairwise, 67/80 仍显著。仅 3 个 borderline 失去显著性。
- MF-4 去重 Bootstrap: 实际只有 **119 unique problems**（每题 10 变体）。CI ~2.2x wider，但 ≥14pp 差异全部保持显著。论文需注明有效 n=119。
- SF-6 Tier Clustering: k=2 在 3/4 模型 + pooled 中最优，与论文划分吻合。
- SF-7 Oscillation: full_trace CV 是 exception_only 的 10x，max drop −5.29pp (step 50→100)。

## Budget Curve 数据混淆教训 (2026-05-22)

之前错误使用了 plan_006 数据（trace-section truncation），而非 Table 12 数据（whole-input tail truncation）。两种截断概念不同，已用正确数据重新生成。

## Phase Transition 跨模型一致性 (2026-05-22)

4 个模型在 tail 384→512 区间全部出现 13~22pp 阶跃。CodeLlama-13B tail-2048 灾难性失败（28.49%）。

## cuda:0 已恢复 (2026-05-23)

服务器重启后 cuda:0 driver context orphan 问题已修复，两张 GPU 均可用。之前 nvidia-smi --gpu-reset 返回 "Not Supported"，重启是唯一方案。

## FullTraceFormatter 缺陷 (2026-05-22)

FullTraceFormatter 只读 ev['locals']，丢弃 ev['exception'] dict，diagnostic token ratio 接近 0 (0.0014)。

## 模型版本已验证

- Qwen2.5-Coder-7B-Instruct: 主力模型
- Qwen2.5-Coder-1.5B-Instruct: 小模型验证
- deepseek-coder-6.7b-instruct: 跨架构验证
- CodeLlama-13b-Instruct-hf: 跨架构+大模型验证
