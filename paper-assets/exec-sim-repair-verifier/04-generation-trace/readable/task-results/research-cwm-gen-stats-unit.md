# research cwm gen stats unit

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_cwm-gen-stats-unit_20260513T203918_result.json`
- **Structured JSON:** [`4eaa4f96ffd5db8e5a6c.json`](../../sessions/4e/4eaa4f96ffd5db8e5a6c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结论明确。

```
generation_stats 单位: characters

计算代码: 第215行
    lengths = [len(r["gen_text"]) for r in results]

理由: len(string) 返回字符数，不是 token 数。
      max=7582 > max_new_tokens=1024 是完全合理的——
      1024 tokens 解码后的文本长度可以远超 1024 个字符
      (英文平均 1 token ≈ 4 chars, 代码/traceback 更长)。
      7582 chars ÷ ~4 ≈ 1896 tokens，但因为 max_new_tokens=1024，
      实际上 7582 chars 对应 ≤1024 tokens，即平均每 token ~7.4 chars，
      这对含代码 traceback 的输出是合理的。
```

generation_stats 没有问题，不存在"超出 max_new_tokens"的异常——它统计的就是字符数，不是 token 数。

---
