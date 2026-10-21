# agent / loop_1.md

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_1.md`
- **Structured JSON:** [`2b10505a813cbb82e5b1.json`](../../sessions/2b/2b10505a813cbb82e5b1.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 1
reason: max_wall_time
updated: '2026-05-17T11:03:42+00:00'
---

### 1. 🔴 硬约束 / 红线
- OT-7B best layer = **Layer 16**（不是 Layer 0）。Layer 0 是 M001 bug 残留。所有论文表格、registry、分析必须用 Layer 16
- R1-8B best layer = **Layer 14**（Layer 12 微幅优 +0.004 但不需要换）。full sweep 0-24 已确认
- Bootstrap 必须用 **matched W**（HS 和 Text 用同一个 W 值）。不能用各自 best W
- Hidden state indexing: `hidden_states[layer_idx + 1]`，layer 0 = transformer block 0（非 embedding）。所有 4 个模型一致
- HF_ENDPOINT=https://hf-mirror.com 必须设置，否则数据集下载失败
- Path B（数据扩展）已被 Director 放弃——annotation validation failed，不要再尝试

### 2. 🖥️ 基础设施快照
- 服务器: autodl-rtx6000, 2× RTX PRO 6000 Blackwell (98GB VRAM each)
- 工作目录: `/root/autodl-tmp/contrastive_trace_safety/`
- Python: `/root/miniconda3/bin/python3.12`
- 模型缓存: R1-32B `/root/autodl-tmp/.hf_cache/deepseek-ai/DeepSeek-R1-Distill-Qwen-32B`, QwQ `/root/autodl-tmp/.hf_cache/Qwen/QwQ-32B`, OT-7B 已下载到 HF cache
- Hidden states: `artifacts/hidden_states/` (R1-8B), `hidden_states_r1_32b/`, `hidden_states_qwq_32b/`, `hidden_states_ot7b/`
- 活跃进程: 无 cron。两个 Worker 运行中（见下）

### 3. 📊 当前状态
刚完成:
- R1-8B layer 0-11 补测 → L12≈L14，无变化
- OT-7B layer 16 验证 → 全面优于 L0，registry 已更新为 Layer 16
- 32B power analysis → R1-32B 需 ~55-75 traces (underpowered), QwQ 基本无 effect

等待中的 Worker 回调:
1. **worker_code_ot7b_layer16_bootstrap_ci_20260517T093734** — OT-7B Layer 16 bootstrap with 95% CI + selectivity control。turn 27, selectivity 5/10。这个 worker 运行时间较长，可能需要检查是否卡住
2. **worker_code_ot7b_gru_layer16_20260517T110235** — OT-7B GRU sequence model (Layer 16), 3 seeds。Claim 3 四模型完整性补充

Registry: 18 experiments 全部 DONE（无 RUNNING/PREPARING）。两个 worker 是 code task 不在 registry 中。

### 4. 📋 待办
- bootstrap_ci worker 完成 → 汇报 Director: 每个 metric 的 HS mean / Text mean / delta / 95% CI / p-value + selectivity (Layer 16) + Layer 0 vs 16 对比表。更新 registry metrics 加入 CI
- GRU worker 完成 → 汇报 Director: coverage / lead / pre_cp_fpr (mean±std, 3 seeds)。与其他 3 模型 GRU 做对比表。注册 artifact
- bootstrap_ci worker 如果超过 40 turns 仍未完成 → 检查是否卡在 selectivity 循环，考虑 cancel 重派
- 两个 worker 都完成后 → Director 可能下令更新论文表格（OT-7B 全部替换为 Layer 16 数据）
- Director 可能要求基于 power analysis 调整论文 framing（R1-32B "directional" narrative）

### 5. 🎯 战略上下文
- 论文核心 claim: HS probe 能比 text probe 更早更准地检测 safety commitment point
- 4 模型格局: R1-8B 3/3 Bonf ✓, OT-7B 3/3 Bonf ✓ (Layer 16), R1-32B directional but underpowered, QwQ 无显著优势
- D022 三路扩展: Path A (OT-7B) = success, Path B (数据扩展) = abandoned, Path C (adaptive window) = appendix only
- Deadline: ARR 2026, May 25
- 易错点: (1) OT-7B 提取的 layers 可能不是 0-27 全部，GRU worker 需要先检查 .pt shape 确认 layer 16 index (2) Worker 容易用 nohup 跑后台然后退出，必须强调同步执行 (3) QwQ-32B 的 position baseline > HS probe (70.6% vs 67.8%)，论文讨论中需要诚实承认这个弱点
- Power analysis 关键数字: R1-32B 需要 n≈55-75 for Bonferroni 80% power，QwQ bal_acc 需要 n≈2365（说明 effect 不存在）


---
