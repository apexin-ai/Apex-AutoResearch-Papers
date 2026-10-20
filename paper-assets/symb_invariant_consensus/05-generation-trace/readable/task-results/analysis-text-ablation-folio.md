# analysis text ablation folio

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_text-ablation-folio_20260521T021006_result.json`
- **Structured JSON:** [`9e1fafa64969a3590622.json`](../../sessions/9e/9e1fafa64969a3590622.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验已在 westd-25068 上稳定运行 (PID 452128)。

**当前状态**：
- T_ext=0.1 正在处理，第 1/204 个问题完成
- 每个问题约 26s（12 traces × extraction）
- 每个 T_ext 约 89 min，共 4 个值需运行（0.1, 0.5, 0.7, 1.0），T_ext=0.3 直接用 exp033 已有结果
- 预计总耗时约 **6 小时**
- 结果将保存到 `/root/symb_invariant_consensus/results/text_ablation_results.json`

**已有 baseline (T_ext=0.3)**：
- SC: 54.41% (111/204)
- SICA: 59.31% (121/204)  
- Δpp: +4.9

可以稍后用 `tail -20 /root/symb_invariant_consensus/results/text_ablation.log` 查看进度。实验完成后我会提取结果并生成最终 JSON 到本地 artifacts 目录。

要我现在做其他事情，还是等实验完成后再继续？

---
