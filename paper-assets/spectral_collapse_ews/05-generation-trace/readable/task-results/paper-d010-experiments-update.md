# paper d010 experiments update

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_d010_experiments_update_20260517T063539_result.json`
- **Structured JSON:** [`d8b4818bc473beb70596.json`](../../sessions/d8/d8b4818bc473beb70596.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有修改已完成。逐项总结：

**(a) ppl increment 精确数值** — line 188: `1.83` → `2.20`，`\to` → `\rightarrow`（匹配实际数据 13.58 - 11.38 = 2.20）

**(b) Temporal lag 描述** — line 194: 删除了原来的"lags...by one generation"及冗余前置句，替换为指定的 two-generation detection delay 表述

**(c) σ₁ caption 说明** — line 170: table caption 末尾增加 "$\sigma_1$ values decrease during decompression and increase during collapse, with lower values indicating more isotropic representations."

**(d) Advantage (2)** — line 194: 从"can be computed from a single forward pass during training without additional generation"改为"spectral metrics require no held-out evaluation set or text generation, only a forward pass through a fixed probe set"

**(4) Controller 参数更新** — 三处变更:
- line 87: τ=0.02 → τ=0.005，信号改为 "normalized log-determinant decline"，移除了 `†` 标记
- line 92: 删除了 "†To be calibrated from Phase~0 pilot." 脚注
- line 117: 原 calibration 句后追加了阈值来源说明段落（Phase~0 Gen 3-5, 0.8%/gen decline rate）

---
