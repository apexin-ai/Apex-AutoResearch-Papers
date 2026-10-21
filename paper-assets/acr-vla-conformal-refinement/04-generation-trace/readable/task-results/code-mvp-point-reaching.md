# code mvp point reaching

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_mvp-point-reaching_20260513T012320_result.json`
- **Structured JSON:** [`9e586a6bf45b09e28ec7.json`](../../sessions/9e/9e586a6bf45b09e28ec7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验结果

**OVERALL: SUCCESS** — 两个关键组（Group 1 oracle, Group 4 K=10 estimated）均 PASS。

### 完整结果表

| Grp | Model | MSE_x | MSE_y | MSE_z | Total |
|-----|-------|-------|-------|-------|-------|
| 1 | A(scalar) | 0.1802 | 0.0250 | 0.0242 | 0.0765 |
| 1 | **B(per-DOF)** | **0.1727** | **0.0155** | **0.0156** | **0.0679** |
| 1 | C(none) | 0.2271 | 0.0255 | 0.0248 | 0.0925 |
| 2 | A(scalar) | 0.0646 | 0.0238 | 0.0230 | 0.0371 |
| 2 | **B(per-DOF)** | **0.0534** | **0.0157** | **0.0157** | **0.0283** |
| 2 | C(none) | 0.0842 | 0.0254 | 0.0248 | 0.0448 |
| 3 | A(scalar) | 0.0429 | 0.0232 | 0.0224 | 0.0295 |
| 3 | **B(per-DOF)** | **0.0330** | **0.0156** | **0.0156** | **0.0214** |
| 3 | C(none) | 0.0530 | 0.0255 | 0.0247 | 0.0344 |
| 4 | A(scalar) | 0.1874 | 0.0247 | 0.0243 | 0.0788 |
| 4 | **B(per-DOF)** | **0.1829** | **0.0191** | **0.0185** | **0.0735** |
| 4 | C(none) | 0.2151 | 0.0250 | 0.0246 | 0.0882 |
| 5 | A(scalar) | 0.0649 | 0.0239 | 0.0236 | 0.0375 |
| 5 | **B(per-DOF)** | **0.0585** | **0.0189** | **0.0185** | **0.0320** |
| 5 | C(none) | 0.0770 | 0.0248 | 0.0246 | 0.0422 |
| 6 | A(scalar) | 0.0418 | 0.0234 | 0.0232 | 0.0295 |
| 6 | **B(per-DOF)** | **0.0363** | **0.0187** | **0.0185** | **0.0245** |
| 6 | C(none) | 0.0484 | 0.0248 | 0.0246 | 0.0326 |

### Pass 标准

- **Group 1 (oracle, σ=0.5/0.1/0.1)**: B vs A y 改善 37.8%, z 改善 35.6%, x 不劣于 A ✓; B vs C 三轴均 >5% ✓ → **PASS**
- **Group 4 (K=10, σ=0.5/0.1/0.1)**: B vs A y 改善 22.8%, z 改善 23.9%, x 不劣于 A ✓; B vs C 三轴均 >5% ✓ → **PASS**

### 关键发现

B(per-DOF) 在所有 6 组实验中全面优于 A(scalar) 和 C(none)。Oracle 不确定性比 K=10 估计提供更大优势（37% vs 23%），但即使用 10 个样本估计的 per-DOF 不确定性也显著优于标量摘要。

---
