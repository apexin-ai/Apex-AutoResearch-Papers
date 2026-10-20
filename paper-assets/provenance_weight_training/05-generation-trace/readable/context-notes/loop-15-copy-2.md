# agent / loop_15.md

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_15.md`
- **Structured JSON:** [`4b92bec1f58e359ad3aa.json`](../../sessions/4b/4b92bec1f58e359ad3aa.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 15
reason: max_wall_time
updated: '2026-05-17T11:19:24+00:00'
---

### 1. 🔴 硬约束 / 红线
- westd-41312 GPU 白名单: cuda:0,1,2,3。westd-30476 GPU 白名单: cuda:0,1,2,3
- M003: 训练脚本绝对禁止 --eval_steps / --eval_data_path（post-hoc eval 用 eval_perplexity.py）
- WANDB_MODE=disabled（所有实验）
- output_dir 必须 /root/autodl-tmp/output/models/（不是 /dev/shm/，后者是 RAM disk 重启丢失）
- westd-47453 已永久下线，不要尝试连接
- nvidia-smi 禁止在 cron/诊断中使用（曾导致 D-state 堆积引发 SSH 池耗尽+cron 误标 failed）
- submit_on_allocated 需要 tmux（30476 刚装好）+ 顶层 server/gpu/account 字段（不只是 spec 内）
- GPU 编号始终从 0 开始（框架注入 CUDA_VISIBLE_DEVICES）

### 2. 🖥️ 基础设施快照
**westd-41312**:
- 工作目录: /root/provenance_weight_training/
- Python: /root/miniconda3/bin/python (conda base)
- 模型: /root/autodl-tmp/models/Qwen3-0.6B, unsloth/Llama-3.2-3B (HF cache)
- 数据: /root/provenance_weight_training/data/scored_data.jsonl (371499条, ρ=0.4)
- 活跃: llama3b_uniform (cuda:0, PID 3112), llama3b_adaptive (cuda:1, PID 4005), grid_b0_2 (cuda:3, PID 45224), cuda:2 待 batchsize16_nmin8_r2

**westd-30476**:
- 工作目录: /root/provenance_weight_training/
- Python: /root/miniconda3/bin/python (conda base)
- 模型: /root/autodl-tmp/models/Qwen3-0.6B（之前 scp 导致 triple underscore，已 mv 修复）
- 数据: scored_data.jsonl + scored_data_rho02.jsonl + scored_data_rho06.jsonl
- **Transformers 版本问题**: 装了 5.8.1 导致全部 4 实验崩溃，worker 正在降级到 4.57.6
- 活跃: 全部 4 实验已崩溃待重启（bs8_auto_nmin_r2 cuda:1, batch_adaptive_tau_rho06_r2 cuda:2, rho02_adaptive_tau09_r2 cuda:3, random_reweight_seed123 cuda:0）

### 3. 📊 当前状态
**正在做**: 
- Worker `worker_ssh_fix_transformers_30476_20260517T111824` 正在降级 transformers 到 4.57.6 + 验证环境
- Worker `worker_ssh_prepare_batchsize16_41312_20260517T111722` 正在 41312 上准备 batchsize16_nmin8_r2 脚本

**Registry RUNNING**（但 30476 的 4 个实际已崩溃需重启）:
- bs8_auto_nmin_r2 (30476:cuda:1) — 崩溃，待重启
- batch_adaptive_tau_rho06_r2 (30476:cuda:2) — 崩溃，待重启
- rho02_adaptive_tau09_r2 (30476:cuda:3) — 崩溃，待重启
- random_reweight_seed123 (30476:cuda:0) — 崩溃，待重启
- llama3b_uniform_seed42 (41312:cuda:0) — 正常运行
- llama3b_adaptive_seed42 (41312:cuda:1) — 正常运行
- grid_b0_2_seed42 (41312:cuda:3) — 90% 完成，含 inline eval，ETA ~2h

**PENDING**: batchsize16_nmin8_r2 (41312:cuda:2) — 审批卡已发

### 4. 📋 待办
- worker_ssh_fix_transformers_30476 完成 → 将 4 个 30476 实验 registry 改回 ALLOCATED → submit_on_allocated 重启全部
- worker_ssh_prepare_batchsize16_41312 完成 + 审批通过 → QUEUED → ALLOCATED → submit_on_allocated
- grid_b0_2 cron 回调 (完成) → spawn eval worker (eval_perplexity.py sliding window) → 与 grid_b0_1(17.657)/b0_3(17.640)/b0_5(17.651) 对比 → 汇报 Director → cuda:3 释放后启动 grid_b0_3_seed456
- llama3b_uniform/adaptive 完成 → post-hoc eval → cross-model generalization 结果汇报（核心 paper claim）
- 30476 重启成功后确认进程存活（几分钟后 check log tail 看 step 推进）

### 5. 🎯 战略上下文
- 核心 narrative: provenance signal (detector score) 是 load-bearing 的，random reweight 降低 PPL 证明信号方向正确
- random_reweight_v2 已完成: PPL=17.830 > uniform(17.688)，hypothesis validated（seed42）
- random_reweight_seed123 是 cross-seed 复现（seed123），pass criteria: PPL > 17.688
- D062 coupling rule: n_min=max(2,bs//2)，batchsize16_nmin8_r2 是关键验证点
- llama3b 实验是 cross-model generalization claim 的支柱，结果很重要
- 易错点: 30476 重启时 registry 状态需要从 RUNNING 回退到 ALLOCATED 再 submit——直接 submit_on_allocated 不接受 RUNNING 状态。可能需要直接编辑 registry.yaml 文件或用 conclusion=failed → 创建新 entry
- 易错点: submit_on_allocated 需要顶层 server/gpu/account 字段，不只是 spec 内的
- τ default formula: pretrain_weighted.py:288 有 τ=1-ρ*0.5 bug，提交前必须改为 fixed τ=0.8（已记录在 memory）


---
