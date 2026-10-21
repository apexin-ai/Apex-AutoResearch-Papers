# agent / loop_18.md

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_18.md`
- **Structured JSON:** [`b074f59f77a9c194caa6.json`](../../sessions/b0/b074f59f77a9c194caa6.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 18
reason: idle_timeout
updated: '2026-05-21T03:30:28+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：rtx5090-4x 的 cuda:0, cuda:1, cuda:2, cuda:3（4张）。bjb2-12179 已不可用（数据迁移中）
- 正在从 bjb2-12179 迁移到 westd-37389（rtx5090-4x），迁移未完成前部分模型/数据可能缺失，提交实验前必须确认文件到位
- LLaMA SFT s42 的 ign_f1=0.5384（不是 0.5514，D130 审计修正），引用时用修正值
- LLaMA RSFT s42 的 ign_f1=0.5714（不是 0.5839，D129 修正），3-seed mean=0.5654±0.0052
- 14B RSFT generate 只完成 62%（doc 1872/3027），resume 需要 M019 脚本修改

### 2. 🖥️ 基础设施快照
- 服务器：rtx5090-4x（即 westd-37389），4× RTX PRO 6000 96GB VRAM，350GB disk
- 工作目录：~/faith-evidence-ie/（迁移目标，数据从 bjb2 rsync 中）
- Python/conda：未确认（迁移中，需 SSH 探测）——bjb2 用 aml-train 镜像 conda base
- 模型路径：迁移中，原 bjb2 路径 ~/autodl-tmp/ 下的 adapters + 基座模型（~207G）
- 活跃进程：
  - migration_bjb2_to_westd（RUNNING，pid 未知，rsync 数据迁移）
  - llama_sft_s43_train_eval_r3（RUNNING，rtx5090-4x cuda:1，pid=15650）
- 活跃 cron：上述 2 个实验各有 cron 监控

### 3. 📊 当前状态
刚收到 `eval_llama_sft_s42_no_evidence_std` 失败回调（EXIT_CODE=1）。已派诊断 Worker（worker_diagnose_eval_llama_sft_s42_no_evidence_std_20260520T112815）去 rtx5090-4x 读日志，**尚未收到回调**。

另有一个更早的诊断 Worker 也在运行：worker_diagnose_eval-no-evi-failure_20260520T112726（可能是上一轮 session 派的，功能重叠）。

Registry 状态：
- RUNNING：migration_bjb2_to_westd（数据迁移）、llama_sft_s43_train_eval_r3（LLaMA SFT s43 重训，r3 因 r1/r2 AutoDL 数据丢失）
- 刚 FAILED：eval_llama_sft_s42_no_evidence_std（标准化 evidence tax 测量）
- 近期 FAILED：llama_sft_s44_train_eval_r2、llama_sft_s43_train_eval_r2（AutoDL 重启丢数据）

尚未向 Director 汇报本次失败（等诊断 Worker 回调后一并汇报）。

### 4. 📋 待办
- 诊断 Worker 回调 → 读诊断结果 → update_registry 写 failure_reason → 判断能否直接重跑（若文件缺失等迁移完成 → 重提交；若代码 bug → 派 Worker 修复后重提交）
- migration_bjb2_to_westd 完成回调 → 确认所有文件到位 → 4 GPU 并行恢复实验（ROADMAP 迁移后计划）：
  - cuda:0 → 14B RSFT gen resume
  - cuda:1 → llama_sft_s43（已在跑 r3）
  - cuda:2 → llama_sft_s44 retrain
  - cuda:3 → eval_llama_sft_s42_no_evidence_std 重跑
- llama_sft_s43_train_eval_r3 完成回调 → 分析 metrics → 与 s42 (0.5384) 对比 → 若 s44 也完成则计算 3-seed SFT variance → 与 RSFT variance (std=0.0052) 对比验证 variance compression
- 所有 LLaMA SFT 3-seed + no-evidence eval 完成 → 填 ROADMAP 表格 LLaMA 行 → 论文 cross-family claim 数据就绪

### 5. 🎯 战略上下文
- 项目核心：FREIGE 论文，3 个 contribution：(1) RSFT+NLI 有效性 (2) Decoupling spectrum (3) Scale-dependent evidence tax + variance compression
- 投稿目标：EMNLP 2026 Main（ARR July，~56 天）
- D131：采纳 Reviewer 统一叙事主线——3 contributions 从独立小文章整合为连贯 story
- 当前关键缺口：LLaMA SFT 3-seed variance（只有 s42 一个 seed，s43 r3 在跑，s44 待重训）；14B RSFT 数据生成 62%；标准化 evidence tax 测量（eval_llama_sft_s42_no_evidence_std 刚失败）
- 易错点：(1) bjb2 和 rtx5090-4x 的文件路径不同，迁移后路径可能变化 (2) 之前 AutoDL 重启导致 s43/s44 r2 数据全丢，现在用 westd 新服务器应该稳定 (3) no-evidence eval 之前有两套结果——独立训练的 no-evidence 模型 vs 同一 SFT adapter 加 --no_evidence flag，方法论上只有后者（std 版）才是正确的 evidence tax 测量 (4) report.md 告警区大量 mvp2_ 前缀实验都是历史遗留，已 killed/failed，不需要处理


---
