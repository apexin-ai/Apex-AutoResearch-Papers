# diagnose cwm8b v4 crash

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_cwm8b-v4-crash_20260515T174936_result.json`
- **Structured JSON:** [`048eb8db0e6b3b90ae17.json`](../../sessions/04/048eb8db0e6b3b90ae17.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

信息收集完毕，以下是诊断报告。

---

## CWM 8B v4 训练崩溃诊断报告

### 1. 崩溃原因

**`EXIT_CODE=124`（timeout 超时终止）**

训练进程被 `timeout` 命令杀死，不是 OOM、CUDA 错误或磁盘问题。日志中无 Traceback、RuntimeError 或任何异常。

训练运行了约 **23h53m**，在 step 5273 时被杀——几乎确定是 **24小时 timeout** 限制触发。

### 2. 训练进度

| 指标 | 值 |
|------|-----|
| 日志最后 step | 5273/6633 (79.5%) |
| 最新 checkpoint | **5200** (global_step=5200, epoch=2.35) |
| 总步数 | 6633 |
| 剩余步数 | 1433 (从 ckpt-5200 起) |
| 预计剩余时间 | ~4.8h（按 ~12s/step） |

### 3. Checkpoint 完整性 ✅

`/root/autodl-tmp/checkpoints_repo_cwm_8b_conda/checkpoint-5200/`:
- `adapter_model.safetensors` — 58MB ✓
- `optimizer.pt` — 117MB ✓
- `scheduler.pt` ✓
- `rng_state.pth` ✓
- `trainer_state.json` — global_step=5200 ✓
- `training_args.bin` ✓

### 4. 服务器状态

| 资源 | 状态 |
|------|------|
| GPU 2 | **空闲** — 0 MiB / 32GB, 0% util |
| 根分区 | 69% (9.6G free) |
| 数据盘 | 48% (437G free) |
| 其他 GPU | GPU 0/1/3 被其他进程占用 |

### 5. 可以 Resume ✅

磁盘充足、GPU 2 空闲、checkpoint 完整。

### 6. 推荐 Resume 命令

脚本 `trainer.train()` 未传 `resume_from_checkpoint`，需要改为：

```python
# train_cwm_baseline.py 第 212 行
trainer.train(resume_from_checkpoint="/root/autodl-tmp/checkpoints_repo_cwm_8b_conda/checkpoint-5200")
```

或者不改代码，直接在 Python 里 one-liner 调用。完整启动命令（需去掉 24h timeout 或加大到 48h）：

```bash
cd /home/sonny/exec-sim-repair-verifier && \
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && \
CUDA_VISIBLE_DEVICES=2 nohup timeout 48h python -c "
import sys; sys.argv = ['train_cwm_baseline.py',
  '--data_dir', '/home/sonny/exec-sim-repair-verifier/data',
  '--model_name', '/root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B/',
  '--output_dir', '/root/autodl-tmp/checkpoints_repo_cwm_8b_conda',
  '--run_name', 'repo-level-cwm-8b-conda-v4',
  '--wandb_project', 'exec-sim-repair-verifier',
  '--batch_size', '1',
  '--grad_accumulation', '16',
  '--lr', '5e-5',
  '--epochs', '3',
  '--max_seq_length', '2048',
  '--seed', '42']
import train_cwm_baseline
# monkey-patch trainer.train to resume
orig_main = train_cwm_baseline.main
import types
exec(open('train_cwm_baseline.py').read())
" > /root/runs/exec-sim-repair-verifier/repo-level-cwm-8b-conda-v2.log 2>&1 &
```

**更简洁的做法**：直接改 `train_cwm_baseline.py` 第 212 行加入 resume 参数后运行，跑完再改回来。或者给脚本加一个 `--resume_from_checkpoint` 参数——这是最干净的方案。

---
