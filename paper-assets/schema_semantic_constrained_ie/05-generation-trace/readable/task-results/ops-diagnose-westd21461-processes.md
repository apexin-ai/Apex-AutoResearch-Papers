# ops diagnose westd21461 processes

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_diagnose_westd21461_processes_20260516T052728_result.json`
- **Structured JSON:** [`ea8c0b3dd106624eb839.json`](../../sessions/ea/ea8c0b3dd106624eb839.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。汇报如下：

---

## westd-21461 诊断结果

### 1. 进程列表

| PID | GPU | 模式 | 数据集 | 输出文件 | 启动时间 |
|-----|-----|------|--------|----------|----------|
| 5576 (父: 5571) | GPU 0 | unconstrained | docred | w6_mistral_docred_unconstrained.jsonl | 13:22:54 |
| 6794 (父: 6789) | GPU 1 | full_s1 (constrained) | docred | w6_mistral_docred_constrained.jsonl | 13:24:48 |

- PID 6126, 6279: **已不存在**（之前的进程已结束）
- 无 tmux session

### 2. 重复进程：**无**

每卡各一个 python3 进程，互不冲突：
- GPU 0 (90% util, 15.3GB/97.9GB): unconstrained 实验
- GPU 1 (88% util, 15.3GB/97.9GB): constrained 实验

两个进程写不同输出文件，无重复写入风险。

### 3. 输出文件状态

| 文件 | 大小 | 行数 | 状态 |
|------|------|------|------|
| w6_mistral_docred_unconstrained.jsonl | 219KB | 33 | 正常写入中 |
| w6_mistral_docred_constrained.jsonl | 108KB | 15 | 正常写入中 |
| w6_mistral_scierc_constrained.jsonl | 0B | 0 | 空文件，无进程写入 |

scierc 文件可能是之前创建后未启动实验，或等待队列。

### 4. xgrammar fix 状态：**已应用**

xgrammar 0.2.0 的 `hf.py:95` 中已使用 `.item()`：
```python
sampled_token = input_ids[i][-1].item()
assert self.matchers[i].accept_token(sampled_token)
```

此外 `run_constrained_extraction.py` 中有 AssertionError fallback 机制——如果 accept_token 仍失败，自动降级为 grammar-only 模式。

### 5. 结论

**安全，无需干预。** 两个实验各自独占一张 GPU，写不同文件，正常运行中。日志无报错（仅有正常的 pad_token_id 警告）。

---
