# code urgent 16980 status and results

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_urgent_16980_status_and_results_20260517T221631_result.json`
- **Structured JSON:** [`6817eec999dcfeb313d1.json`](../../sessions/68/6817eec999dcfeb313d1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Both retry runs are active (GPUs at 84-85% util). Models loaded, first docs processing. Here's the complete status report:

---

## westd-16980 状态
- **Qwen constrained**: 完成 (246/246), success=197, fail=49
- **Llama constrained**: 完成 (246/246), success=212, fail=34
- **GPU utilization**: 84%/85% (retry runs in progress)

## Qwen Constrained 结果
- **Parse Success**: 197/246 (80.1%)
- **Violation Rates**: ET=0.0%, EV=0.0%, RoV=0.4%, AC=2.4%, CF=19.5%
- **Trigger F1**: 0.1380, **Argument F1**: 0.0183, **Entity F1**: 0.1384
- **Go/No-go (RoV+AC)**: 2.77%
- **对比 unconstrained** (EV 24.0%, RoV 74.9%): **EV Δ=-24.0pp, RoV Δ=-74.5pp**
- **F1 对比**: Trigger 0.1184→0.1380 (+0.020), Arg 0.0009→0.0183 (+0.017), Entity 0→0.1384
- Parse failure doc IDs (49): scenario_en_kairos_65, 61_VOA_EN_NW_2017.03.22.3777524, 35_VOA_EN_NW_2015.04.08.2711451, wiki_mass_car_bombings_0_article, wiki_drone_strikes_2_news_11, wiki_ied_bombings_5_news_4, suicide_ied_105, 21_VOA_EN_NW_2015.04.21.2728323, scenario_en_37, 2_VOA_EN_NW_2015.01.04.2583337, ... (全部49个是token截断导致的JSON解析失败)

## Llama Constrained 结果
- **Parse Success**: 212/246 (86.2%)
- **Violation Rates**: ET=0.0%, EV=0.0%, RoV=0.0%, AC=3.7%, CF=15.3%
- **Trigger F1**: 0.0803, **Argument F1**: 0.0116, **Entity F1**: 0.1795
- **Go/No-go (RoV+AC)**: 3.69%
- **对比 unconstrained** (EV 10.5%, RoV 88.8%): **EV Δ=-10.5pp, RoV Δ=-88.8pp**
- **F1 对比**: Trigger 0.0572→0.0803 (+0.023), Arg 0→0.0116 (+0.012), Entity 0→0.1795
- Parse failure doc IDs (34): 61_VOA_EN_NW_2017.03.22.3777524, 55_VOA_EN_NW_2014.06.30.1947653, 7_VOA_EN_NW_2017.03.07.3753687, wiki_ied_bombings_5_news_4, suicide_ied_105, wiki_drone_strikes_0_news_10, 2_VOA_EN_NW_2015.01.04.2583337, ... (全部34个)

## 补跑状态
- **Qwen retry**: tmux `qwen_constrained_retry`, cuda:0, `--max_new_tokens 8192 --resume` (49 docs to retry), models loaded, processing started
- **Llama retry**: tmux `llama_constrained_retry`, cuda:1, `--max_new_tokens 8192 --resume` (34 docs to retry), models loaded, processing started
- 策略：从输出文件中移除了 `parsed_output=None` 的条目，`--resume` 仅跳过已成功条目

## westd-21461 进度
- **Mistral constrained v2** (cuda:0): 60/246, GPU 83% util
  - 部分RoV验证: ET=0%, EV=0%, RoV=0.1%, **AC=17.1%**, CF=13.7%
  - ⚠️ AC rate 异常高 (对比 Qwen 2.4%, Llama 3.7%)
  - Parse failures: 16/60 (26.7%)
- **Mistral grammar_only** (cuda:1): 154/246, GPU 78% util

---

**关键发现**: Constrained decoding 在 EV 和 RoV 上效果极其显著（接近归零），F1 也全面提升。但 Mistral v2 的 AC 违反率 17.1% 远高于其他模型，需要调查原因。

---
