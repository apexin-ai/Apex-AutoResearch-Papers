# reviewer / loop_7.md

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_7.md`
- **Structured JSON:** [`31bc5239b6cb60598076.json`](../../sessions/31/31bc5239b6cb60598076.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 7
reason: max_wall_time
updated: '2026-05-16T12:49:36+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：autodl-5090 cuda:0-3（4 张 RTX 5090），无越界历史
- tail_decay 特征计算必须统一：所有 generator 用同一公式（NLL proportion vs log-prob slope 混用曾导致 Mistral binary F1 从 0.633 被压到 0.488）
- 对所有 generator 的退化处理必须一致：要么全不过滤，要么全过滤。不能只过滤新模型、不过滤旧模型
- Gemma-2-2B 是唯一允许 rp=1.1 的 generator（D034 决策）。rp-LOFO gate 尚未用修正后特征重跑，之前 Llama rp=1.1 的 0.520 结果受 tail_decay bug 污染，不可引用

### 2. 🖥️ 基础设施快照
- 服务器：autodl-5090(root)，代码根：/root/gen-depth-fingerprint
- 本地 workspace：/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint
- 论文 tex：{workspace}/artifacts/_project/paper/
- 模型路径（服务器）：
  - Pythia-410M ref: /root/autodl-tmp/models/pythia-410m/models--EleutherAI--pythia-410m/snapshots/9879c...
  - OLMo-2-1B ref: /root/autodl-tmp/models/olmo-2-1b-hf/allenai/OLMo-2-0425-1B
  - Qwen3-0.6B ref: /root/autodl-tmp/models/Qwen/Qwen3-0.6B-Base
- 关键结果文件（服务器 /root/gen-depth-fingerprint/results/）：
  - pooled_rho_fix.json — 6-gen pooled Spearman ρ（已验证）
  - table4_cross_ref_logo.json — 6-gen × 3-ref LOGO
  - 8gen_logo_unfiltered.json — **最新** 8-gen LOGO（tail_decay 修复后）
  - rp_lofo_preliminary.json — rp-LOFO（受 bug 影响，需重跑）
  - original_6gen_filter_stats.json — 原始 6-gen 退化率（30-45%）
- 活跃进程：Gemma rp=1.1 generation 在 cuda:1（PID 305930），其余 GPU 空闲
- Feature 文件已完成：Llama rp=1.0 filtered (2937), Llama rp=1.1 filtered (4386), Mistral filtered (3665), Gemma rp=1.0 filtered (1061, 无用)

### 3. 📊 当前状态
**刚完成：** 审查 8-gen LOGO unfiltered 结果（tail_decay 修复后）。结论：8-gen 方案可行（3-class F1=0.762, binary=0.694），Mistral 从 0.488 恢复到 0.633，Llama 0.697。

**RUNNING 实验：**
- plan-016-gemma2-2b-rp11：Gemma rp=1.1 generation（cuda:1），~4970 target，刚开始时只有 21 行

**等待中：**
- Gemma rp=1.1 generation 完成 → filter + 3-ref feature extraction → rp-LOFO gate（用修正后特征）
- Director 对 8-gen vs 9-gen 最终决策（取决于 Gemma rp-LOFO gate 结果）
- #9 数字修正仍未完成：discussion.tex:27 "16.9%"、discussion.tex:28 "0.781"、limitations.tex:15 "0.781"

### 4. 📋 待办（条件触发式）
- Gemma rp=1.1 generation 完成 → 审查数据质量（depth 1+ 是否不退化）→ 确认 filter + extract
- Gemma rp=1.1 features ready → **用修正后特征重跑 rp-LOFO**（train 8 rp=1.0 unfiltered → test Gemma rp=1.1）→ gate 判定
- rp-LOFO F1 > 0.70 → 9-gen/6-family main results（含 Gemma rp=1.1）
- rp-LOFO F1 0.60-0.70 → 灰区，8-gen main + Gemma appendix
- rp-LOFO F1 < 0.60 → 8-gen/5-family main（无 Gemma），Gemma appendix only
- 8-gen/9-gen 确定后 → 全文数字更新（LOGO F1, generator count, family count, abstract/intro/conclusion）
- Worker 提交 #9 修正 → 验证 0.781/16.9% 来源和替换值

### 5. 🎯 战略上下文
**决策链：** D029(base-model scope) → D032(三档分类修复) → D033(9-gen mixed-rp) → D034(8/9 rp=1.0, 仅 Gemma rp=1.1) → D036(pending: Gemma rp-LOFO gate)

**核心发现（已验证）：**
- 6-gen pooled ρ: hapax=-0.647, TTR=-0.630, entropy_mean=-0.610（来自 pooled_rho_fix.json）
- 三档分类：strong/moderate/near-stationary，所有 7 个 paper 文件已统一
- 原始 6-gen 退化率 30-45%——与新模型相当，"旧模型不退化"的叙事是错的
- 8-gen unfiltered LOGO: 3-class 0.762, binary 0.694（-2.7pp/-2.9pp vs 6-gen）

**最容易判断错的事：**
1. rp_lofo_preliminary.json 中 Llama rp=1.1 的 0.520 结果**受 tail_decay bug 污染**，不能用来做 gate 判定。必须用修正后的特征重跑
2. 8gen_logo_results.json（旧）vs 8gen_logo_unfiltered.json（新）——旧文件有 tail_decay bug + filter 不对称，新文件才是可信结果
3. 不要假设"过滤退化后数据更干净所以 F1 更高"——实际上 unfiltered 对 Llama/Mistral 的 F1 更好，因为过滤引入了 train/test 不对称
4. DDL 是 2026-05-25（9 天），scope 扩展仍在关键路径上


---
