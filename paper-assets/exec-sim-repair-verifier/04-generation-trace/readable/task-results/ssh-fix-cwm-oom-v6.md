# ssh fix cwm oom v6

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_fix-cwm-oom-v6_20260512T190022_result.json`
- **Structured JSON:** [`af1d05d1db7fd040532e.json`](../../sessions/af/af1d05d1db7fd040532e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练在 **cuda:2** 上正常运行，已完成 31/6633 步。

## 产出汇总

### 1. train_repo_cwm.py 修改

| 参数 | 改前 | 改后 |
|------|------|------|
| `batch_size` | 2 | 1 |
| `grad_accumulation` | 16 | 32 |
| `save_steps` | 500 | 50 |

effective batch size 不变（2×16 = 1×32 = 32）

### 2. Dry-run / 验证结果

先前错误提交（GPU 0）+ 当前正确提交（GPU 2）均证实修复有效：
- **GPU VRAM**: 22,342 MiB / 32,607 MiB（68.5%，**10GB headroom**）
- **速度**: ~8.0 s/step
- **总步数**: 6,633（3 epochs × 70,748 samples / batch 1 / accum 32）
- **预计时长**: ~14.7 小时

### 3. repo-level-cwm-v6 已提交

- **状态**: RUNNING on cuda:2, PID 84887
- **tmux session**: repo-level-cwm-v6
- **日志**: `~/runs/exec-sim-repair-verifier/repo-level-cwm-v6.log`
- **checkpoint**: `/root/autodl-tmp/checkpoints_repo_cwm_v6/`
- **parent**: repo-level-cwm-v5
- **spec**: command, server, data_path, data_count=70748, model_name=Qwen/Qwen3-4B, seed=42 已写入

### 4. v5 OOM 根因

v5 crash 在 `model.to(device)` 阶段——**另一个进程（PID 77816）占用 25.99GB**，导致 GPU 余量不足。v6 修复后即使单独运行，峰值也从 ~26.5GB 降到 22.3GB，避免类似争用风险。

---
