# code fix exp002v3 d026 params

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix-exp002v3-d026-params_20260519T073319_result.json`
- **Structured JSON:** [`12c64e722c6715f6ac3d.json`](../../sessions/12/12c64e722c6715f6ac3d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

远程和本地均已修正完毕。

```
修正前 → 修正后:
- R1_WEIGHT: 0.5 → 0.4
- R3_WEIGHT: 0.5 → 0.6
- lora_alpha: 128 → 64
- resume_from_checkpoint: None → /root/contrastive_entrain_calib/checkpoints/exp002v2_dcgrpo_cosine/checkpoint-500
- trainer import 路径: sys.path → /root/mvp_v2_1_expanded/training（dcgrpo_trainer.py 已含 r1_scale_factor 支持，L130/271/674）
- recalibration_interval: 500 ✓（L137，已设置）
```

注意：`/root/contrastive_entrain_calib/training/` 下无 `dcgrpo_trainer.py`，run script 通过 `sys.path.insert` 从 `/root/mvp_v2_1_expanded/training/` 导入，该文件已有 `r1_scale_factor` 支持，无需额外同步。

---
