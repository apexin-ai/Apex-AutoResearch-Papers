# reviewer / loop_2.md

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_2.md`
- **Structured JSON:** [`19fa4e37519ea19a57aa.json`](../../sessions/19/19fa4e37519ea19a57aa.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 2
reason: max_wall_time
updated: '2026-05-21T18:15:07+00:00'
---

### 1. 🔴 硬约束 / 红线
- westd-35807: cuda:0(A1 spa), cuda:1(baseline LoRA spa), cuda:2(A1 obj), cuda:3(baseline LoRA obj) — 不可越界
- westd-45947: cuda:0(A3 spatial), cuda:1(已空闲，A3 obj完成) — A3 spatial 用 cuda:0，eval 可用 cuda:1
- A3 object_pudding registry 标记 failed 是 **false positive**（EXIT_CODE=124 timeout），训练实际已完成 30000/30000。已报 Director，等待修正。不要二次报告同一问题。
- constraints.yaml 为空——无法做 L1 #4 GPU 白名单检查，已建议 Director 配置

### 2. 🖥️ 基础设施快照
- **westd-35807**: 4× RTX PRO 6000 96GB, `/root/colliforce-vla`, conda env `libero`, python `/root/miniconda3/envs/libero/bin/python`
- **westd-45947**: 2× RTX PRO 6000 96GB, `/root/colliforce-vla`, conda env `base`, python `/root/miniconda3/bin/python`
- 模型权重: `/root/autodl-tmp/openpi_weights/pi0_base/model.safetensors`
- Checkpoints: `/root/autodl-tmp/checkpoints/{exp_name}/{exp_name}_seed0/`
- A3 obj_pudding 完成 checkpoint: `/root/autodl-tmp/checkpoints/a3_grad_refine_object_pudding/a3_grad_refine_object_pudding_seed0/` (30000, 29999, best)
- A3 spatial 活跃: PID 191747, tmux session `a3_spatial`, log `/tmp/spatial_bowl.log`（log 文件是快照不实时更新，用 checkpoint 目录判断进度）
- WANDB_MODE=offline/disabled（全部实验）
- Eval 脚本就绪: `eval_batch.sh` + `sweep_lambda.sh`

### 3. 📊 当前状态
**刚做完**：确认 A3 object_pudding 训练完成（false positive timeout），发 CRITICAL 给 Director 要求修正 registry + 启动 eval。

**RUNNING 实验**：
| exp_id | server:gpu | step | ETA |
|--------|-----------|------|-----|
| a3_gradient_spatial_bowl_s0 | 45947:0 | ~8000/30K | May 23 ~01:30 UTC |
| a1_lora_spatial_bowl_s0 | 35807:0 | ~10K/30K | ~22h |
| baseline_lora_spatial_bowl_s0 | 35807:1 | ~13.5K/30K | ~18h |
| a1_lora_object_pudding_s0 | 35807:2 | ~12K/30K | ~20h |
| baseline_lora_object_pudding_s0 | 35807:3 | ~13.5K/30K | ~18h |

**等待中**：Director 修正 A3 obj_pudding registry + 启动 eval（GPU 1 on westd-45947 已空闲）

### 4. 📋 待办
- Director/Agent 修正 registry 并启动 eval → 审查 eval 结果（CAR ≥15%? TSR <10%?）= MVP gate
- A3 spatial checkpoint 8000 出现 → 确认进程正常推进（之前 checkpoint 停滞引起过误判）
- A3 spatial 完成 → 第二个 A3 数据点，强化 MVP 结论
- baseline_lora 完成 → A1/A3 对比的 fair baseline 就位
- 任何实验 registry 再次触发 timeout → 先查 log 尾部确认是否 false positive（本次教训）

### 5. 🎯 战略上下文
- **MVP gate**: CAR ≥15% reduction + TSR <10% loss = PASS。A3 obj_pudding 是第一个数据点。
- **决策链**: D001(锁定 π0) → D004(Phase B 启动) → D005(暂停 s1) → D006(停旧 A1，启 LoRA baseline)
- **易错点**：
  1. submit_training_job 的 24h timeout 不杀 tmux 进程——registry "failed" ≠ 训练真的失败，必须查 log 尾部
  2. A3 spatial log `/tmp/spatial_bowl.log` 是静态快照，不是实时更新。用 checkpoint 目录时间戳判断进度更可靠
  3. A3 spatial 进度条从 step 0 开始（`--resume` 传了但 checkpoint 曾为空），这是 from-scratch 训练不是 resume
  4. A3 obj_pudding best_loss=0.01439 at step 26000，eval 建议用 best checkpoint 而非 final（final 略 overfit）
  5. 6 个实验中只有 A3 用 conda base + python 3.12；其他全用 conda libero + python 3.10——环境不要搞混


---
