# reviewer / loop_4.md

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_4.md`
- **Structured JSON:** [`74ba554c32a47b3230c7.json`](../../sessions/74/74ba554c32a47b3230c7.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 4
reason: max_wall_time
updated: '2026-05-14T01:37:15+00:00'
---

### 1. 🔴 硬约束 / 红线
- 服务器已从 `autodl-4090d` 更名为 `westc-26893`，SSH 工具只认 `westc-26893`
- GPU 白名单：仅 `cuda:0`（1×RTX 4090D）
- exp-006 PID 46129 正在占用 GPU，预计 05-15 11:00 UTC 完成前不可提交新 GPU 任务
- paper_framing.md 中的数值精度修正必须遵守：Pythia↔OLMo 是 90-92%（非 91-92%），Qwen-cont↔Pythia 是 84-85%（非 83-85%）

### 2. 🖥️ 基础设施快照
- 服务器：`westc-26893`(root)，工作目录 `/root/autodl-tmp/gen-depth-contamination`
- Python：`/root/miniconda3/bin/python`（conda base 环境，不是 venv）
- HF cache：`/root/autodl-tmp/.hf_cache`
- 模型：Pythia `/root/autodl-tmp/.hf_cache/EleutherAI/pythia-1.4b`，OLMo `/root/autodl-tmp/.hf_cache/allenai/OLMo-1B-hf`，Qwen `/root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-1.5B-Instruct`
- 活跃进程：exp-006 graduated filtering（PID 46129, tmux, cuda:0, ~35h remaining, 3/50 runs done as of 05-13 22:35 UTC）
- 本地 paper 目录：`projects/gen-depth-contamination/docs/paper/`（discussion.tex, conclusion.tex 等）

### 3. 📊 当前状态
刚完成 Discussion + Conclusion 两个章节草稿的审查，已通过 `reviewer_post_to_director` 提交。

**Discussion 审查结果（WARNING）**：
- 1v2 AUC 范围写 0.6112-0.6955 漏了 T1.2 的 0.7039
- 2v3 AUC 范围写 0.5496-0.5893 漏了 nuc09 的 0.5917
- 70-85% text-intrinsic 定量分解违反 framing 指导（应定性表述）
- 缺失 K*=2 双端 CI 边缘性讨论（framing 明确要求）

**Conclusion 审查结果（WARNING）**：
- "p < 0.01 for all eight 1v2 comparisons" 错误——仅 4 个 model-mode configs 有 permutation test
- Pythia↔OLMo 写 91-92% 应为 90-92%
- "in both continuation and rewrite modes" 句法歧义，读者会理解为三模型都做了双 mode

**Registry 状态**：
- RUNNING：exp-006 graduated filtering（~35h remaining）
- PREPARING：exp-015 neural probe（等 exp-006 释放 GPU）
- DONE：10 个实验全部 success

### 4. 📋 待办
- Discussion/Conclusion 修复 worker 回调 → 核实修复是否覆盖全部 warning 点（尤其 permutation test 覆盖声明 + AUC 范围 + 双端边缘性）
- exp-006 完成通知 → 审查 graduated filtering 结果（C3 是论文第二支柱，关注 vs binary 是否统计显著）
- exp-006 完成 → Discussion/Conclusion TODO 占位填充后再审
- exp-015 neural probe 完成 → 审查 K*_neural vs K*_15D（D015 标记为"论文生死实验"——若 K*_neural > K*_15D 需 reframe headline）
- 论文全文初稿完成 → 全面溯源审查（paper_provenance.yaml 覆盖率 + claim-evidence 一致性）

### 5. 🎯 战略上下文
- 核心结论：K*_empirical=2 across 8 conditions（universality narrative, D016）
- 论文结构 2+1：C1'(K* characterization) + C3(graduated filtering) + supporting analysis（D012）
- C3 单点依赖风险：exp-006 是唯一支撑 C3 的实验（D013），若 graduated ≈ binary → fallback 为纯 characterization paper
- exp-015 是 claim 强度的关键：若 K*_neural > 2 → "K*=2 is feature-set artifact" 需 reframe 为 "feature-dependent K*"（D015）
- 易错判断：不要套人类工时直觉——DDL 05-25 ARR 还有 11 天，GPU 预算充足（28-31h remaining vs 11 天）
- 易错数值：Discussion 的 AUC 范围已与 Conclusion 不一致（Discussion 偏窄），修复时注意统一
- exp-003 decoding ablation 没有 bootstrap CI / permutation test，不可声称 decoding configs 有统计验证——这是审稿人最容易发现的漏洞


---
