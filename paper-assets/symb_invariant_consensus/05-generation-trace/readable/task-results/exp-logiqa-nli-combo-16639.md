# exp logiqa nli combo 16639

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_logiqa-nli-combo-16639_20260523T165310_result.json`
- **Structured JSON:** [`d5c5b35c3f1082d054d4.json`](../../sessions/d5/d5c5b35c3f1082d054d4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总：

**3 个 NLI verifier × 4 个 generator × 3 个 weight = 36 组实验，全部在 ~3 分钟内跑完。**

核心结论：**0/36 显著**。NLI combo 在 LogiQA 上无效。

| 指标 | LogiQA | ProofWriter (对比) |
|------|--------|-------------------|
| NLI standalone | 26.5–33.0% (近随机) | ~46% |
| Capability gap | −20 to −55pp | +6.8pp (弱 gen) |
| 显著改善 | 0/36 | 多个 |

原因：零样本 NLI 模型不具备 LogiQA 所需的多跳逻辑推理能力，NLI standalone 几乎等于随机猜（25%），无法为 SC 投票提供有信息量的信号。

产出文件：
- `results/logiqa_nli_combo_deberta.json`
- `results/logiqa_nli_combo_bart.json`
- `results/logiqa_nli_combo_roberta.json`
- artifact 已注册 (`art_20260523_2c0e3e`)

注意：cuda:3 当前被占用（83GB），只使用了 CPU。Blackwell GPU 的 DeBERTa 有 nvrtc 编译问题，但 CPU 推理够快（66s/46s/40s per verifier）。

---
