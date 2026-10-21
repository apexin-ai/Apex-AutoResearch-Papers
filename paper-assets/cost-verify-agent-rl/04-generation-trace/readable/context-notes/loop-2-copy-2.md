# agent / loop_2.md

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_2.md`
- **Structured JSON:** [`7f0487aa812c31d70b9a.json`](../../sessions/7f/7f0487aa812c31d70b9a.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 2
reason: idle_timeout
updated: '2026-05-14T05:54:57+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：仅 bjb1-17606:cuda:0 和 cuda:1（2× RTX PRO 6000 Blackwell 94GB）
- 服务器用 conda 环境（`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`），不要创建 .venv
- submit 命令必须自带环境激活，GPU 编号始终从 0 开始
- exp007 checkpoint 路径：/root/autodl-tmp/checkpoints/exp_007/，不要覆盖

### 2. 🖥️ 基础设施快照
- 服务器：bjb1-17606，账号 root
- 工作目录：/root/cost-verify-agent-rl/RAGEN
- Python：/root/miniconda3/bin/python（conda base）
- 数据：/root/autodl-tmp/alfworld/（3553 train split）
- 模型：Qwen3-1.7B（HF 下载，具体路径需 SSH 确认）
- Checkpoint：/root/autodl-tmp/checkpoints/exp_007/
- 日志：/root/autodl-tmp/exp007_formal.log
- 环境变量：ALFWORLD_DATA=/root/autodl-tmp/alfworld
- W&B：回调说 "W&B data available"，run_id 未记录在 registry，Worker 应从日志中提取
- 活跃进程：无（exp007 已退出）
- Cron：reconcile 显示 0 个活跃

### 3. 📊 当前状态
- **刚做完**：收到 exp007 ANALYZING 回调，完成 session 初始化，已 spawn Worker（worker_analysis_exp007_20260514T025245）分析结果
- **等待中**：Worker 回调——它会 SSH 读日志 + 拉 W&B 指标 + 判断 conclusion + 更新 registry + 写分析报告
- **Registry**：exp007 = ANALYZING；其余全是 DONE(failed) 或 PREPARING（历史残留 dryrun）
- **GPU**：2 张分配，0 张在跑（exp007 刚结束）

### 4. 📋 待办（条件触发式）
- Worker 回调 conclusion=success → 更新 report.md + 向 Director 汇报 + 立即准备 Phase B（B-IAVR selective verification）
- Worker 回调 conclusion=negative → 产出 Framing 调整提案（red-section）+ 汇报 Director + 评估 SFT warmup 备选方案（artifacts/sft_warmup_plan.md 已就绪）
- Worker 回调 conclusion=failed → 读 on-experiment-failed skill + 诊断 + 汇报
- 无论结论如何 → GPU 空闲，需立即规划下一步实验占满 2 张卡

### 5. 🎯 战略上下文
- **决策链**：D001(ALFWorld+Qwen3-1.7B) → D002(全量微调) → D003(kill exp003 bootstrap失败) → D004(修解析器+prompt增强)
- **核心假设链**：exp003 证明 Qwen3 不输出 `&lt;answer>` → exp007 用 fallback regex 解决解析 → 但 action_is_valid 仅 5.4%（模型输出可解析但不是有效 ALFWorld 命令）→ 30 步 GRPO 能否从稀疏 reward 学到正确命令是 Phase A 成败关键
- **Phase A 标准**：success_rate ≥ 76% = PASS；step 10 后 action_is_valid < 10% = FAIL
- **易错点**：
  - invalid_action（解析失败）vs action_is_valid（命令有效）是两个不同指标，别混淆
  - dryrun 时 action_is_valid 仅 5.4%，如果 30 步训练后仍 <10%，按标准应判 negative，不是 failed
  - Phase B 代码已就绪（61 tests passed），但被 Phase A checkpoint 阻塞
  - SFT warmup 是备选路线（先用专家数据 SFT 再 GRPO），artifacts/sft_warmup_plan.md 有方案
- **历史坑**：exp_001/001b/002/003 全部 failed，原因都是 Qwen3 格式不兼容 RAGEN 解析器，exp007 是第一个解决了解析问题的正式训练


---
