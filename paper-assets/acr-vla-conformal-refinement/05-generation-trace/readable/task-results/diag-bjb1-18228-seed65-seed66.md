# diag bjb1 18228 seed65 seed66

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_bjb1-18228-seed65-seed66_20260521T025310_result.json`
- **Structured JSON:** [`e34977e9df37ed9e0886.json`](../../sessions/e3/e34977e9df37ed9e0886.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。汇总如下：

---

### 1. eval-obs-only-object-norm005-seed65
- **状态**: ✅ **已完成**
- PID 622479 已退出，JSON 输出完整
- **SR = 0.14** (14/100)
- Registry 已正确标记为 `DONE/success`，metrics 已录入，无需修正

### 2. seed66 × 3 — 全部正常运行中
| 实验 | PID | GPU | 显存 | 运行时间 | Registry |
|------|-----|-----|------|----------|----------|
| norm003-seed66 | 642428 | GPU 0 | 4316 MiB | 1h23m | RUNNING ✅ |
| norm005-seed66 | 642506 | GPU 2 | 4316 MiB | 1h23m | RUNNING ✅ |
| norm01-seed66 | 642775 | GPU 3 | 3851 MiB | 1h23m | RUNNING ✅ |

Cron 误标为 failed，实际全部在跑。Registry 当前状态为 RUNNING，无需修正。

### 3. seed67
| 实验 | 状态 | 位置 |
|------|------|------|
| norm003-seed67 | 不在 bjb1-18228（无进程） | Registry RUNNING，应在其他服务器 |
| norm005-seed67 | 不在 bjb1-18228 | Registry RUNNING |
| norm01-seed67 | PID 666593, GPU 1, 5242 MiB, 9min | RUNNING ✅ |

### GPU 占用
4 张 GPU 全部在用，无冲突：
- GPU 0: seed66-norm003
- GPU 1: seed67-norm01（seed65 完成后释放）
- GPU 2: seed66-norm005
- GPU 3: seed66-norm01

**结论**: seed65 已正常完成且 registry 已是 success 状态。seed66×3 和 seed67-norm01 正常运行中，cron 标记的 failed 为误报。seed67-norm003 和 norm005 不在本服务器上。

---
