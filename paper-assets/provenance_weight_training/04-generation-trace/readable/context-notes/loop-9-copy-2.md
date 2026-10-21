# agent / loop_9.md

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_9.md`
- **Structured JSON:** [`a15bb89975f241625695.json`](../../sessions/a1/a15bb89975f241625695.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 9
reason: idle_timeout
updated: '2026-05-15T18:49:19+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单仅 westd-47453 的 cuda:0/1/2/3，不得用其他服务器或其他 GPU 编号
- bs8 实验 OOM 已发生两次（bs8_nmin2_seed42 在 96G RTX 6000 Pro 上 OOM），bs8 配置需降低显存：减小 max_length 或启用 gradient_checkpointing，不要原样重试
- τ sweep 已完成 6/6，τ>0.8 confirmed negative（D036），不要再跑 τ>0.8 的实验
- adaptive_v2_seed42/123/456 三个 PREPARING 实验标记为 killed，registry 残留态，不要试图恢复它们——需要重新创建
- submit_training_job 的 command 必须自带环境激活（`source /root/miniconda3/bin/activate && ...`），GPU 编号写 0（框架注入 CUDA_VISIBLE_DEVICES）
- 投稿目标 EMNLP 2026 ARR May 25（距今 **10 天**），GPU 预算仅剩 ~40h，P1 实验需做优先级取舍

### 2. 🖥️ 基础设施快照
- **服务器**: westd-47453（4× RTX 6000 Pro 96GB）
- **工作目录**: `/root/provenance_weight_training/`
- **Python**: `/root/miniconda3/bin/python`（conda base 环境，不是 venv）
- **数据**: `/root/provenance_weight_training/data/scored_data.jsonl`（ρ=0.4，132M+ tokens，Qwen3-0.6B）
- **模型**: Qwen3-0.6B（路径在训练脚本中已配置）
- **W&B**: 项目名 `provenance_weight_training`（已配置）
- **HF cache**: 未特殊设置（非 AutoDL 实例）
- **活跃进程**:
  - `nmin4_seed42`: PID 225265, cuda:1, tmux=nmin4_seed42, log=`~/runs/provenance_weight_training/nmin4_seed42.log`
  - `ess_only_seed123`: PID 233872, cuda:0, log=`~/runs/provenance_weight_training/ess_only_seed123.log`
  - `ess_only_seed456`: PID 233952, cuda:3, log=`~/runs/provenance_weight_training/ess_only_seed456.log`
- **Cron 监控**: 3 个 active cron 对应上述 3 个 RUNNING 实验（reconcile 已确认全部 still running）

### 3. 📊 当前状态
**刚做完**: τ sweep 6/6 完成 + bs8_seed42/bs8_nmin2_seed42 两次失败诊断（EXIT_CODE=129 + CUDA OOM）+ zombie kill + report.md 刷新

**RUNNING 实验 (3/4 GPU)**:
| exp_id | GPU | 进度 | ETA (UTC) | 用途 |
|--------|-----|------|-----------|------|
| ess_only_seed123 | cuda:0 | ~14% | ~22:00 | Claim 1 多 seed 加固 |
| nmin4_seed42 | cuda:1 | ~27% | ~21:45 | n_min=4 边界条件（预期 b*=0 → PPL≈uniform） |
| ess_only_seed456 | cuda:3 | ~14% | ~22:00 | Claim 1 多 seed 加固 |

**cuda:2 空闲** — bs8 实验连续两次失败，尚未安排新实验。这是失职状态，需立即处理。

**等待中**:
- 3 个 cron 回调（上述 RUNNING 实验完成时触发）
- 无 running worker（Worker 池=0，低于红线 2）
- adaptive_v2_seed42/123/456 在 PREPARING 但已 killed，需要 Director 决策是否重新创建

**Registry 统计**: 44 个实验，DONE 38（success 30, negative 2, failed 3, killed 3），RUNNING 3，PREPARING 3（killed）

### 4. 📋 待办（条件触发式）
- **立即** → cuda:2 空闲，需向 Director 汇报并建议下一个实验（候选：contamination_60_datagen 数据生成，或 bs8 降显存重试，或 nmin5 ablation）
- **立即** → Worker 池=0，需 spawn ≥2 个 Worker（建议：1 个准备 bs8 OOM 修复方案 + 1 个准备 ρ=0.6 数据生成脚本）
- `ess_only_seed123` 完成 → spawn worker eval → 更新 registry metrics → 与 ess_only_seed42 对比（预期 PPL > uniform）
- `ess_only_seed456` 完成 → 同上 → 3 seeds 齐全后 Claim 1 多 seed 结论可写
- `nmin4_seed42` 完成 → spawn worker eval → 预期 PPL≈17.69（b*=0 退化为 uniform）→ n_min curve 4/4 点完成（n_min=1/2/3/4）
- 上述 3 个全部完成 → Claim 1 + n_min robustness 证据齐全 → 向 Director 汇报是否启动论文初稿
- 如果 ess_only 多 seed 出现任何 negative（PPL < uniform）→ 走 red-section framing 提案流程，不默默跑下一个
- bs8 OOM 修复方案就绪 + cuda:2 空闲 → 提交 bs8_nmin2_v2（需 gradient_checkpointing 或减小 seq_len）
- 论文初稿启动前 → 先 `dream_simulate(review_mode="full")` 验证 reframed story

### 5. 🎯 战略上下文
**核心结论链**:
- D019: MVP PASS（adaptive ≈ grid-best, ratio 88.6%）
- D023: Dual-constraint 框架（α_eff 下界 + ESS 上界 → 最小干预准则）
- D025: τ 降级为 empirical HP（不能 claim proportion-free 理论推导）
- D029: ESS-only PPL=17.728 > uniform → max-intervention 失败 → min-intervention 必要性确认
- D035/D036: τ sweep 6 点完成，[0.5,0.8] safe range，τ=0.8 optimal
- D037: bs8 配置修正（n_min=4→2），但 OOM 未解决

**Claim 证据覆盖进度**:
- Claim 1 (dual > ESS-only): 1/3 seeds done, 2 running
- Claim 2 (adaptive ≈ grid): ✅ complete (3 seeds)
- Claim 3 (unknown proportion): ✅ complete (τ sweep 6pt)
- n_min robustness: 3/4 done, nmin4 running
- batch_size 泛化: 0/1 (bs8 连续失败)

**最容易判断错的事**:
1. **bs8 OOM 不是简单重试能解决的** — 96GB 显卡 OOM 说明 batch_size=8 + grad_accum=2 + 默认 max_length 超出显存，必须改配置（gradient_checkpointing / 减小 max_length / 减小 grad_accum）
2. **adaptive_v2 三个 PREPARING+killed 是残留态** — 不要试图提交，需要重新走 experiment 创建流程
3. **GPU 预算仅剩 ~40h** — contamination_60 全套（datagen + uniform + adaptive + grid）需 ~14h，Llama-3.2-3B 需 ~25h，两者不能同时做。P1 实验大概率需要砍
4. **ess_only 多 seed 结果对 Claim 1 是关键的** — 如果任一 seed 表现 PPL < uniform（即 ESS-only 反而好），Claim 1 的 narrative 需要重写
5. **论文 framing 已 STABLE**（D023+D029+D035），不要轻易改动。但 bs8 泛化性如果最终跑不出来，n_min knife-edge 叙事会成为 reviewer 攻击面


---
