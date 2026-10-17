# 诊断报告: X-VLA Random Goal seed43 三连崩溃

## 结论

**Root cause: 外部信号杀死进程（SIGHUP），非代码 bug。** 三次运行均在裸 SSH 会话中启动（未使用 tmux），SSH 断开时进程被 SIGHUP 杀死。

## 时间线

| 版本 | 启动时间 | 死亡时间 | 运行时长 | 到达位置 | 日志行数 |
|------|---------|---------|---------|---------|---------|
| v1 | 04:54:18 | 05:17:37 | ~23 min | Task 5 Ep 18 | 304 |
| v2 | 05:45:14 | 05:47:26 | ~2 min | Task 0 Ep 33 | 59 |
| v3 | 06:18:56 | 06:22:25 | ~3.5 min | Task 1 Ep 4 | 81 |

## 关键证据

### 1. 无 traceback、无错误信息
三个版本的日志均干净截断，最后一行都是正常的 `Ep X/50 | SUCCESS/FAIL` 输出。没有 Python exception、没有 CUDA error、没有 segfault。这是外部 SIGKILL/SIGHUP 的典型表现。

### 2. 崩溃位置不一致
用户以为都在 ~ep33 崩溃，实际：
- v1 跑了 269 个 episode（到 Task 5）
- v2 跑了 33 个 episode（Task 0 Ep 33）
- v3 跑了 54 个 episode（Task 0 完整 + Task 1 Ep 4）

不是同一位置崩溃，排除了特定 episode/task 触发 bug 的可能。

### 3. 死亡时间与新实验启动高度相关
- v2 死于 05:47:26 → 05:48 新一批 tmux 实验启动（l2norm goal/object/long on GPU 0/1/2）
- v3 死于 06:22:25 → 06:24 spatial 实验启动（GPU 3）

推测：操作者（或自动化系统）断开旧 SSH 会话启动新实验，附带杀死了正在运行的 goal 进程。

### 4. 对比：同服务器其他实验正常
当前正在运行的 4 个实验全部使用 tmux 会话，运行稳定（已 38+ 分钟）：
- GPU 0: l2norm_k05_goal_seed43 (tmux)
- GPU 1: l2norm_k05_object_seed43 (tmux)
- GPU 2: random_k05_long_seed43 (tmux)
- GPU 3: random_k05_spatial_seed43

### 5. 排除的原因
- **GPU OOM**: 排除。4×RTX PRO 6000 (98GB)，每进程仅用 ~5GB
- **磁盘满**: 排除。根分区 29% (22GB free)
- **CUDA 错误**: 排除。GPU 健康，其他实验正常
- **代码 bug**: 排除。v1 在完全相同的代码下跑了 23 分钟/269 episodes 无异常

## 修复建议

必须用 tmux 启动所有 eval 任务，与当前正在运行的 l2norm 实验相同的模式：

```bash
tmux new-session -d -s eval_xvla_random_k05_goal_seed43 \
  'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && \
   cd /root/autodl-tmp/importance_margin_vla_compress && \
   CUDA_VISIBLE_DEVICES=3 TRANSFORMERS_OFFLINE=1 HF_HUB_OFFLINE=1 \
   HF_HOME=/root/autodl-tmp/.hf_cache MUJOCO_GL=egl \
   python -u eval_xvla_pruning_libero.py \
     --model_path /root/autodl-tmp/X-VLA-Libero \
     --suite libero_goal --keep_ratio 0.5 --mode random \
     --num_episodes 50 --seed 43 --domain_id 3 --gpu 0 \
   2>&1 | tee logs/eval_xvla_random_k05_goal_seed43_v4.log'
```

注意：需要等当前 GPU 3 上的 spatial 实验完成后再启动，或选用空闲 GPU。
