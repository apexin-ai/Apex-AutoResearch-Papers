# agent / loop_11.md

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_11.md`
- **Structured JSON:** [`76294f48656d653ec7ef.json`](../../sessions/76/76294f48656d653ec7ef.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 11
reason: idle_timeout
updated: '2026-05-15T11:30:00+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单只有 cuda:0 和 cuda:1（2 × RTX PRO 6000 96GB），服务器 westd-39279
- 所有 eval 必须用 `proofwriter_fol_100.jsonl`，禁止用 `test_100.jsonl`（D062/D063 教训，用错测试集导致结论作废）
- ISR β=0.1 hacking rate 论文中标 "lowest hacking rate"，不标 "no hacking"（D044）
- plan013 vs plan017 公式结构不同，不可简化为 "additive vs convex" 对照（D027）
- premise-count-matched 倍率是 1.06x，2.4x 已作废（D051）

### 2. 🖥️ 基础设施快照
- 服务器：westd-39279，工作目录 `/root/autodl-tmp/solver-trace-ablation/`
- Python：`/root/miniconda3/bin/python`（conda base 环境，非 venv）
- 模型：Qwen2.5-3B 系列，路径 `/root/autodl-tmp/` 下
- 数据：`data/proofwriter_fol_100.jsonl`（eval），训练数据 FOLIO 500
- 活跃进程：
  - plan002-additive-b01-s42-1000 (PID 171076, cuda:0) — ISR β=0.1 1000步扩展
  - plan009-sft-baseline-s44 (PID 188375, cuda:1) — SFT 第3个 seed
- Cron：2 个活跃（分别监控上述两个实验）

### 3. 📊 当前状态
刚处理完 plan009-sft-baseline-s43 完成回调（success，PR=0.15, genuine=93.3%, H7=0%），已更新 registry 并汇报 Director。分析 Worker 卡在重复 update_registry 调用，已取消。

**RUNNING**:
- plan002-additive-b01-s42-1000 — ISR β=0.1 1000步，完成后做 exec-only vs ISR vs random 三方对比
- plan009-sft-baseline-s44 — SFT 第3个 seed，完成后获 3-seed SFT 统计

**QUEUED**:
- plan018-additive-random-b01-s42-1000 — Random β=0.1 1000步控制组，等 cuda:0 空出

**Workers**:
- worker_analysis_wilson-ci-complete (running) — Wilson CI 统计分析
- worker_research_sft-literature-linkage (running) — SFT 文献联动检查

### 4. 📋 待办
- plan002-b01-s42-1000 cron 回调 → spawn worker 分析 1000步 ISR β=0.1 结果 → 与 plan016 (exec-only 1000步 PR=0.96/ISR=0.003) 对比 → 立即提交 plan018-random-b01-s42-1000 到 cuda:0
- plan009-sft-s44 cron 回调 → spawn worker 计算 3-seed SFT mean±std → 更新论文 Table
- plan018-random-b01-s42-1000 完成 → 1000步三方对比 (exec-only vs ISR vs random) 完整数据，写入论文 §4
- Wilson CI worker 完成 → 整合 D072 Wilson CI 结论到论文统计表述
- 两个 running workers 完成 → 检查 Worker 池是否 ≥ 2，不足则补充写作/分析 Worker

### 5. 🎯 战略上下文
- **阶段**: Writing + 审稿准备，DDL 2026-05-25（剩 10 天）
- **核心 framing**: STA/ISR 是 GRPO 的诊断工具 + Goodhart's Law 案例研究。ISR 从诊断指标变成优化目标时出现 Goodhart 转折
- **三大 Claims 均已有证据支撑**: Claim 1 (STA 诊断), Claim 2 (Goodhart/ISR 无结构优势, D057), Claim 3 (跨逻辑泛化, D059)
- **Bootstrap CI 已完成**: genuine rate parity p=0.637 (n.s.), H7 gaming p=0.0004, ISR* inflation p<0.001
- **D072 (Wilson CI)**: 可能翻转 bootstrap 结论——ISR β=0.1 genuine 显著高于 random。Wilson CI worker 正在分析，结果将影响 §4.2 表述
- **易错点**:
  - β=0.3 系列只有 single-seed observation，不能做 3-seed 统计推断
  - Prolog STA 3/3 seeds 是 gaming（含 query-as-fact），Reviewer 已核实，不要标 genuine
  - D066 暂停了 "Goodhart instability" 叙事变更，等 proofwriter 数据确认
  - SFT s42 曾多次失败重训（s42-r4 才成功），提交 s44 时注意用相同配置


---
