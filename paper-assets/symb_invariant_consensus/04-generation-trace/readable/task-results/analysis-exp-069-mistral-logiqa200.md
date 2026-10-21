# analysis exp 069 mistral logiqa200

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp-069-mistral-logiqa200_20260519T131439_result.json`
- **Structured JSON:** [`34b2ebfc3b02d49ae2c6.json`](../../sessions/34/34b2ebfc3b02d49ae2c6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

没有 McNemar 和 W&B 数据。所有核心信息已收集完毕。

## exp-069-mistral-logiqa200 分析结果

**模型**: Mistral-7B-Instruct-v0.3
**数据集**: LogiQA-200
**SC accuracy**: 49.50% (99/200)
**SICA accuracy**: 46.50% (93/200)
**Delta (SICA - SC)**: **-3.00pp**
**McNemar p-value**: 未输出
**Conclusion**: **negative**

**理由**:
1. SC = 49.5%，低于 Goldilocks zone 预测的 55-65% 下界。Mistral 在 LogiQA 上的基线能力不足。
2. Delta = -3.0pp，SICA **劣于** SC，方向与 hypothesis 完全相反。SICA 的约束提取在模型能力不足时引入了噪声，反而损害了准确率。
3. 对比 FOLIO-204 结果（SC≈55%, Δ=+4.90pp）：Goldilocks zone 假说未能跨数据集验证——Mistral 在 LogiQA 上的 SC 基线过低，不满足 Goldilocks 条件。

**Extraction 质量**: 2312/2397 成功 (96.5%)，fail_empty=61 最多，说明约束提取本身运行正常，问题在于模型能力不足导致提取的约束质量差。

**Checkpoint/Log 路径**:
- results: `/root/symb_invariant_consensus/results/exp069_mistral_logiqa200/exp069_results.json`
- intermediates: `/root/symb_invariant_consensus/results/exp069_mistral_logiqa200/intermediates/` (200 files, 全量)
- log: `/root/symb_invariant_consensus/results/exp069_mistral_logiqa200/exp069_run.log`
- W&B: 未集成

**GPU 状态**:
| GPU | 型号 | 显存占用 | 利用率 |
|-----|------|---------|--------|
| 0 | RTX PRO 6000 Blackwell (96GB) | 88.3GB | 96% |
| 1 | RTX PRO 6000 Blackwell (96GB) | 88.1GB | 0% |
| 2 | RTX PRO 6000 Blackwell (96GB) | 88.3GB | 0% |
| 3 | RTX PRO 6000 Blackwell (96GB) | 88.1GB | 96% |

**vLLM 进程状态**: GPU 1 占用 88GB 但利用率 0%，大概率 vLLM 仍在内存中空转（exp069 使用 cuda:1 + port 8001）。建议清理释放显存。

---
