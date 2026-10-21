# eval exp 004 r2 attention extraction

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_exp-004-r2-attention-extraction_20260519T165830_result.json`
- **Structured JSON:** [`876d1b3e45e182b9f632.json`](../../sessions/87/876d1b3e45e182b9f632.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

HGRN2 提取进行中：1% (51/5153)，GPU 10% / 3317 MiB。一切正常。

按 retnet 的速度 (~10 it/s)，HGRN2 ~8 分钟完成，之后自动运行 analysis。

状态汇总：

| Arch | 状态 | 输出文件 |
|------|------|----------|
| GDN | **DONE** | `gdn_attention_patterns.pt` (126MB), `gdn_attention_entropy.csv` (59MB) |
| RetNet | **DONE** | `retnet_attention_patterns.pt` (126MB), `retnet_attention_entropy.csv` (59MB) |
| HGRN2 | **RUNNING** (1%, screen session exp004) | — |

- Screen session: `518663.exp004` (Detached)
- HGRN2 PID: 519463
- Log: `/tmp/exp004.log`
- 脚本链式运行：HGRN2 完成后自动执行 `--analyze`
- Registry: exp-004-r2 = RUNNING
- 已清除上次 Worker 残留的 orphan 进程 (PID 515917/519328)
- 预计 HGRN2 ~8 min + analysis ~1 min = 全部完成约 9 分钟后

---
