# writing r3w1 d0 inflation

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_writing_r3w1-d0-inflation_20260516T010831_result.json`
- **Structured JSON:** [`f82c4307dc70ea11b47a.json`](../../sessions/f8/f82c4307dc70ea11b47a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

验证结果：

| 检查项 | 状态 |
|--------|------|
| Abstract 同时报告含/不含 d0 的 accuracy | **通过** — L5: "70--85% four-class accuracy ... 58.8--82.6% when excluding the near-perfectly separable d0 class" |
| Table 1 含 d1-d3 三分类 accuracy | **通过** — caption 明确 "d1--d3 three-class accuracy in parentheses (chance = 25% / 33%)"，数据行如 `78.2\,(71.2)` |
| Table 5 (cross-model) 含排除 d0 的 balanced accuracy | **通过** — caption: "d1--d3 bal. acc: Pythia 49.9%, OLMo 59.2%, GPT-2~XL 57.2% (mean 55.4%)"；正文 L64-65 明确说明 d0 膨胀 |
| Table 6 (cross-strategy) 含排除 d0 的 accuracy | **通过** — caption: "d0 recall ≥89% inflates headline; d1--d3 mean: 45.9%"；正文 L89 同步 |
| 无仅报 4-class 而不提 d0 inflation 的位置 | **通过** — Table 3 (baselines) 仅报 4-class，但其目的是展示分类器收敛性（spread ≤0.4pp），非 headline claim；Table 4 (e2e) 直接列 per-class F1 使 d0 膨胀可见 |

R3-W1 在 `review_issues.yaml` 中已标记为 `resolved`（L492, resolution_round: 3），resolution 描述准确覆盖全部 5 处修改。无需额外修改。

---
