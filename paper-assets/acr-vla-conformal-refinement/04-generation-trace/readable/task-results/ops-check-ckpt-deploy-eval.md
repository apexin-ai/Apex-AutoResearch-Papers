# ops check ckpt deploy eval

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-ckpt-deploy-eval_20260521T191852_result.json`
- **Structured JSON:** [`0c11692447034dda1d45.json`](../../sessions/0c/0c11692447034dda1d45.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**结果：spatial checkpoint 缺失，无法继续。**

| Checkpoint | 状态 |
|---|---|
| `object/crm_best.pt` | 存在，2.4M |
| `spatial/crm_best.pt` | **不存在** |

**训练状态：**
- **Object**: 仍在运行，epoch 8 batch 850/1950，loss ~0.01，占用 GPU 0（557 MiB）
- **Spatial**: **已失败** — `FileNotFoundError: No precomputed cache at /root/autodl-tmp/crm_cache_pi05/spatial. Run with --precompute first, or use --auto.`

GPU 1/2/3 全部空闲。

**结论**：Spatial CRM 训练因缺少 precomputed cache 而崩溃，需要先对 spatial benchmark 运行 `--precompute`（或 `--auto`）生成 cache，再重新训练 spatial CRM。Object 训练还在跑，尚未完成。两个 checkpoint 都还没准备好，暂时无法进入 Step 2。

---
