# agent / loop_4.md

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_4.md`
- **Structured JSON:** [`1addbee7d6d347e04d42.json`](../../sessions/1a/1addbee7d6d347e04d42.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 4
reason: idle_timeout
updated: '2026-05-14T21:49:52+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 只能用 bjb2-23165 的 cuda:0 和 cuda:1（RTX 5090 32G×2）
- Gold set 标注是 GO/NO-GO gate——**最晚 5/16 必须启动**，否则赶不上 5/25 DDL
- D039 pivot 已定：TLM 判死，论文 framing 是 empirical analysis paper，不要再跑 TLM 相关实验
- 论文定位 EMNLP 2026 ARR 5/25 Findings，不是 main conference
- gold_dryrun_v3 的 dry-run 已成功（pipeline 验证通过），等用户确认标注人力后直接跑正式版，不需要再验证 pipeline

### 2. 🖥️ 基础设施快照
- 服务器：bjb2-23165，工作目录 `/root/autodl-tmp/agent_progress_probe/`
- Python：`/root/miniconda3/bin/python`（conda base 环境，不是 venv）
- 激活命令：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- 数据：`/root/autodl-tmp/agent_progress_probe/data/windows_labeled.jsonl`（15401 windows）
- Gold set 评估脚本：`/root/autodl-tmp/agent_progress_probe/evaluate_gold_set.py`（已就绪）
- 模型 checkpoint：`checkpoints_full/best_model.pt`（probe_001）
- 活跃进程：无（GPU 空闲，等 gold set 标注）
- Cron：reconcile 返回 0 active

### 3. 📊 当前状态
实验主体全部完成：40 DONE（24 success / 6 negative / 1 failed / 9 killed），0 RUNNING。10 个 PREPARING 是历史遗留（killed/superseded），不需要处理。

**刚完成的关键里程碑**：
- paired-bootstrap 显著性检验完成（3 个 in-domain 比较 p<0.001）
- F1_stag per-class breakdown 分析完成（详见 memory.md）
- experiment_plan.yaml 32 实验已写入（D041）
- paper_framing.md 已更新至 D039 pivot 版本
- dream_simulate(review_mode="full") 已触发（dream_20260514T214352），等待完成

**等待中**：
- 用户确认 gold set 标注人力（650 windows）
- dream review 完成回调
- Paper Agent Full Draft 队列中（不依赖 gold set 的章节可先写）

### 4. 📋 待办（条件触发式）
- 用户确认标注人力 → 启动 650 窗口标注流程 → 标注完成后一条命令跑 `evaluate_gold_set.py`（pipeline 已验证）
- dream review 回调到达 → 读取审查意见 → 修改论文对应章节 → 汇报 Director
- 5/16 仍无标注确认 → 向 Director 升级：gold set 是 critical path，再拖就赶不上 DDL
- Paper Agent draft 完成 → review + 迭代（不等 gold set 的章节：intro, method, LF temporal, TLM negative, related work）
- Gold set 验证结果出来 → 补入 paper Results + Discussion → 最终 polish

### 5. 🎯 战略上下文
**核心结论链**：
- D039: TLM（TWV/HMM/lag-HMM）全面失败，从 core claim 降级为 negative finding
- D036/D035: Structural features 跨域碾压 probe（GB 0.967 vs probe 需 few-shot 适配）
- 论文三层贡献：(1) Structural signal discovery（主）；(2) LF temporal dynamics + cross-agent；(3) TLM negative

**关键指标**：
- Struct GB in-domain: 0.9951 macro_f1
- Struct GB cross-agent: 0.967
- vs LLM judge: +33.3pp
- Probe conf≥2: f1_stag=0.8522

**易踩的坑**：
- 10 个 PREPARING 实验是历史残留（killed/superseded），不要试图恢复或提交它们
- Gold set 是唯一非 circular 评估——所有现有实验都用 LF 弱标签训练+评估，存在 circular evaluation 风险
- 跨域 baseline 数值引用规则见 D042：统一用 cross-agent-structural 实验结果
- 距 DDL 仅 11 天，GPU 当前空闲是正常的（等标注），但标注一完成必须立即跑验证


---
