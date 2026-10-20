# agent / loop_8.md

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_8.md`
- **Structured JSON:** [`121118656881d40afd92.json`](../../sessions/12/121118656881d40afd92.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 8
reason: idle_timeout
updated: '2026-05-15T14:34:15+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：westb-23072 cuda:0/1 + westd-11672 cuda:0/1，共 4 卡，无例外（C001+C003）
- 大文件只写 `/root/autodl-tmp/recovery_aware_struct_prune/`，根分区 ~30GB 极易满（C002）。HF cache 必须设 `HF_HOME=/root/autodl-tmp/.hf_cache` + `HF_DATASETS_CACHE=/root/autodl-tmp/.hf_cache/datasets`（v7 双卡崩溃教训）
- GRPO 训练 GPU 参数始终 `--gpu 0`，物理卡通过 `CUDA_VISIBLE_DEVICES` 映射（v7 bug：`--gpu 1` 导致访问不存在的设备）
- submit_training_job 的 command 必须自带 `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`，两台服务器均用 conda 不是 venv
- EMNLP 2026 ARR deadline 2026-05-25，距今 10 天。GRPO 是唯一核心实验路径，失败 = 项目需根本性 pivot

### 2. 🖥️ 基础设施快照
- **westb-23072**: 2× RTX PRO 6000 Blackwell ~98GB | 工作目录 `/root/recovery_aware_struct_prune` | 数据盘 `/root/autodl-tmp/` (250GB, ~110GB free) | Python `/root/miniconda3/bin/python` (conda base)
- **westd-11672**: 2× RTX PRO 6000 ~95GB | 同上目录结构 | 磁盘空间充足
- 模型路径: `/root/autodl-tmp/pruned_rasp_20`, `/root/autodl-tmp/pruned_standard_20`, `/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20`, `/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20`
- GraSP 模型: `/root/autodl-tmp/recovery_aware_struct_prune/pruned_graspune_20/`
- α ablation checkpoints: `/root/autodl-tmp/recovery_aware_struct_prune/sft_ablation/alpha_{0.0,0.5,1.0,2.0,4.0}`
- CKA 分数缓存: `results/cka_scores.pt`
- 活跃进程: 无确认 RUNNING 实验（v7 双卡已崩溃，v8 正由 Worker 启动中）
- Cron: 0 个活跃（reconcile 确认）

### 3. 📊 当前状态
**刚做完**: GRPO v7 双组崩溃（D032: 根分区磁盘满 + GPU 映射 bug），已派 worker_ops_westb-v8-launch 启动 v8（修复 HF cache 重定向 + GPU 映射）。sft-alpha-1p0 成功完成（loss=0.64, token_acc=0.83）。

**Registry 摘要** (33 experiments: 6 success / 5 negative / 10 failed / 12 killed+preparing):
- westb cuda:0/1: 等待 GRPO v8 RASP + Standard 启动（Worker 正在操作）
- westd cuda:0: grasp_baseline_westd (PREPARING) — GraSP N=100 eval 应该已提交，可能需要确认状态
- westd cuda:1: eval-sft-alpha-0p0 (PREPARING) — α=0.0 SFT eval 已提交

**活跃 Worker (4)**:
1. `worker_code_alpha0-sft-eval-and-queue` — α=0.0 post-SFT eval + 排队后续 α
2. `worker_ops_westb-v7-fix` — 可能已过时（v7 已确认失败）
3. `worker_status_westb_grpo_v7_check` — 同上，v7 状态检查
4. `worker_ops_westb-v8-launch` — **关键**: 正在 westb 启动 GRPO v8 双卡

**等待中**: 4 个 Worker 回调。v8 launch Worker 最关键——回调后需确认双卡 RUNNING + 注册 cron 监控。

### 4. 📋 待办（条件触发式）
- worker_ops_westb-v8-launch 回调 → 确认 v8 双卡 PID 存活 → update_registry(status=RUNNING, spec) → 注册 cron 监控 → 汇报 Director
- v8 如果再次 OOM/崩溃 → 考虑 ref_model CPU offload 或 LoRA-only GRPO（不要再加 8-bit 以外的 optimizer hack）
- GRPO v8 完成（ETA ~21h, ~5/16 12:00 UTC）→ spawn worker eval 两模型 (N=100, greedy) → 判定 |RASP-Standard|: >15pp/5-15pp/<5pp → 按 ROADMAP contingency table 行动
- eval-sft-alpha-0p0 完成 → 记录 α=0.0 post-SFT accuracy → 与 α=0.5(待跑)/1.0(57%)/4.0(62%)/Standard(64%) 对比
- grasp_baseline_westd eval 完成 → 确认 GraSP N=100 准确率（50 样本 checkpoint: 8%）→ 接着跑 sft_grasp_20_westd SFT → eval
- GraSP SFT eval 完成 → 三方对比: Standard 64% vs RASP 57% vs GraSP ?% (post-SFT)
- α=0.5 和 α=2.0 的 SFT 尚未跑 → westd cuda:1 空闲时逐个排队
- GRPO v8 结果出来 + 所有 α SFT eval 完成 → 向 Director 汇报完整数据表 + narrative 建议

### 5. 🎯 战略上下文
**核心结论链**: D027 摧毁了 post-prune 29x advantage claim（实际 4pp, p=0.54）。D029 确认 SFT 阶段 Standard > RASP (64% vs 57%)。整个论文 narrative 现在 100% 押注 GRPO recovery 阶段 RASP > Standard。如果 GRPO v8 也失败（技术层面）或 RASP ≈ Standard（假设层面），项目需要根本性 pivot。

**最容易判断错的事**:
1. **不要信 registry 里 PREPARING 的 PID**——v7 崩溃后 westb 进程已死，PREPARING 实验的 PID 可能是僵尸。必须 SSH 确认。
2. **westb 磁盘可能还是紧张**——v8 Worker 应该已设 HF cache 到数据盘，但 verify 磁盘空间 (`df -h /`) 是启动后第一件事。
3. **GRPO v1-v7 已失败 7 次**，v8 的修复点是 HF cache + GPU 映射，但 OOM 根因（8-bit optimizer 在 ~95GB 卡上跑 ref_model + train_model）尚未从根本解决——v6 在 step 9 OOM，v7 的 8-bit optimizer 理论上够但没跑到那一步就磁盘满了。v8 是第一次真正验证 8-bit optimizer 能否跑完。
4. **α ablation 数据不完整**——只有 α=0.0/1.0/4.0 跑了 SFT，α=0.5/2.0 还缺。完整 α-recovery 曲线需要全部 5 点。
5. **GraSP 是安全牌**——无论 GRPO 结果如何，RASP >> GraSP (3.6x) 已成立，可以用于 gradient-based baseline 对比。但单靠 GraSP 不够撑 paper。


---
