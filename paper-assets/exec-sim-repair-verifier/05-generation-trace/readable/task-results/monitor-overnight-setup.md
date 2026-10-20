# monitor overnight setup

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_overnight-setup_20260517T172711_result.json`
- **Structured JSON:** [`8512d58d11d3f1ebb113.json`](../../sessions/85/8512d58d11d3f1ebb113.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总：

```
Home (home-1x5090):
- TRAJ eval: COMPLETED (May 17 10:23)
  - Results: eval_deepseek_traj_func_m001_reverify_run2.json
  - Accuracy: 83.04% (vs 53.6% majority baseline)
  - Resolved F1=79.9, Unresolved F1=85.4
  - Consistency rate: 77.5%
- Active tmux: eval_8b_val5120_fix — TERMINATED at 6553/9335 (70%)
  - This was a CLS eval (not TRAJ), killed externally
  - GPU: 0%, 0 MiB — idle

Seetacloud (seetacloud-westd-4x5090):
- Process 1: cls-v4-eval-8192 (tmux), PID=664774, GPU 0 (89%, 31.4G)
  - eval_repo_cls.py, ckpt=cls_repo_v4/checkpoint-4422, max_seq=8192
  - Progress: 960/9784 (9.8%), running_acc=70.0%
  - Rate: ~16.8 samples/min → ~8.7h remaining

- Process 2: cwm-eval-s42 (no tmux), PID=662946, GPU 1 (53%, 17.3G)
  - eval_repo_cwm.py, ckpt=cwm_repo/best/, split=test
  - Running 1h07m, no visible progress counter
  - batch_size=1, max_seq=4096, max_new_tokens=512

- Process 3: cls-s123-eval-8192 (tmux), PID=665019, GPU 2 (91%, 31.4G)
  - eval_repo_cls.py, ckpt=cls_repo_s123/best, max_seq=8192
  - Progress: 840/9784 (8.6%), running_acc=74.3%
  - Rate: ~14.8 samples/min → ~10h remaining

- Process 4: cwm-train-s123 (no tmux), PID=542906, GPU 3 (99%, 18.1G)
  - train_unified.py, task=cwm, seed=123, 3 epochs
  - Progress: 10036/13266 (75.6%), ~8.4s/step → ~7.5h remaining
  - ⚠️ eval_loss=nan at epoch 2 checkpoint (checkpoint-8844)
```

注意事项：
1. **Home 的 CLS eval 被杀了**（Terminated），不是 TRAJ eval — TRAJ reverify 已完成。
2. **CWM training eval_loss=nan** 需要关注，可能是 eval 计算问题或训练发散。

---
