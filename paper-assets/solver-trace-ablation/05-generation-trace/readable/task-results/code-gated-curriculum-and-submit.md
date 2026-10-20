# code gated curriculum and submit

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_gated-curriculum-and-submit_20260516T142942_result.json`
- **Structured JSON:** [`a00bd40e7d101ada1ad9.json`](../../sessions/a0/a00bd40e7d101ada1ad9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

双卡启动成功。

### 汇报

**Kill 确认**
- `gated-isr-t03-s42` / `gated-isr-t03-s43` 均已终止，GPU 释放确认

**代码改动（`scripts/train_grpo.py`）**
- `make_reward_fn` 新增 `warmup_steps` 参数
- `isr_gated` 模式：`step <= warmup_steps` 时使用 exec-only reward，之后切入 ISR-gated
- Phase 切换时打印 `=== Phase 2: ISR-gated reward activated ===`
- 日志输出中 warmup 阶段标记 `[WARMUP]`
- CLI 新增 `--warmup_steps` 参数

**新增 config**: `configs/grpo_isr_gated_curriculum.yaml`（τ=0.2, warmup=100, lr=1e-6）

**Dry-run 结果**
- Step 1（warmup）: prove_rate=0.375, reward=0.375, `[WARMUP]` ✓
- Step 2（ISR-gated）: prove_rate=0.0, reward=0.0（无 WARMUP 标记）✓

**双卡运行状态**

| 指标 | s42 (GPU 0) | s43 (GPU 1) |
|------|------------|------------|
| PID | 863510 | 863586 |
| VRAM | 81638 MiB / 97887 MiB | 82244 MiB / 97887 MiB |
| 进度 | step 4/500 | step 6/500 |
| Step 1 reward | 0.375 | — (scrolled past) |
| `[WARMUP]` 标记 | ✓ (steps 1,3) | ✓ (steps 3,5) |

---
