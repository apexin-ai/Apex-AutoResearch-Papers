# fix d112 shard0 restart cuda3

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_d112_shard0_restart_cuda3_20260519T000608_result.json`
- **Structured JSON:** [`8ab5a46bd6a97181edfa.json`](../../sessions/8a/8ab5a46bd6a97181edfa.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 更新完成。

**汇报：**

| 项目 | 结果 |
|---|---|
| 非分片 run (PID 584466) | 已 kill，cuda:3 释放 |
| 已有数据 | 288 docs / 2304 行，已移至 `shard_0/`，全部在 shard 0 范围内 |
| shard 0 重启 | 成功，tmux `d112_gen_shard0`，cuda:3，resume 模式，剩余 468 docs |
| step2 合并 | `rsft_score_filter.load_generations` 已原生支持 `shard_*/generations.jsonl` 自动合并去重，无需额外脚本 |
| 4 卡状态 | cuda:0 = shard 3, cuda:1 = shard 1, cuda:2 = shard 2, cuda:3 = shard 0，全部正常运行 |
| Registry | `d112_rsft_s44_generate` → conclusion=killed, status=DONE |

---
