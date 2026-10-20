# reviewer / loop_2.md

**Does Reward Curation Kill Diversity? Systematic Evidence of Surprising Resilience in Iterative Self-Training** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_2.md`
- **Structured JSON:** [`3475da9f479e6db99b0a.json`](../../sessions/34/3475da9f479e6db99b0a.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 2
reason: max_wall_time
updated: '2026-05-16T20:56:52+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目只能用 cuda:0 和 cuda:1（服务器 bjb2-23165 双卡 RTX 5090 32GB）
- Full-FT 必须 gradient_checkpointing=True + bf16=True（fp16 会 ValueError，无 grad_ckpt 会 OOM）
- 不同实验必须用独立 OUTPUT_DIR（checkpoint 按 condition_id + gen_idx 寻址，路径重叠会污染）
- K=8 GEN_BATCH_SIZE ≤ 8（16×8=128 序列 OOM）；K=16 需 ≤ 4
- AutoDL 离线模式必须设 HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1

### 2. 🖥️ 基础设施快照
- 服务器：bjb2-23165(root)，工作目录 `/root/autodl-tmp/carr`
- Python：`/root/miniconda3/bin/python`（conda base，不用 venv）
- 基座模型：`/root/autodl-tmp/models/Qwen3-0___6B`（Qwen3-0.6B, 596M params）
- 奖励模型：`/root/autodl-tmp/models/RLHFlow/ArmoRM-Llama3-8B-v0___1`（~16GB，已 patch LLAMA_INPUTS_DOCSTRING）
- HF cache：`/root/autodl-tmp/.hf_cache`（UltraFeedback 已缓存）
- 输出目录：outputs/(K=4 LoRA), outputs_k8/, outputs_fullft_k4/, outputs_fullft_nocuration/, outputs_fullft_lr2e5/
- 活跃进程：
  - `carr_fullft_nocuration_01` PID 521921 (cuda:0, tmux) — Full-FT no_curation baseline
  - `carr_fullft_lr2e5_probe_01` PID 523802 (cuda:1, tmux) — Full-FT LR=2e-5 关键实验

### 3. 📊 当前状态
**刚完成审查**：K=8 和 Full-FT(LR=5e-6) 都 P1 FAIL，已向 Director 报告诊断梯全面失败 + 战略建议。

**Registry 活跃实验**：
- `carr_fullft_lr2e5_probe_01` — PREPARING/RUNNING (cuda:1)：LR=2e-5, 3 epochs, K=4 single_reward。**最后一搏**——如果 4x LR 仍不 collapse，项目需 pivot
- `carr_fullft_nocuration_01` — RUNNING (cuda:0)：Full-FT no_curation 对照组（LR=5e-6）
- `carr_fullft_k4_probe_02` — registry 显示 RUNNING 但实际已 failed（zombie entry）

**等待中**：两个实验预计 3-4h 后完成（约 UTC 00:00）

### 4. 📋 待办
- `carr_fullft_lr2e5_probe_01` 完成 → 核心判断：Gen 2 loss 是否显著低于 LR=5e-6 版本（0.26）？Vendi 是否终于下降？如果 loss < 0.15 + Vendi 下降 → P1 可能 PASS，项目活了。如果 loss 仍高 + Vendi 不降 → 建议 Director pivot
- `carr_fullft_nocuration_01` 完成 → 作为 Full-FT 对照，比较 Vendi 趋势（预期类似 LoRA baseline +3%）
- 两个都完成 → 做完整四条件对比表（LoRA baseline / LoRA curation / Full-FT baseline / Full-FT curation），发 Director 最终判断
- 如果 LR=2e-5 产生 collapse → 需追加 K=8 Full-FT 确认 dose-response

### 5. 🎯 战略上下文
**核心结论链**：K=4 LoRA(-0.28%) → K=8 LoRA(-0.03%) → Full-FT LR=5e-6(+0.9%) → 全部 FAIL。LoRA 不是瓶颈（Full-FT 更不 collapse）。LR=5e-6 Full-FT 实际在 underfitting（loss 仅降 12%，grad_norm 6-10）。

**关键洞察（已报 Director）**：
- 自然趋势（无 curation）Vendi 上升 +3.1%，所以 P1 的"绝对下降 5%"阈值可能永远不触发
- Curation 的真实效果是"抑制自然增长"而非"导致下降"——这是一个更微妙的故事
- K=4 和 K=8 在 Gen 2 收敛到完全相同的 Vendi (107.25)——选择压力不是瓶颈

**易错点**：
- 不要因为 Full-FT(LR=5e-6) 比 LoRA 更不 collapse 就认为"Full-FT 不行"——是 LR 太低导致 underfitting，不是 Full-FT 本身的问题
- `carr_fullft_k4_probe_02` 在 registry 是 zombie（RUNNING+failed），不要以为 GPU 1 有第三个进程
- ArmoRM 已 patch 两处（模型目录 + HF module cache），transformers 升级需重新 patch


---
