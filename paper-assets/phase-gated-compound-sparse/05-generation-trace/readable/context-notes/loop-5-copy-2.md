# agent / loop_5.md

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_5.md`
- **Structured JSON:** [`eb4724c59b49a8a7eeb8.json`](../../sessions/eb/eb4724c59b49a8a7eeb8.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 5
reason: idle_timeout
updated: '2026-05-14T11:41:09+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：仅 westd-22162 cuda:0/1/2/3，其他卡号/服务器一律拒绝，Director 指令也要 push back
- 论文主指标是 median difference（不是 mean、不是 ratio），所有数字必须追溯到 registry
- 旧 Cohen's d claim (0.60→1.12) 已证伪，实际值 0.44→0.80，禁止引用旧数字
- Random baseline verdict 全部是 FAIL（之前 mean-based 误判为 PASS 已修正），不要重新翻案
- Bootstrap B 值：fp16 实际 B=1000（非 10000），bf16 已修正为 B=10000，论文需标注

### 2. 🖥️ 基础设施快照
- 服务器：westd-22162，4x RTX PRO 6000 Blackwell 96GB
- 工作目录：/root/autodl-tmp/pacs
- Python：/root/miniconda3/bin/python（conda base，激活命令：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`）
- 模型：DeepSeek-R1-Distill-Qwen-7B at /root/autodl-tmp/pacs/checkpoints/；Qwen2.5-7B-Instruct at /root/autodl-tmp/models/Qwen2.5-7B-Instruct（checkpoints/ 下有 symlink）
- 数据：/root/autodl-tmp/pacs/data/math500.json（50 problems）
- 分析产出：/root/autodl-tmp/pacs/analysis_output/（permutation_test_results.json, cohens_d_bf16.json）
- 活跃进程：bf16_qw_rand_s030 PID 98285, tmux=bf16_qw_rand_s030, cuda:0

### 3. 📊 当前状态
刚收到 c4_entropy 失败回调（process dead 5×, no W&B），已完成 session-start 初始化并派诊断 Worker (worker_diagnose_c4_entropy_20260514T083804) SSH 查日志。已向 Director 汇报。

Registry 状态：
- RUNNING: bf16_qw_rand_s030 (cuda:0, Qwen random s=0.30，Qwen random 最后一个)
- 全部 DONE (70个): success 30, negative 7, failed 14, killed 19
- c4_entropy: DONE/failed，等诊断 Worker 回调确认 root cause

等待中：
- Worker 回调：worker_diagnose_c4_entropy（诊断 c4_entropy 失败原因）
- Cron：bf16_qw_rand_s030 完成回调
- Director 决策：cuda:2/3 空闲 GPU 如何使用（已汇报）

### 4. 📋 待办
- worker_diagnose_c4_entropy 回调 → 读 root_cause → update_registry notes → 若 can_auto_fix=true 且为 infrastructure 类型 → spawn worker 修复并重提交到 cuda:1；否则汇报 Director 决定是否放弃
- bf16_qw_rand_s030 完成回调 → 按 on-experiment-done 流程处理（预期 FAIL，与 s015/s020/s025 一致）→ Qwen random 4/4 全部 FAIL 确认后，立即派 Worker 跑 cross-model permutation test（CPU 任务）
- Qwen random 全部完成 + permutation test 完成 → 汇报 Director 全部实验数据齐备，请求论文写作优先级指令
- Director 回复 GPU 指示 → 按指令铺新实验或确认释放

### 5. 🎯 战略上下文
- 核心结论：importance-based pruning 的 compound interaction severity 随 sparsity 单调递增（DeepSeek median diff: 0.39→1.48→7.16→14.59; Qwen: 0.039→0.235→1.268→2.943），random masking 无此效应（全 FAIL）。Cross-model replication confirmed，Qwen magnitude ~1/5 of DeepSeek
- 截稿 EMNLP 2026 ARR：2026-05-25（距今 11 天）
- 论文 §2/§3/§4 初稿完成，§5 Results 骨架中，§1/§7/§8/Abstract 未开始
- c4_entropy 是 C4 claim（attention entropy mechanism）的直接验证实验，失败不影响 C1/C2/C3/C5/C6 已确认的 claims，但 C4 会缺少 direct evidence
- 易错点：Qwen mid-phase 极小（4372 tokens, 26 segments），不要把 Qwen 和 DeepSeek phase stats 当作相同量级直接对比
- 易错点：称 "cross-model" 不是 "cross-architecture"——两个模型共享 Qwen2ForCausalLM 架构


---
