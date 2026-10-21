# eval rho06 uniform ood seed456 seed123

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_rho06_uniform_ood_seed456_seed123_20260520T161827_result.json`
- **Structured JSON:** [`4a523085ec2e9f32a15d.json`](../../sessions/4a/4a523085ec2e9f32a15d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。

## 结果

| Model | OWT PPL | Wiki PPL |
|-------|---------|----------|
| uniform_seed456 | **18.449** | **15.420** |
| uniform_seed123 | N/A | N/A |
| adaptive_tau07_seed456 (已有) | 18.411 | 15.424 |
| adaptive_tau07_seed123 (已有) | 18.385 | 15.329 |
| Δ(adaptive - uniform) seed456 | **-0.038** | **+0.004** |
| Δ(adaptive - uniform) seed123 | N/A | N/A |

**seed456 OOD 差异极小**：OWT 上 adaptive 略优 0.038，Wiki 上几乎持平（+0.004）。这符合预期——OOD 性能不应受 in-domain 加权策略的显著影响。

**问题：`contamination_60_uniform_seed123` checkpoint 不存在。** 服务器上没有这个模型目录。`uniform_ood_seed123` 是另一个实验（使用 `mixed_data.jsonl`，ρ=0.2），不匹配。需要先训练 seed123 uniform ρ=0.6 才能完成对比。GPU 0 当前空闲，可以启动训练（约 4 小时）。是否需要启动？

---
