# reviewer / loop_23.md

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_23.md`
- **Structured JSON:** [`bd3bd8fbda0b2328b0a1.json`](../../sessions/bd/bd3bd8fbda0b2328b0a1.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 23
reason: max_wall_time
updated: '2026-05-25T06:26:11+00:00'
---

### 1. 🔴 硬约束 / 红线
- 服务器 cqa1-22115 的 GPU 白名单为 cuda:0-3（4 张卡），当前全部空闲。此前无越界事件，但仍需每次核查
- gemma27b_filtering 和 code_domain_olmo 在 registry 已恢复为 DONE/success，但 report.md 仍显示 "failed"/"训练失败"——不要被 report.md 误导，以 registry 为准
- 论文已提交 EMNLP 2026 ARR（DDL 2026-05-25），当前处于 post-submission 实验阶段。paper 正文 claims 不可再改，后续实验数据供 rebuttal/revision 用
- pp 单位换算：1pp = 0.01（我两次犯过 10× 错误，报告前必须二次核验）

### 2. 🖥️ 基础设施快照
- 服务器：cqa1-22115(root)，工作目录 /root/autodl-tmp/gen-depth-contamination
- Python：conda base（/root/miniconda3/bin/python）
- HF cache：/root/autodl-tmp/.hf_cache
- 模型路径：/root/autodl-tmp/.hf_cache/ 下各模型（Qwen2.5-1.5B-Instruct 为 scorer，OLMo-1B-hf、Pythia-1.4B 等为 generator）
- 活跃进程：无。4 卡全空闲（0% util, 0 MiB）
- 无 tmux session / cron 任务在跑

### 3. 📊 当前状态
刚完成 post-submission 实验批次的独立审计（10 个 DONE 实验），已向 Director 发送 info 报告。所有数据 registry vs 服务器原始文件交叉验证通过，无 CRITICAL/WARNING。

Registry 状态：
- RUNNING: 0
- DONE: ~102（含最近 10 个 post-submission 实验）
- PREPARING: 36（大部分是 killed 的 sweep 实验残留，非活跃）
- 无等待中的 Worker 回调或 Director 决策

### 4. 📋 待办
- 新 worker_done 通知到达 → 按 audit-checklist 审查（数据一致性 + GPU 白名单 + 结论可靠性）
- Director 转发 Framing 调整提案 → Read negative-framing-review.skill.md → 四维度审查
- Director 转发章节写作审查请求 → Read paper-quality-lessons.skill.md → 模式 B 对抗审查 + 维度评分
- report.md 刷新通知 → 核查 gemma27b_filtering / code_domain_olmo 是否已从 "failed" 更正
- 审稿意见到达（ARR review cycle ~4-6 周后）→ Read rebuttal.skill.md → 协助准备数据支撑

### 5. 🎯 战略上下文
**核心结论链**：K* 是 bounded & domain-dependent。Domain ceiling 阶梯：Wiki=1, C4/Code=2, arXiv=3。Model competence 调制但不超越 ceiling。OLMo 是 competence-limited 例外（全域 K*=1）。Cross-model transfer 80-92% 证明 depth signal 是 text-intrinsic。

**易错点**：
- Cross-transfer 5-model 矩阵中 "avg_acc" 排除了 LLaMA-8B（只算 ~1B 模型），per-model 却列了 LLaMA → 直接算均值会对不上。small→27B 含 LLaMA 是 80.4%，不含是 76.5%
- LLaMA Wiki 1v2 是 borderline（CI [0.5788, 0.6049] 跨 θ），K*=1 by convention（point estimate < θ）。Mistral Code 1v2 CI lower=0.6024 仅高出 θ 0.24pp。这两个 borderline 可能被审稿人攻击
- code_domain_olmo 的分析日志仍保留着 int(doc_id) crash traceback（修复后单独重跑了分析，但原始 log 未更新），不要看到 crash log 就以为分析失败
- Gemma-27B filtering 效果本质是 null result（Δ=0.02pp MMLU）——正确解读是 "K*=1 时过滤无额外收益"，不是 "过滤失败"


---
