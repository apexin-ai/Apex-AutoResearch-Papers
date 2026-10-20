# reviewer / loop_1.md

**Does Reward Curation Kill Diversity? Systematic Evidence of Surprising Resilience in Iterative Self-Training** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_1.md`
- **Structured JSON:** [`e2dc4b509e1fc069b2c6.json`](../../sessions/e2/e2dc4b509e1fc069b2c6.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 1
reason: max_wall_time
updated: '2026-05-16T14:25:15+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目只能用 cuda:0 和 cuda:1（服务器 bjb2-23165 双卡 RTX 5090 32GB）
- AutoDL 环境必须 `source /etc/network_turbo` 才能联网；离线使用已缓存数据集时必须设 `HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1`
- K=8 生成时 `GEN_BATCH_SIZE` 必须从 16 降至 8 或更低（16×8=128 序列 OOM），通用公式：`max(1, 64 // K_CANDIDATES)`
- 不同 K 值实验必须使用独立输出目录，否则 checkpoint 系统会加载错误的生成数据（按 condition_id + gen_idx 寻址，K=4 和 K=8 路径完全重叠）

### 2. 🖥��� 基础设施快照
- 服务器：bjb2-23165(root)，工作目录 `/root/autodl-tmp/carr`
- Python：`/root/miniconda3/bin/python`（conda base 环境，不用 venv）
- 基座模型：`/root/autodl-tmp/models/Qwen3-0___6B`（Qwen3-0.6B）
- 奖励模型：`/root/autodl-tmp/models/RLHFlow/ArmoRM-Llama3-8B-v0___1`（~16GB，已 patch LLAMA_INPUTS_DOCSTRING）
- HF cache：`/root/autodl-tmp/.hf_cache`（UltraFeedback 已缓存于 `openbmb___ultra_feedback/`）
- 输出目录：`/root/autodl-tmp/carr/outputs/`（K=4 数据在此）
- 活跃进程：baseline no_curation PID 501406（cuda:1，tmux 或直接 bash），已运行 ~2h，Gen 1 进行中
- GPU 0 完全空闲（K=8 两次启动均失败）

### 3. ��� 当前状态
**我刚完成的工作**：
- 发现并报告 K=8 两个 critical：①checkpoint 污染（已部分修复）②OOM（batch_size 未调整，未修复）
- GPU 0 自 14:11 起约 2h 空转，等待 Worker 修复 K=8 重启

**Registry 状态**：
- `carr_quick_probe_k8_01` — RUNNING（实际已崩溃，registry 未更新）：K=8 加压诊断，两次失败
- `carr_baseline_no_curation_01` — RUNNING（cuda:1，正常）：Gen 0 完成（vendi=105.42），Gen 1 生成中（~1776/2000）
- `carr_quick_probe_03` — DONE：K=4 P1 FAIL（Vendi decline -0.28%，阈值 5%）

**等待中**：Director 决策 K=8 修复方案（batch_size + 输出目录隔离）→ Worker 重启

### 4. 📋 待办
- K=8 Worker 修复完成通知 → 验证：①进程活着 ②GPU 0 有负载 ③日志显示 "Generating 8 candidates" 且无 "Resumed from checkpoint" ④batch 正常推进无 OOM
- Baseline 完成通知 → 对比 no_curation vs single_reward 的 Vendi 轨迹（Gen 0: 105.42 vs 107.54，需 Gen 1-2 数据判断是否自然漂移）
- K=8 完成 → 核心判断：Vendi decline ≥5% → P1 PASS，approve Full MVP；<5% → 建议 K=16 或 full-FT 升级
- K=16 若启动 → 必须确认 batch_size ≤ 4（16×4=64 序列），且 VRAM 估算可行

### 5. 🎯 战略上下文
- **核心问题**：K=4 + LoRA + 3代产生不了可观测的 collapse（Vendi 仅降 0.28%）。诊断梯 K=8 → K=16 → full-FT → pivot
- **关键洞察**：no_curation Gen 0 Vendi=105.42 竟然低于 single_reward 的 107.54——quality 选择在 Gen 0 不一定与 diversity 冲突。Collapse 假设依赖迭代累积效应，单代观察不够
- **Self-BLEU 是噪音**：绝对值 0.006-0.009 在 noise floor，不可解读为 collapse 证据
- **易错点**：
  - 不要套人类时间直觉判断 deadline 风险——只看 GPU-hours 是否够
  - checkpoint 系统按 `gen_idx + condition_id` 寻址，不按 K 值区分——任何新 K 值实验必须独立 output_dir
  - ArmoRM 已 patch 两处（模型目录 + HF module cache），如果有 transformers 升级需重新 patch
  - baseline 和 single_reward 用同一 seed=42 同一 prompt 集，Gen 0 Vendi 差异不是随机分割导致的——是 curation 策略差异的真实信号


---
