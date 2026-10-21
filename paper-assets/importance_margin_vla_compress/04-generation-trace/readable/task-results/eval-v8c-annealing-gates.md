# eval v8c annealing gates

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_v8c_annealing_gates_20260516T103406_result.json`
- **Structured JSON:** [`f44c045958f210880d74.json`](../../sessions/f4/f44c045958f210880d74.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。评估完成，结果汇总：

## v8c_annealing Gate 评估结果

| Gate | 值 | 阈值 | 判定 |
|------|-----|------|------|
| **G1** margin ratio | **108.15x** | ≥ 2.0x | **PASS** |
| **G2** preservation diff | **+60.92pp** | ≥ +10pp | **PASS** |
| **G3** ACIS+Prune/baseline | **2.04x** | ≤ 1.10x | **FAIL** |
| **G4** LED median | **0.1046** | < 1.0 | **PASS** |

**Overall: FAIL**（G3 不过）

## 与 v8b_twostage 对比

| Gate | v8c_annealing | v8b_twostage |
|------|--------------|--------------|
| G1 | 108.15x | 93.23x |
| G2 | +60.92pp | +56pp |
| G3 | **2.04x** ❌ | **0.87x** ✓ |
| G4 | 0.1046 | 0.135 |

**分析**：v8c 在 margin（G1）和 preservation（G2）上略优于 v8b，但 ACIS+Prune 后的 action loss（G3）从 v8b 的 0.87x 退化到 2.04x。Annealing 策略虽然让 importance scorer 学得更好（更大 margin），但 backbone 没有像 v8b 的 two-stage 方式那样充分适配 pruned input，导致部署时的 action loss 过高。

---
