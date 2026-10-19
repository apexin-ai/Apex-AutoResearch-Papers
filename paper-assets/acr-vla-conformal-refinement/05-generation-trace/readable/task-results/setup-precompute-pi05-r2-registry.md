# setup precompute pi05 r2 registry

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_setup_precompute-pi05-r2-registry_20260523T050219_result.json`
- **Structured JSON:** [`7ca586e83cb9784e119b.json`](../../sessions/7c/7ca586e83cb9784e119b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

4 个 registry 条目全部创建完成，状态均为 RUNNING。

## 汇总

| exp_id | PID | GPU | 总样本 | 已处理 | 进度 | 状态 |
|--------|-----|-----|--------|--------|------|------|
| precompute-pi05-object-2048-r2 | 113456 | cuda:0 | 72,507 | ~15,900 | 22% | RUNNING |
| precompute-pi05-spatial-2048-r2 | 113796 | cuda:1 | 60,250 | ~15,600 | 26% | RUNNING |
| precompute-pi05-goal-2048-r2 | 114159 | cuda:2 | 61,728 | ~15,800 | 26% | RUNNING |
| precompute-pi05-long-2048-r2 | 114507 | cuda:3 | 136,090 | ~16,700 | 12% | RUNNING |

所有进程运行约 8h43m，速度 ~1.9-2.0s/sample。预估剩余时间：object ~31h, spatial ~25h, goal ~25h, long ~62h。输出目录 `/root/autodl-tmp/crm_cache_pi05_2048/{benchmark}/`，每 500 样本保存一个 partial pt 文件。

---
