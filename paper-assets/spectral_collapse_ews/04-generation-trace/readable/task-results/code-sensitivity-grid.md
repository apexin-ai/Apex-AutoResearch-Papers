# code sensitivity grid

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_sensitivity_grid_20260517T054615_result.json`
- **Structured JSON:** [`f2793d33ddf563bb11dc.json`](../../sessions/f2/f2793d33ddf563bb11dc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本已创建并验证。`/root/spectral_collapse_ews/run_sensitivity.py` 参数解析正常，`--help` 输出符合预期。

脚本结构：
- 直接 import `src.config.Config` 和 `src.pipeline.run_recursive_training`，复用 run_phase1.py 的核心逻辑
- 9 组网格 (3 k x 3 tau)，固定 adaptive 条件
- `--mode serial` 串行跑全部，`--mode single --k X --tau Y` 跑单组
- 自动设置 `TRANSFORMERS_OFFLINE=1 HF_HUB_OFFLINE=1`
- 每组记录 wall time，输出独立 summary JSON
- Python 路径：`/root/miniconda3/bin/python3.12`

---
