# reviewer / loop_4.md

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_4.md`
- **Structured JSON:** [`5db24d2db83083cdad43.json`](../../sessions/5d/5db24d2db83083cdad43.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 4
reason: max_wall_time
updated: '2026-05-13T19:27:00+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：cuda:0 (m2_full_qwen), cuda:1 (m2_full_starcoder)。项目独占 bjb1-42106 双卡，但仍需核对进程不越界
- Full M2 go/no-go 阈值已锁定（D019/D020），结果出来前不得修改。任何 Agent 提议修改阈值 → severity: critical
- 不做预判性 framing pivot（D018）。paper_framing.md 在 Full M2 结果出来前不改
- StarCoder registry notes 仍显示旧超参（batch_size=4, epochs=2）——实际训练用 batch_size=8, epochs=3。如果 Agent 引用 registry 旧参数做分析，要拦

### 2. 🖥️ 基础设施快照
- 服务器：bjb1-42106 (root)，2× NVIDIA RTX PRO 6000 96GB
- 代码目录：/root/structfuse（注意：/root/structfuse-context 不存在，重命名推迟到训练完成后）
- Python：/root/miniconda3/bin/python（conda base env）
- 数据：/root/autodl-tmp/structfuse/full_m2_training_data/（Qwen），/root/autodl-tmp/structfuse/full_m2_starcoder_data/（StarCoder）
- Checkpoints：/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/ 和 m2_full_starcoder/
- Logs：/root/runs/m2_full_qwen/random_s42.log，/root/runs/m2_full_starcoder/random_s42.log（per-run logs）；主 wrapper log 在 /root/runs/structfuse-context/m2_full_{qwen,starcoder}.log
- WANDB_MODE=offline，日志在 /root/autodl-tmp/structfuse/wandb_logs/
- 活跃进程：GPU 0 PID 73558 (Qwen random_s42 ~step 300/4242)，GPU 1 PID 76627 (StarCoder random_s42 ~step 50/4242)
- SWE-bench eval pipeline 已就绪：/root/structfuse/evaluation/eval_swebench.py（dry-run 通过）

### 3. 📊 当前状态
刚完成一轮密集审查（7 个 worker + 1 个 ROADMAP 更新），全部已 post 给 Director。

**RUNNING 实验：**
- m2_full_qwen：cuda:0，9 runs sequential（random/embedding/dataflow × seeds 42/43/44），目前跑 random_s42 epoch 1，首次 eval@500 预计 ~30-60 min
- m2_full_starcoder：cuda:1，Phase 2 刚启动，random_s42 step 50，loss=0.8462

**关键审查结论已发送：**
- D019/D020 阈值审查通过（Claim 1 三级 + Claim 2 三态 + n=3 功效限制声明）
- 64% M1 error 根因修正：非 SWE-smith 数据质量问题，是瞬态 FS 故障（可恢复 28,276 instances，但不中断当前训练）
- Negative difficulty 分析：Qwen embedding space 高度压缩（median cos sim 0.967），StarCoder 自然分辨力更好（median 0.615）。**但缺 query-positive similarity 做 margin 分析**，已建议补跑
- Framing analysis worker 产出了 Conditional Go 叙事方案，与我的独立评估方向一致（Findings 目标）
- SWE-bench eval pipeline 审查通过，缺 bootstrap CI（plan_016 范围）

### 4. 📋 待办（条件触发式）
- Qwen random_s42 eval@500 出现 → 核对 loss/recall 与 pilot 一致性（pilot best R@1=0.5357 at step 500），检查有无过拟合信号
- m2_full_qwen 任一 run 完成 → 检查 checkpoint 目录有 best_by_val_loss + best_by_recall_at_1 双 checkpoint
- m2_full_qwen 全部 9 runs 完成 → 独立核算 D019 go/no-go（bootstrap CI + paired t-test），不等 Agent 的结论
- m2_full_starcoder 全部完成 → 同上 + 交叉编码器一致性判定
- Agent 提议修改 paper_framing.md 或 D019/D020 阈值 → severity: critical 拦截
- Agent 补跑 negative difficulty + query-positive margin → 审查 margin 是否支持 "StarCoder 已经懂了" 的解释
- Agent 提议在 Full M2 完成前启动 M1 re-extraction → 评估是否干扰训练 I/O

### 5. 🎯 战略上下文
**决策链**：D001→D008 (MVP pass) → D009 (Dream WA/WR/R) → D011 (Z%=74% Best Framing) → D015 (Z%=78% 全量确认) → D016-D017 (pilot 验证：embedding>random 跨编码器一致，dataflow mixed) → D018 (不预判 pivot) → D019/D020 (量化阈值锁定)

**最容易判断错的事：**
1. **plan_013_starcoder conclusion=negative ≠ failed**。Coverage matrix 计为 failed，实际是 "hypothesis not supported"（回答了科学问题）。Claim 1 有效覆盖率应为 3/13=23.1% 而非 2/13=15.4%
2. **Claim 2 原始 MVP 证据 (-27pp) 已失效**。那是 BM25 proxy 在 pool=26 的数据，不是 true embedding mining。Full M2 的 embedding vs random 对比才是真数据。如果 Agent 仍引用 -27pp 做决策 → 拦截
3. **n=3 paired t-test 功效极低**（df=2, t_crit=4.303）。如果 Full M2 delta 类似 pilot（<2pp），几乎不可能 p<0.05。落入 (C) No-Go 不等于 "dataflow 无效"，必须讨论 Type II error
4. **Qwen 主 wrapper log 只有 3 行**——训练输出在 per-run log（/root/runs/m2_full_qwen/random_s42.log），不要以为训练没跑
5. **64% M1 error 是 FS 瞬态故障**，不是 SWE-smith 数据问题。前次 error_pattern_analysis 的 "buggy_file_not_found = 上游问题" 结论已被 fuzzy_match_verify 推翻


---
