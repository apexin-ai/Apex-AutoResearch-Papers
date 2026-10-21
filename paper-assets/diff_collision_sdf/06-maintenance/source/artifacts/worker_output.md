# 诊断: eval_a3_object_pudding_no_refine 反复失败

## 失败根因

**Eval进程未在tmux中运行，SSH会话断开/超时后进程收到SIGHUP被静默杀死。** 训练任务 `a3_spatial_bowl` 正确地运行在tmux session `a3_spatial` 中（PID 191747→PPid 191741 bash in tmux），但所有eval进程都是裸SSH启动，无持久化保护。

## 关键证据

1. **日志无错误信息** — 所有3份日志（v1/v5/v8）均在运行中突然截断，无stack trace、无CUDA error、无OOM
2. **dmesg无OOM记录** — 排除内核级内存不足杀进程
3. **tmux只有一个session** — `a3_spatial: 1 windows`，没有eval的session
4. **v5运行了14分钟到Episode 10/50后被杀** — 与SSH工具超时窗口吻合
5. **eval进程已全部死亡** — `ps aux | grep eval_safelibero` 无结果，`/proc/253116` 不存在

## 次要问题：GPU分配错误

- 训练占GPU 0（`CUDA_VISIBLE_DEVICES=0`，24GB VRAM，100% utilization）
- eval未指定GPU，默认也跑GPU 0
- **GPU 1完全空闲**（1MiB/97GB, 0% utilization）

## 关键日志摘录

```
# v5: 正常运行到Episode 10后被杀（无后续输出）
2026-05-22 03:46:16,060 [INFO] Loading policy (model_type=a3)...
2026-05-22 03:47:07,246 [INFO] Setting up SafeLIBERO benchmark: safelibero_object (level II)
2026-05-22 04:00:50,991 [INFO]   Episode 10/50: success=False, collided=True, steps=300, sdf_min=1.4158, refined=0
# === 日志在此截断，无任何错误信息 ===

# tmux sessions:
a3_spatial: 1 windows (created Fri May 22 01:12:18 2026)
# 无eval session

# nvidia-smi:
GPU 0: 32567MiB/97887MiB, 100% util  ← training + eval挤在一起
GPU 1:     1MiB/97887MiB,   0% util  ← 完全空闲
```

## 建议修复方案

```bash
# 在tmux中启动eval，使用空闲的GPU 1
tmux new-session -d -s eval_no_refine
tmux send-keys -t eval_no_refine "cd /root/colliforce-vla && CUDA_VISIBLE_DEVICES=1 python scripts/eval_safelibero.py \
  --model_type a3 \
  --checkpoint /root/autodl-tmp/checkpoints/a3_grad_refine_object_pudding/a3_grad_refine_object_pudding_seed0/best \
  --suite safelibero_object \
  --sdf_gt_path /root/colliforce-vla/data/sdf_gt_object_chocolate.npz \
  --n_episodes 50 \
  --no_refine \
  2>&1 | tee /root/autodl-tmp/eval_results/a3_object_pudding_no_refine_v9.log" Enter
```

## 附注

- 姐妹实验refine版已完成（task1, 50 episodes），结果 TSR=0, CAR=0（collision_step=0，碰撞发生在第0步）
- no_refine v5的10个已完成episode也全部 success=False, collided=True — 策略本身表现也很差，但这是独立于进程被杀的问题
