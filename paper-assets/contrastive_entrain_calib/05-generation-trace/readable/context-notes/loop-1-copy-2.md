# agent / loop_1.md

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_1.md`
- **Structured JSON:** [`d6e7e8b6e4edb7d7a872.json`](../../sessions/d6/d6e7e8b6e4edb7d7a872.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 1
reason: idle_timeout
updated: '2026-05-19T10:24:44+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：westd-29046: cuda:0, cuda:1 | westd-28034: cuda:0, cuda:1, cuda:2, cuda:3。白名单外禁止启动，即使 Director 指令也必须 push back
- westd-28034 无外网，HuggingFace 加载必须 `HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1`
- DeepSpeed 与 submit_training_job 的 CUDA_VISIBLE_DEVICES 冲突：命令必须 `unset CUDA_VISIBLE_DEVICES && deepspeed --include localhost:X,Y`
- 评估指标已统一（D027）：**废弃 WRR**，主报 ToF/NoF/SYCONScore（NLI-based），禁止再用 string matching 或报 WRR
- exp-002v3 需要 DeepSpeed ZeRO-2 双卡（单卡 ~64GB 不够），设计用 28034 GPU 0+3，但 GPU 0 当前跑 exp-004，**必须等 exp-004 完成后才能启动**

### 2. 🖥️ 基础设施快照
- **westd-29046**: 工作目录 `/root/contrastive_entrain_calib`，Python `/root/miniconda3/bin/python`（.bashrc 无 conda init，必须绝对路径）
- **westd-28034**: 同上，DeepSpeed `/root/miniconda3/bin/deepspeed`
- 模型缓存：28034 `/root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B`，29046 类似路径
- NLI 模型：`/root/.cache/huggingface/hub/models--cross-encoder--nli-deberta-v3-base/`
- d_syc 方向文件（正确版）：`/root/contrastive_entrain_calib/results/exp001/directions.pt`（181 对），**不要用** `output/directions.pt`（旧版 320 对，M016 假警报根因）
- 训练数据：`/root/mvp_v2_1_expanded/data/calibration_v2_1_expanded.jsonl`（362 samples）
- **活跃进程**：
  - exp-003: PID 70649, westd-29046 GPU 1, cron 监控中
  - exp-004: PID 18204, westd-28034 GPU 0, cron 监控中
  - exp-008v3: westd-28034 GPU 1+2 (DeepSpeed), cron 监控中
  - exp002v2-recalib: PID 172838, westd-29046 GPU 0, cron 监控中
- **活跃 Worker**: `worker_eval_exp016-actadd-unified-reeval`（exp-016 ActAdd 统一指标重评估）

### 3. 📊 当前状态
上一轮完成了：vanilla baseline eval（preset: ToF=0.818, NoF=0.663, SYCONScore=0.732）、exp-016 ActAdd 成功（α=5 NoF +8.8pp）、exp-008v3 部署、exp002v2-recalib 部署、D027 指标统一、exp-014 kill + eval（mode collapse confirmed）。

**RUNNING（4 个实验，6 张 GPU 满载）**：
| exp_id | 服务器/GPU | 进度 | ETA |
|--------|-----------|------|-----|
| exp-003 (R3-only GRPO) | 29046 GPU 1 | ~1714/8000 | ~May 21 |
| exp-004 (ACT baseline) | 28034 GPU 0 | ~5700/8000 | **~May 19 20:00（最先完成）** |
| exp002v2-recalib (cosine R1 + recalib) | 29046 GPU 0 | 刚启动 step ~510 | ~May 22 |
| exp-008v3 (Binary Probe GRPO) | 28034 GPU 1+2 | step ~10 | ~May 22 |

**等待中**：
- exp-016 统一指标重评估 Worker 运行中
- exp-002v3（PREPARING）：代码 + launch script 已就绪（`launch_exp002v3.sh`），等 28034 GPU 0（exp-004 完成后）+ GPU 3 释放
- exp-003-s2（PREPARING）：等 29046 GPU 空出

### 4. 📋 待办（条件触发式）
- **exp-004 cron 回调到达** → spawn Worker 跑完整 eval（多 checkpoint: 500/1000/2000/4000/8000），更新 registry，28034 GPU 0 释放后立即提交 exp-002v3（DeepSpeed GPU 0+3）
- **exp-016 reeval Worker 完成** → 整合统一指标到 registry，更新 report.md
- **exp-003 cron 回调** → eval + 与 exp002v2-recalib 对比（关键：如果两者 NoF 差异 <2pp，R1 cosine 信号确认无效，exp-002v3 scaling 成为唯一 cosine 救命稻草）
- **exp-008v3 cron 回调** → eval，与 exp-003 和 vanilla 对比。如果 binary probe > R3-only，Story B 成立
- **exp002v2-recalib 回调** → 与 exp-003 对比，判断 recalibration 是否解决了 R1 drift 问题
- **Director venue 决策** → 如果确认冲 May 25 EMNLP，需要极度紧凑的写作计划；如果推迟到 ARR August，节奏可放宽

### 5. 🎯 战略上下文
**核心问题**：cosine R1 信号太弱（仅占 combined reward 8%），当前跑的 exp002v2-recalib 大概率和 exp-003 (R3-only) 无差异。项目命运取决于：
1. **exp-002v3**（scaled cosine，scale_factor=5）能否让 R1 产生差异 → 验证 Story A
2. **exp-008v3**（binary probe GRPO）能否优于 R3-only → 验证 Story B（备选主线）

**双线 narrative 策略**（Director+Reviewer 已确认）：无论 cosine scaling 成败，binary probe 路径都可以撑起论文。两条线都支撑"direction information matters"核心贡献。

**易错点**：
- 不要把 `output/directions.pt` 当成当前方向文件，那是旧版（M016 教训）
- exp-014 的 mode collapse 不是方法失败，是 continuous probe 被 adversarial gaming 的证据——这是论文正面素材
- Probe gaming 是原创实证贡献（文献调研确认无先例），务必保留在论文叙事中
- exp-004 可能过拟合（step 850 后 SFT loss 归零），eval 需要看多个 checkpoint 不能只看最终
- EMNLP May 25 DDL 极度紧张（6 天），核心实验 May 22 才完成，用户尚未决定是否冲这一轮


---
