# ops eval phi4 arc cuda0

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_eval-phi4-arc-cuda0_20260520T165129_result.json`
- **Structured JSON:** [`64e070810d4d1f15f935.json`](../../sessions/64/64e070810d4d1f15f935.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

任务已提交并注册。汇总：

**产出**
- 脚本：`/root/contamcal-irt-calibration/scripts/eval_phi4_arc_s0_s42.sh`
- tmux session：`eval_phi4_arc_s0_s42`
- 日志：`/root/contamcal-irt-calibration/logs/eval_phi4_arc_s0_s42.log`
- Registry：`eval_phi4_arc_s0_s42` → RUNNING，parent=`sft_phi4_s0_sweep`
- GPU：westd-29999 cuda:0

**合规检查**
- C004: `CUDA_VISIBLE_DEVICES=0` 显式设置 ✓
- C006: lora_alpha=32 验证（脚本内 + 提前抽查） ✓
- C009: evaluate.py md5 校验（脚本启动时通过） ✓
- C001/C002: nvidia-smi 确认 cuda:0 空闲 ✓

**范围**：10 个 eval（s0×5 dosages + s42×5 dosages），ARC-Challenge 25-shot，batch_size=8。Phi-4 约 14B 参数，预计每个 eval ~10-15 分钟，总计 ~2-2.5 小时。

---
