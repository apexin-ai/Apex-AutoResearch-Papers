# check debugbench readiness

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_debugbench_readiness_20260515T235904_result.json`
- **Structured JSON:** [`cbb0f32609d60ebf87c7.json`](../../sessions/cb/cbb0f32609d60ebf87c7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇报如下：

## Part 1: DebugBench VOTA 数据 — 就绪

| 文件 | 行数 | 预期 | 状态 |
|------|------|------|------|
| `debugbench_vota_train.jsonl` | 1622 | 1622 | 匹配 |
| `debugbench_vota_test.jsonl` | 426 | 426 | 匹配 |

数据完全就绪。

## Part 2: 训练进度

### full_trace_256tok_seed42 (pid=187860) — 已完成，进入 eval

- 训练 3/3 epoch, 444/444 steps 已完成
- train_loss: 0.1094, eval_loss: 0.2676, mean_token_accuracy: 95.3%
- 模型已保存到 `full_trace_256tok/final`
- 当前状态：**正在加载 checkpoint 进行评估**（Loading checkpoint shards），进程 CPU=0.0% 说明在等待 GPU 推理
- 运行时长：53 分 26 秒

### full_trace_512tok_seed42 (pid=197608) — 训练中

- 当前 epoch 2/3，step 356/444（80%）
- 速度：~6.75s/it
- 剩余 steps：88，预计剩余 ~10 分钟完成当前 epoch
- 还需完成 epoch 3（148 steps, ~16 分钟）+ eval
- **预计总剩余：~30 分钟**
- 运行时长：43 分 12 秒，CPU 102%（正常训练中）

## Part 3: 代码兼容性 — 已支持

`train_sft.py` 和 `evaluate.py` 的 `--condition` 参数均已包含 DebugBench 相关选项：
- `debugbench_no_trace`
- `debugbench_vota`
- `debugbench_full_trace`
- `debugbench_ae_only`
- `debugbench_exception_only`

无需额外修改，直接用 `--condition debugbench_vota` 即可启动训练。

---
