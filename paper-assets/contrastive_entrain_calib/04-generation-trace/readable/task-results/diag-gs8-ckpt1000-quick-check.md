# diag gs8 ckpt1000 quick check

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_gs8-ckpt1000-quick-check_20260523T000644_result.json`
- **Structured JSON:** [`54d3dab8a80e9f3f8f3c.json`](../../sessions/54/54d3dab8a80e9f3f8f3c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三个 eval 全部仍在运行：

| Eval | GPU | 进度 | 预估 |
|------|-----|------|------|
| **gs8 ckpt-1000** (PID 140553) | GPU 0 | 140/362 (~39%) | 已跑 ~30min，预计还需 ~45min |
| **s2 ckpt-6500** | GPU 2 | 80/362 (~22%) | 预计还需 ~20min（速度快很多，~80s/20样本） |
| **s2 ckpt-7000** | GPU 3 | 60/362 (~17%) | 预计还需 ~25min |

GPU 显存占用：GPU0 16.9GB, GPU1 21.8GB, GPU2 17.7GB, GPU3 17.7GB — 四卡都在工作。

eval_results 目录暂无新结果，只有之前的 exp-003-s2-ckpt8000、exp-004-s2-ckpt2000/3000。

---
