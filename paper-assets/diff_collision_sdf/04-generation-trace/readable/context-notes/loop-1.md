# director / loop_1.md

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_1.md`
- **Structured JSON:** [`70afa798ceefb0024713.json`](../../sessions/70/70afa798ceefb0024713.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 1
reason: max_messages
updated: '2026-05-21T17:32:11+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单（C001）：仅 westd-35807:cuda:0-3 + westd-45947:cuda:0-1，共 6 张
- A3 训练必须用 tmux 启动（C002）：禁止 submit_training_job，默认 24h timeout 不够（M013/M014，已三次超时失败）
- Checkpoint 目录隔离：不同实验配置必须用 --exp_name 区分，否则 SAVE_TOTAL_LIMIT=2 会互删 checkpoint（M015）
- 碰撞检测用 L1 norm（`np.sum(np.abs(delta))`），不是 L2，与 AEGIS/SafeLIBERO 标准一致
- eval_safelibero.py 参数名：--checkpoint（不是 --ckpt），--n_episodes（不是 --num_episodes），--suite（不是 --task）

### 2. 🖥️ 基础设施快照
- **westd-35807**（4× RTX PRO 6000 96GB）：工作目录 /root/colliforce-vla，Python /root/miniconda3/bin/python，conda base
  - Checkpoints: /root/autodl-tmp/checkpoints/
  - Eval results: /root/autodl-tmp/eval_results/
  - Eval scripts ready: /root/colliforce-vla/scripts/eval_batch.sh, sweep_lambda.sh
  - Full-FT baseline checkpoints（已完成）: baseline_spatial_bowl/…/best, baseline_object_pudding/…/best
- **westd-45947**（2× RTX PRO 6000 96GB）：同上路径结构
  - A3 spatial_bowl: PID 191747, tmux session（名称未知，可能是 a3_spatial），cuda:0，从 step 6000 resume，**registry 未更新**（仍显示 DONE/failed）
  - A3 object_pudding: PID 165984, cuda:1，step ~29500/30000，日志 /tmp/object_pudding.log，**即将完成**
  - A3 object_pudding checkpoint: /root/autodl-tmp/checkpoints/a3_grad_refine_object_pudding/a3_grad_refine_object_pudding_seed0/best
- 共享 LoRA 模块：/root/colliforce-vla/colliforce/lora_utils.py（所有方法统一使用）
- 文献 map：19 篇已填充，distill 待用户触发

### 3. 📊 当前状态
我刚处理完 Reviewer warning（registry 不一致 + A3 超时风险），添加了 C001/C002 约束，批准了 RESET_BOTH。

**RUNNING 实验（5 个）：**
| 实验 | 服务器:GPU | 进度 | ETA |
|------|-----------|------|-----|
| a3_gradient_object_pudding_s0 | westd-45947:cuda:1 | ~29500/30K (98%) | **<30 min** |
| a3_gradient_spatial_bowl_s0 | westd-45947:cuda:0 | ~8000/30K (27%)，tmux，**registry 未追踪** | ~24h |
| baseline_lora_spatial_bowl_s0 | westd-35807:cuda:1 | 13447/30K (45%) | ~18h |
| baseline_lora_object_pudding_s0 | westd-35807:cuda:3 | 13421/30K (45%) | ~18h |
| a1_lora_spatial_bowl_s0 | westd-35807:cuda:0 | 9935/30K (33%) | ~22h |
| a1_lora_object_pudding_s0 | westd-35807:cuda:2 | 11812/30K (39%) | ~20h |

**等待中：**
- A3 object_pudding 完成回调 → 第一次 MVP eval
- Agent 刚被 RESET，新 Agent 需要接手 eval 任务

### 4. 📋 待办（条件触发式）
- A3 object_pudding 完成（<30min）→ 在 westd-45947 cuda:1 跑 eval：先 A3 with refinement（50 ep），再 A3 no_refine（50 ep）；同时在 westd-35807 跑 full-FT baseline eval on object_pudding → 对比 CAR/TSR，做 MVP gate check
- MVP gate check 结果出来 → CAR ≥15% reduction + TSR <10% loss = PASS → complete_mvp() → 进入 post-MVP kickoff（paper_framing.md → experiment_plan.yaml → dream_simulate）
- MVP CONDITIONAL（CAR ≥15% 但 TSR 10-20%）→ 等更多数据点（spatial_bowl A3 + LoRA baselines）再判断
- MVP FAIL → 诊断原因，考虑 lambda_refine 调参或方法改进
- A3 spatial_bowl registry 未追踪 → 新 Agent 需要重新注册 PID 191747 或手动监控 tmux，确保完成时能触发 eval
- LoRA baselines / A1 LoRA 完成（~18-22h）→ 正式 MVP 全矩阵 eval（eval_batch.sh）

### 5. 🎯 战略上下文
- **项目核心**：ColliForce-VLA，将可微分 SDF 梯度注入 VLA 训练，让机器人生成碰撞感知动作。目标 CoRL 2026。
- **决策链**：D001 锁定 π0/openpi → D002 否决 OpenVLA-OFT → D003 接受非 watertight SDF → D004 Phase B 启动 → D005 MVP 只需 1 seed → D006 统一 LoRA（lora_utils.py），杀旧 A1 释放 GPU 给 LoRA baseline
- **方法三变体**：π0-LoRA（baseline，33.5M params）、ColliForce-Aux（A1，SDF auxiliary loss）、ColliForce（A3，SDF gradient refinement + aux loss）
- **竞品 AEGIS**：SafeLIBERO 上 CAR=77.85% avg（CBF+QP training-free）。我们的方法是 training-time 集成，论文 framing 走 Pareto front（lambda_refine sweep 展示可控 collision-success trade-off）
- **最容易判错的事**：A3 object_pudding eval 出来后，**不要只看 CAR 绝对值**，要看 A3 vs baseline 的 relative improvement（≥15% CAR reduction）。也不要忘记跑 --no_refine 版本——它隔离训练效果 vs 推理时修正效果，对论文 story 至关重要
- **易踩的坑**：(1) eval 参数名容易搞错（见红线），(2) westd-35807 上 4 个训练占满 GPU，baseline eval 要等有 GPU 空出或用 eval 和 training time-share（eval 短，可以临时抢），(3) A3 spatial_bowl 的 tmux 进程不在 registry 里，完成时不会自动触发回调，必须手动监控


---
