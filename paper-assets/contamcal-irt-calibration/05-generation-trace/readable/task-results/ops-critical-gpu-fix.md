# ops critical gpu fix

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_critical-gpu-fix_20260514T065510_result.json`
- **Structured JSON:** [`c1a4aa7815a07d248f10.json`](../../sessions/c1/c1a4aa7815a07d248f10.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

d025_05B_v3 OOM 死在 GPU 0 — 同一个 `CUDA_VISIBLE_DEVICES` 覆写 bug。PID 291380 (3B d100) 占了 13GB，PID 251924 (1.5B d100) 占了 9.8GB，导致 0.5B 模型也挤不进去。

## 汇总

### 1. PID 291380 kill
已不存在（之前已被 kill 或自行退出）。GPU 0 当前 10055/24564 MiB (13%)。

### 2. train_sft.py 修复
服务器 `/root/contamcal-irt-calibration/exp001/train_sft.py` 第 113-114 行已删除：
```diff
-    if args.gpu:
-        os.environ["CUDA_VISIBLE_DEVICES"] = args.gpu
```
`--gpu` 参数定义保留（argparse 中），但不再有任何引用。本地 artifact 副本同步更新。

### 3. git commit
服务器不是 git repo（代码直接部署），无法 commit。**文件已直接 sed 修复。**

### 4. 3B d100 重提交 — **未执行（C001 约束）**
GPU 3 已有 PID 319555 正确运行同一实验：
- tmux session `exp_001_sft_d100_3B`，wrapper 设 `CUDA_VISIBLE_DEVICES=3`
- 命令未传 `--gpu` 参数，bug 未触发，GPU 绑定正确
- 进度：897/3384 steps (26%)，~3.5h 剩余
- checkpoint 目录已清空重建，不影响后续 epoch 保存

### 5. GPU 5 状态
- PID 318748 运行 `evaluate.py`（Qwen2.5-3B raw baseline, gsm8k+humaneval），6548 MiB
- **不是** d025 训练

### 6. d025 实验状态
- `exp_001_sft_d025_05B_v3` 在 step 897/3384 OOM 崩溃 — 同一个 CUDA_VISIBLE_DEVICES bug 导致跑到 GPU 0，被 3B d100 (13GB) + 1.5B d100 (9.8GB) 挤爆
- lora_adapter 为空，需要重跑
- 现在 bug 已修复，GPU 5 evaluate 跑完后可重提交 d025 到 GPU 5

---
