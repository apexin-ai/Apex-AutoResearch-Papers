# code add seed param

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_add-seed-param_20260515T140410_result.json`
- **Structured JSON:** [`1383b0895b3530014cb1.json`](../../sessions/13/1383b0895b3530014cb1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。修改了 2 个文件：

**`run_full_mvp.py`**：
- 添加 `--seed SEED` 参数（int, default=None）
- main() 开头设置 `random.seed()` + `np.random.seed()`
- `build_generator()` 传递 `seed=args.seed` 给 VLLMGenerator 和 APIGenerator

**`sica/trace_generator.py`**：
- `VLLMGenerator.__init__` 接收 `seed` 参数，存为 `self.seed`
- `_generate_n_batch()` 和 `_generate_single()` 将 seed 传递到 OpenAI API 调用
- `APIGenerator.__init__` 同样接收和存储 seed
- `APIGenerator.generate()` 将 seed 传递到 API 调用

`--help` 确认 `--seed` 参数正常显示。import 验证通过。`pipeline.py` 无需修改（seed 已内置在 generator 实例中）。

---
