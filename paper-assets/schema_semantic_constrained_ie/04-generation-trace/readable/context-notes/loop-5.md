# director / loop_5.md

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_5.md`
- **Structured JSON:** [`fb173f3d56087bbbf636.json`](../../sessions/fb/fb173f3d56087bbbf636.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 5
reason: max_wall_time
updated: '2026-05-16T14:57:23+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目只有 westd-16980 和 westd-21461 两台服务器，各 2 张卡（cuda:0, cuda:1）。westd-37397 已关机移除，不要尝试连接
- DocRED latency 数据只能从 `/tmp/latency_benchmark_docred_results.json` 提取。`/tmp/latency_benchmark_results.json` 是 SciERC 旧数据，绝对不能用于 DocRED
- Qwen tokenizer regex warning 是 transformers 4.57.6 false positive (D034)，**绝对不能设 fix_mistral_regex=True**——会把 Qwen regex 替换成 Mistral tekken regex 导致结果错误
- 模型名称是 Qwen3-8B（不是 Qwen2.5-7B），ft_ablation_analysis.md 已修正过一次
- Agent 经常把已完成实验报告为失败（基于 exit code 而非输出完整性）——cron 报 FAILED 时先检查 output 文件 wc -l

### 2. 🖥️ 基础设施快照
- **westd-16980**: 2×GPU，conda base env，`/root/miniconda3/bin/python`，项目目录 `/root/schema_semantic_constrained_ie`
  - cuda:0: 空闲（latency benchmark 已完成）
  - cuda:1: w8_llama_docred_ft_semantic_only (PID 361202)
- **westd-21461**: 2×GPU，同上 conda base env
  - cuda:0: w8_qwen_docred_ft_grammar_only (PID 18555)
  - cuda:1: w8_qwen_docred_ft_semantic_only (PID 20035)
- 模型 checkpoints: `/root/autodl-tmp/checkpoints/` 下 `qwen3_8b_lora_scierc_merged`, `llama_lora_docred_merged` 等
- 3 个 RUNNING 实验均有 cron 120s 轮询监控

### 3. 📊 当前状态
**刚做完**：DocRED latency benchmark 完成（+5.4% max overhead），已派 Paper Agent patch 入稿。论文 Round 4 Reviewer = 7/10，连续两轮无 CRITICAL/WARNING。ROADMAP 刚更新。

**RUNNING (3)**：
- w8_llama_docred_ft_semantic_only — westd-16980 cuda:1, ~17% 时约 3h（从 ~12:30 UTC 启动）
- w8_qwen_docred_ft_grammar_only — westd-21461 cuda:0, ~64% 时约 2h
- w8_qwen_docred_ft_semantic_only — westd-21461 cuda:1, ~49% 时约 3h

**Paper Agent**: Round 4 收敛(7/10)，待命等下一批 Patch（DocRED FT ablation 数据）

**等待中**：3 个实验的 cron 完成回调 → Agent 跑 violation checker → 汇报 metrics

### 4. 📋 待办
- w8_qwen_docred_ft_grammar_only 完成 → Agent 跑 violation checker + metrics → 预期 DR≈0.76%（grammar 不降 DR）
- w8_qwen_docred_ft_semantic_only 完成 → Agent 跑 violation checker → 预期 DR 降 40-68%
- w8_llama_docred_ft_semantic_only 完成 → Agent 跑 violation checker → 预期 DR 降 40-68%
- 3 个实验全部完成 → 派 Paper Agent [Patch] DocRED FT ablation 表格补全 → 提交 Round 5 Reviewer
- Round 5 收敛后 → 更新 ROADMAP → 考虑 dream_simulate(review_mode="full") 做最终评估
- 论文最终版 → submit_paper_to_review 正式提交审稿团队（Group C）

### 5. 🎯 战略上下文
- **核心结论已站住**：Grammar 层消除 ET/RV，Semantic 层消除 DR，两层互补不可替代。Composability 2×2 全部通过。3 模型泛化性已验证。
- **Post-hoc defense (C2)**: constrained recall > post-hoc recall 在 6/6 ZS 组成立。Mistral DocRED 有 crossover point（reject>70% 时 constrained F1 > post-hoc F1）。
- **CF 叙事**: model-dependent——well-calibrated 模型 CF↑（因 per-relation type commitment），poorly-calibrated Mistral CF↓（56.87%→1.27%，grammar 修复格式不一致）。论文用 "baseline calibration" 框架统一。
- **易错点**：Agent reset 后经常不知道 latency benchmark 已完成，会尝试重新跑——拦住它。也容易把 SciERC latency 文件误当 DocRED 数据。
- **Dream 审稿暴露的 5 个结构性问题**：related work (SynCode/IterGen/BoostCD) ✅已补、FT ablation ✅正在补、FT post-hoc ✅已做、entity types 太少（决定不加 NYT29, D031）、novelty 定位（Paper Agent 已调整 framing）
- **距 DDL May 25 还有 9 天**，时间充裕。当前瓶颈纯粹是等 3 个 GPU 实验跑完。


---
