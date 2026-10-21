# ops cqa1 eval mmlu arc only

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_cqa1-eval-mmlu-arc-only_20260518T214911_result.json`
- **Structured JSON:** [`37714fc942cd9d2f3c69.json`](../../sessions/37/37714fc942cd9d2f3c69.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

执行状况总结：

1. **旧进程**：已清理，无残留（kill 前已无运行进程）
2. **脚本**：`/root/contamcal-irt-calibration/exp001/run_eval_mmlu_arc_original.sh`
   - 10 个 7B adapter，只跑 MMLU + ARC original
   - d000_s42 智能跳过已完成的 MMLU，只跑 ARC
   - CUDA_VISIBLE_DEVICES=0 显式设置
3. **PID**：160404（子进程 PID 160420 在 GPU 上运行）
4. **GPU 状态**：RTX 4090D，16599MiB/24564MiB，85% 利用率
5. **当前进度**：d000_s42 ARC 评估中，586 样本 ~2 it/s

**时间估算**：
- ARC: 586 items / 2 it/s ≈ 5 min
- MMLU: ~14K items / 2 it/s ≈ 2h
- d000_s42 (ARC only): ~5 min
- 其余 9 adapter (MMLU+ARC each): ~9 × 2h5min ≈ 19h
- **总计约 19 小时**

日志路径：`/root/autodl-tmp/exp001/logs/eval_mmlu_arc_original.log`

---
