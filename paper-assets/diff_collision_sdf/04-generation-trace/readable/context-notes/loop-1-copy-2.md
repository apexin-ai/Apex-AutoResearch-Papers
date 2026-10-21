# agent / loop_1.md

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_1.md`
- **Structured JSON:** [`0369aef55d075e3e1093.json`](../../sessions/03/0369aef55d075e3e1093.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 1
reason: max_wall_time
updated: '2026-05-21T17:33:47+00:00'
---

### 1. 🔴 硬约束 / 红线
- westd-35807 只能用 cuda:0/1/2/3，westd-45947 只能用 cuda:0/1（gpu_ids 白名单）
- submit_training_job 有 24h timeout (EXIT_CODE=124)，长训练必须用 tmux 直接启动（A3 已因此被 kill 3 次）
- Registry API 拒绝 DONE→RUNNING 转换，resume 场景必须直接 Edit registry.yaml
- eval_safelibero.py 参数名：--checkpoint（非 --checkpoint_path）、--suite（非 --scene）、--n_episodes（非 --max_episodes）、--save_dir（非 --output_dir）
- train_a1_sdf_aux.py 内部覆盖 CUDA_VISIBLE_DEVICES（M013），必须用 --gpu N 传 GPU 编号
- object_pudding 的 SDF GT 文件名是 sdf_gt_object_chocolate.npz（SCENE_CONFIG 映射表决定，不是文件名拼接）
- 两台服务器之间无直接 SSH，代码同步靠 base64 中转
- westd-35807 上的 lora_utils.py LoRALinear 还没有 weight/bias property 修复（只修了 westd-45947 的 train_a3_hook.py）

### 2. 🖥️ 基础设施快照
- **westd-35807**: 4× RTX PRO 6000 96GB
  - 工作目录: /root/colliforce-vla
  - Python: /root/miniconda3/bin/python, conda env: `libero`
  - 激活: `source /root/miniconda3/etc/profile.d/conda.sh && conda activate libero`
  - 数据: /root/autodl-tmp/colliforce_data/safelibero_spatial/ + safelibero_object/
  - Checkpoints: /root/autodl-tmp/checkpoints/
  - SDF GT: /root/colliforce-vla/colliforce/assets/sdf_gt_*.npz
  - 活跃进程:
    - cuda:0 — a1_lora_spatial_bowl_s0, PID 299910
    - cuda:1 — baseline_lora_spatial_bowl_s0, PID 281554
    - cuda:2 — a1_lora_object_pudding_s0, PID 292258
    - cuda:3 — baseline_lora_object_pudding_s0, PID 281629

- **westd-45947**: 2× RTX PRO 6000 96GB
  - 工作目录: /root/colliforce-vla
  - Python: /root/miniconda3/bin/python, conda env: `base`
  - 激活: `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
  - Checkpoints: /root/autodl-tmp/checkpoints/
  - 活跃进程:
    - cuda:0 — a3_gradient_spatial_bowl_s0, PID 191747, tmux `a3_spatial`, 日志 /tmp/spatial_bowl.log
    - cuda:1 — a3_gradient_object_pudding_s0, PID 165990, 日志 /tmp/object_pudding.log
  - A3 object_pudding best checkpoint: /root/autodl-tmp/checkpoints/a3_grad_refine_object_pudding/a3_grad_refine_object_pudding_seed0/best/ (best_loss 0.01439 @ step 26000)

- Eval 脚本: /root/colliforce-vla/scripts/eval_safelibero.py（两台服务器都有，已同步）
- eval_batch.sh + sweep_lambda.sh 已就绪

### 3. 📊 当前状态
刚处理完 A3 restart worker 回调并汇报 Director。

**Registry RUNNING 实验（6/6 满载）**:
| 实验 | 服务器 | GPU | Step/30K | ETA |
|------|--------|-----|----------|-----|
| a3_gradient_spatial_bowl_s0 | westd-45947 | cuda:0 | ~7900 (26%) | ~24.5h → 5/23 01:30 |
| a3_gradient_object_pudding_s0 | westd-45947 | cuda:1 | ~29250 (98%) | **~50 min → 即将完成** |
| baseline_lora_spatial_bowl_s0 | westd-35807 | cuda:1 | ~13K (44%) | ~19h |
| baseline_lora_object_pudding_s0 | westd-35807 | cuda:3 | ~13K (44%) | ~19h |
| a1_lora_spatial_bowl_s0 | westd-35807 | cuda:0 | ~9.6K (32%) | ~23h |
| a1_lora_object_pudding_s0 | westd-35807 | cuda:2 | ~13K (44%) | ~19h |

**已完成（success）**: baseline_spatial_bowl_s0_v2, baseline_object_pudding_s0_v2（full-FT baselines）

**等待中**: 无 pending Worker。A3 object_pudding cron 回调预计 ~50 min 内触发。

### 4. 📋 待办（条件触发式）
- A3 object_pudding cron 回调（训练完成）→ 在 westd-45947 cuda:1 启动 eval：`CUDA_VISIBLE_DEVICES=1 python scripts/eval_safelibero.py --model_type a3 --checkpoint /root/autodl-tmp/checkpoints/a3_grad_refine_object_pudding/a3_grad_refine_object_pudding_seed0/best --suite object_pudding --n_episodes 50 --save_dir /root/autodl-tmp/eval_results/a3_object_pudding --gpu 1` → eval 完成后接着跑 --no_refine 版本
- A3 object_pudding eval 启动后 → 同时在 westd-35807 跑 full-FT baseline object_pudding eval
- A3 spatial_bowl 训练完成（~24.5h）→ 同样流程 eval
- baseline_lora / a1_lora 完成（~19-23h）→ eval_batch.sh 批量评估
- westd-35807 lora_utils.py 需补 weight/bias property 修复（目前只 westd-45947 修了 train_a3_hook.py 里的 LoRALinear）——在 A1 eval 前必须修，否则 A1 eval 会崩

### 5. 🎯 战略上下文
- **核心目标**: MVP 验证 ColliForce-VLA，Pass/Fail 标准：A3 vs Baseline CAR 下降 ≥15%，TSR 下降 <10%
- **决策链**: D001 锁定 π0/openpi → D003 接受非 watertight SDF → D004 Phase B 启动 → D005 MVP 只需 1 seed → D006 kill 旧 A1（Phase 2 LoRA 解冻从未生效），释放 GPU 启动 LoRA baseline
- **A3 是最高优先级数据点**: object_pudding 即将完成，这是第一个可以做 A3 vs baseline 对比的场景
- **A1 Phase 2 已确认生效**: aux_metadata.pt 显示 phase=2（grep 日志因 tqdm \r 字符遮蔽而误报无输出）
- **M014 教训**: A1 旧版 Phase 2 LoRA 解冻从未生效（脚本未注入 LoRA 层），当前 a1_lora_* 用的是修复后的 lora_utils.py，Phase 2 已确认触发
- **易错点**: 
  - 不要用 submit_training_job 跑长训练（24h 超时会 kill）
  - cron 可能误报——A3 spatial 的旧 log 路径指向失败日志，实际进程日志在 /tmp/spatial_bowl.log
  - eval 参数名和训练参数名不同，已在第 1 节列出


---
