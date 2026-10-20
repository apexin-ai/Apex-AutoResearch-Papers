# ops figure update dose response

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_figure-update-dose-response_20260519T145652_result.json`
- **Structured JSON:** [`939703d4be498f3fed14.json`](../../sessions/93/939703d4be498f3fed14.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 报告

**1. westd 上找到的文件**

| 文件 | 大小 |
|------|------|
| `mmlu_dose_response.pdf` | 18,954 B |
| `arc_dose_response.pdf` | 26,353 B |
| `baseline_vs_effect.pdf` | 23,713 B |

**2. 图内容确认：5-family 版本**

生成脚本 `/root/autodl-tmp/exp001/analyze_phase2.py` 确认包含 5 个 model family：Phi-4 14.7B, Qwen2.5-14B, Qwen2.5-7B, Gemma-2 9B, OLMo-2 7B。X 轴为 dosage (0/5/25/50/100%)，Y 轴为 accuracy。

**3. "taxonomy" 标签：未发现**，无需修改。

**4. 本地写入文件**（两个目录各 3 个，共 6 个）

- `docs/paper/figures/fig_dose_response.pdf` (18,954 B) — 替换旧版
- `docs/paper/figures/arc_dose_response.pdf` (26,353 B) — 新增
- `docs/paper/figures/baseline_vs_effect.pdf` (23,713 B) — 新增
- `figures/paper/` 下同名副本

**5. 异常：无。** 所有 PDF 通过 header/trailer 验证。

---
