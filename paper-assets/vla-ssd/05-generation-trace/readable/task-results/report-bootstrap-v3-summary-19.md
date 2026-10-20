# report bootstrap v3 summary 19

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_report_bootstrap_v3_summary_19_20260523T120509_result.json`
- **Structured JSON:** [`f4ac939258e59cfe879b.json`](../../sessions/f4/f4ac939258e59cfe879b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Bootstrap v3 Summary Table (19/20, tracvla_long/untrained = PENDING)

| Model | Suite | Cond | Peak Lyr | Peak R² | Exit R² | Δ | CI Low | CI High | Boot Mean | Boot Std | Δ∈CI | \|Δ\|>0.1 | Sig (CI≠0) | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| tracvla | goal | trained | L13 | 0.5399 | 0.2065 | 0.3334 | 0.2069 | 0.4508 | 0.3155 | 0.0642 | Y | Y | YES | 100 |
| tracvla | goal | untrained | L11 | 0.5048 | 0.4403 | 0.0645 | -0.1084 | 0.0510 | -0.0232 | 0.0407 | N | N | NO | 100 |
| tracvla | spatial | trained | L13 | 0.6871 | 0.5315 | 0.1557 | 0.0906 | 0.2244 | 0.1539 | 0.0333 | Y | Y | YES | 100 |
| tracvla | spatial | untrained | L4 | 0.6120 | 0.5643 | 0.0477 | -0.6067 | -0.4606 | -0.5427 | 0.0357 | N | N | YES | 100 |
| tracvla | object | trained | L13 | 0.6315 | 0.2692 | 0.3623 | 0.2834 | 0.5038 | 0.3788 | 0.0582 | Y | Y | YES | 100 |
| tracvla | object | untrained | L17 | 0.6274 | 0.6184 | 0.0090 | -0.0669 | 0.0169 | -0.0239 | 0.0208 | Y | N | NO | 100 |
| tracvla | long | trained | L13 | 0.5897 | 0.2319 | 0.3579 | 0.1714 | 0.5333 | 0.3236 | 0.0984 | Y | Y | YES | 100 |
| nora | goal | trained | L8 | 0.4489 | -0.0062 | 0.4551 | 0.9099 | 1.6077 | 1.2155 | 0.1786 | N | Y | YES | 100 |
| nora | goal | untrained | L5 | 0.4203 | 0.3397 | 0.0806 | -0.0147 | 0.1102 | 0.0454 | 0.0313 | Y | N | NO | 100 |
| nora | spatial | trained | L20 | 0.5763 | 0.2683 | 0.3080 | 0.3011 | 0.5119 | 0.3926 | 0.0532 | Y | Y | YES | 100 |
| nora | spatial | untrained | L4 | 0.5125 | 0.4240 | 0.0885 | -0.0128 | 0.0931 | 0.0423 | 0.0277 | Y | N | NO | 100 |
| openvla | goal | trained | L1 | 0.4177 | 0.3313 | 0.0864 | -0.0560 | 0.1064 | 0.0173 | 0.0414 | Y | N | NO | 100 |
| openvla | goal | untrained | L27 | 0.4230 | 0.3672 | 0.0558 | 0.0113 | 0.0773 | 0.0396 | 0.0166 | Y | N | YES | 100 |
| openvla | spatial | trained | L24 | 0.5649 | 0.5278 | 0.0371 | 0.0087 | 0.1020 | 0.0508 | 0.0233 | Y | N | YES | 100 |
| openvla | spatial | untrained | L28 | 0.5391 | 0.4955 | 0.0437 | 0.0295 | 0.1113 | 0.0666 | 0.0209 | Y | N | YES | 100 |
| openvla | object | trained | L3 | 0.5695 | 0.5325 | 0.0370 | -0.0038 | 0.0854 | 0.0413 | 0.0226 | Y | N | NO | 100 |
| openvla | object | untrained | L3 | 0.5619 | 0.5105 | 0.0513 | -0.0044 | 0.0905 | 0.0417 | 0.0250 | Y | N | NO | 100 |
| openvla | long | trained | L23 | 0.5328 | 0.5003 | 0.0325 | 0.0037 | 0.1030 | 0.0484 | 0.0259 | Y | N | YES | 100 |
| openvla | long | untrained | L29 | 0.5316 | 0.4968 | 0.0349 | 0.0261 | 0.1047 | 0.0597 | 0.0202 | Y | N | YES | 100 |
| tracvla | long | untrained | — | — | — | — | — | — | — | — | — | — | **PENDING** | — |

## Summary

| Metric | Count |
|---|---|
| VLM→VLA trained substantial (\|Δ\|>0.1) | **6/6** |
| OpenVLA trained substantial (\|Δ\|>0.1) | **0/4** |
| All untrained substantial (\|Δ\|>0.1) | **0/9** |
| Significant (CI excludes 0) trained | 8/10 |
| Significant (CI excludes 0) untrained | 4/9 |
| Observed Δ within bootstrap CI | 16/19 |

## tracvla_long/untrained 进度

正在运行（PID 738149, 100% CPU），Task 7/10，进度约 3800/5000 samples。日志最后一行 `20:06:17`。预计还需约 15–20 分钟完成。

**注意**: nora_goal/trained 的 CI [0.91, 1.61] 远离观测 Δ=0.4551（Δ∈CI=N），bootstrap 均值 1.2155 与点估计差异大，可能需要检查该条件的 probe 稳定性。

---
