# reviewer / loop_3.md

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_3.md`
- **Structured JSON:** [`bc5cd708fe0d6a235054.json`](../../sessions/bc/bc5cd708fe0d6a235054.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 3
reason: max_wall_time
updated: '2026-05-14T21:48:33+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单: cuda:0, cuda:1（RTX 5090 32G × 2）。其他设备号越界立即 CRITICAL
- experiments.tex 有 **3 个 critical 数据错误尚未修复**，不可在未修复状态下提交或进入 Paper Agent review 循环：
  - L41/L107(method.tex): dropout=0.3 → 实际代码 default=0.1
  - L78: "24.3pp" → 应为 33.3pp（RF vs LLM，24.3pp 是 probe vs LLM）
  - L96: "5 seeds" → 实际 3 seeds (42, 123, 456)
- method.tex L33 LF 形式化定义 λ_j : w_i → {0,1} **遗漏 abstain (-1)**，导致 conf=1 在数学上不可能存在。代码 `labeling_functions.py` 有 `ABSTAIN = -1` 且 6 处返回。审稿人一定会抓

### 2. 🖥️ 基础设施快照
- 服务器: bjb2-23165, 工作目录 /root/autodl-tmp/agent_progress_probe
- Python: 未深查（read-only 角色），训练脚本用 `python3`/`python`
- 本地 workspace: /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/
- artifacts 路径: 同上 + artifacts/_project/paper/ (experiments.tex, method.tex 实际写在这里)
- docs 路径: 同上 + docs/paper/sections/ (experiments.tex 和 method.tex 也有副本)
- 活跃进程: 无 RUNNING 实验，GPU 空闲
- W&B: 未配置（本项目不检查 W&B）

### 3. 📊 当前状态
**刚完成的审查**:
1. experiments.tex — 3 critical + 4 warning 已提交 Director，未修复
2. method.tex — 2 critical (dropout + abstain 形式化) + 2 warning 已提交
3. paired-bootstrap — PASS，3 个 in-domain 对比 p<0.001；跨域比较因 eval set 不匹配跳过
4. ROADMAP.md — 4 个问题已报告，Director 已修复（24.3→33.3pp、计数、f1-stag 状态、bootstrap 标记）
5. 24.3pp 系统性错误扩散 — ROADMAP 已修复，experiments.tex 和 literature_map.yaml 头部注释待修

**Registry 状态**: 30 DONE, 0 RUNNING, gold_dryrun_v1/v2 PREPARING(killed), gold_dryrun_v3 PREPARING(success 未更新 status), 1 planned (gold-set)

**等待中**: dream_simulate 已触发 (dream_20260514T214352)；Paper Agent Full Draft 在队列中

### 4. 📋 待办（条件触发式）
- dream_simulate 完成 → 审查模拟审稿结果，重点看审稿人是否命中已知 critical（dropout/abstain/24.3pp）
- Paper Agent 提交章节 → 按 §5 对抗审查模式 B 审查，带维度评分
- experiments.tex critical 修复后重新提交 → 重新验证 3 处数据点
- gold set 标注启动 → 审查标注指南合理性、样本选择偏差
- gold set 验证实验完成 → 核实 GPU 设备号合规、结果与 dry-run 一致性、leakage fix 是否生效
- 跨域 paired-bootstrap 补跑 → 审查 GB 在 OH test split 上的 inference 是否正确配对

### 5. 🎯 战略上下文
- **D039 pivot**: TLM 全面失败，论文从 method paper 转为 empirical analysis paper。核心 story = structural signal discovery (C1) + LF temporal dynamics (C2) + TLM negative (C3)
- **Gold set 是唯一关键路径**: 论文 §5.7 有 \goldset{} 占位符，这是唯一非 circular 评估。Pipeline v3 dry-run 已验证，但标注人力未确认。最晚 5/16 必须启动
- **易错点**:
  - 不要被 structural F1 0.9951 的高数字迷惑——这是 circular eval（structural features 重建 LF 投票），论文已有 caveat 但容易在讨论中遗忘
  - Probe conf≥2 test = 1824 windows vs all-conf test = 8101 windows，两个测试集的数字不能混用（Table 5 footnote 已有这个问题）
  - encoder ablation 结果反直觉：BGE-M3 (0.9413) > E5 (0.9363) > Qwen3 (0.9055)，老编码器反而好，说明架构贡献 > 编码器质量
  - 文件位置注意：论文 .tex 同时存在于 artifacts/_project/paper/ 和 docs/paper/sections/，注意核查两边是否一致


---
