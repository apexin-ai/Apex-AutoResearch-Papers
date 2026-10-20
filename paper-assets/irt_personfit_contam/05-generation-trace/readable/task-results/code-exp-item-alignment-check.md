# code exp item alignment check

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp-item-alignment-check_20260520T101720_result.json`
- **Structured JSON:** [`ec5a5e8344406a8adbf7.json`](../../sessions/ec/ec5a5e8344406a8adbf7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验完成。结论: **negative** — 直接位置对齐不可行。

核心发现:

| 指标 | 结果 |
|------|------|
| 直接位置匹配率 | 54.56% (≈随机) |
| Content-based 重排后 (Mistral) | 88.46% |
| Content-based 重排后 (Vicuna) | 72.48% |
| 可映射 items | 12068/14042 (86%) |

**原因**: PSN-IRT 和 v1 leaderboard 都按 MMLU subject 字母序分组，但 v1 在 subject 内部 shuffle 了 items。更重要的是，即使 content-based 对齐后仍有 ~12% 不一致——PSN-IRT 是独立评测，不是复用 v1 leaderboard 数据。Vicuna 的 8% 准确率差距进一步证实了不同的评测协议。

**建议**: 使用 PSN-IRT 自己的 combine.csv 配合自己的 item 参数（内部一致）。混用 v1 responses + PSN-IRT parameters 会引入 ~10% 噪声。

---
