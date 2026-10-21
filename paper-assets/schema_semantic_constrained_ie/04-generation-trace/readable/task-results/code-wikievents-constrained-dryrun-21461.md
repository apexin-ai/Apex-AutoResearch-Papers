# code wikievents constrained dryrun 21461

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_wikievents_constrained_dryrun_21461_20260517T183326_result.json`
- **Structured JSON:** [`8c7cdc739441055babbf.json`](../../sessions/8c/8c7cdc739441055babbf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

7/20 完成。constrained 解码比 unconstrained 慢（每个 sample 约 30-60 秒），这在预期范围内。

总结：

- **WikiEvents constrained dry-run 已成功在 westd-21461:cuda:1 上运行**
- tmux session: `constrained_dryrun`
- 模型: Qwen/Qwen3-8B（通过 hf-mirror.com 下载，约 16GB）
- 模式: `full_s1`（xgrammar + semantic 双层约束）
- 已完成 7/20 samples，GPU 利用率 84%，VRAM 18.9GB
- 输出: `outputs/wikievents_qwen_constrained_dryrun_test20.jsonl`
- 日志: `outputs/constrained_dryrun.log`（因管道缓冲暂未实时更新，但输出文件在正常增长）
- cuda:0 上的 Mistral baseline 似乎已经跑完（0MiB VRAM）

---
