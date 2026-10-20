# director / loop_5.md

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_5.md`
- **Structured JSON:** [`c3b6f8287b7a3699ad0a.json`](../../sessions/c3/c3b6f8287b7a3699ad0a.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 5
reason: max_messages
updated: '2026-05-14T16:06:37+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目 GPU 白名单：cuda:0-5（6 张 4090D），严禁使用白名单外 GPU
- C003 约束（刚加的）：标记实验 failed 时必须同时 kill 所有关联 GPU 进程；submit 新任务到 GPU 前必须先 nvidia-smi + ps 确认该 GPU 无残留进程（已两次违规）
- HumanEval 不在 contamination 注入数据中（只有 ARC/GSM8K/MMLU），不参与 dose-response 分析，作为 negative control 处理
- 3B GSM8K 已被 D018 排除出 dose-response（LoRA SFT 导致 CoT 灾难性遗忘，baseline 崩塌使曲线无意义）

### 2. 🖥️ 基础设施快照
- 服务器信息需通过 `get_resource_inventory` / `get_project_status` 获取，本轮我作为 Director 未直接 SSH
- 模型：Qwen2.5-0.5B / 1.5B / 3B，eval 路径 `/root/autodl-tmp/exp001/eval_results/`
- 注入数据覆盖 3 benchmarks：ARC (1172), GSM8K (1319), MMLU (14042)
- exp-008 Signal Survival 代码已完成 dry-run，产出在 artifacts 目录

### 3. 📊 当前状态
**刚处理完**：GPU 2 三进程冲突（CRITICAL）— v3 残留进程已 kill，v4 独占运行，C003 约束已添加。

**RUNNING 实验**（Agent reset 前状态）：
- exp_001_eval_05B_d100_aligned_v4（GPU 2）：GSM8K 进行中，预计 ~2.5-3h 完成全部 4 benchmarks
- exp_001_eval_05B_d005_para（GPU 5）：d005 paraphrase eval，MMLU 已完成，GSM8K 进行中
- 其他 4 GPU 也在跑（Agent 报告 6/6 GPU 全占）

**已派未收回的指令**：
- 告诉 Agent 立即跑 exp-008 `--exp002-only --skip-compute`（CPU 路径，用现有 exp-002 数据）
- P0 GSM8K 诊断 + P2 HumanEval 异常分析的 Worker 报告可能已完成但 Agent reset 前未汇报

**Reviewer 待处理**：
- v4 registry 状态仍为 PREPARING 需改 RUNNING（Reviewer warning）
- 3B d100 GSM8K 69.7% > raw 60.5% 的记忆化膨胀对比（raw→d000 SFT 11.7%→d100 contaminated 69.7%）建议作为论文 case study

### 4. 📋 待办
- Agent reset 完成 → 确认 6 GPU 实验状态，确保无中断；催促修复 v4 registry 状态
- exp_001_eval_05B_d100_aligned_v4 完成 → 收集 0.5B d100 全部 benchmark 结果，更新 dose-response 分析
- exp_001_eval_05B_d005_para 完成 → 收集 paraphrase eval 结果，对比 original vs paraphrased 分数
- exp-008 CPU 分析完成 → 审查 signal survival 真实数据结果，决定是否需要 GPU 路径跑完整管道
- 所有 0.5B eval 完成 → 启动 dose-response 曲线绘制（0.5B/1.5B/3B 三模型 × 多 dosage）

### 5. 🎯 战略上下文
- 项目核心：IRT-based calibration 检测 LLM benchmark contamination。通过不同 dosage level 的 contamination 注入，观察 IRT 参数变化来检测污染
- 关键发现待利用：3B GSM8K 对比（raw 60.5% → d000 SFT 11.7% → d100 contaminated 69.7%）是"污染掩盖真实能力退化"的绝佳 case study，Reviewer 建议突出呈现
- HumanEval 作为 negative control 是论文 story 加分项——证明方法能区分 genuine capability gain vs contamination-driven inflation
- DDL 紧张（May 25），3B LoRA 配置根因修复（~20h GPU）被搁置，论文需在 Discussion/Limitations 中说明
- 易错点：GPU 2 进程管理已出问题 4 次，新 Agent 必须严格遵守 C003 约束


---
