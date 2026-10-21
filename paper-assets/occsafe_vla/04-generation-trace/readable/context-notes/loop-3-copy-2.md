# agent / loop_3.md

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_3.md`
- **Structured JSON:** [`5782014995f9451736b6.json`](../../sessions/57/5782014995f9451736b6.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 3
reason: idle_timeout
updated: '2026-05-25T06:52:39+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：westd-10894:cuda:0-3 + westd-34685:cuda:0-3，共 8 张，不可用其他
- westd-34685 eval 时 `MUJOCO_EGL_DEVICE_ID` 必须与 cuda 编号一致（cuda:2→DEVICE_ID=2）
- 训练命令必须用 `submit_training_job`，禁止 nohup；eval 也走 submit_training_job
- conda 环境名 `occsafe`（westd-34685）；激活方式 `source /root/miniconda3/etc/profile.d/conda.sh && conda activate occsafe`
- Checkpoint 目录名格式固定：`openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--50000_chkpt`，用 ls 确认实际名称再引用
- CoRL 2026 deadline: Abstract May 26（明天）, Paper May 29（4天）

### 2. 🖥️ 基础设施快照
- **westd-34685**: 工作目录 `/root/occsafe_vla/openvla-oft`，数据 `/root/autodl-tmp/data/modified_libero_rlds/`，模型 `/root/autodl-tmp/models/openvla-7b`，checkpoint 根目录 `/root/autodl-tmp/checkpoints/`，occ 数据 `/root/occsafe_vla/occ_data`，日志 `~/runs/occsafe_vla/`，磁盘余量充裕（879G 用 2%）
- **westd-10894**: 同样结构，磁盘 879G 用 50%
- Python: `/root/miniconda3/bin/python`，conda env: `occsafe`
- W&B: 项目配置中自动读取 entity/project

### 3. 📊 当前状态
**刚做完**：收到 `cutoff_25k_s1` 和 `reverse_cutoff_s1`（训练）完成回调。已派 Worker `worker_ops_verify_and_eval_cutoff25k_reverse_s1_20260524T145043` 去验证 checkpoint 并提交两个 eval job（cuda:2 cutoff_25k_s1_eval, cuda:3 reverse_cutoff_s1_eval）。

**RUNNING 实验**（等回调）：
| exp_id | 服务器:GPU | 用途 |
|--------|-----------|------|
| full_occ_ln_s0 | 10894:1 | 2×2 factorial 缺失格（LN+gradient flow）|
| full_occ_ln_s1 | 10894:2 | 同上 seed 2 |
| full_occ_ln_s2 | 10894:3 | 同上 seed 3 |
| ablation_occ_detach_s0_retrain | 10894:0 | same-seed 梯度重分析 |
| cutoff_15k_s1 | 34685:1 | dose-response 15K seed 43 |
| cutoff_45k_s1 | 34685:0 | dose-response 45K seed 43 |

**等待中**：
- Worker `worker_ops_verify_and_eval_cutoff25k_reverse_s1` 回调 → 确认 eval 已提交
- cutoff_25k_s1_eval / reverse_cutoff_s1_eval cron 回调 → 分析 CAR 并汇报 Director
- cutoff_15k_s1 / cutoff_45k_s1 完成 → 同样流程：验证 → eval → dose-response 曲线

### 4. 📋 待办（条件触发式）
- Worker 回调到达 → 确认 cutoff_25k_s1_eval + reverse_cutoff_s1_eval 已启动，GPU 34685:2/3 满载
- cutoff_25k_s1_eval 完成 → 与 s0 (CAR=0.688) 对比，更新 2-seed 均值，写入 dose-response 表
- reverse_cutoff_s1_eval 完成 → 与 s0 (CAR=0.700) 对比，确认 withdrawal 效应跨 seed 一致性
- cutoff_15k_s1 完成 → 验证 + 提交 eval（s0 CAR=0.804，这个数据点很关键——如果 s1 也高则非单调 dose-response 是真实的）
- cutoff_45k_s1 完成 → 验证 + 提交 eval（s0 CAR=0.764）
- full_occ_ln ×3 全部完成 → eval → 填完 2×2 factorial 表，这是论文 BN vs LN × gradient flow 的核心证据
- ablation_occ_detach_s0_retrain 完成 → 4-condition same-seed 梯度分析（Vanilla/Full OCC/Detach+LN/Detach BN 各 s0）
- 所有 dose-response + 2×2 factorial 完成 → 向 Director 汇报完整结果，推进论文写作

### 5. 🎯 战略上下文
- **核心发现 (D037)**：Dual mechanism — BN interference + gradient flow absence。SigLIP late-layer "double jeopardy"（cooperative alignment 被破坏）vs DINOv2 purely orthogonal 更耐受
- **Framing**：分析论文，"representation-behavior dissociation + differential encoder vulnerability"
- **条件排序已明确**：Full OCC (0.797) > Random OCC (0.789) > Vanilla (0.780) > Detach+LN (0.765) > Detach (0.746) > reverse_cutoff (0.700) > cutoff@25K (0.688)
- **关键待验证**：cutoff_15k_s0 CAR=0.804 比 Full OCC 还高——如果 s1 复现，dose-response 是非单调的（U 形），这对叙事有重大影响。不要假设一定是 seed variance
- **易错点**：
  - cutoff 实验的 `occ_loss_cutoff_mode` 有 `after`（cutoff 后停止 occ loss）和 `before`（cutoff 前不用 occ loss）两种，reverse_cutoff 用的是 `before`
  - eval 日志文件名和 registry log_path 可能不一致（之前出现过 v2/v3 后缀），以 registry 中的 log_path 为准
  - 10894 和 34685 的 conda env 都叫 `occsafe`，但不要假设其他包版本完全一致


---
