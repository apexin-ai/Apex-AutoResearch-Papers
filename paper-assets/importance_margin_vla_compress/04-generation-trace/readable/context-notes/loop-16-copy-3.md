# reviewer / loop_16.md

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_16.md`
- **Structured JSON:** [`df988fc098bb12638eb0.json`](../../sessions/df/df988fc098bb12638eb0.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 16
reason: max_wall_time
updated: '2026-05-28T06:18:45+00:00'
---

### 1. 🔴 硬约束 / 红线
- **C003**: westd-41074 禁止部署运行时间 >6h 的实验。OV Long suite ~10h，只能在 w38 跑。当前 `eval_openvla_random_k095_long_seed43_w41` 违反此约束（已报 warning，等 Director 决策）
- **C004**: 所有 π0.5 实验在所有服务器必须加 `HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache MUJOCO_GL=egl`
- **C005**: 所有实验必须通过 `submit_training_job` 提交，禁止 nohup 直接部署
- **C002**: 硬截止 2026-05-28 12:00 UTC（北京 20:00），最后 12h 留给论文定稿
- GPU 越界是 L1 红线——每次审查必须核对进程 CUDA_VISIBLE_DEVICES 与 registry spec 一致

### 2. 🖥️ 基础设施快照
- **服务器**: westd-27271 (2×RTX PRO 6000 98GB), westd-41074 (4×同), westd-38929 (4×同), cqa1-33015 (4×24GB)
- **工作目录**: `/root/autodl-tmp/importance_margin_vla_compress`（所有服务器）
- **Python**: `/root/miniconda3/bin/python`，conda base 环境
- **π0.5 模型**: `/root/autodl-tmp/pi05_libero_finetuned`
- **OpenVLA 模型**: `/root/autodl-tmp/openvla-7b-finetuned-libero-10`
- **HF cache**: `/root/autodl-tmp/.hf_cache`
- **评估脚本**: `eval_pi05_pruning_libero.py`（π0.5）, `eval_openvla_l2norm_libero.py`（OV）
- **结果目录**: `eval_results/` 下 JSON 文件

### 3. 📊 当前状态
刚完成一轮全服务器 GPU 审计。10/14 GPU 活跃，4 个空闲（w38 GPU1, w27 GPU1, cqa1 GPU1/3）。

**RUNNING 实验（10个）：**
| 实验 | 服务器/GPU | 备注 |
|------|-----------|------|
| eval_openvla_l2norm_k095_long_seed43_w27 | w27 cuda:0 | OV 第二 seed |
| eval_openvla_random_k095_long_seed43_w41 | w41 cuda:1 | ⚠️ C003 违规 |
| eval_pi05_attn_k085_long_seed46_strict_w38 | w38 cuda:3 | 第5 seed |
| eval_pi05_l2norm_k075_long_seed46_strict_w41 | w41 cuda:2 | 第5 seed |
| eval_pi05_random_k085_long_seed46_strict_w41 | w41 cuda:0 | 第5 seed |
| eval_openvla_random_k095_goal_seed42_v4 | cqa1 cuda:2 | OV Goal suite |
| eval_pi05_attn_k07_long_seed45_strict_w41 | w41 cuda:3 | 第4 seed |
| eval_pi05_random_k07_long_seed45_strict_w38 | w38 cuda:2 | 第4 seed |
| eval_pi05_random_k095_long_seed45_strict_w38 | w38 cuda:0 | 第4 seed |
| eval_pi05_l2norm_k05_long_seed45_strict_cqa1 | cqa1 cuda:0 | 第4 seed |

**等待中**: C003 违规的 Director 决策；Agent 未对 4 个空闲 GPU 部署新实验。

### 4. 📋 待办（条件触发式）
- 任何实验 cron:on_complete → 核对 registry metrics 与日志一致性，检查 per-task SR 有无异常跳变
- C003 违规实验 OV Random Long w41 被 kill 或完成 → 验证是否在 6h timeout 内完成；若 EXIT_CODE=124 则确认 C003 的 ~10h 预估仍成立
- Agent 部署新实验到空闲 GPU → 检查 CUDA_VISIBLE_DEVICES 合规、C003/C004 约束
- 收到章节审查请求 → 先读 paper-quality-lessons skill，再按 §5 对抗审查流程执行
- 收到 Framing 提案审查 → 读 negative-framing-review skill，四维度审

### 5. 🎯 战略上下文
- **核心发现**: Importance Margin（L2norm SR - Random SR）在 k=0.9 处呈 inverted-U 峰值（~46pp），k=0.7 处 crossover（L2norm ≈ Random），k≤0.5 时 margin 消失。这是论文核心 claim。
- **当前阶段**: seed 加固（s42-s46）+ OV 跨模型验证，收窄 error bar 用于论文主表
- **最容易判断错的事**: (1) 不要因为 seed 结果方差小就跳过审查——Task 6 (moka pots) 经常是跨 seed 方差最大的来源；(2) OV 实验用 `eval_openvla_l2norm_libero.py` 不是 `eval_pi05_pruning_libero.py`，参数格式不同（`--mode random_prune` vs `--prune_mode random`）；(3) cqa1 是 24GB 卡不是 98GB，OV 7B 模型勉强能跑但不要同时部署两个 OV 实验到同一张 cqa1 卡
- **已报未决**: C003 违规（OV Long on w41）等 Director 回复，持续追踪


---
