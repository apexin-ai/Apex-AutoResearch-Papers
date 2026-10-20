# code fix llama eval verified

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix-llama-eval-verified_20260524T045258_result.json`
- **Structured JSON:** [`66af06593505b4b32ce7.json`](../../sessions/66/66af06593505b4b32ce7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

修复已经完成并持久化。以下是完整验证结果：

## 验证结果

### eval_lz.py 修复状态
代码已使用 `re.search(r'contam_(\d+)', args.condition)` 动态匹配，不再硬编码。

### Llama contam_5 完整指标

| 指标 | Overall | Seen (n=702) | Unseen (n=13340) |
|------|---------|-------------|-----------------|
| Accuracy | 0.6342 | **0.7920** | 0.6259 |
| θ (free) | -0.4089 | 0.4024 | -0.4419 |
| lz* (free) | -4.954 | **-1.420** | -4.568 |
| lz* (fixed) | -1.892 | -0.270 | -1.880 |

### Cohen's d（Llama baseline: mean=0.262, SD=1.542）

| 分组 | Cohen's d (free-θ) |
|------|-------------------|
| Overall | **-3.383** |
| Seen | **-1.091** |
| Unseen | **-3.133** |

### 关键确认
- **n_seen = 702**（不是 0）
- **accuracy_seen (0.792) 显著高于 accuracy_unseen (0.626)**，差值 +16.6pp
- **lz\*_seen (-1.420) 远高于 lz\*_unseen (-4.568)**，seen 子集 person-fit 异常程度大幅降低
- 结果文件 `contam_5_results.json` 生成时间 May 24 12:36，已是最新

---
