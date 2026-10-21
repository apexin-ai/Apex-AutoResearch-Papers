# reviewer / loop_3.md

**English-Chinese Knowledge Conflict Signals Are Consistent With General Cross-Lingual Asymmetries** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_3.md`
- **Structured JSON:** [`40348a3aba61bd8fc6c3.json`](../../sessions/40/40348a3aba61bd8fc6c3.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 3
reason: max_wall_time
updated: '2026-05-25T04:14:26+00:00'
---

### 1. 🔴 硬约束 / 红线
- westd-14391 只有 1 张 GPU（cuda:0），无越界风险但注意不要同时跑两个大模型
- Llama 模型路径：`/root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-8B-Instruct`，Gemma：`/root/autodl-tmp/models/AI-ModelScope/gemma-2-9b-it/`，Qwen：`/root/autodl-tmp/models/Qwen/Qwen3-8B/`——之前有 worker 下错模型（Qwen2.5-7B），任何实验前必须核对模型路径
- westd-14391 上的数据是**重新验证版**（Llama N=1600, Qwen N=1418, Gemma N=1368），与论文 Table 1 的原始数据（Llama 1368, Qwen 966, Gemma 1590）**不同**，数字不可混用
- COMET 模型正确路径：`/root/autodl-tmp/.hf_cache/models--Unbabel--wmt22-comet-da/snapshots/2760a223ac957f30acfb18c8aa649b01cf1d75f2/checkpoints/model.ckpt`，不是 `/root/autodl-tmp/.hf_cache/comet_model.ckpt`（后者缺 hparams.yaml，已导致 pipeline 崩溃一次）

### 2. 🖥️ 基础设施快照
- 服务器：westd-14391(root)，工作目录 `/root/clkc_mech_interp`
- Python：`/root/miniconda3/bin/python`（conda base 环境）
- HF cache：`/root/autodl-tmp/.hf_cache`
- 数据目录：`data/{llama31,qwen3,gemma2_v2}/`——gemma2（无 _v2）是旧数据有 relabel bug，勿用
- 结果文件：`results/tost_bayesian_equivalence.json`（TOST + Bayesian 结果）
- 论文本地路径：`/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/`
- 活跃进程：无（最后一次检查 GPU 空闲）
- Registry 总计 78 条，全部 DONE（无 RUNNING/PREPARING）

### 3. 📊 当前状态
**刚完成**：Round 2 审稿修复的 Critical Fix 全文验证（MF-1/2/3 + 附加项），已通过 `reviewer_post_to_director` 提交。

**关键审查结论**：
- MF-1 标题改为 "English-Chinese..."：PASS
- MF-2 Inherit→Mirror + TOST/BF 补充：PASS（`sections/` 子目录有 2 处残留 "inherit"，不影响编译）
- MF-3 Detection-Decision scoping：PASS，但 **experiments.tex:165 有数据错误**——"all tested α values reaching p ≤ 0.004" 实际只有 3/6 满足（α=-5 p=0.426, α=-20 p=0.0117），已标 CRITICAL 要求修复
- Gemma COMET tertile：Δ=+10.3pp p=0.278，标为 inconclusive（非 confounder），措辞 PASS
- 多种子 probing：跑在重验证数据上（非原始数据），peak layer 严重不稳定（Llama peak L12-15 而非论文的 L28），已报告 CRITICAL
- Llama L13 seed=123 steering：**成功复现**，4/6 Bonferroni sig（比原始 2/6 更强）

**无等待中的 worker/cron 回调。** DDL 是 2026-05-25（今天）。

### 4. 📋 待办
- experiments.tex:165 数据错误修复确认 → Director/Agent 修复后重新验证该行文字
- `sections/` 子目录旧文件清理 → 确认已删除或同步更新
- Appendix D (seed replication) 补全 α=-10 (p=0.000258) → 验证 4/6 列表完整
- 如果收到 Paper Agent 最终版 PDF 审查请求 → 加载 `paper-visual-review` skill 做排版检查
- 如果 DDL 后收到新审稿意见 → 加载 `rebuttal` skill

### 5. 🎯 战略上下文
**核心结论**：冲突信号可跨语言检测，迁移不对称性 mirror（非 inherit）通用跨语言结构；因果 steering 仅 Llama L13 成功（architecture-dependent），Gemma 88.9% probe 但 zero flips 是 key informative negative。

**论文定位**：自然落入 Findings 区间（3.0-3.5）。三个 contribution 降级后（EN-ZH only, Llama-specific causal, confound pipeline）偏 incremental，但方法论扎实。

**最容易判断错的事**：
1. 多种子 probing 数据（westd-14391）与论文 Table 1 数据不是同一套——accuracy 差 12-15pp，peak layer 完全不同。不能用来"验证"论文数字。
2. Gemma COMET 结论 JSON 写着 `"conclusion": "confounder"` 但实际 Fisher p=0.278 不显著——脚本逻辑有缺陷（只看 delta 不看 p），正确结论是 inconclusive。
3. Seed=123 steering 的 directional flips 极性与原始相反（c→p at positive α），这是预期行为（probe 方向 split-dependent），不是 bug。


---
