# code plan 003 data prep

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan_003_data_prep_20260515T045842_result.json`
- **Structured JSON:** [`1b301ab1640d7f213860.json`](../../sessions/1b/1b301ab1640d7f213860.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。

## 产出汇总

### 3 个新数据文件
路径: `/root/autodl-tmp/trace-verdict-study-data/`

| 文件 | 样本数 | 说明 |
|------|--------|------|
| `ae_only_train.jsonl` / `_test.jsonl` | 4720 / 1190 | 只保留 `[ASSERT] actual=X, expected=Y` |
| `exception_only_train.jsonl` / `_test.jsonl` | 4720 / 1190 | 只保留 `[ERROR]` 异常摘要 |
| `loop_only_train.jsonl` / `_test.jsonl` | 4720 / 1190 | 只保留 `[LOOP]` 循环压缩 |

### Token 分布统计

| Condition | Median | Mean | Truncated | Empty Component |
|-----------|--------|------|-----------|-----------------|
| **ae_only** | 1570 | 1398.7 | 27.0% | 2.5% |
| **exception_only** | 228 | 508.5 | 0.9% | 66.7% |
| **loop_only** | 1023 | 1213.2 | 15.4% | 0.0% |

所有数据集 >2048 token 的样本比例: **0.0%**（CHAT_TEMPLATE_OVERHEAD=32 生效）。标签分布: pass 67.0% / fail 33.0%（与 VOTA 一致）。

### 代码变更
- **新增**: `/root/trace-verdict-study/data/format_component_ablation.py` — 从 raw_traces.jsonl 重新处理，调用 VOTACompressor 内部组件方法
- **修改**: `/root/trace-verdict-study/train/train_sft.py` — `--condition` 新增 `ae_only`, `exception_only`, `loop_only` 三个选项

### 注意
- `exception_only` 有 66.7% 的样本没有异常数据（主要是 pass 样本），这对 ablation 是预期行为——如果 exception 信号强，模型应该能学会 "无异常→pass"
- `ae_only` truncation 率 27%，与 full VOTA 类似（ae 是 VOTA 中最大的组件）

---
