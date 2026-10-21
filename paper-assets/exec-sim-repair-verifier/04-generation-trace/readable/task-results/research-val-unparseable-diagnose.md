# research val unparseable diagnose

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_val-unparseable-diagnose_20260514T145443_result.json`
- **Structured JSON:** [`1e060b1c5bce9e83a6bf.json`](../../sessions/1e/1e060b1c5bce9e83a6bf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Job 正在运行，进度正常。

## 诊断结论

### 根因：100% 由输入截断导致

| 指标 | Val (n=9335) | Test (n=9784) |
|------|-------------|--------------|
| Mean prompt tokens | 1252 | 902 |
| Max prompt tokens | **8768** | 2481 |
| P90 | 4865 | 2041 |
| >2048 tokens | **1883 (20.2%)** | 484 (4.9%) |
| >4096 tokens | 1406 (15.1%) | 0 (0%) |

**完全重合**：1883 unparseable = 1883 truncated，0 例外。截断后输入丢失了 generation prompt 和问题结构，模型生成空文本，parse 失败，回退到 majority class。

### Val 长度分布呈双峰

| 截断阈值 | >阈值样本数 | 占比 |
|---------|-----------|------|
| 2048 | 1883 | 20.2% |
| 3072 | 1406 | 15.1% |
| 4096 | 1406 | 15.1% |
| 5120 | 234 | 2.5% |
| 6144 | 36 | 0.4% |

3072-4096 之间无样本，存在明显 gap。**5120 是性价比最优阈值**（unparseable 从 15.1% 降到 2.5%）。

### 已有 val eval 汇总

| Checkpoint | val@2048 (acc) | val@4096 (acc) | unparseable |
|-----------|---------------|---------------|-------------|
| ckpt-400 | 80.72% | 82.57% | 1883→1406 |
| ckpt-600 | 76.78% | 79.18% | 1883→1406 |
| ckpt-800 | 81.81% | **running** | — |
| ckpt-1000 | 82.30% | — | — |

### 已启动任务

- **ckpt-800 val@4096** — PID 3125543，正在运行，running_acc=85.0% @ 160/9335

### 建议

1. `build_prompt_ids` 的截断方式有问题：`ids[:max_len]` 从末尾砍，丢失 generation prompt。应改为**截断输入内容而非整个 prompt**（保留 system prompt + 问题结构 + generation prompt，只砍 code/test 内容）。
2. 长期方案：val eval 统一用 **5120**（2.5% unparseable），或修复截断逻辑后用 4096。

---
