# infra verify evaluate deploy

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_verify-evaluate-deploy_20260515T172513_result.json`
- **Structured JSON:** [`87063f379fb0006744e3.json`](../../sessions/87/87063f379fb0006744e3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 报告

### 1. evaluate.py 3 个 bug 修复部署状态

| Bug | 状态 | 证据 |
|-----|------|------|
| Bug 1: noise/time 参数化 | ✅ | `smolvla_wrapper.py:302` — `compute_importance_scores` 接受 `noise: Optional[Tensor] = None` 参数 |
| Bug 2: baseline_forward | ✅ | `evaluate.py:192-193` — 调用 `baseline_forward(model, batch)` |
| Bug 3: preprocess_batch | ✅ | `evaluate.py:188-189` — 调用 `preprocess_batch(batch, tokenizer, device=device)` |

三个修复均已部署到服务器。

### 2. Baseline v5 Checkpoint 状态

**Checkpoints:**
- `step_005000`, `step_010000`, `step_015000`, `step_020000`, `step_025000`
- `latest` → `step_025000`

**当前进度:** step 26500 / 30000 (88.3%)

**最新 loss:** 0.0024 (step 26500), eval action_loss 0.0015 (step 26000)

**训练速度:** 4.0 steps/sec，预计剩余 ~15 分钟完成

### 3. Baseline v5 完成状态

**未完成**，当前在 step 26500/30000，仍在运行中。按 4.0 sps 估算，约 15 分钟后到达 30000 步。

---
