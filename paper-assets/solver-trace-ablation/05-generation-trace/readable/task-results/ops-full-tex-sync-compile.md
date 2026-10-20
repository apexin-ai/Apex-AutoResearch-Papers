# ops full tex sync compile

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_full-tex-sync-compile_20260515T163130_result.json`
- **Structured JSON:** [`129162e025855f26d6f0.json`](../../sessions/12/129162e025855f26d6f0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Label warning 已消除。

## 报告

### 编译结果
- **状态**: 成功
- **页数**: 16
- **文件大小**: 534,695 bytes (~522 KB)

### 数字一致性检查

| 检查项 | 结果 | 位置 |
|--------|------|------|
| H7 rate = 69.7% (非旧版 64.5%) | 通过 | experiments.tex:68,157; introduction.tex:27,33; conclusion.tex:5,16; abstract.tex:7 |
| SFT prove rate = 13.0% (非 14%) | 通过 | experiments.tex:34; introduction.tex:23 |
| SFT non-hacking = 92.2% (非 92.9%) | 通过 | experiments.tex:34; introduction.tex:23 |
| eight-mode taxonomy (非 seven) | 通过 | method.tex:71; experiments.tex:11,156 |
| seed~42 qualifiers | 通过 | experiments.tex:19,24,68,84,128,152,157; conclusion.tex:5,16; introduction.tex:33 |
| 500-step qualifiers for H7 | 通过 | experiments.tex:9,26,68,84,157; conclusion.tex:5,16; abstract.tex:7 |

### 编译 Warnings
- `h` float specifier changed to `ht` (3 处) — 无害，LaTeX 标准行为
- hyperref token warnings (7 处) — 来自 section title 中的数学符号，不影响输出
- 无 Error，无 Label 问题

---
