# ops arc s123 eval batch

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_arc-s123-eval-batch_20260520T160447_result.json`
- **Structured JSON:** [`ff76f48e28d9667bec72.json`](../../sessions/ff/ff76f48e28d9667bec72.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

提交完成。汇总：

**脚本路径**: `/root/contamcal-irt-calibration/scripts/eval_arc_s123_batch.sh`

**提交详情**:
- PID: 371979 (shell) → 371989 (python, 已在 cuda:2 占用 32726 MiB)
- 服务器: westd-29999, cuda:2
- Registry: `eval_arc_s123_batch` → RUNNING

**执行顺序** (串行, 4 families × 5 dosages = 20 runs):
1. Qwen2.5-14B (bs=4) — 正在运行 d000
2. Phi-4 (bs=8)
3. Qwen2.5-7B (bs=8)
4. OLMo-2 (bs=8)

**合规检查**:
- C001/C002: cuda:2 确认空闲 ✓
- C004: CUDA_VISIBLE_DEVICES=2 显式设置 ✓
- C006: 脚本内 lora_alpha=32 校验 ✓
- C009: evaluate.py md5 校验 ✓

**预计完成时间**: ~55-65 分钟。ARC-Challenge 1172 items, Qwen-14B ~5.3 it/s (~3.7 min/dosage), 7B 模型更快 (~2 min/dosage)。日志: `/root/contamcal-irt-calibration/logs/eval_arc_s123_batch.log`

---
