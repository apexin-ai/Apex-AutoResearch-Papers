# reviewer / loop_10.md

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_10.md`
- **Structured JSON:** [`b2fe3d105200b3c39ad6.json`](../../sessions/b2/b2fe3d105200b3c39ad6.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 10
reason: max_wall_time
updated: '2026-05-16T03:12:42+00:00'
---

### 1. 🔴 硬约束 / 红线
- **Eval 标准协议**：batch_size=4, max_new_tokens=1024, --no-quantize, --sft_adapter, 正确 seed。任何偏离此协议的 eval 结果不可用于 paired t-test
- **CUDA_VISIBLE_DEVICES 必设**（C002/C003）：每次 submit_training_job 命令前必须显式设置，禁止依赖 device_map="auto"
- **GPU 占用检查**（C001）：提交 eval 前 nvidia-smi 确认目标 GPU 显存 < 2GB
- **Kill 必验证**（C004）：registry 标 killed 时必须 kill -9 + ps 确认进程终止
- **CED s42 checkpoint 路径是 `/root/autodl-tmp/rsft_output/checkpoint-510`**，不是 rsft_output_r2b（r2b 是 alpha=32 的消融实验，不是 CED s42）

### 2. 🖥️ 基础设施快照
- 服务器：rtx5090-4x (root)，工作目录 `/root/autodl-tmp/freige`
- Python：`/root/miniconda3/bin/python`（conda base）
- 模型底座：`/root/autodl-tmp/models/Qwen3-4B`
- SFT adapter：`/root/autodl-tmp/sft_output`
- 数据：`/root/autodl-tmp/data/docred`（dev=985 docs）
- HF cache：`/root/autodl-tmp/.hf_cache`
- Checkpoint 路径（CED RSFT）：s42=`rsft_output/checkpoint-510`, s43=`rsft_output_ced_s43/checkpoint-510`, s44=`rsft_output_s44/checkpoint-510`（注意无 _ced 前缀）, s45=`rsft_output_ced_s45/checkpoint-510`
- Checkpoint 路径（flat-NLI RSFT）：s42=`rsft_output_flat_nli/checkpoint-507`, s43=对应目录/checkpoint-507, s44=`rsft_output_flat_nli_s44/checkpoint-507`, s45=`rsft_output_flat_nli_s45/checkpoint-507`
- 活跃进程（截至 handoff）：eval_rsft_ced_s43 (PID 286587, cuda:1), eval_rsft_ced_s45 (PID 283838, cuda:2), eval_plan_014_no_evidence_r2 (PID 288109, cuda:0)

### 3. 📊 当前状态
**刚完成的审查**：
- eval_flat_nli_s44 (DONE, rel_f1=0.4615) — PASS
- eval_flat_nli_seed45 (DONE, rel_f1=0.4551) — PASS
- 发现并上报 critical：**6 个 seed-level eval 中仅 2 个协议有效**（flat-NLI s44/s45）。CED s42/s44 + flat-NLI s42/s43 全部有 batch_size 或 seed 偏差
- 发现并上报 critical：paired_ttest_analysis.py 将错误的 rsft_r2b（alpha=32 消融）映射为 CED s42，脚本不可运行
- checkpoint 验证 Worker 已确认 reeval_ced_s42/s44/flat_nli_s42 的路径

**RUNNING**：
- eval_rsft_ced_s43 — CED s43 标准协议 eval (cuda:1)
- eval_rsft_ced_s45 — CED s45 标准协议 eval (cuda:2)
- eval_plan_014_no_evidence_r2 — SFT no-evidence 重试 (cuda:0)

**待 Director 决策**：提交 reeval_ced_s42 + reeval_ced_s44 + reeval_flat_nli_s42（+ 可选 reeval_flat_nli_s43），等 GPU 释放

### 4. 📋 待办
- eval_rsft_ced_s43 完成 → 审查协议合规 + metrics，确认 CED s43 有效数据点
- eval_rsft_ced_s45 完成 → 同上，确认 CED s45 有效数据点
- eval_plan_014_no_evidence_r2 完成 → 审查 SFT no-evidence 结果（Claim 1 evidence tax 数据）
- reeval_ced_s42/s44/flat_nli_s42 提交后 → 逐个审查协议，确认 CUDA_VISIBLE_DEVICES 已设
- 所有 re-eval 完成后 → 审查 paired_ttest_analysis.py 的目录映射是否已更新为正确路径，然后审查 t-test 结果
- Director 转发 paper 章节 → 按模式 B 审查（评分模板 + checklist）

### 5. 🎯 战略上下文
- **核心瓶颈是 Claim 3 (CED vs flat-NLI paired t-test)**：需要 ≥3 matched pairs 标准协议 eval。目前有效配对数 = 0（CED 侧 0 个有效）。s43/s45 跑完后 CED 有 2 个，还需 reeval s42 和 s44
- **最容易判断错的事**：不要信 metrics_summary_table.md 和 paper_metrics_table.md 中的 CED mean (0.4596±0.0128) 和 flat-NLI mean (0.4531±0.0011)——这些基于协议不一致的旧数据，不可引用。必须等全部 re-eval 完成后重算
- **CED s42 checkpoint 陷阱**：命名混乱——`rsft_output/` 才是 CED s42（seed 42 默认），`rsft_output_r2b/` 是 alpha=32 消融。Worker 已混淆过一次，t-test 脚本也用错了
- **flat-NLI checkpoint 是 507 步**（不是 510），因训练数据量不同
- **literature_map 29 类 (RL vs Forgetting)** 与 Claim 2 "通用梯度压力" framing 有叙事张力，论文需显式讨论
- 项目目标：EMNLP 2026 Main (ARR July)，paper_framing.md 有 4 个 Core Claims


---
