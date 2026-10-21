# director / loop_8.md

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_8.md`
- **Structured JSON:** [`e3bb730702dcc8209211.json`](../../sessions/e3/e3bb730702dcc8209211.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 8
reason: max_messages
updated: '2026-05-19T08:45:22+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目 GPU 白名单：rtx5090-4x cuda:0-3（4 张）。绝不在白名单外的卡上启动实验
- 1.7B RSFT seed expansion 使用 **Method A**（共享 s42 SFT base + s42 scored data），不是 full pipeline。D114 裁决。改成 seed-specific adapter 会造成 adapter/data 不匹配，比 Method A 更糟（M011 教训）
- 判断 seed expansion 正确性时必须追溯四要素一致性：generation source → CED scoring → filtered data → training adapter，四者必须来自同一 SFT base
- submit_training_job 后必须在同一 Worker 中完成 registry 注册（正确格式 `gpu: "cuda:0"` 非数组）+ cron 注册，三步一体。这个问题连续出现 4 次（M007/M008 + 14B + D112）
- 14B 训练用 2-GPU DeepSpeed ZeRO-3（D108），不是 tensor parallelism
- 远程服务器需要 `HF_HUB_OFFLINE=1` + `TRANSFORMERS_OFFLINE=1`（网络不通）

### 2. 🖥️ 基础设施快照
- 服务器：rtx5090-4x (connect.bjb2.seetacloud.com)，第二台 bjb2-12179 待确认
- 远程工作目录：`/root/autodl-tmp/freige/`
- 模型路径：`/root/autodl-tmp/models/Qwen/Qwen3-{1.7B,4B,8B,14B}/`
- NLI 模型：本地缓存（HF_HUB_OFFLINE）
- 关键 adapters：
  - 4B SFT: `sft_output_seed{42,43,44}/`
  - 4B RSFT (from s42 base): `rsft_output_qwen3_4b_k1_s{42,43,44,45}/`
  - 8B SFT: `sft_output_qwen3_8b_bf16/` (s42), `sft_output_qwen3_8b_bf16_s44/`
  - 8B RSFT: `rsft_output_qwen3_8b_k1_s{42,44}/`
  - 1.7B SFT: `sft_output_qwen3_1_7b_bf16/` (s42), `_seed43/`, `_seed44/`
  - 1.7B RSFT: `rsft_output_qwen3_1_7b_k1_s{42,43,44}/`（s43/s44 是 r2 重跑版）
  - 14B SFT: `sft_output_qwen3_14b_bf16/`（刚完成，144 steps, loss=0.5457）
  - D112 RSFT (4B from s44 base): `rsft_output_4b_sft_s44/`
- 活跃进程（handoff 时刻）：
  - cuda:0: D112 step 4 eval (~2.5h remaining)
  - cuda:1: 14B SFT eval (~5h remaining, PID 626093)
  - cuda:2: 14B no-evidence eval (~4.5h remaining, PID 626175)
  - cuda:3: 1.7B RSFT s44_r2 eval (~2.4h remaining, PID 632051)

### 3. 📊 当前状态
**刚完成**：
- 14B SFT 训练完成（144/144, loss=0.5457）→ eval 已在 cuda:1+2 跑
- 1.7B RSFT s43_r2 eval 完成：ign_f1=0.5109（vs s42=0.5122，差 0.13pp，跨 seed 稳健）
- Paper Agent 完成 tables + §4.2/§4.4 叙事 reframe（variance compression 为新核心叙事）
- ROADMAP 已更新（含 D115 8B 结果、Wave 1 完成状态）
- Comprehensive results table 已编译（art_20260519_a97536）

**RUNNING 实验**：
- `d112_rsft_s44_eval` (cuda:0) — D112 step 4，验证 RSFT 在 SFT s44 base 上的泛化性。**最关键实验**
- `plan017_14b_sft_eval` (cuda:1) — 14B SFT baseline eval
- `plan017_14b_sft_no_evidence_eval` (cuda:2) — 14B evidence tax
- `plan019_1_7b_rsft_s44_r2_eval` (cuda:3) — 1.7B 第 3 seed eval

**等待中**：无 pending Worker 回调。4 个 eval 各有 cron 监控。

### 4. 📋 待办（条件触发式）
- **D112 step 4 eval 完成** → 最高优先级：harvest ign_f1。如 > SFT s44 (0.4734) → Claim 1 robust，更新 paper_framing.md；如 < 0.4734 → 需 reframe（RSFT 可能仅在弱 base 上有效）。**必须拉 Reviewer 深度审视**，D112 训练 loss 偏高 (0.66 vs 正常 0.55)
- **1.7B s44_r2 eval 完成** → harvest + 编译 1.7B 3-seed RSFT 统计（s42=0.5122, s43=0.5109, s44=?）→ cuda:3 接 1.7B no-evidence eval → 再接 NLI ablation (plan_010)
- **14B SFT eval + no-evidence eval 完成** → 计算 14B evidence tax → cuda:1+2 释放后启动 14B RSFT pipeline（单卡 4-bit: candidates gen → CED score → filter → train → eval）
- **Paper Agent 待 D112 结果** → 统一更新 Intro/Abstract/Conclusion 数字和叙事

### 5. 🎯 战略上下文
**项目核心**：EMNLP 2026 Main (ARR July, ~57 天)，Round 1 = 3.0 (Findings)，目标 4.0 (Main)。

**叙事重心已转移**（本 session 最重要的发现）：
- 原叙事："RSFT provides +5pp improvement" → 新叙事："RSFT is a variance-reducing stabilizer"
- 4B RSFT gain 从 +4.92pp 降到 +1.24pp（因为 SFT s42 是 outlier 最弱 seed）
- 但 variance 压缩 7.5x (4B) / 5x (8B) 是更有价值的 finding
- Paper Agent 已按此方向 reframe §4.2 和 §4.4

**关键决策链**：D108(14B ZeRO-3) → D109(Random确证CED) → D110(GRPO bf16无forgetting) → D111(s42 reeval=0.3974) → D112(全RSFT基于最弱seed) → D113(GRPO ckpt-100最优) → D114(1.7B Method A正确) → D115(8B RSFT 0.5451, variance 5x压缩)

**最容易判断错的事**：
1. **D112 结果解读**：不要只看 ign_f1 绝对值，要对比 SFT s44 (0.4734)。D112 训练 loss 偏高 (0.66)，可能信号异常，需要 Reviewer 仔细看
2. **Method A vs full pipeline 混淆**：4B/1.7B/8B 的 RSFT seed expansion 都是 Method A（共享 s42 base），只有 D112 是 Method B（s44 base）。两者的 variance 含义不同，论文中必须精确区分
3. **14B RSFT 用 QLoRA 不是 bf16**：14B SFT 用了 2-GPU bf16 LoRA，但 14B RSFT 改为单卡 QLoRA（Agent 评估结论）。注意 QLoRA 在 4B GRPO 上导致过 catastrophic forgetting（D110），14B QLoRA RSFT 需要格外关注
4. **experiment_plan.yaml 长期不同步**：多个 plan entry 的 registry_id 过期，Agent 有 CPU Worker 在修但可能没完成


---
