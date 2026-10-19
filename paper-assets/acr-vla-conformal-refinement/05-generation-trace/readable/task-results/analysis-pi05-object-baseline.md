# analysis pi05 object baseline

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_pi05-object-baseline_20260521T114246_result.json`
- **Structured JSON:** [`1af50f9b3b6a1b1fffff.json`](../../sessions/1a/1af50f9b3b6a1b1fffff.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。汇总结果：

## π0.5 VLA-only Object Baseline 结果

### 三个 seed 结果一致：全部 0.0% SR

| Seed | Overall SR | Total Rollouts | Status |
|------|-----------|----------------|--------|
| 42 | 0.0% (0/200) | 200 | EXIT_CODE=0 |
| 43 | 0.0% (0/200) | 200 | EXIT_CODE=0 |
| 44 | 0.0% (0/200) | 200 | EXIT_CODE=0 |

**Mean ± Std: 0.0% ± 0.0%**

所有 10 个 task 的 per-task SR 均为 0.0%，无一例外。

### 根因分析

**这不是合理的实验结果，而是模型推理失败。** 排查发现：

1. **代码层面没有明显 bug** — image flip (line 158), action queue replay, normalizer 都在
2. **没有 runtime error** — 无 CUDA OOM，无异常，EXIT_CODE=0
3. **关键线索：`policy_preprocessor.json` 差异**
   - bjb2（D103 72% quick verify 所在服务器）：tokenizer_name 被手动改为 `/root/autodl-tmp/.ms_cache/AI-ModelScope/paligemma-3b-pt-224`
   - bjb1（当前 3 个实验）：仍为 `google/paligemma-3b-pt-224`（离线模式下可能加载失败）
4. **D103 的 72% 只是 bjb2 上的手动 quick verify，不在这些 log 文件中**

### Registry 状态

Registry 已有这 3 个实验的记录，全部标记为 `DONE` + `conclusion: failed`。无需再次更新。

### 建议

π0.5 baseline 需要在 bjb1 上排查 `from_pretrained` 是否因 tokenizer 路径问题导致模型部分初始化失败。可能需要：
1. 将 bjb1 上的 `policy_preprocessor.json` 的 tokenizer_name 改为本地路径（与 bjb2 一致）
2. 或者在 bjb2 上用已验证的环境重跑 3-seed full eval

---
