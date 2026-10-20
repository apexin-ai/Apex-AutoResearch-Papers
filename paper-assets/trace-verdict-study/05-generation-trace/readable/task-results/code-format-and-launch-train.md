# code format and launch train

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_format-and-launch-train_20260514T173457_result.json`
- **Structured JSON:** [`b7c8fd59e3d26aa6d114.json`](../../sessions/b7/b7c8fd59e3d26aa6d114.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**no_trace 训练已开始** — 0/444 steps, ~2.8s/it。vota 还在 tokenization（较慢因为 trace 更长）。

两个任务都正常运行，训练配置：
- no_trace: 444 steps (4720 samples / batch 4 / accum 8 × 3 epochs ≈ 444), ~3s/step ≈ 22 分钟
- vota: tokenization 更慢但正常推进

---

## 汇报

### 1. Verdict 标签验证
- 原始数据 verdict 为布尔值：`true`=3958 (67.0%), `false`=1952 (33.0%), 共 5910
- 映射逻辑 `"pass" if item["verdict"] else "fail"` 正确，无需修改

### 2. 格式化数据统计

| 条件 | Train | Test | pass | fail | avg tokens | p50 | p95 | max | >2048截断率 |
|------|-------|------|------|------|-----------|-----|-----|-----|-----------|
| no_trace | 4720 | 1190 | 3107 | 1613 | 178 | 151 | 370 | 1260 | 0.0% |
| vota | 4720 | 1190 | 3107 | 1613 | 3070 | 2573 | 6423 | 9828 | 88.7% |
| full_trace | 4720 | 1190 | 3107 | 1613 | 9033 | 6350 | 17101 | 284984 | 94.9% |

- 标签 "pass"=[6385] "fail"=[18403] 均为单 token ✓
- 6 个文件全部生成 ✓

### 3. 训练提交

| Job ID | 条件 | GPU | PID | 状态 |
|--------|------|-----|-----|------|
| no_trace_seed42_v3 | no_trace | cuda:0 | 710523 | 训练中 (0/444 steps) |
| vota_seed42_v3 | vota | cuda:1 | 710601 | tokenizing |

- 日志：`~/runs/trace-verdict-study/{no_trace_seed42_v3,vota_seed42_v3}.log`
- 报告：tensorboard（W&B 未配置，已自动回退）

### 4. 修复记录
- **import 修复**：`format_training_data.py` 添加 `/root/trace-verdict-study` 到 sys.path（vota.py 需要 `from src.assert_decompose`）
- **TRL 兼容**：`max_seq_length` → `max_length`（TRL 1.1.0 参数更名）
- **W&B 回退**：`report_to` 改为条件判断，无 API key 时回退 tensorboard
- **warning**：`torch_dtype` deprecation（无影响）；vota/full_trace 截断率高（88.7%/94.9%），MVP 可接受

---
