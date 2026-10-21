# analysis numerical audit m2 m5

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_numerical_audit_m2_m5_20260518T052223_result.json`
- **Structured JSON:** [`22232af980d1fd8da593.json`](../../sessions/22/22232af980d1fd8da593.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审计完成。5 项结果汇总：

| 项目 | 论文值 | 权威值 | 状态 |
|---|---|---|---|
| **M2 retrain 1v2** | 0.9484 | **0.9471** [0.9432, 0.9509] | 错误，差 -0.0013 |
| **M2 retrain 2v3** | 0.8888 | 0.8888 [0.8832, 0.8943] | 正确 |
| **M2 retrain 3v4** | 0.7982 | **0.7994** [0.7920, 0.8067] | 错误，差 +0.0012 |
| **m1 arXiv Pythia 2v3** | 0.6544 | **0.6545** | 差 0.0001，应用 0.6545 |
| **m2 Qwen-7B C4 1v2** | .6168/.6178/.618 | **不存在此实验** | 严重问题 — 无 Qwen-7B×C4 实验。0.6168 实际是 exp_016 (Qwen-1.5B base×C4) 的 CI 下界，该实验 mean=0.626 |
| **m4 Wiki exp_023 0v1** | 0.985 (Tab S12) | **0.9961** | 错误，差 +0.0111。generator 确认为 Qwen2.5-1.5B base |
| **m5 Wiki λ** | 3.1 | **2.98 / 6.28 / 3.31**（三个 Wiki 实验），mean=**4.19** | 论文 3.1 不匹配任何值。最近个体 2.98（Qwen-1.5B），均值 4.19。C4 range 2.15–3.51 与论文 "2.2–3.5" 基本吻合 |

关键发现：m2 "Qwen-7B C4" 根本不存在对应实验，论文可能混淆了模型标签或误用了 CI 下界作为均值。

---
