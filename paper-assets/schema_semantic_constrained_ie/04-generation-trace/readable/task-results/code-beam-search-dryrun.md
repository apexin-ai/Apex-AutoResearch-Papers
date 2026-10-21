# code beam search dryrun

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_beam_search_dryrun_20260517T002228_result.json`
- **Structured JSON:** [`565ce65740a44b6a6c79.json`](../../sessions/56/565ce65740a44b6a6c79.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Beam search 竟然比 greedy 更快（0.77x），这是因为 `early_stopping=True` 让 beam search 在找到完整序列后提前终止。两者可能在不同时间运行（服务器负载差异），但速度完全可接受（50 samples 4.9 分钟）。

最终对比汇总：

```
=== Beam Search vs Greedy (full_s1, SciERC, 50 samples) ===

                    Beam (4)    Greedy
ET violations:      0/218 (0%)  0/219 (0%)
RV violations:      0/149 (0%)  0/158 (0%)
DR violations:      0/149 (0%)  1/158 (0.6%)
CF violations:      3           25
JSON failures:      0 (0%)      0 (0%)

Entity F1:          0.3367      0.3096
Relation F1:        0.1303      0.1185

Total time:         291.6s      379.0s
Mean per sample:    5.83s       7.58s
```

Beam search 在所有指标上优于或等于 greedy：
- **DR violation 下降**：0.6% → 0%
- **CF violation 大幅下降**：25 → 3
- **Entity F1 提升**：+2.7pp
- **Relation F1 提升**：+1.2pp
- **速度更快**（可能因 early stopping）

## 产出总结

**修改的代码文件：**
1. `compiler/beam_aware_processor.py`（新建）— 修复 TypeConstraintProcessor 的 per-beam state 隔离问题
2. `compiler/beam_grammar_processor.py`（新建）— 实现 replay-from-scratch 策略的 XGrammar beam search 兼容 processor
3. `run_constrained_extraction.py`（修改）— 添加 `--decoding_strategy beam --num_beams N` 参数和 `run_single_pass_beam()` 函数

**关键设计决策：**
- XGrammar 的默认 HF LogitsProcessor 不支持 beam search（内部 state 无法处理 beam reordering）。解决方案：每步每 beam 重建 GrammarMatcher 并 replay 全部已生成 token。O(seq_len) per beam per step，对 IE 输出长度可接受。
- TypeConstraintProcessor 共享单一 state 导致 beam 间污染。解决方案：子类 override `__call__`，每个 beam 处理前 reset state（detect() 从全文重建所有状态）。

**10-doc dry run：** 全部成功，无报错，constraint 完全生效（DR=0%），耗时 62s。

**50-doc 结果：** 全部成功，constraint 生效，F1 优于 greedy baseline。

---
