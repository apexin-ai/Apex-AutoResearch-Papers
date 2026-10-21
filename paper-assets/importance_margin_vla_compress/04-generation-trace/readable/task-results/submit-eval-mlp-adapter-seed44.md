# submit eval mlp adapter seed44

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_submit_eval_mlp_adapter_seed44_20260519T131430_result.json`
- **Structured JSON:** [`217b4a12e0b46fad469b.json`](../../sessions/21/217b4a12e0b46fad469b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

无法提交实验。原因：

1. **cqa1-33015 数据盘已满**：250G 中仅剩 463MB，无法存放 1.8GB 的 `mlp_adapter_control/checkpoint.pt`
2. **Checkpoint 缺失**：cqa1 上没有 `mlp_adapter_control` checkpoint，仅 westd-27271 上有

磁盘占用大户（checkpoints 目录）：
| 目录 | 大小 |
|------|------|
| libero_imm_twostage_fullft_seed0 | 17G |
| baseline_control | 13G |
| libero_full_ft / seed0 / seed1 | 13G × 3 |
| libero_baseline / seed0 | 8.7G × 2 |

GPU 方面，cuda:0/2/3 空闲，可以跑。

**需要你决定**：是否清理 cqa1 上部分旧 checkpoint 腾出空间？至少需要释放 ~1.5GB。或者改用其他服务器。

---
