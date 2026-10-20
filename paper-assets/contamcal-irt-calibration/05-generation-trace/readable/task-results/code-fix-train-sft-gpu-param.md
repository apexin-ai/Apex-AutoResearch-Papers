# code fix train sft gpu param

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix-train-sft-gpu-param_20260515T045911_result.json`
- **Structured JSON:** [`d28ba6a6cfb577744db3.json`](../../sessions/d2/d28ba6a6cfb577744db3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

**改动**：`exp001/train_sft.py` 中移除了 `--gpu` argparse 参数（原第93-94行）和 `os.environ["CUDA_VISIBLE_DEVICES"] = args.gpu` 覆盖逻辑（原第112-113行）。后续 GPU 选择完全由调用方的 `CUDA_VISIBLE_DEVICES` 环境变量控制。`evaluate.py` 无同类问题。已 commit（`dd81ae2`）。

---
