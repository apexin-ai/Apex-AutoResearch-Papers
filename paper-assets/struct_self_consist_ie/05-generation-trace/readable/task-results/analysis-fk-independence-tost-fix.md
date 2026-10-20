# analysis fk independence tost fix

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_fk-independence-tost-fix_20260515T215445_result.json`
- **Structured JSON:** [`1e6624ad5fa61a95f058.json`](../../sessions/1e/1e6624ad5fa61a95f058.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两项分析完成，artifacts 已注册。总结：

---

## Task 1: FK Independence Instance-Level Test (R3-W4)

原问题：n=5 的 t-test 功效太低。改为 **instance-level 分析**（每个 instance 一个 FK 值，n=529–2756）：

| Config | n | FK | 95% CI | t | p |
|--------|---|-----|--------|------|------|
| SciERC | 529 | 0.402 | [0.376, 0.428] | 30.8 | 4.0e-120 |
| CoNLL LLaMA | 2756 | 0.927 | [0.919, 0.935] | 225.9 | <1e-300 |
| CoNLL Qwen | 2756 | 0.720 | [0.706, 0.734] | 102.1 | <1e-300 |

Permutation test (null FK ≈ −0.14) 全部 p < 0.001。Split-half r = 0.39–0.58。

## Task 2: TOST External Delta (R4-M2)

原问题：δ 基于 oracle headroom，循环论证。改用三个外部基准：
- **δ_SEM** = bootstrapped SE of greedy F1（0.43–1.33 pp）
- **δ_practical** = 0.5 pp（部署意义阈值）
- **δ_literature** = 1.0 pp（文献最小有意义改进）

结果：LLaMA-CoNLL 所有 signal 在所有外部 δ 下通过等价（p<0.001）；SciERC/Qwen-CoNLL 仅 SJ 在 δ_SEM 通过。

## 产出文件
- 服务器：`analysis_round8/fk_independence_instance_test.json`、`analysis_round8/tost_external_delta.json`、`analysis_round8/analysis_fk_tost_round8.md`
- Artifacts：`art_20260515_6544c0` (report)、`art_20260515_89fa94` (FK data)、`art_20260515_7a9cb0` (TOST data)

---
