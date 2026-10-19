# reviewer / loop_5.md

**action cond info bottleneck** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_5.md`
- **Structured JSON:** [`e651e38be0fe82bb8955.json`](../../sessions/e6/e651e38be0fe82bb8955.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 5
reason: max_wall_time
updated: '2026-05-17T07:25:50+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目 GPU 白名单：cuda:0 和 cuda:1（westb-13953 只有 2 张 RTX PRO 6000 96GB）
- v7.1 训练必须从 `lerobot/smolvla_libero` 原始 checkpoint 开始，绝不能从受损的 v7 checkpoint (`/root/acib/outputs/acib_v7_contrastive`) 继续
- 训练命令必须同时包含 `--train_scorer_only` 和 `--freeze_action_expert`，缺一不可
- α=0.0 eval 在 v7.1 中 by construction 等于 baseline——如果不等则是 freeze 实现 bug，必须 CRITICAL

### 2. 🖥️ 基础设施快照
- 服务器：westb-13953(root)，代码目录 `/root/acib`，数据 `/root/autodl-tmp/libero_dataset`
- Python：`/root/miniconda3/bin/python`，conda env = base
- 模型：base=`lerobot/smolvla_libero`（HF 自动缓存），v7.1 输出=`/root/autodl-tmp/acib_v7.1_scorer_only_seed{1,2}`
- 日志：`/root/runs/action_cond_info_bottleneck/v71_seed{1,2}.log`
- 活跃进程（服务器 13:55 重启后）：
  - v7.1 seed1: PID 3619, tmux=v71_seed1, CUDA_VISIBLE_DEVICES=0, seed=42
  - v7.1 seed2: PID ~3693, tmux=v71_seed2, CUDA_VISIBLE_DEVICES=1, seed=123
  - 训练 step 100/20000 @ 1.8 steps/s，预计 ~09:45 UTC 完成
- Alpha sweep 结果目录：`/root/autodl-tmp/v7_alpha_sweep/alpha_{0.0,0.1,0.3}/`

### 3. 📊 当前状态
刚完成：
- α=0.0 spatial 最终结果确认：**58.2%**（500 ep），证实 base model 被 joint training 损坏（D038）
- ROADMAP 修订版审查通过（D039：MVP 标准改为 α=1.0 SR ≥ baseline-2pp）
- 向 Director 提交了 paper framing 审查（gradient pollution 定位建议 Option B hybrid）

Registry RUNNING/PREPARING：
- `acib_v71_scorer_only_seed1` — PREPARING（实际已在训练）
- `acib_v71_scorer_only_seed2` — PREPARING（实际已在训练）

等待中：
- v7.1 训练完成 (~09:45 UTC) → Worker 会启动 4-suite eval
- Director 可能回复 paper framing 讨论

### 4. 📋 待办
- v7.1 step 5000 (~07:30 UTC) → 检查 Probe A cos < 0.8，scorer_mean 趋势是否合理
- v7.1 训练完成 → 审查 eval 启动配置（α=1.0 是 MVP 核心 gate，α=0.0 是 sanity check）
- v7.1 eval 出结果 → 按 ROADMAP partial success 路径判定：α=1.0 4-suite avg ≥ baseline-2pp = PASS
- 如果 Probe A cos ≥ 0.8 → CRITICAL，scorer-only 模式下 conditioning 失效需要 rethink
- 如果 α=1.0 回退 > 2pp 但 < 5pp → 建议调低 training-time scoring_alpha 或降低 IB beta
- Director 转发 paper framing 提案 → 走 negative-framing-review skill 四维度审查

### 5. 🎯 战略上下文
**决策链**：v5 shortcut(D029) → v6 conditioning bug(D030-31) → v7 contrastive fix(D033-34) → v7 joint training 损伤(D036-38) → v7.1 scorer-only(D039)

**核心结论**：joint training 的 IB/contrastive/diversity 梯度 corrupt base policy（α=0.0=α=1.0≈58% vs baseline 66%）。问题在训练期间，非 eval 时。decoupled training 是唯一路径。

**易错点**：
1. 不要再用 "distribution coupling at eval time" 解释回退——已被 α=0.0 数据推翻。正确说法是 "training-time gradient interference"
2. v7.1 的 MVP gate 是 **α=1.0 eval SR**（训练时默认 α=1.0），不是 α=0.0（那是 tautology）
3. 64-token pruning efficiency gain 有限（端到端估计 10-20%）——efficiency 是 secondary contribution，>15% 才升为 core claim
4. 服务器 westb-13953 在本 session 中重启过一次（~05:30 UTC 左右），导致 α=0.0 full 4-suite 和 α=0.3 eval 被 kill。spatial 结果已从日志恢复，但 object/goal/libero_10 需重跑
5. α=0.1 per-task 数据显示巨大方差（T5=0%, T0=84%）——这是统计噪声不是 systematic pattern，不要过度解读单个 task


---
