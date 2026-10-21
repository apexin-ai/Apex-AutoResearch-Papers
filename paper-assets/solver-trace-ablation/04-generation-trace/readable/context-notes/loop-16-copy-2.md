# reviewer / loop_16.md

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_16.md`
- **Structured JSON:** [`fb25daaa599f03fb4626.json`](../../sessions/fb/fb25daaa599f03fb4626.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 16
reason: max_messages
updated: '2026-05-16T20:47:38+00:00'
---

### 1. 🔴 硬约束 / 红线
- 服务器 `westd-39279`，两张 RTX PRO 6000 (98GB)。GPU 分配无固定限制但必须遵守 C002/C005/C007（显式 CUDA_VISIBLE_DEVICES、submit 前 nvidia-smi 确认无残留）
- 数据必须用 `data/train_500_seed42.jsonl`（C001），eval 必须用 `data/proofwriter_fol_100.jsonl`（C008/C009）
- `save_total_limit=1` 硬约束（C003），脚本默认值已是 1 但 YAML 配置需显式写
- 跨 run ISR 对比禁止用训练日志，必须用 eval_sta.py 统一评估（C004）
- Taxonomy: `genuine = proved − H7 − H1_exact − H8`，H1-near 保留为 genuine 但单独标记（C013）

### 2. 🖥️ 基础设施快照
- 服务器：`westd-39279(root)`，代码 `/root/solver-trace-ablation`，数据盘 `/root/autodl-tmp`（250GB，~50GB free）
- Python：`/root/miniconda3/bin/python`（conda base），激活：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- 模型：4B `/root/autodl-tmp/models/Qwen3-4B`，1.7B `/root/autodl-tmp/models/Qwen3-1.7B`
- 活跃进程（截至 handoff）：
  - PID 921646, tmux=random_1_7b, GPU-0: `w2-qwen3-1.7b-random-b01` (additive_random β=0.1 s42, 500步, ~71min)
  - PID 921785, tmux=isr_1_7b, GPU-1: `w2-qwen3-1.7b-isr-b03` (additive_bonus β=0.3 s42, 500步, ~71min)
- 关键 checkpoint：`/root/autodl-tmp/outputs/gated_warmstart_v3_t015_s43/`（τ=0.15 里程碑模型）
- eval 结果：`/root/autodl-tmp/outputs/gated_warmstart_v3_t015_s43/eval_results.json`（228KB, 已完成）

### 3. 📊 当前状态
**刚完成**：τ=0.15 eval 结果的独立审计。发现 worker 原报 "97.6% genuine" 严重虚高——genuine 审计 worker 确认修正为 **48.8% strict / 63.4% C013 标准**。已向 Director 提交两份 CRITICAL 报告：
1. 15/41 proved ISR=0 + folio_1030 实为 H7 非 H1 + 新 H8b 模式（仅量词必要）
2. 审计 worker 结果交叉验证通过，建议 registry genuine_pct 更新为 63.4%

**RUNNING 实验**：上述两个 1.7B 实验（约 20:55 UTC 完成）

**等待中**：
- 两个 1.7B 实验完成后需 eval
- Director 对 genuine% 修正的决策（是否更新 registry、是否影响论文 claim）
- τ=0.15 replication (s42, s44) 尚未启动——s42 warmstart checkpoint 存在但有 H7a 风险，s44 需先跑 exec-retrain
- H9 paper integration 连续 4 次失败，需要不同策略

### 4. 📋 待办
- 1.7B 实验完成通知 → 审查训练曲线是否正常、GPU 释放确认、eval 结果核实
- Director 回复 genuine% 修正 → 确认 registry 是否已更新、论文 claim 是否调整
- τ=0.15 replication 启动 → 审查 s42 checkpoint 是否仍有 H7a 问题（之前 s42 exec-retrain checkpoint-200 收敛到 H7a 模式，warmstart 全部失败 gate_pass=0）
- 论文章节审查请求 → 检查 genuine% 是否已用修正值、H9 是否已集成（目前仍是 "8 modes"）

### 5. 🎯 战略上下文
**核心发现**：ISR-gated warmstart (τ=0.15) 是项目首个训练成功的 ISR-gated 实验。prove_rate=41% 是真实的，但 genuine 率远低于最初声称。三层 genuine 定义（strict 48.8% / C013 63.4% / worker 原始 97.6%）是论文叙事的关键张力点。

**易错判断**：
1. **不要信 worker 的 hacking 分类**——已证明 H7 检测遗漏了 folio_1030（结论=premise 6-10），H1 分类只标了 1 个但实际 15 个 ISR=0。所有 hacking 数字需独立 grep 核实。
2. **C013 taxonomy 是关键**——ISR=0 不全是 H1_exact，很多是 C006 定义的"冗余编码"（自由变量滥用），按 C013 算 genuine。但 H8b（n_necessary>0 但仅量词必要）是新发现，C013 未明确覆盖。
3. **Registry 中 gated-isr-warmstart-t02-s43-r2 conclusion="success" 有误**——prove_rate 仅 21% 且有 premise inflation 退化，应为 failed。
4. **s42 warmstart checkpoint 有毒**——exec_retrain_v3_s42/checkpoint-200 收敛到 H7a 模式，不要用它做 ISR-gated warmstart。


---
