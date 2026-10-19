# ops audit bjb1 18228 after tmux crash

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_audit-bjb1-18228-after-tmux-crash_20260518T204434_result.json`
- **Structured JSON:** [`4b17d43f66399189741c.json`](../../sessions/4b/4b17d43f66399189741c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部就绪。最终状态汇报：

## 审计结果

### 存活进程（未受 tmux 崩溃影响，3个）
| GPU | 实验 | 状态 |
|-----|------|------|
| 1 | obs_only norm003 seed43 | tmux 运行中（之前已重新部署） |
| 2 | perdof norm003 seed44 | orphan 进程运行中 |
| 3 | perdof default seed43 | orphan 进程运行中 |

### 已完成（1个）
| GPU | 实验 | JSON 写入时间 |
|-----|------|--------------|
| 3 | obs_only norm01 seed48 | May 18 19:39 ✓ |

### 重新部署（4个）
| GPU | 实验 | tmux session |
|-----|------|-------------|
| 0 | obs_only norm=0.03 seed47 | `eval-obs-only-norm003-seed47` |
| 0 | perdof norm=0.3 seed48 | `eval-perdof-norm03-seed48` |
| 1 | obs_only norm=0.03 seed46 | `eval-obs-only-norm003-seed46` |
| 2 | obs_only norm=0.05 seed46 | `eval-obs-only-norm005-seed46` |

### GPU 状态（验证通过）
| GPU | 进程数 | VRAM |
|-----|--------|------|
| 0 | 2 | 10771MiB / 24564MiB |
| 1 | 2 | 10945MiB / 24564MiB |
| 2 | 2 | 7909MiB / 24564MiB |
| 3 | 1 | 2410MiB / 24564MiB |

共 5 个 tmux session + 2 个 orphan 进程 = 7 个实验在跑，1 个已完成。8 个实验全部覆盖。

---
