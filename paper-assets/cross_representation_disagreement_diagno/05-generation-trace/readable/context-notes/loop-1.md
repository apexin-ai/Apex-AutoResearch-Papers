# director / loop_1.md

**Cross-Representation Disagreement as a Diagnostic Signal for LLM Reasoning Errors** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_1.md`
- **Structured JSON:** [`09d48164e6a4e1ab9d3c.json`](../../sessions/09/09d48164e6a4e1ab9d3c.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 1
reason: max_wall_time
updated: '2026-05-14T12:44:11+00:00'
---

### 1. 🔴 硬约束 / 红线
- 模型锁定 Qwen3-32B-AWQ（Apache 2.0 开源），模型选择是核心方法论决策，换模型必须 Director 审批（D004 教训）
- GPU 只有 1 张实际可用：gpu-6000pro-4 的 GPU 跑 vLLM 推理服务，autodl-rtx6000pro 实际是同一台机器或无独立 GPU。不要尝试在 vLLM 占用的 GPU 上跑其他实验
- 不要同时启动两个 pipeline 进程写同一输出文件（本轮发生过数据损坏事故，两个 PID 同时写 mvp_v4_full.json）
- Pipeline 启动用 nohup 即可，不要用 tmux + nohup 双重启动（导致过重复进程）

### 2. 🖥️ 基础设施快照
- 服务器：gpu-6000pro-4 (connect.westd.seetacloud.com)，账户 root
- 工作目录：/root/autodl-tmp/crdd
- vLLM：PID 19902，Qwen3-32B-AWQ，awq_marlin 量化，端口 8000，max-model-len 16384，65 tok/s
- GPU：NVIDIA RTX PRO 6000 Blackwell Server Edition 98GB，vLLM 占用 88.5GB/97.9GB
- 数据集：/root/autodl-tmp/crdd/data/folio-validation.jsonl（204 条 FOLIO validation）
- 模型路径：/root/autodl-tmp/models/Qwen3-32B-AWQ
- 活跃进程：mvp_pipeline_003b (PID 29177, nohup, 全量 204 条 pipeline v4)
- Cron 监控：300s 间隔监控 pipeline 进程
- 无 W&B，无 Git remote

### 3. 📊 当前状态
全量 204 条 MVP pipeline v4 正在运行（PID 29177，--resume 断点续跑）。v4 修复了 FOL 截断问题（thinking tokens 耗尽 max_tokens → 检测 finish_reason=='length' → 关闭 thinking 重试），日志确认修复生效。预计总耗时 8-12 小时（从 ~19:00 启动）。

Registry：
- mvp_baseline_001: DONE (success) — baseline accuracy 74%, PASS_FOLIO
- mvp_pipeline_001: DONE (negative) — v1, FOL crash 78%
- mvp_pipeline_002: DONE (negative) — v3, Code crash 0% 但 FOL 截断 80%
- mvp_pipeline_003b: RUNNING — v4 全量 204 条

等待中：pipeline 完成后 cron 自动回调 Agent → Agent 跑 analyze.py → 汇报 C1-C5

### 4. 📋 待办
- Pipeline 完成回调到达 → 让 Agent 跑 `python src/analyze.py results/mvp_v4_full.json`，汇报 C1-C5 全部指标
- C1-C5 ≥ 3/5 pass 且核心指标（C1 disagree≥10%, C4 repair≥blind+5pp）pass → complete_mvp() 进入 research 阶段 → post-mvp-kickoff skill
- C1-C5 不足 → 分析具体失败项。区分"工程问题可修"vs"假设不成立"：若 FOL crash 仍高说明截断修复不够（加大 max_tokens 到 8192）；若双端都执行但 disagree=0% 说明假设可能有问题
- 假设彻底失败 → 考虑 Agent 提的路径 B（Code-Code 双策略）快速验证，或 kill 项目
- MVP 硬截止 Day 4 = 2026-05-18

### 5. 🎯 战略上下文
- 核心假设：FOL 和 Python 两种表征独立犯错，分歧信号可用于错误定位和定向修复。假设本身从未在全量数据上被验证过——之前所有 negative 都是工程实现问题（Z3 prompt 质量、thinking token 泄漏、token 预算截断）
- 决策链：D001(MVP 设计) → D002(FOLIO 数据集) → D003(5 条 C1-C5 标准) → D004(禁止擅自换模型) → D005(本地 GPU 部署) → D006(v4 截断修复而非 pivot)
- 最容易判断错的事：Agent 倾向于在小样本 negative 后立即提 pivot（v3 10 条就建议 kill/换方向）。n=10 的结果方差极大（FOL crash 在 10%-80% 间波动），不要在小样本上做方向决策。v4 全量 204 条才是第一次真正的假设检验
- 易踩的坑：Agent 经常"完成修改"但实际没同步到服务器（本轮发生过 2 次），务必要求 cat 验证。启动 pipeline 时只用一种方式（nohup），不要 tmux + submit_on_allocated 同时来
- EMNLP 2026 ARR DDL = 2026-05-25，剩 11 天。MVP 过了还需要 paper_framing → experiment_plan → dream_simulate → 全套研究实验 → 写论文，时间极紧


---
