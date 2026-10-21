# reviewer / loop_7.md

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_7.md`
- **Structured JSON:** [`cb824bbb10a19ec55bf0.json`](../../sessions/cb/cb824bbb10a19ec55bf0.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 7
reason: max_wall_time
updated: '2026-05-17T07:44:15+00:00'
---

### 1. 🔴 硬约束 / 红线
- westd-27271 两块 GPU (0,1) 均为本项目使用，cqa1-33015 四块 GPU (0-3) 均为本项目使用
- eval_success_rate_libero.py 的 `register_acis_hook` 刚修复（07:18 UTC）——之前版本的所有 pruning eval 结果（mode=acis_prune/random_prune）**全部无效**（hook dimension mismatch 导致 pruning 是 no-op）。修复前的 "44.8% lossless compression" 是假象
- cron on_failed 对 ACIS k=0.7/k=0.3 训练频繁误报——进程活着但 cron 检测不到。先 tail log 确认进程状态再判断

### 2. 🖥️ 基础设施快照
- **westd-27271** (root): `/root/autodl-tmp/importance_margin_vla_compress`, Python: `/root/miniconda3/bin/python`
  - GPU 0: eval_stage1only_object_v2_fixed 运行中（PID 140055, 修复后真实 ACIS prune eval）
  - GPU 1: 空闲（k07 bypass/stage1 k07 eval 均已完成）
- **cqa1-33015** (root): `/root/autodl-tmp/importance_margin_vla_compress`
  - GPU 0: 空闲
  - GPU 1: libero_fullft_batch64_v2（PID 8723, step ~100/100K, sps=0.3, ~3.8 天完成）
  - GPU 2: train_acis_stage1only_k07（step ~6K/10K, sps=4.2, ~16 min 完成）
  - GPU 3: train_acis_stage1only_k03（类似进度）
- Checkpoints 关键路径: `checkpoints/libero_imm_twostage_fullft/stage1_done/checkpoint.pt` (原始 expert + ACIS), `checkpoints/libero_full_ft_100k/checkpoint.pt` (baseline)
- Eval results: `eval_results/` on westd

### 3. 📊 当前状态
**正在运行**:
- `eval_stage1only_object_v2_fixed` (westd GPU 0): **修复后真实 pruning eval**, Tasks 0-4 全部 0/50 (0/250)，Task 5+ 进行中，约 20 min 完成。预期最终 0/500
- `libero_fullft_batch64_v2` (cqa1 GPU 1): batch=64 强 baseline 训练，step ~100/100K，~May 21 完成
- `train_acis_stage1only_k07` (cqa1 GPU 2): ACIS k=0.7 Stage1 训练，即将完成
- `train_acis_stage1only_k03` (cqa1 GPU 3): ACIS k=0.3 Stage1 训练，即将完成

**等待中**: Director 对项目方向终审的决策（已发 critical 报告：IMM 方法论对 VLA closed-loop 不成立）

### 4. 📋 待办
- `eval_stage1only_object_v2_fixed` 完成 → 读 JSON 确认最终 0/500，发最终确认报告给 Director
- ACIS k=0.7/k=0.3 训练完成 → 鉴于 k=0.5 pruning = 0% SR，k=0.7/k=0.3 的 eval 也预期灾难性。但仍应跑验证（用修复后脚本），因为 k=0.9（仅移除 13/128 tokens）理论上有微弱可能存活
- Director 决策到达 → 审查新方向是否有实验支撑（可能 pivot 到 negative results paper / token merging / 其他 compression 方法）
- `libero_fullft_batch64_v2` checkpoint 出现 → 验证 batch=64 是否修复 87.3% SR gap（预期 SR >>50%），这是唯一还可能产出正面结果的实验线

### 5. 🎯 战略上下文
**项目核心结论链**:
1. IMM two-stage (Stage1 train ACIS + Stage2 retrain expert): Stage2 **摧毁** expert weights → bypass 0/500, acis_prune 10.4%
2. Stage1-only inference pruning: eval script 有 bug (hook dimension guard 静默跳过), 修复后真实 pruning → 0/250+ (灾难性)
3. **VLA closed-loop 对 50% token pruning 零容忍**，无论 importance scoring 质量如何。这是方法论层面的 negative result

**最易判断错的事**:
- **不要相信之前的 "44.8% = lossless" 结论**——那是 eval bug 造成的假象。修复前所有 mode=acis_prune/random_prune 的结果都是实际未 pruning 的 baseline 行为
- **cron on_failed 频繁误报**——先 `tail log` 确认进程死活，不要立刻标 CRITICAL
- **不要因为 "0% SR" 就认为 ACIS 本身无价值**——MVP 阶段的 offline metrics (G1 margin, G2 preservation) 表明 ACIS 确实学到了 importance ranking，但 offline metrics 不 translate to closed-loop SR。区分 "scoring quality" 和 "pruning tolerance" 是论文的关键 framing 点


---
