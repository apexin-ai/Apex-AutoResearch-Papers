# ssh scp hf datasets cache

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_scp-hf-datasets-cache_20260519T001721_result.json`
- **Structured JSON:** [`b221a72c460e2bbb70f7.json`](../../sessions/b2/b221a72c460e2bbb70f7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部通过。结果汇总：

| 项目 | 状态 |
|------|------|
| SCP cqa1→westd | 成功（220M, 22s） |
| datasets cache 大小 | 220M（含 hub metadata） |
| evaluate.py --help | 正常，无网络错误 |
| ARC-Challenge test | 1172 items |
| MMLU test | 14042 items |
| GSM8K test | 1319 items |
| HumanEval test | 164 items |

4 个 benchmark 的离线加载全部验证通过，`HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1` 模式下从 `/root/autodl-tmp/.hf_cache` 正常读取 cached 数据。cqa1 临时文件已清理。

---
