# reviewer / loop_8.md

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_8.md`
- **Structured JSON:** [`9215fe99684bf6c76be0.json`](../../sessions/92/9215fe99684bf6c76be0.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 8
reason: max_wall_time
updated: '2026-05-15T14:29:10+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：cuda:0, cuda:1, cuda:2, cuda:3（westd-47453 四卡全可用）。每次审查 RUNNING 实验必须 `nvidia-smi` 核对进程 GPU 编号。
- eval 输出路径不统一：Agent 有时写 `output/eval_results/` 有时写 `output/models/{exp}/eval_results.json`，独立验证时两个路径都要查。
- ess_only_seed42 的 registry 中 `vs_uniform_ppl_delta` 已修正为 "+0.038"（此前是错误的 "+0.06"，我提了 warning 后被修正）。但 Agent 分析文档（`artifacts/ess_only_seed42/report/ess_only_seed42_analysis.md`）中的数值错误仍未修正（uniform PPL 写成 17.67、adaptive_fix b* median 写成 0.069 等），如果这些数字进论文需要再拦一次。

### 2. 🖥️ 基础设施快照
- 服务器：westd-47453(root)，代码根：`/root/provenance_weight_training`
- Python：`/root/miniconda3/bin/python`（conda base 环境）
- 模型：`/root/provenance_weight_training/models/Qwen/Qwen3-0.6B`
- 数据：`/root/provenance_weight_training/data/scored_data.jsonl`（训练），`data/human/eval_holdout.jsonl`（eval，4,077,068 tokens）
- W&B：WANDB_MODE=disabled（全部实验）
- 活跃进程（截至 handoff 时刻）：
  - PID 209829 — tau_0.7_seed42（GPU 0，干净重启后的单实例）
  - PID 205657 — tau_0.5_seed42（GPU 1）
  - PID 213283 — tau_09_seed42（GPU 3，刚启动 ~1 min）
  - GPU 2 空闲（nmin1_seed42 刚完成）
- auto_eval_watcher PID 99508 存在但功能受限（不会自动 eval 非 grid 实验，Agent 手动触发 eval）

### 3. 📊 当前状态
刚完成 nmin1_seed42 训练完成通知审查（cron:on_complete），registry 状态 ANALYZING，等待 eval worker。

**已验证完成的实验（seed42，PPL 已独立核实）**：
| exp_id | PPL | 结论 |
|--------|-----|------|
| uniform | 17.690 | baseline |
| adaptive_fix (τ=0.8) | 17.650 | best so far |
| grid_b=0.5 | 17.650 | ties adaptive |
| golden_ratio (oracle) | 17.654 | adaptive ≈ oracle |
| tau_06 (τ=0.6) | 17.681 | negative vs τ=0.8 |
| ess_only | 17.728 | worse than uniform |

**RUNNING / 待 eval**：
- nmin1_seed42 — ANALYZING，训练完成待 eval。预测 PPL 会很差（b≈20 极端降权，ESS=1.0）
- tau_07_seed42 — RUNNING（GPU 0），干净重启后刚开始
- tau_05_seed42 — RUNNING（GPU 1），约 1h+ old
- tau_09_seed42 — 刚提交（GPU 3），PREPARING

### 4. 📋 待办
- nmin1_seed42 eval 完成 → 独立验证 PPL，与 ess_only 对比。若 PPL ≥ 17.72 → 确认 n_min=1 退化为 max-intervention，支持 n_min≥2 必要性论述
- tau_05_seed42 完成 → 验证 PPL，补充 τ sweep 最低端数据点。预期 b 更低、PPL 更接近 uniform
- tau_07_seed42 完成 → 验证 PPL，填充 τ=[0.6, 0.7, 0.8] sweep
- tau_09_seed42 完成 → 验证 PPL，τ=0.9 是否比 τ=0.8 更好？如果是，最优 τ 可能 > 0.8
- 全部 τ sweep 完成后 → 审查 inverted-U 曲线完整性，检查是否需要 τ=0.95 补点
- Agent 产出论文章节 → 按 §5 对抗审查流程，重点检查 τ sweep 数据是否被 cherry-pick

### 5. 🎯 战略上下文
**核心结论链**：dual-constraint (τ=0.8, n_min=2) PPL=17.650 ≈ golden_ratio oracle (17.654) >> uniform (17.690) >> ess_only (17.728)。adaptive 在不知道真实标签的情况下逼近 oracle，这是论文最强叙事点。

**τ 与 b 的关系容易搞反**：更高的 τ（更严的 α_eff 下界）→ 更大的 b（更强降权）。这在 min-intervention 框架下是反直觉的。Agent 已经在 tau_06 分析中写反过一次（"更低的 τ 意味着更严格的 α_eff 下限"），我已 warning。论文中如果出现因果方向描述，务必核对。

**nmin1 是关键 ablation**：从 step_metrics 看 b 频繁打到 20（上界），ESS=1.0，weighted_loss 是 unweighted 的 2 倍。如果 eval 确认 PPL 差，则 n_min 和 ess_only 形成双重 ablation 证据（一个证明 α_eff 约束必要，一个证明 ESS 约束必要）。


---
