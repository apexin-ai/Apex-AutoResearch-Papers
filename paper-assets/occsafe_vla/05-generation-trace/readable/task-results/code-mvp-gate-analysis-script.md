# code mvp gate analysis script

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_mvp_gate_analysis_script_20260521T042256_result.json`
- **Structured JSON:** [`150db0b6e1e965fcd57c.json`](../../sessions/15/150db0b6e1e965fcd57c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本运行成功。概要：

**脚本**: `/root/occsafe_vla/scripts/analyze_mvp_gate.py`

**功能**: 读取 vanilla/occ eval JSON → per-task breakdown → overall 统计 → paired t-test → MVP gate 判定

**当前输出**(occ 文件尚不存在):
- 3 个 vanilla seed 全部加载
- Vanilla baseline: TSR 91.8%±1.4%, CAR 77.0%±0.5%, Hard-task CAR 30.6%±2.5%
- MVP gate 阈值已计算: Overall CAR ≥ 82.0%, Hard-task CAR ≥ 40.6%, TSR ≥ 88.8%
- 提示等待 occ eval 完成后重新运行

---
