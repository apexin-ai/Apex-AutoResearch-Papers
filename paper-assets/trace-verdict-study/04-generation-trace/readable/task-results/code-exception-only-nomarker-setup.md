# code exception only nomarker setup

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exception_only_nomarker_setup_20260516T153751_result.json`
- **Structured JSON:** [`9e6104b4c46961f185d7.json`](../../sessions/9e/9e6104b4c46961f185d7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验已提交并正在运行。总结：

**代码修改**：更新了 `data/nomarker/prepare_nomarker_data.py`，从仅移除 `[No exception data in trace]` 扩展为移除所有 4 类 bracket-enclosed format markers：

| Marker | 影响样本数(train) | 处理方式 |
|--------|----------|---------|
| `[No exception data in trace]` | 3099 (pass) | 整行移除 |
| `[ERROR]` prefix | 1391 (fail) | 去除前缀，保留异常内容 |
| `[No trace available]` | 230 | 整行移除 |
| `[...trace truncated...]` | 43 | 整行移除 |

**数据验证**：4720 train + 1190 test，全部 5910 样本处理后零残留 marker。
- Pass 样本：`Execution trace:\n\n` （空 trace，无 marker）
- Fail 样本：`AssertionError at line 10: ...` （异常语义保留，`[ERROR]` 前缀移除）

**实验提交**：tmux session `nomarker_seed42`，GPU cuda:0，已启动训练（444 steps, ~80min），训练完成后自动运行 eval。需要 `--gradient_checkpointing` 因为 GPU 0 可用内存约 46GB。

---
