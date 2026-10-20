# reviewer / loop_4.md

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_4.md`
- **Structured JSON:** [`655474cf6e97c29e3289.json`](../../sessions/65/655474cf6e97c29e3289.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 4
reason: max_wall_time
updated: '2026-05-15T01:49:17+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单: autodl-5090 cuda:0-3，越界即 CRITICAL
- Dose-response 必须用 same-seed vanilla 做 baseline（seed=42 → vanilla-seed42=61.7%），不能用 3-seed 均值 65.3%。之前踩过这个坑（ROADMAP 曾写错 -16.4pp，正确是 -12.8pp）
- 50% vs 25% 差异仅 1/47 tasks，不可解读为"50% 优于 25%"——是噪声，正确叙事是 plateau
- 文献综述 (dose_response_literature_survey.md) 中多个引用未验证（Ye et al. ICLR 2025、Dohmatob & Feng ICLR 2025、Seddik et al.），论文写作前必须 reference-audit

### 2. 🖥️ 基础设施快照
- 服务器: autodl-5090 (root), 工作目录 `/root/autodl-tmp/tax_error_inject_agent`
- Python: `/root/miniconda3/bin/python` (conda base)
- 模型: `/root/autodl-tmp/models/Qwen/Qwen3-8B`
- Eval 脚本: `eval/recovery.py --model_path &lt;ckpt> --base_model &lt;model> --no_inject --output &lt;json>`
- 本地 workspace: `/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/`
- Artifacts: `artifacts/comprehensive_results.md`, `artifacts/dose_response_literature_survey.md`
- 分析脚本: `analysis/multiseed_stats.py` + `scripts/analyze_multiseed.py`（seed=123 已修复 ✓）

### 3. 📊 当前状态
**刚完成**: TaxEI dose-response 全部 4 点 + Random inject10 eval + training dynamics 分析

**RUNNING**:
- `v4-random-fixed-inject50-eval` (cuda:3) — eval 中，~7/47 进度

**关键未派发**:
- `v4-random-fixed-inject25-eval` — **最关键实验，已报告 3 次未被派发**。Checkpoint 就绪: `checkpoints/v4_random_fixed_inject25/v1-20260515-084707/checkpoint-1635`。3 GPU 空闲(cuda:0,1,2)

**已完成的 dose-response 数据**:
| 注入% | TaxEI | Random |
|-------|-------|--------|
| 0% | 61.7% | 61.7% |
| 10% | 61.7% (0pp) | 68.1% (+6.4pp) |
| 25% | 48.9% (-12.8pp) | **待 eval** |
| 50% | 51.1% (-10.6pp) | eval 中 |

### 4. 📋 待办
- random-inject50-eval 完成 → 核对结果 vs TaxEI 50% (51.1%)，更新 dose-response 对照表
- **random-inject25-eval 派发后完成** → 这是论文叙事分叉点：若 ≈48.9% 则"数据稀释阈值"；若远高于 48.9% 则"TaxEI 结构化错误有额外毒性"
- 6 点 dose-response 全齐 → 审查 comprehensive_results.md 更新、ROADMAP 更新
- 论文写作启动时 → 触发 reference-audit skill 验证所有引用
- training dynamics CSV 缺 taxei-inject10/inject25 → 需从 logging.jsonl 重新提取（训练成功但 CSV 提取失败）

### 5. 🎯 战略上下文
**项目**: Negative result paper → EMNLP 2026 Insights from Negative Results

**核心结论链**:
- D008: TaxEI=Vanilla (61.7%) → Gate 3a FAIL
- D014: Recovery eval TaxEI ≤ Random → 项目转 negative
- D015/D016: 3-seed TaxEI p=0.054 (NS)，方差梯度是最稳健 finding
- 新发现: dose-response 阈值-plateau 效应（10%=安全, 25-50%=崩溃平台）

**最容易判断错的事**:
1. Random inject10 = 68.1% 看起来是"random 注入有益"，但这是单 seed n=47，+6.4pp = 3 tasks，不能 overclaim
2. 所有均值比较都 NS（最小 p=0.054）——方差梯度（Vanilla 3.3 < Random 7.0 < TaxEI 8.6）才是 paper 最核心、最可辩护的 finding
3. Training dynamics 显示注入越多 train loss 越低但 eval 越差——这是 overfitting-to-noise，不是"注入改善训练"
4. PALADIN confound: ~30pp 来自 retrieval 不是 SFT，与我们的设定不可直接对比


---
