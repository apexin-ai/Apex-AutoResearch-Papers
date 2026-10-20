# code csmp implementation

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_csmp_implementation_20260518T161544_result.json`
- **Structured JSON:** [`1434bfd747115272f77e.json`](../../sessions/14/1434bfd747115272f77e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。输出摘要：

**文件结构**（`csmp/` 下 5 个文件）:
- `__init__.py`, `cusum_monitor.py`, `calibrate.py`, `evaluate.py`, `run_csmp.py`

**产出**（`artifacts/csmp_results/`）:
- `calibration.json`, `evaluation.json`, `csmp_report.md`

**关键结果**:

| k | h | FAR | predictive alarm | reactive alarm |
|---|---|-----|-----------------|---------------|
| 0.05 | 1.5297 | 0% | gen 3 (EDD=2) | gen 2 (EDD=0) |
| 0.1 | 1.0047 | 0% | gen 1 (EDD=0) | gen 1 (EDD=-1) |
| 0.25 | ~0 | 0% | gen 1 (EDD=0) | gen 1 (EDD=-1) |
| 0.5 | ~0 | 0% | gen 1 (EDD=0) | gen 1 (EDD=-1) |
| 1.0 | ~0 | 0% | gen 1 (EDD=0) | gen 1 (EDD=-1) |

- k >= 0.1 时 CUSUM 在 gen 1 即发出 alarm，与 predictive trigger 同步，比 reactive trigger 早 1 代
- k=0.05 因 null 数据漂移导致 h 较高，检测延迟到 gen 3
- 推荐操作点 k=0.25：null 上 CUSUM 统计量恒为零（h 近零即可控制 FAR），对 collapse 信号响应即时

---
