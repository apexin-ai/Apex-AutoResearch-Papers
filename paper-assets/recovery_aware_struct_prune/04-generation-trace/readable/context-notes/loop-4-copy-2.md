# agent / loop_4.md

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_4.md`
- **Structured JSON:** [`cf28bae3ffa36015623a.json`](../../sessions/cf/cf28bae3ffa36015623a.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 4
reason: idle_timeout
updated: '2026-05-14T20:00:21+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：**只能用 cuda:0 和 cuda:1**（westb-23072，config gpu_ids 限定）
- Post-recovery eval **必须用 full GSM8K test 1319 samples**，不是 N=100（D008 明确要求）
- RewardDesertCallback 在当前配置下**不会触发**（patience×logging_steps=500=total_steps），不能作为 Standard 失败的 evidence
- 已有的 N=100 eval 结果（eval_baseline_7b_quick_fixed.json / eval_pruned_rasp_20_quick.json / eval_pruned_standard_20_quick.json）只是快速探针，**不能作为论文数字**
- Worker `prepare_full_eval_d008` 已准备好 full eval 脚本 `src/eval_full_gsm8k.sh`，训练完成后直接用

### 2. 🖥️ 基础设施快照
- **服务器**: westb-23072，2× RTX PRO 6000 Blackwell 94GB
- **工作目录**: `/root/recovery_aware_struct_prune`
- **Python**: `/root/miniconda3/bin/python`（conda base，不是 venv）
- **环境激活**: `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- **基础模型**: `/root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B`
- **剪枝模型**: `/root/autodl-tmp/pruned_rasp_20`（RASP 20%）、`/root/autodl-tmp/pruned_standard_20`（Standard 20%）
- **恢复输出**: `/root/autodl-tmp/recovered_rasp_20`（cuda:0）、`/root/autodl-tmp/recovered_standard_20`（cuda:1）
- **日志**: `/root/autodl-tmp/recovery_aware_struct_prune/logs/grpo_rasp_20_fast.log` / `grpo_standard_20_fast.log`
- **活跃进程**: grpo_rasp_20_fast（tmux session，cuda:0）+ grpo_standard_20_fast（tmux session，cuda:1），cron 监控中
- **HF cache**: 未显式设置（未用 AutoDL，westb 是本地服务器）

### 3. 📊 当前状态
两个 GRPO recovery 训练正在跑（快速配置：max_completion=1024, 1 epoch, 2000 samples, ~25s/step × 500 steps），预计 ~21:15 UTC 完成。Cron 监控活跃，完成后会自动回调。

**Registry 全貌（8 个实验）**:
| exp_id | status | conclusion | 摘要 |
|--------|--------|------------|------|
| grpo_rasp_20_fast | RUNNING | — | RASP-pruned 20% GRPO 恢复（cuda:0）|
| grpo_standard_20_fast | RUNNING | — | Standard-pruned 20% GRPO 恢复（cuda:1）|
| mvp_rasp_pipeline_v4 | PREPARING | — | 父实验，管理整个 V4 pipeline |
| grpo_rasp_20 | DONE | killed | 旧版 GRPO（270h 预估），D007 kill |
| grpo_standard_20 | DONE | killed | 旧版 GRPO（270h 预估），D007 kill |
| mvp_rasp_pipeline_v3 | DONE | negative | 35% sparsity → 两者都崩（0%/1%）|
| mvp_rasp_pipeline_v2 | DONE | failed | min_keep_mlp=4 导致 early layer 过度剪枝 |
| mvp_rasp_pipeline | DONE | failed | GQA constraint violation crash |

**关键数字**（N=100 快速 eval，非论文级）:
- Baseline (Qwen2.5-7B): 94%
- RASP 20%: 29%（post-prune）
- Standard 20%: 1%（post-prune）
- MLP 总参数量相同（395,232），纯分布策略差异 → Scenario B 确认（D006）

**无等待中的 Worker / 无待处理的 Director 决策。** 所有 10 个历史 Worker 已完成。

### 4. 📋 待办（条件触发式）
- **grpo_rasp_20_fast + grpo_standard_20_fast cron 回调到达** → spawn Worker 跑 `src/eval_full_gsm8k.sh` 对 4 个 checkpoint 做 full 1319 samples eval（baseline / rasp_20 / standard_20 / recovered_rasp_20 / recovered_standard_20）→ 按场景 A/B/C 判定 MVP pass/fail → 汇报 Director
- **场景 A（RASP recovered ≥50%，Standard 不恢复）** → MVP 明确 PASS → update registry conclusion=success → 启动 Phase 2（P1 多 seed 优先）
- **场景 B（RASP recovered ~35%，Standard 不恢复）** → full 1319 eval 收窄 CI → 若显著则 PASS；否则追加 2-3 epochs + lr=5e-6 再跑一轮
- **场景 C（RASP ≤30%，两者都不恢复）** → 追加 3 epochs + lr=5e-6；若仍不恢复考虑 SFT warmup → GRPO 两阶段
- **MVP pass 后** → Phase 2 优先级：P1 多 seed (42,123,7) → P2 GRASPrune baseline（memory.md 已有完整集成方案）→ P3 RLVR vs SFT → P4 per-group correlation → P5 多剪枝率 → P6 Bonsai → P7 扩展 benchmark
- **standard_25 / rasp_25 eval** 未完成（被 GRPO OOM 打断），训练结束 GPU 空出后需补跑

### 5. 🎯 战略上下文
- **核心假设**: CKA functional overlap 引导的 RASP 剪枝比 importance-only Standard 剪枝更好保留推理能力（matched sparsity）。20% sparsity 下 post-prune 29% vs 1% 已初步验证，post-recovery 是 MVP 的最后一块拼图。
- **D008 claim scope 分层**: MVP claim 是 model-level 显著性（p<0.05），per-group ρ≥0.4 是 Phase 2 mechanism claim——不要混淆。
- **目标会议**: EMNLP 2026 ARR May 25（距今 11 天），时间紧，MVP pass 后需立即全速铺 Phase 2。
- **决策链**: D001(MLP-only OK) → D002(暂缓 SFT) → D003(审计剪枝) → D004(fix min_keep_mlp) → D005(降至 20%) → D006(Scenario B 确认) → D007(kill 270h runs) → D008(claim scope 分层)
- **易踩的坑**:
  - 不要把 N=100 的 eval 数字当论文数字，必须 full 1319
  - RewardDesertCallback 没触发不代表 Standard 没有 reward desert，只是配置使它不可能触发
  - experiment_plan.yaml 是空的（实验都直接在 registry），Phase 2 启动前应该填充
  - GRASPrune 集成方案在 memory.md 里详细写了，但代码还没 clone 到服务器，Phase 2 P2 时需要 Worker 去做


---
