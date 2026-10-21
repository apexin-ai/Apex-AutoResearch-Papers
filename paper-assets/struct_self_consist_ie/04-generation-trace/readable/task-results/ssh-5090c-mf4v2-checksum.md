# ssh 5090c mf4v2 checksum

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_5090c_mf4v2_checksum_20260521T175343_result.json`
- **Structured JSON:** [`bcda4da8a76448d8521c.json`](../../sessions/bc/bcda4da8a76448d8521c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果汇总：

| 文件 | 行数 | 大小 | N_samples | MD5 | Valid | Invalid |
|------|------|------|-----------|-----|-------|---------|
| `conll_mf4v2_seed42/samples.jsonl` | 3453 | 56.9 MB | [8] | `8c3ff024f4abf11968176dd7e3af308d` | 3453 | 0 |
| `conll_mf4v2_s42_rerun/samples.jsonl` | 3453 | 56.9 MB | [8] | `4159462c2a3b5d73040562b7188eaf36` | 3453 | 0 |

两个文件均通过完整性检查：
- 行数一致（3453 行），每行 JSON 格式有效，必要字段（id/gold/samples/greedy）齐全
- 每条样本 N_samples=8，符合预期
- **MD5 不同**：说明两次推理结果不完全相同（seed42 原始 vs rerun），符合 sampling 的随机性预期
- 结果已保存到 `/root/autodl-tmp/struct_self_consist_ie/mf4v2_checksum_5090c.txt`

注意：5090-c 上只有 **conll** 的 MF4v2 数据（2个目录），未发现 fewnerd_mf4v2 或 scierc_mf4v2 文件。

---
