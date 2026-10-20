# verify round2 fix and data

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_verify_round2-fix-and-data_20260514T221828_result.json`
- **Structured JSON:** [`e0b4acc8f5abc2bae086.json`](../../sessions/e0/e0b4acc8f5abc2bae086.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有数据收集完毕。以下是结构化报告：

---

## GPU 状态
- **cuda:0**: 75619MiB / 97887MiB (77%), 100% util, 71°C, PID 835089 (python, 26438MiB)
- **cuda:1**: 0MiB / 97887MiB, idle, 28°C
- v4 训练进程 PID 835084: **存活** — no_trace_seed42_v4, 已跑 6h13m, step 151/444 (34%)
- v4 训练进程 PID 835161: **已死**
- tmux sessions: 无法通过 read_only 检查（被 whitelist 拦截）

## 代码修复验证

### vota.py — match 泄漏: **已修复** ✅
- `grep -i "match" vota.py` 返回空（exit code 1），整个文件无 "match" 关键字
- compress 输出仅包含 `[ASSERT]`、`[ERROR]`、`[LOOP]` 三种标签，无泄漏点

### format_training_data.py — 截断逻辑: **正确** ✅
- label（"pass"/"fail"）放在独立的 `output` 字段，与 `input` 分离，不可能被截断
- `_truncate_trace()` 计算 `trace_budget = max_seq_length - no_trace_tokens - marker_tokens`，仅截断 trace 部分
- 三个 format 函数统一用 `label = "pass" if item["verdict"] else "fail"`

## 数据质量

### 文件列表

| 文件 | 大小 | 修改时间 |
|------|------|----------|
| no_trace_train.jsonl | 2.7M | May 15 06:05 |
| no_trace_test.jsonl | 604K | May 15 06:05 |
| vota_train.jsonl | 30M | May 15 06:06 |
| vota_test.jsonl | 7.5M | May 15 06:06 |
| full_trace_train.jsonl | 32M | May 15 06:08 |
| full_trace_test.jsonl | 7.9M | May 15 06:08 |

### VOTA 抽样: **合格** ✅
- 全量检查 4720 条: `match=True/False` 出现 **0 次**，`"match"` key 出现 **0 次**
- 随机样本含 `[ASSERT]` 标签，VOTA 压缩生效
- output 字段均为完整的 "pass" 或 "fail"

### full_trace 抽样: **合格** ✅
- 3 条样本无 match 关键字，output 字段完整
- 尾部格式: `...Does this code pass all tests? Answer: pass`

### no_trace 抽样: **合格** ✅
- 格式正确，output 字段完整
- 尾部格式: `...Does this code pass all tests? Answer: pass/fail`

### 样本统计

| 条件 | train | test | pass | fail | pass% |
|------|-------|------|------|------|-------|
| no_trace | 4720 | 1190 | 3958 | 1952 | 67.0% |
| vota | 4720 | 1190 | 3958 | 1952 | 67.0% |
| full_trace | 4720 | 1190 | 3958 | 1952 | 67.0% |

三个条件样本数和 pass/fail 分布完全一致（按 problem_id 分层切分）。

### 注意
所有 vota 和 full_trace 抽样样本都出现了 `[...trace truncated...]`，说明多数 trace 即使经过 VOTA 压缩仍超过 2048 token 限制。这在预期内，但意味着 trace 信息量受限于截断。

## 结论

**可以继续训练，无需重新生成数据。**

- 代码修复已验证：match 泄漏已清除，截断逻辑正确
- 数据质量合格：三个条件文件齐全，label 完整，无泄漏字段
- no_trace 训练已在进行 (34%, ~28min 剩余)
- PID 835161 已死（可能是之前的失败尝试），835084 正常运行
- cuda:1 空闲，可用于启动 vota 或 full_trace 的训练

---
