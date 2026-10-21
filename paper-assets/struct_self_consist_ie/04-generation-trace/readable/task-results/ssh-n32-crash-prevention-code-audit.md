# ssh n32 crash prevention code audit

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_n32_crash_prevention_code_audit_20260522T152939_result.json`
- **Structured JSON:** [`dbf9a0f4c476a7c59f0f.json`](../../sessions/db/dbf9a0f4c476a7c59f0f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

代码全部读完。以下是分析。

---

## Save 机制分析

**架构**：全部推理结果存在内存，最后一次性写文件。

流程：
1. `run_sampling_pipeline()` → 在内存中完成所有 stochastic sampling (N=32) + greedy sampling (N=1)
2. 结果组装到 `sampled_instances: list[dict]` 列表
3. 最后调用 `save_sampled_results(sampled_instances, output_path)` 一次性写 JSONL
4. **无任何 intermediate checkpoint**——没有 pickle、没有 partial save、没有 batch flush

**Crash 点**：`sampling.py:673`
```python
with open(path, "w", encoding="utf-8") as f:
    for inst in sampled:
        f.write(json.dumps(inst, ensure_ascii=False) + "\n")
```
`ensure_ascii=False` + vLLM 生成的 lone surrogates → UTF-8 编码器拒绝 → `UnicodeEncodeError`。

## 关键发现：fix 并未部署

服务器上的 sampling.py **没有** `errors='replace'`——`grep -n "errors" sampling.py` 返回空。文件仍是原始的 `open(path, "w", encoding="utf-8")`。运行中的 N=32 进程加载的代码 100% 是有漏洞的版本。

## Crash 风险评估

| 问题 | 结论 |
|------|------|
| N=32 save 会 crash 吗？ | **高概率会。** N=16 在 72% save 位置就撞到了 surrogate。N=32 每个 instance 有 2x 更多 samples，遇到 surrogate 的概率更高。 |
| Partial output 可用吗？ | **可用。** 写到 crash 之前的行都是完整有效的 JSONL（每行一个完整 json.dumps 输出）。可以用 `load_sampled_results()` 直接加载。 |
| 能否跳过推理只恢复 save？ | **不行。** 没有中间 pickle/cache。推理结果只存在于 `run_sampling_pipeline()` 的局部变量 `sampled_instances` 里。UnicodeEncodeError 导致进程退出，内存丢失。 |
| 能否热补丁？ | **不可行。** Python bytecode 已编译进内存，修改磁盘文件不影响运行中的进程。理论上可以 gdb attach + py-call 替换函数对象，但风险极高，可能直接 crash 进程。 |
| 完全重跑需要多久？ | 11h / 0.7 ≈ **15.7h 总推理时间**。剩余推理 ~4.7h，加上推理后的 greedy pass + parse + save。 |

## 推荐方案

**继续跑，不要杀进程。同时做两件准备：**

1. **立即修复磁盘上的 sampling.py**，把 line 672 改为：
   ```python
   with open(path, "w", encoding="utf-8", errors="replace") as f:
   ```

2. **准备 rescue 脚本**：N=32 推理完成后（~4.7h），save 大概率 crash。此时：
   - 统计 partial JSONL 已写入行数 → 这些 instance 数据完好
   - 用 `--skip_sampling --samples_path &lt;partial_file>` 先跑 evaluation（拿到部分结果）
   - 如果需要完整数据：用 `--start_index <已保存数> --end_index &lt;total>` 只对缺失 instance 重跑推理（磁盘上已是修复版代码），然后拼接两个 JSONL

**不建议杀掉重跑**的原因：已投入 ~11h；让它跑完后 partial output 至少覆盖 ~70%+ instance（参考 N=16 经验），这些数据可以直接用于评估。最坏情况下只需补跑剩余 ~30% instance（~4-5h），比完全重跑（~15.7h）节省大量时间。

---
