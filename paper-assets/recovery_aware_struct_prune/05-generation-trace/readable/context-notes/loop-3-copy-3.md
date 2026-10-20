# reviewer / loop_3.md

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_3.md`
- **Structured JSON:** [`8372248638def80e32a4.json`](../../sessions/83/8372248638def80e32a4.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 3
reason: max_wall_time
updated: '2026-05-14T17:34:55+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单 C001：仅 cuda:0 和 cuda:1（westb-23072）。当前 grpo_rasp_20 用 cuda:0（CUDA_VISIBLE_DEVICES=0），grpo_standard_20 用 cuda:1（CUDA_VISIBLE_DEVICES=1），已核实合规。
- 大文件只写 /root/autodl-tmp/（C002）。pruned models 在 /root/autodl-tmp/pruned_rasp_20 和 /root/autodl-tmp/pruned_standard_20，output 在 /root/autodl-tmp/recovered_rasp_20 和 /root/autodl-tmp/recovered_standard_20。根分区仅 30GB。
- 20% sparsity 下 RASP 和 Standard MLP 总参数量相同（395,232，74.53%）——这是 Scenario B 的核心前提。任何质疑恢复差异的审查必须先确认参数量一致性。

### 2. 🖥️ 基础设施快照
- 服务器：westb-23072(root)，2× RTX PRO 6000 Blackwell 94GB
- 工作目录：/root/recovery_aware_struct_prune
- Python：/root/miniconda3/bin/python（conda base 环境，不是 venv）
- 模型源：/root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B
- Pruned models：/root/autodl-tmp/pruned_rasp_20, /root/autodl-tmp/pruned_standard_20
- GRPO output：/root/autodl-tmp/recovered_rasp_20, /root/autodl-tmp/recovered_standard_20
- 日志：~/runs/recovery_aware_struct_prune/grpo_rasp_20.log, grpo_standard_20.log
- 活跃进程：
  - PID 221271: train_grpo.py rasp 20（cuda:0, tmux=grpo_rasp_20）
  - PID 221911: train_grpo.py standard 20（cuda:1, tmux=grpo_standard_20）
- GPU 状态（截至 handoff）：双卡均 ~72GB/98GB used，99%/98% util
- 无活跃 Cron 任务

### 3. 📊 当前状态
本 session 刚启动即收到 handoff 请求，尚未执行任何审查。

Registry 全景（6 条）：
- **grpo_rasp_20** — RUNNING。RASP 20% pruned model (post-prune 29% GSM8K) GRPO 恢复训练，cuda:0，3 epochs，lr=1e-6
- **grpo_standard_20** — RUNNING。Standard 20% pruned model (post-prune 1% GSM8K) GRPO 恢复训练，cuda:1。关键风险：1% accuracy 起点极低，可能触发 RewardDesertCallback（patience=50）
- **mvp_rasp_pipeline_v4** — PREPARING（父实验，上述两个 GRPO 是它的子实验）
- **mvp_rasp_pipeline_v3** — DONE/negative（35% sparsity，Standard 0% / RASP 1%，即使加 per-layer 40% floor 也不行）
- **mvp_rasp_pipeline_v2** — DONE/failed（min_keep_mlp=4 导致 early layer collapse）
- **mvp_rasp_pipeline** — DONE/failed（GQA constraint violation crash）

无等待中的 Worker 回调或 Director 决策。

### 4. 📋 待办（条件触发式）
- grpo_rasp_20 或 grpo_standard_20 完成 → 立即 tail 日志 + 读 output_dir checkpoint，核实 GSM8K accuracy、loss 曲线、reward 统计。重点关注：
  - Standard_20 是否触发 RewardDesertCallback 提前终止（1% 起点极有可能）
  - RASP_20 恢复后 accuracy 是否显著高于 Standard_20（这是 MVP 核心假设）
  - 两者训练步数是否可比（如果 Standard 提前终止而 RASP 跑满 3 epochs，对比公平性需标注）
- 若 RASP recovery 显著优于 Standard → [severity: info] 确认 Scenario B，提醒 Director 推进 Phase 2
- 若两者恢复差异 <2pp → [severity: warning] 建议补 seed 实验排除噪声
- 若 Standard_20 被 RewardDesertCallback 终止 → 审查是否应给 Standard 更多 patience 或 SFT warmup 再对比（公平性问题）
- ROADMAP 显示 DDL 为 EMNLP 2026 ARR May 25（距今 11 天）→ 需关注 Phase 2 实验是否有时间完成

### 5. 🎯 战略上下文
**核心假设**：CKA functional overlap F(h) 预测结构化剪枝后 RLVR recoverability。RASP scoring S(h)=I(h)×(1-F(h))^α 选择的结构被剪后比 standard importance-only 更容易通过 GRPO 恢复。

**决策链演进**：D001(MLP-only OK) → D002(GRPO 无信号) → D003(审计代码) → D004(修 min_keep_mlp) → D005(弃 35% 转 20%/25%) → D006(20% RASP 29% vs Standard 1%，Scenario B)

**当前最大判断风险**：
1. **Scenario B 的公平性**：RASP post-prune 29% vs Standard 1% 的巨大差距已经说明 RASP pruning 本身就更好，GRPO recovery 对比可能只是在放大 pruning 阶段的优势而非 recovery 阶段的优势。下一个"我"需要区分"RASP 让 pruning 更好"和"RASP 让 recovery 更好"——前者已被证明，后者才是论文的核心 novelty claim。
2. **Standard_20 只有 1% accuracy**：GRPO 在近乎随机的模型上可能完全无法学习（reward desert），这会使对比不公平。如果 Standard 因 desert 提前终止，RASP 的 recovery 优势可能是"起点高所以 GRPO 能工作"而非"RASP 选的结构更 recoverable"。这需要在审查中明确区分。
3. **GRASPrune baseline**（memory.md 有详细调研）：Phase 2 P1 计划引入 GRASPrune 作为第三个 baseline。它有 rescale compensation 而我们的方法没有，公平性需关注。


---
