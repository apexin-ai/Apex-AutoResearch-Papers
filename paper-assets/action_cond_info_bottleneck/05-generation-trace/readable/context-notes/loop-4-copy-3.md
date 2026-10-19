# reviewer / loop_4.md

**action cond info bottleneck** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_4.md`
- **Structured JSON:** [`cc856241f83d640fa185.json`](../../sessions/cc/cc856241f83d640fa185.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 4
reason: max_wall_time
updated: '2026-05-16T13:42:27+00:00'
---

### 1. 🔴 硬约束 / 红线
- 服务器 westb-13953 只有 2 块 GPU (cuda:0, cuda:1)，无白名单限制但只有这两块
- v7 全程训练占 cuda:0 (PID ~960110)——不得 kill，这是当前唯一正向实验
- cross_task_probe.py 运行需加载完整 VLM (~6GB)，必须指定 --device cuda 到空闲 GPU
- cron 误报模式：wrapper PID 死→cron 报 failed→但训练子进程存活——已发生 4 次，不要盲信 registry "failed" 状态
- contrastive loss 实现有 cos-sim 零梯度 bug（losses.py 原版），已修为 log-barrier；如果看到 ctr=1.0000 恒定不动 = 旧 bug 未修

### 2. 🖥️ 基础设施快照
- 服务器：westb-13953 (root)，工作目录 `/root/acib`
- Python：`/root/miniconda3/bin/python3`（conda base 环境）
- 模型：`lerobot/smolvla_libero`（HF cache `/root/autodl-tmp/.hf_cache`）
- 数据集：`/root/autodl-tmp/libero_dataset`（273K frames）
- 训练输出：`/root/acib/outputs/acib_v7_contrastive/`
- 训练日志：`/root/runs/action_cond_info_bottleneck/acib_v7_contrastive.log`
- Baseline 结果：`/root/acib/outputs/baseline_std_v3/`（4 suites done）、`/root/acib/outputs/baseline_plus_v2/`（4 suites done）
- v6 checkpoint-20000 (完成)：`/root/acib/outputs/acib_v6_conditioned/checkpoint-20000/`
- Eval 脚本已更新 dtype fix：`/root/acib/scripts/eval_acib.py` line 141
- v7 eval wrapper：`/root/acib/scripts/run_v7_eval.sh`（worker 已准备）
- WandB: project `acib_mvp`，run name `acib_v7_contrastive_logbarrier`

### 3. 📊 当前状态
**v7 全程训练 RUNNING** (step ~5700/20000, 1.8 steps/s, ~2.2h elapsed, ~2.4h remaining)。β=0.01 已稳定，ctr≈1.2-1.9 (implied cos≈0.70-0.84)——conditioning 存活。checkpoint-5000 已保存但 **Probe A 未运行**（GPU 1 空闲可跑）。

**GPU 1 空闲**——应立即分配给 Probe A on ckpt-5000 或 v5 eval (dtype fix)。

Registry 无 RUNNING 实验（v7 未被注册为 RUNNING——诊断 worker 的遗留问题）。

**已完成 baseline 汇总**：
- baseline_std: spatial=66.0%, object=67.8%, goal=76.4%, libero_10=54.2%, avg=66.1%
- baseline_plus: spatial=81.6%, object=88.8%, goal=87.8%, libero_10=67.2%, avg=81.35%

### 4. 📋 待办（条件触发式）
- v7 checkpoint-5000 存在 + GPU 1 空闲 → 立即运行 Probe A (`cross_task_probe.py --checkpoint_dir .../checkpoint-5000 --device cuda` on CUDA_VISIBLE_DEVICES=1)
- v7 Probe A step 5000 cos < 0.85 → conditioning 确认存活，继续等 step 10000/20000
- v7 Probe A step 5000 cos > 0.9 → conditioning 退化，建议 kill + 提高 lambda_contrastive 到 0.3-0.5
- v7 训练完成 (step 20000) → 立即启动 4-suite standard SR eval (`run_v7_eval.sh`) + perturbation eval
- v7 standard SR eval 结果出 → 对比 baseline_std (66.1%)，regression > 2pp = warning
- GPU 1 持续空闲 → 建议并行跑 v5 eval (ckpt-10000, dtype fix 已��入，需 `CUDA_VISIBLE_DEVICES=1`)
- Worker 报 v7 "failed" → 先查日志 + nvidia-smi 确认是否 wrapper 死亡误报（第 5 次了）

### 5. 🎯 战略上下文
**决策链核心**：v5 (position prior, cos=1.0) → v6 (architecture fix, cos=0.9999, training dynamics 失败) → v7 cos-sim (零梯度 bug) → **v7 log-barrier λ=0.1 (cos=0.70, 首次成功)**。

**论文 framing**：ACIB 作为 data-aug 的互补 IB-grounded regularizer (D006)。需证明在 smolvla_libero_plus 基础上仍有增益（尚未实验）。

**最易判断错的事**：
1. 不要把 v7 sweep 结果 (step 500, β=0) 外推为全程训练效果——β warmup 后 scorer_mean 从 0.08-0.35 恢复到 0.27-0.34，分布完全不同
2. ctr 数值不是 cosine similarity——它是 -log(1-cos+ε)，ctr=1.2 对应 cos≈0.70
3. v8 FiLM 单独跑无效 (cos>0.999)——问题在 loss signal 不在架构。FiLM+contrastive 组合即 v7 当前配置 (`conditioning_mode: "film"`)
4. baseline_plus libero_10=67.2% 看似不高但这是最难 suite，baseline_std 只有 54.2%
5. CoRL abstract 5/26 (10天), paper 5/29 (13天)——v7 训练~今天完成，eval 需 ~14h，时间紧但够用


---
