# gpu exp 062 gemma27b run

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_gpu_exp-062-gemma27b-run_20260519T084441_result.json`
- **Structured JSON:** [`fccb877a83d4a2bfed26.json`](../../sessions/fc/fccb877a83d4a2bfed26.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全量运行已确认启动。

## 总结

**exp-062-gemma27b-folio204 全量运行已启动。**

执行过程中解决了两个问题：

1. **vLLM `max-model-len=4096` 过小** — trace generation 的 `max_tokens=4096` 占满全部上下文导致 400 错误；降至 2048 后 constraint extraction 的 prompt（含完整 trace ~2000+ tokens）又超限。重启 vLLM 用 `--max-model-len 8192` 解决。

2. **`build_extractor()` 未传递 `max_tokens`** — extractor 默认用 4096，和 generator 脱节。已 patch `run_full_mvp.py` 使 extractor 也使用命令行传入的 `max_tokens`。

**Dry-run 结果（3/3 正确）：**
| Problem | GT | SICA | SC | SC votes |
|---------|---------|------|------|----------|
| folio_0 | Unknown | V | V | 11/12 |
| folio_1 | True | V | V | 5/12 |
| folio_2 | False | V | V | 10/12 |

**全量运行配置：**
- tmux: `exp062_run` (pipeline) / `exp062_vllm` (vLLM server)
- GPU: cuda:3, RTX PRO 6000 (98GB)
- 预计耗时: ~6-7 小时（~122s/problem * 204）
- Registry: RUNNING

---
