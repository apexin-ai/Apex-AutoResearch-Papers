# ssh emergency full server scan

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_emergency-full-server-scan_20260517T101916_result.json`
- **Structured JSON:** [`b4c1637059bff175ffc5.json`](../../sessions/b4/b4c1637059bff175ffc5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。以下是完整扫描结果。

---

## bjb1-18228
| GPU | 实验 | PID | 状态 | SR% |
|-----|------|-----|------|-----|
| 0 | obs_only norm=0.1 seed45 | 474319 | RUNNING ~25h | - |
| 1 | perdof norm=0.1 seed44 | 531970 | RUNNING ~14h | - |
| 2 | obs_only norm=0.1 seed46 | 587763 | RUNNING ~6h | - |
| 3 | obs_only norm=0.1 seed47 | 588037 | RUNNING ~6h | - |

0 空闲 GPU。

## bjb1-32546
| GPU | 实验 | PID | 状态 | SR% |
|-----|------|-----|------|-----|
| 0 | obs_only norm=0.2 seed47 | 319128 | RUNNING ~17h | - |
| 1 | - | - | **空闲** | - |
| 2 | perdof norm=0.1 seed45 | 309151 | **已完成** ✓ | **11%** |
| 3 | argmin(reconvla) seed47 | 322337 | RUNNING ~17h | - |
| 4 | perdof norm=0.1 seed46 | 393646 | RUNNING ~6h | - |
| 5 | perdof norm=0.3 seed45 | 319463 | RUNNING ~17h | - |

2 空闲 GPU (GPU 1, GPU 2)。

## bjb2-28827
| GPU | 实验 | PID | 状态 | SR% |
|-----|------|-----|------|-----|
| 0 | scalar seed45 | 224628 | RUNNING ~28h, **~80%** | - |
| 1 | perdof norm=0.2 seed45 | 222830 | RUNNING ~28h, **~80%** | - |
| 2 | obs_only norm=0.1 seed47 bjb2 | 363223 | RUNNING ~6h | - |
| 3 | obs_only default seed45 | 242264 | RUNNING ~26h, **~80%** | - |
| 4 | obs_only norm=0.1 seed46 bjb2 | 365893 | RUNNING ~6h | - |
| 5 | perdof norm=0.2 seed44 | 326085 | RUNNING ~12h | - |

0 空闲 GPU。**注意**：GPU 0/1/3 的实验使用 `n_rollouts=20`（非 10），所以耗时是其他实验的 2 倍。日志显示已到第 8/10 个 task，预计再 5-7h 完成。

## bjb2-40593
| GPU | 实验 | PID | 状态 | SR% |
|-----|------|-----|------|-----|
| 0 | perdof norm=0.1 seed47 | 388460 | RUNNING ~0.5h | - |

0 空闲 GPU。

---

## 空闲 GPU 汇总
| 服务器 | GPU | 可部署 |
|--------|-----|--------|
| bjb1-32546 | cuda:1 | ✓ |
| bjb1-32546 | cuda:2 | ✓（刚释放） |

共 **2 个空闲 GPU**，均在 bjb1-32546。

## 已完成实验汇总
| exp_id | SR% | Registry 状态 |
|--------|-----|---------------|
| eval-perdof-object-norm01-seed45 | **11%** | 已更新 → DONE(success) |

## 数据不一致原因
- **"GPU 全空闲"的 report 完全错误**：实测 15/17 GPU 在跑，仅 2 个空闲
- Registry 有 15 个 RUNNING（现 14 个，1 个刚标 DONE），不是 17 个
- 用户预期 3 个实验已完成（bjb2-28827 GPU 0/1/3），实际仍在运行（`n_rollouts=20` 导致耗时翻倍）
- 唯一真正完成的是 bjb1-32546 GPU 2 的 perdof norm=0.1 seed45（SR=11%，与 seed42 一致）

---
