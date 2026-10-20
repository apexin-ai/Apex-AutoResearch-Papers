# eval 3B d000 s42 gpu1

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_3B_d000_s42_gpu1_20260514T005235_result.json`
- **Structured JSON:** [`211a9bc4523ad82c127d.json`](../../sessions/21/211a9bc4523ad82c127d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已完成：

- **exp_001_eval_3B_d000_s42** 已在 GPU 1 上启动（PID 249294，tmux session `exp_001_eval_3B_d000_s42`）
- GPU 1 有 20.4GB 空闲，3B eval 需要 ~12-15GB，显存充足
- 使用 `CUDA_VISIBLE_DEVICES=1` 控制 GPU 分配（之前 `--gpu` 参数导致崩溃的 bug 已规避）
- Registry 已更新：status=RUNNING, parent=exp_001_sft_0pct_3B, hypothesis 已设置
- 日志：`~/runs/contamcal-irt-calibration/exp_001_eval_3B_d000_s42.log`

---
