# analysis mvp strong model disambig

**trace distill repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_mvp_strong_model_disambig_20260515T161705_result.json`
- **Structured JSON:** [`c72a600d51c8cf729504.json`](../../sessions/c7/c72a600d51c8cf729504.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## mvp_strong_model_disambig 实验结果分析

### Per-Condition Summary

| Condition | N | Judge Mean | Judge>=4 | Test Pass | Diff Apply |
|---|---|---|---|---|---|
| **no_trace** | 14 | **1.29** | 7.1% | **6/14 (42.9%)** | 12/14 (85.7%) |
| full_trace | 14 | 1.00 | 0.0% | 4/14 (28.6%) | 8/14 (57.1%) |
| structural_filtered | 14 | 1.00 | 0.0% | 5/14 (35.7%) | 9/14 (64.3%) |
| line_filtered | 14 | 1.14 | 0.0% | 6/14 (42.9%) | 10/14 (71.4%) |

### Head-to-Head 对比

| 对比 | W-T-L | Sign Test p | 结论 |
|---|---|---|---|
| structural vs no_trace | **0-11-3** | p=1.000 | no_trace 更优，structural 0胜 |
| line vs no_trace | **2-10-2** | p=0.688 | 持平 |
| structural vs line | **1-10-3** | p=0.938 | line 更优 |
| full_trace vs no_trace | **0-10-4** | p=1.000 | no_trace 明显更优 |

### Per-Instance Detail

| Instance | no_trace | full_trace | structural | line |
|---|---|---|---|---|
| black_1 | j=1 FAIL da=Y | j=1 FAIL da=N | j=1 FAIL da=N | j=1 FAIL da=Y |
| cookiecutter_1 | j=1 **PASS** | j=1 **PASS** | j=1 **PASS** | j=1 **PASS** |
| cookiecutter_2 | j=1 FAIL | j=1 FAIL | j=1 FAIL | j=1 FAIL |
| cookiecutter_3 | j=1 FAIL | j=1 FAIL | j=1 FAIL | j=1 FAIL |
| fastapi_2 | j=1 FAIL | j=1 FAIL | j=1 FAIL | j=1 FAIL |
| httpie_2 | j=1 FAIL | j=1 FAIL | j=1 FAIL | j=1 FAIL |
| luigi_5 | j=1 FAIL | j=1 FAIL | j=1 FAIL | j=1 FAIL |
| sanic_2 | j=1 FAIL | j=1 FAIL | j=1 FAIL | j=1 **PASS** |
| scrapy_2 | **j=4 PASS** | j=1 **PASS** | j=1 **PASS** | j=1 **PASS** |
| scrapy_7 | j=1 **PASS** | j=1 **PASS** | j=1 **PASS** | j=1 **PASS** |
| tornado_2 | j=1 FAIL | j=1 FAIL | j=1 FAIL | j=1 FAIL |
| youtube-dl_1 | j=1 **PASS** | j=1 FAIL | j=1 **PASS** | j=2 **PASS** |
| youtube-dl_20 | j=1 **PASS** | j=1 FAIL | j=1 FAIL | j=1 **PASS** |
| youtube-dl_5 | j=2 **PASS** | j=1 **PASS** | j=1 **PASS** | j=2 FAIL |

### C001 Kill Criteria 判定

| 条件 | 要求 | 实际 | 结果 |
|---|---|---|---|
| (1) no_trace judge >= 3.0 | judge_mean >= 3.0 | **1.29** | **FAIL** |
| (2) structural > no_trace (p<0.15) | sign test p<0.15 | **0-11-3, p=1.000** | **FAIL** |
| (3) 至少1个条件 test_pass > 0% | any > 0% | 6/14 = 42.9% | PASS |

**C001 判定：MVP FAIL。** 三条中只有第(3)条满足，(1)(2)均 FAIL。

### 关键发现

1. **强模型下 structural 不优于 no_trace，反而更差。** structural 0胜3负，是所有 trace 条件中表现最差的。

2. **强模型未翻转 line > structural 趋势。** v4-pro 阶段 structural vs line = 1-3-6（line 领先），Claude Sonnet 4 下 structural vs line = 1-10-3（line 仍然领先）。趋势一致。

3. **trace 信息在强模型上非但没有放大正向信号，反而表现出负面影响：**
   - full_trace 是所有条件中最差的（test_pass 28.6%，diff_apply 57.1%）
   - no_trace 反而是最好的（test_pass 42.9%，diff_apply 85.7%）
   - 提供 trace 降低了 diff 应用成功率，说明 trace 可能干扰了模型生成正确格式的补丁

4. **judge 评分全面崩溃：** 几乎所有结果 judge=1，意味着生成的修复与 ground truth 完全无关。唯一的 judge>=4 出现在 scrapy_2 的 no_trace 条件（j=4）。模型虽然能通过部分测试，但修复路径与 ground truth 不同。

5. **与 v4-pro 对比：** 强模型换用 Claude Sonnet 4 并未带来改善。no_trace 基线 judge=1.29 远低于 kill criteria 要求的 3.0，说明这批 benchmark 实例本身对 LLM 修复来说太难了，trace 信息无法弥补。

### 建议

根据 C001 kill criteria，**实验明确 FAIL，应终止消歧线路。** structural trace 在两代模型（deepseek-v4-pro 和 Claude Sonnet 4）上都未能超越 no_trace baseline，且强模型实验是 C001 规定的最后一次消歧机会。

---
