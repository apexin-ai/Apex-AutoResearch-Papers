# check training quick

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_training_quick_20260523T053258_result.json`
- **Structured JSON:** [`98069954f97b5ade934f.json`](../../sessions/98/98069954f97b5ade934f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

4 个进程运行中，4 卡全部满载。

| 实验 | Step | 进度 | Weighted Loss | Unweighted Loss | ETA |
|------|------|------|--------------|----------------|-----|
| rho03_adaptive_seed456_r2 | 2957/6103 | 48% | 2.710 | 2.710 | ~2h16m |
| rho03_uniform_seed456 | 4285/6103 | 70% | 2.257 | 2.257 | ~1h14m |
| bs8_nmin4_adaptive_seed123_r2 | 3442/6103 | 56% | 2.466 | 1.993 | ~1h57m |
| bs8_nmin4_uniform_seed123_r2 | 3505/6103 | 57% | 1.866 | 1.866 | ~2h00m |

GPU 利用率：GPU0 100%, GPU1 94%, GPU2 100%, GPU3 100%。

bs8_nmin4_adaptive 的 weighted/unweighted loss 差距（2.466 vs 1.993）说明自适应加权在拉高污染样本权重；rho03_adaptive 当前 b=0 即该 batch 无污染样本，两个 loss 一致。rho03_uniform 进度最快，预计约 1h14m 完成。

---
