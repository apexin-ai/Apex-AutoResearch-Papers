# eval plan017 mlm perturbation

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_plan017-mlm-perturbation_20260518T061416_result.json`
- **Structured JSON:** [`872c4ac392245005a9db.json`](../../sessions/87/872c4ac392245005a9db.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果汇总：

**plan_017 MLM 对抗扰动评估 — 假设被否定**

| K | MLM delta | Treatment delta | Baseline delta | TF-IDF delta |
|---|-----------|-----------------|----------------|--------------|
| k=1 | **-0.0922** | -0.0256 | -0.1464 | -0.0959 |
| k=2 | -0.0396 | 0.0 | -0.121 | -0.0411 |
| k=3 | -0.0395 | 0.0 | -0.1382 | -0.0133 |
| full | **-0.0263** | **0.0** | -0.1176 | -0.0133 |

MLM model 扰动鲁棒性处于中间水平：优于 vanilla baseline（-0.1176），但明显不如 persuasion treatment（0.0）。结论：domain adaptation 仅提供部分扰动鲁棒性，分类监督信号（persuasion-augmented data 上的 classification supervision）是实现完全鲁棒性的必要条件。

---
