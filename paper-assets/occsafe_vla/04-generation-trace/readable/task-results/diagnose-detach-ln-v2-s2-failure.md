# diagnose detach ln v2 s2 failure

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_detach_ln_v2_s2_failure_20260528T015532_result.json`
- **Structured JSON:** [`3adf3ed9178bd3c65e3b.json`](../../sessions/3a/3adf3ed9178bd3c65e3b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。报告已写入 `artifacts/diagnose_batch_failure_20260528.md`。

关键发现：

1. **根因**：`finetune.py:727` 的 `save_training_checkpoint` 在合并 LoRA 时需要从 `cfg.vla_path` 加载 base model。两个失败实验的 `--vla_path` 指向旧 checkpoint（15000_chkpt / 10000_chkpt），但这些 checkpoint 已被清理脚本删除 → `OSError`。

2. **确认的失败**：
   - `detach_ln_v2_s2`：15000_chkpt 被删，现存 20000/25000/30000
   - `vanilla_object_s0`：10000_chkpt 被删，现存 15000/20000/25000

3. **未找到的日志**：`detach_bn_object_s0` 和 `full_occ_bn_object_s0` 在 westd-34685 上不存在，可能在其他服务器。

4. **安全的实验**：cuda:2/3 上的 `full_occ_ln_v2_s3` 和 `detach_ln_v2_s3` 使用原始 `openvla-7b` 作为 vla_path，不受影响。

5. **重启建议**：最快方案是加 `--merge_lora_during_training=false` 重启；或者直接用现存的最新 merged checkpoint（30000/25000）做评估，跳过重启。

---
