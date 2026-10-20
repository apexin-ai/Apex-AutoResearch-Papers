# agent / loop_10.md

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_10.md`
- **Structured JSON:** [`0bcf17c793f3de5ab652.json`](../../sessions/0b/0bcf17c793f3de5ab652.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 10
reason: idle_timeout
updated: '2026-05-15T03:55:08+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单仅 westd-22162 cuda:0~3，当前分配：cuda:0+1 → c2_n500_deepseek, cuda:2+3 → c2_qw_n500_r3。不得用其他 GPU
- d_z 报告规则（D059）：within-importance 对比保留 d_z，涉及 random 的对比只报 Wilcoxon + median_diff，不报 d_z
- II 主指标是 **median**（非 mean）+ median bootstrap CI B=10000（D054）
- Framing 硬约束（D015）：必须是 "emergent phase-strategy interaction"，禁止 "importance is broken"，禁止无限定词说 "importance masking produces super-additive interaction"
- n=500 分析完成后由 Director 派 Paper Agent 更新论文，Agent 不自行改论文
- s030 random 若 n=500 显著 → 论文措辞必须调整（见 memory.md "s030 random 显著性重点关注"）

### 2. 🖥️ 基础设施快照
- 服务器：westd-22162，工作目录 `/root/autodl-tmp/pacs`
- Python：`/root/miniconda3/bin/python`（conda base 环境，激活命令 `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`）
- 分析命令（一键）：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/pacs && python3 analyze_n500_unified.py --csv --latex`
- 数据：`/root/autodl-tmp/pacs/data/MATH-500/`（Qwen）、`/root/autodl-tmp/pacs/data/math500.json`（DeepSeek）
- 活跃进程：
  - c2_n500_deepseek: screen c2_n500_gpu0/gpu1, cuda:0+1, PID=c2_n500_gpu0
  - c2_qw_n500_r3: screen c2_qw_gpu2/gpu3, cuda:2+3, PID=159269/159794
- Cron：2 个活跃 cron 监控上述两实验（reconcile 已确认 still running）

### 3. 📊 当前状态
83 个实验（81 DONE + 2 RUNNING）。EMNLP 2026 ARR 截稿 2026-05-25（距今 10 天）。论文 §1-§8 全部完成，PDF 可编译，等 n=500 数据更新。

两个 RUNNING 实验进展（截至 2026-05-15 08:55 UTC+8）：
- **c2_n500_deepseek**（cuda:0+1）：s015✓ s020✓ s025 进行中(imp 233/500, rand 285/500) s030 待启动。ETA 全部完成 ~15:30 UTC+8
- **c2_qw_n500_r3**（cuda:2+3）：s015✓ s020✓ s025 进行中(imp 362/500, rand 337/500) s030 待启动。ETA 全部完成 ~13:27 UTC+8

无等待中的 Worker 回调或 Director 决策。Cron 会在实验完成时自动回调。

### 4. 📋 待办（条件触发式）
- c2_qw_n500_r3 cron 回调（预计先完成）→ 检查 s025-s030 数据完整性，等 c2_n500_deepseek 也完成后一起分析
- c2_n500_deepseek cron 回调 → 两实验均完成时，spawn Worker 跑 `analyze_n500_unified.py --csv --latex`
- 分析完成 → **第一时间检查 random s025/s030 是否 n=500 下显著**（这是论文措辞调整的分叉点）。汇报 Director：事实+对比 n=50+建议论文更新方案
- Director 派 Paper Agent 更新论文 → 更新 n=500 tables/figures + C5b §8 future work + C8 限定语 + Qwen caveat（若 s015 CI 仍跨零则叙事改为 "compound effect emerges above threshold sparsity ~s020"）
- 论文更新完成 → 提交 Group C full review

### 5. 🎯 战略上下文
- **核心结论**：importance-based eviction 的 compound interaction severity 随 sparsity 单调递增（DeepSeek 0.32→9.94，Qwen 0.048→2.619），random 7/8 FAIL。这是 phase-modulated emergent property，不是固定常数
- **n=500 是最后一个实验**。不会再开新实验。目的是 C7（statistical power confirmation），同时验证 dry-run 信号是否在全量下稳健
- **最容易判断错的事**：
  1. Qwen s015 大概率 CI 仍跨零（n=50 dry-run 已有信号）→ 这不是 negative，是预注册的 threshold narrative（"s≥0.20 onset"），不需要 Framing 提案
  2. 若 random s030 在 n=500 下显著 → 不是推翻结论，而是细化："moderate sparsity 下 random 无 compound effect，high sparsity 下 random 也有但幅度远小于 importance"。这需要论文措辞调整但不需要 panic
  3. c2_qw_n500_r3 是 c2_qw_n500 的 continuation（c2_qw_n500 因 cron false positive 被标 failed，实际 s015 已跑完），不要混淆这两个 exp_id
- **决策链关键节点**：D054（median 主指标）→ D058（Qwen paired 不显著等 n=500）→ D059（d_z 分场景报告）→ D060（C8 partially_confirmed）→ D061/D062（n=500 实验启动）


---
