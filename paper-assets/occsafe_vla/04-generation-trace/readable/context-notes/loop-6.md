# director / loop_6.md

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_6.md`
- **Structured JSON:** [`4c6b0a07e186360b74ee.json`](../../sessions/4c/4c6b0a07e186360b74ee.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 6
reason: max_messages
updated: '2026-05-25T03:16:50+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目 GPU 白名单：westd-10894 cuda:0-3 + westd-34685 cuda:0-3，共 8 张，不可用其他服务器/GPU
- NCCL false-fail 模式：torchrun 训练结束时 `destroy_process_group()` 产生 exit code=1，cron 误判为 failed。收到训练 "failed" 通知必须先检查日志 "Max step reached" + 50K checkpoint 是否存在，再判断
- 10894 磁盘紧张（~50G 可用），禁止跨服务器 SCP 大文件或启动新训练。中间 checkpoint（20K/40K）清理指令已发但 Agent 可能尚未执行
- D043 "BN coupling crossover" 假说已被 D044 撤回（s1 CKA=0.965 未复现 s0 的 DINOv2 漂移）。不要用 crossover interaction 叙事

### 2. 🖥️ 基础设施快照
- **westd-10894**: connect.westd.seetacloud.com, root, 项目路径 /root/occsafe_vla, checkpoints /root/autodl-tmp/checkpoints/
- **westd-34685**: connect.westd.seetacloud.com, root, 同上路径结构
- 镜像 aml-train（conda 环境，`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`）
- HF_HOME=/root/autodl-tmp/.hf_cache
- W&B 未配置（WANDB_MODE=disabled）
- Same-seed 梯度分析 checkpoint 全部在 10894：vanilla_retrain_s0 / full_occ_retrain_s0（SCP 自 34685）/ ablation_occ_detach_s0_retrain / full_occ_ln_s0
- 活跃进程：10894 上 3 个 eval（full_occ_ln_s1_eval, s2_eval, ablation_retrain_eval）+ CKA s2；34685 上 cutoff_15k_s1_eval + 3 个训练（cutoff_45k_s1, cutoff_25k_s2, reverse_cutoff_s2）

### 3. 📊 当前状态
**刚做完**：CKA s1 确认 s0 DINOv2 漂移是 outlier（D044），撤回 crossover 假说。综合指令合并混乱队列，8/8 GPU 全满。

**RUNNING**（约 15-30min 内完成）：
- full_occ_ln_s1_eval, full_occ_ln_s2_eval（10894:0,3）→ 2×2 factorial 3-seed CAR
- ablation_occ_detach_s0_retrain_eval（10894:2）→ same-seed detach baseline
- cka_full_occ_ln_s2（10894:1）→ 确认 s0 outlier 的最后数据点
- cutoff_15k_s1_eval（34685:1）→ dose-response 第二 seed

**RUNNING 训练**（数小时）：
- cutoff_45k_s1（34685:0, ~20%, ~9h）
- cutoff_25k_s2（34685:2, ~54%, ~5h）
- reverse_cutoff_s2（34685:3, ~54%, ~5h）

**等待回调**：4 个 eval + 1 个 CKA 的 Worker done 回调。Agent 队列深度 ~4。

**未执行的已发指令**：10894 中间 checkpoint 清理（90G 可释放）在 Agent 队列中待处理。

### 4. 📋 待办
- eval 回调到达 → 汇总 2×2 factorial 3-seed 结果表，更新 paper_framing.md 中的 evidence table
- cka_full_occ_ln_s2 完成 → 如 DINOv2 CKA≈0.96 则 s0 outlier 确认，附录中报告；如异常则重新评估
- 10894 eval 完成释放 GPU → 立即在 cuda:1 上启动 same-seed 4 条件梯度分析（checkpoint 已就位）
- cutoff_15k_s1_eval 完成 → 清理 34685 中间 checkpoint（60G），汇报 dose-response 数据
- cutoff_25k_s2 / reverse_cutoff_s2 完成（~5h）→ eval → 3rd seed 确认 withdrawal 效应
- cutoff_45k_s1 完成（~9h）→ eval → dose-response 曲线最后数据点
- 所有 eval/CKA/gradient 分析完成 → 更新 ROADMAP，评估是否具备 CoRL abstract 提交条件

### 5. 🎯 战略上下文
- **CoRL 2026**：Abstract DDL May 26（今天/明天），Paper DDL May 29
- **核心叙事**：Dual mechanism — BN interference（表征层面 ~56%）+ gradient flow absence（行为层面 ~44%），representation-behavior dissociation 是核心亮点
- **Framing**：分析论文（Option B），非方法论文。"BN interference" 是单方向效应（仅在无梯度流时有害），不是 crossover
- **决策链**：D034（dual mechanism）→ D035（representation-behavior dissociation）→ D036（gradient orthogonality）→ D037（differential encoder vulnerability）→ D043（crossover 假说）→ D044（撤回 crossover）
- **易错点**：
  1. s0 CKA outlier（DINOv2=0.640）不要用来支持任何 claim，这是种子噪声
  2. Full OCC vs Vanilla 差异 +1.7pp 不显著，用 "comparable/maintains" 不用 "improves"
  3. cutoff 实验的实现是 weight=0 但 forward pass 未停止 = 后半段是 Detach 模式（BN 干扰仍在），不是 Vanilla
  4. Agent 队列容易堆积，注意检查 depth 再发消息，必要时用 replace_agent_queue 合并


---
