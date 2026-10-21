# reviewer / loop_2.md

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_2.md`
- **Structured JSON:** [`dc58aad9504fcd787799.json`](../../sessions/dc/dc58aad9504fcd787799.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 2
reason: max_wall_time
updated: '2026-05-15T18:41:15+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单 C001：仅 westd-34887 的 cuda:0 和 cuda:1，越界必须 CRITICAL + 要求 kill
- `vanilla_teal_sparse_ppl` 已标记 `_INVALID`（66036），禁止引用为 training-free baseline 证据——这是 strawman，已在审查 #7 CRITICAL 打回过一次
- 所有 eval 必须 `--seq_len 2048`，s0 曾因 1024 被 CRITICAL（已修复）
- Reviewer 只读：只用 read_registry / ssh_read_only / tail_logs / fetch_wandb / read_project_file，唯一输出渠道 reviewer_post_to_director

### 2. 🖥️ 基础设施快照
- 服务器：westd-34887(root)，代码 `/root/distill_sparse_swiglu/`，日志 `~/runs/distill_sparse_swiglu/`
- Python：conda base `/root/miniconda3/bin/python`，激活 `source /root/distill_sparse_swiglu/setup_env.sh`
- 模型：`/root/autodl-tmp/models/llama-3.1-8b`
- Checkpoints：`/root/distill_sparse_swiglu/checkpoints/{mvp_kl_norm_v2_s42,kl_only_s0,kl_only_s1,spon_kl_s42,bce_comp_staged_s42,...}/`
- WANDB_MODE=disabled（全项目），不检查 W&B
- 截至 handoff：两个 GPU 均空闲（bce_comp 和 spon 刚完成），等待 SPON seq2048 验证和 STE baseline 提交

### 3. 📊 当前状态
**刚完成**：审查 #1-#8 全部已 post。重点成果：
- 5-seed KL headline 验证 PASS（12.32±0.71，排除 s456 后 12.00±0.07）
- spon_training DONE/negative（recovery 3.8%），bce_comp_staged_s42 DONE/negative（25.44 vs KL 9.19）
- Training-free baselines TEAL greedy=50035, WINA=82567, R-Sparse=74929（结果待注册 registry，这是我重点跟踪项）

**Registry 状态**：
- RUNNING/ANALYZING: 0（全部完成）
- 即将提交: SPON seq_len=2048 验证 (cuda:0), plan_002 STE baseline 3 seeds (cuda:1)
- spon_kl_s42: PREPARING（关联 spon_training 的 eval 实验壳）

**等待中**：Director 应调度 SPON 2048 验证和 STE baseline 到空闲 GPU

### 4. 📋 待办
- Training-free baselines 注册到 registry → 独立交叉验证数字（TEAL greedy 50035 需特别审查——greedy 不应这么高，可能 calibration_samples=32 不够或 50% 是 SwiGLU 破坏阈值）
- SPON seq_len=2048 完成 → 核实是否改善 3.8% recovery，决定 Claim 2 最终 framing
- STE baseline 完成 → 验证 loss function vs relaxation method 的贡献隔离（Reviewer Concern #3）
- s456 outlier 调查结果出来 → 审查 root cause 是否可信，论文是否需要标注
- WINA greedy allocation 是否追加运行 → 如果 Director 采纳审查 #8 建议，跟踪结果
- SPON TEAL+SPON metrics 补录 → 确认 teal_with_spon=11.93 和 dense 退化 6.12→6.19 进入 registry

### 5. 🎯 战略上下文
**核心结论链**：D001(MVP设计) → D003/D004(KL坍塌→Lagrangian+归一化) → D006(Reviewer发现÷vocab_size bug) → D007(MVP PASS: KL 12.52 vs BCE 44.45) → D008/D009(BCE-comp negative, SPON negative → Claim 2 reframe "KL subsumes SPON")

**最容易判断错的事**：
1. "Training-free baselines 全崩"看起来像 KL 大获全胜，但 WINA/R-Sparse 用的是 global top-K（不是 greedy）——审稿人会要求最强 baseline。务必追问 WINA greedy 是否运行。
2. SPON eval_spon.log 中 teal_no_spon=12.15 与 registry 旧值 12.08 不同（calibration 随机性）——不要把两次不同 eval 的数字混在一张表里。
3. BCE-comp sparsity=0.558 vs KL 0.498，不在同一稀疏水平——数字对比要加 caveat。
4. paper_framing.md Claim 2 仍写"additive composition"但 ROADMAP 已 tentative reframe "KL subsumes SPON"——两边不一致是正常的（pending 验证），但 reframe 确认后必须同步更新。
5. 项目节奏是 AI Agent 级别（分钟级迭代），不要用人类时间尺度判断"来不来得及"——只看 GPU-hours 够不够。


---
