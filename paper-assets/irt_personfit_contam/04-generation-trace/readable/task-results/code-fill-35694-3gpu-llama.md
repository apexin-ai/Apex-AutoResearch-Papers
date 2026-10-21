# code fill 35694 3gpu llama

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fill-35694-3gpu-llama_20260521T130300_result.json`
- **Structured JSON:** [`47efcaca9fbcc750efd7.json`](../../sessions/47/47efcaca9fbcc750efd7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部就绪。

## 结果汇总

| GPU | 实验 | PID | 显存 | GPU 利用率 |
|-----|------|-----|------|-----------|
| cuda:0 | clean_s8 (seed=305) | 143378 | 17,850 MiB | 86% |
| cuda:1 | clean_s9 (seed=306) | 143458 | 22,012 MiB | 88% |
| cuda:2 | GRPO v3 (不动) | 141866 | 9,920 MiB | 83% |
| cuda:3 | clean_s10 (seed=307) | 143599 | 15,730 MiB | 96% |

**4/4 GPU 满载运行。**

**修改内容：** train.py 的 SEED_MAP 添加了 `clean_s9: 306`, `clean_s10: 307`；DATA_DIR_MAP 添加了对应的 `clean` 映射。

**预计训练时长：** QLoRA SFT, 5000 samples, 3 epochs, batch=4×4=16 — 在 RTX PRO 6000 上预计 1-2 小时（参考之前 s4-s7 同配置）。

**无异常。**

---
