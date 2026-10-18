# eval v8 trajectory recovery

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_v8-trajectory-recovery_20260516T025040_result.json`
- **Structured JSON:** [`c43b4a2e668a82e71c38.json`](../../sessions/c4/c43b4a2e668a82e71c38.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有工作已由前一个 Worker 完成。汇总：

## 服务器状态
- **训练**: 完成（step_029999，latest symlink 已指向）
- **Eval 进程**: 全部完成，无残留进程
  - `traj_eval_补跑.log` → "ALL TRAJECTORY EVALS COMPLETE"（覆盖 22K-26K）
  - `traj_eval_28k_30k.log` → "ALL TRAJECTORY + BYPASS DONE"（覆盖 28K-30K）

## Registry 数据已完整
`checkpoint_trajectory` 已包含 2K→29999 全部 15 个数据点。JSON 文件与 registry 值一致。

### 22K-30K trajectory（registry 已有）

| Step | standard | acis_prune | bypass | acis_advantage |
|------|----------|------------|--------|----------------|
| 22K | 0.00753 | 0.0039 | 0.0326 | 0.01222 |
| 24K | 0.00750 | 0.00383 | 0.03241 | 0.01317 |
| 26K | 0.00663 | 0.00341 | 0.03167 | 0.01201 |
| 28K | 0.00673 | 0.00333 | 0.03235 | 0.01203 |
| 30K | 0.00659 | 0.00330 | 0.03230 | 0.01246 |

### 500-batch eval（也已完成）
- Standard: clean=0.005297, acis_pruned=0.005936
- Bypass: clean=0.03019
- Gate: G1=48.2x PASS, G2=47.1pp PASS, **G3a=1.299 FAIL**（目标≤1.10）, G4=0.169 PASS → **Overall FAIL**

### 趋势
- standard 和 acis_prune 在 16K 后进入平台期，最终 acis_prune=0.0033 达到 baseline(0.00408) 的 81%
- bypass 收敛极慢，稳定在 ~0.032，是 standard 的 ~5x → 确认 IMM 训练改变了权重分布
- acis_advantage 在 20K 后稳定在 ~0.012

无需额外操作，所有 trajectory eval 和 registry 更新已完成。

---
