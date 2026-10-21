# director / loop_2.md

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_2.md`
- **Structured JSON:** [`dc884db4d714fecd9378.json`](../../sessions/dc/dc884db4d714fecd9378.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 2
reason: max_messages
updated: '2026-05-23T21:36:16+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：rtx6000-4x cuda:0/1/2/3, autodl-8gpu cuda:0/1/2/3。严禁使用其他卡
- vLLM max-model-len **必须 ≥8192**。之前 Worker "优化"降到 4096 导致所有长 prompt 被 400 跳过，造成系统性数据空洞（M022）。绝不允许再降
- 论文占位符（XX/TBD）只能用 N=17 MCMC 结果填写，不能填 N=8 旧数据——§4.1 和 limitations 已按 N=17 重写
- API proxy: http://47.94.22.126/v1，402=余额不足。RPM 当前设置：sonnet 150, gemini/deepseek/qwen3 100
- MCMC hard cutoff: **May 25 16:00 UTC**，用 J=6 full-coverage 启动（D035），不等 DeepSeek

### 2. 🖥️ 基础设施快照
- **rtx6000-4x** (connect.westd.seetacloud.com, root): /root/gated_mfrm_judge_bias
  - cuda:0 vLLM LLaMA-3.3-70B (port 8000), cuda:1 Qwen2.5-72B (port 8001), cuda:2 Mistral-Large-2 (port 8002), cuda:3 空闲
  - collect.py: LLaMA(PID 665441) Qwen(PID 665509) Mistral(PID 665583), 全部 --workers 10
  - API judges: Sonnet(PID 653489) Gemini(PID 653490) DeepSeek(PID 653491) Qwen3(PID 653492), --workers 10
  - Partial judges: GPT-5.5(PID 659566) Opus(PID 659677), --workers 5, N=8 数据
  - 日志：logs/llama_fixed.log, qwen_fixed.log, mistral_fixed.log（可能需 -u 参数才有输出）
- **autodl-8gpu** (connect.westd.seetacloud.com, root): /root/gated_mfrm_judge_bias
  - cuda:0 exp-017 (Murphy-Topel coverage, PID 318082, 148/800 fits), cuda:1/2/3 空闲
- 论文源码：/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/
- MCMC 脚本：run_exp003_n17.py (warmup=6000, samples=4000, chains=4, stop-loss R̂>1.1 or ESS<50)
- 下游分析：run_n17_downstream.py (6-step pipeline)
- 匿名仓库：https://github.com/anonymous-nlp-2026-2/gated_mfrm_judge_bias (commit 3c3f7da)

### 3. 📊 当前状态
刚完成 vLLM max-model-len 修复（8192 恢复），Reviewer 已验证通过。等 15 分钟稳态速率确认。

**Judge 进度（截至修复前，约 May 24 05:00 UTC）：**
| Judge | 完成/目标 | DDL 可行？ |
|-------|----------|-----------|
| Sonnet | ~11,500/18,000 | ✅ ETA ~9h |
| Qwen3-235B | ~8,300/18,000 | ✅ ETA ~16h |
| LLaMA-local | ~7,000/18,000 | ✅ 修复后需确认 |
| Gemini | ~7,800/18,000 | ✅ ETA ~19h |
| Qwen-local | ~9,850/18,000 | ✅ 修复后需确认 |
| Mistral-local | ~9,400/18,000 | ⚠️ 修复后需确认 |
| DeepSeek | ~6,900/18,000 | ⚠️ ETA ~23h, 可能超 cutoff |
| GPT-5.5 partial | ~8,500/9,000 | ✅ |
| Opus partial | ~9,150/9,000 | ✅ 需 dedup |

**Registry RUNNING**: exp-017 (Murphy-Topel coverage, 148/800), exp-019 (N=17 MCMC, 待 judge 完成)
**数据审计**：完成，无数值错误。appendix 四舍五入已确认无需修改（值已正确）。

### 4. 📋 待办（条件触发式）
- Reviewer 稳态速率报告到达 → 确认本地 judge 400 错误消除 + 速率恢复；如果仍慢，降 --workers 到 4
- 全部 ≥6 judge JSONL 达到 18,000 行 → 启动 MCMC（run_exp003_n17.py），Opus JSONL 需先 dedup
- MCMC 完成 → 派 Agent 跑 run_n17_downstream.py（LOO/WAIC, baselines, bootstrap Δτ, weight sensitivity, bias absorption, facet fit）
- 下游分析完成 → 派 Paper Agent 填写所有 TBD/XX 占位符（abstract/experiments/limitations/conclusion/appendix），更新 Table 1 N=17 列
- 论文更新完成 → 派 Agent 做最终数据审计 + 编译 → 重推匿名仓库 → submit_paper_to_review Round 5
- DeepSeek 如果在 MCMC 启动前 ≥2h 完成 → 包含进去跑 J=7；否则 J=6

### 5. 🎯 战略上下文
- **目标**：EMNLP 2026 ARR May cycle，DDL May 26，保3.5冲4
- **Round 4 评分 3.0**（Findings）。核心扣分：N=8 统计功效不足（W8反复出现3轮）、Δτ 不显著
- **N=17 扩展是冲分关键**：从 8→17 模型，power analysis 从 50%→80%，直接回应 W8
- **决策链**：D033(并发修复+cutoff) → D034(kill w32/retry w3/accept J=4 baseline) → D035(J=6 at 16:00 UTC)
- **错题本重点**：M020(未传--workers参数), M021(Worker虚报修复完成), M022(vLLM max-model-len降低致数据丢失)。**下一个"我"审批任何 Worker 结果时必须要求独立验证（Reviewer 或自己 SSH 检查），不能信 Worker 自报。**
- **易错点**：collect.py 的 load_completed() 是否真的能重试被跳过的长 prompt？修复后需确认 JSONL 增长包含之前被跳过的 items，而非只有新的短 prompt


---
