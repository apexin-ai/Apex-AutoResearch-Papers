# code add start gen and submit 14b

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_add_start_gen_and_submit_14b_20260517T192822_result.json`
- **Structured JSON:** [`b530130bb8dd546364ff.json`](../../sessions/b5/b530130bb8dd546364ff.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成：

1. **`iterative_train.py` 已修改** — 添加 `--start_gen` 参数，支持从指定 generation 恢复训练（加载前一代 checkpoint，跳过已完成的 gen，收集已有 metrics）
2. **Pythia-1.4B 训练已提交** — 在 `cuda:1` 上运行，从 gen_6 checkpoint 恢复，正在执行 gen_7 的合成数据生成阶段。日志确认 checkpoint 加载成功，已进入 Generation 7/10。

---
