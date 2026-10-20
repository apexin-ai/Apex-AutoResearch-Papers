# code per task analysis script

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_per-task-analysis-script_20260521T132439_result.json`
- **Structured JSON:** [`ef0884925f75e5e2f044.json`](../../sessions/ef/ef0884925f75e5e2f044.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本运行成功。生成的文件：

**脚本**: `/root/occsafe_vla/scripts/analyze_learning_curve.py`

**图表** (均有 PDF + PNG, DPI=300):
- `/root/occsafe_vla/figures/learning_curve.png` — OCC s1 整体+per-task CAR 学习曲线 vs Vanilla baseline
- `/root/occsafe_vla/figures/car_heatmap.png` — Per-task CAR 热力图 (30K→45K)
- `/root/occsafe_vla/figures/delta_car.png` — ΔCAR 柱状图 (OCC 3-seed avg vs Vanilla 2-seed avg)

**关键发现**:
- OCC s1 整体 CAR 从 30K(65.0%) → 40K(73.0%) 上升后 45K(69.0%) 回落
- Hard tasks (T3/T5) 在 OCC 中持续改善 (+6.3pp / +13.0pp vs vanilla)
- T6 和 T7 是主要退化点 (−23.3pp / −18.7pp)，T7 跨 seed 方差极大 (s0=100%, s1=35%, s2=100%)

---
