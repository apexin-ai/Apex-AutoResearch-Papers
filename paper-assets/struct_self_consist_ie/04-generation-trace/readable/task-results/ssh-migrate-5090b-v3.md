# ssh migrate 5090b v3

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_migrate_5090b_v3_20260521T104244_result.json`
- **Structured JSON:** [`64cbaa35adfaa1b9abbf.json`](../../sessions/64/64cbaa35adfaa1b9abbf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

迁移完成。报告如下：

## 迁移报告：bjb2-11496 → autodl-5090

**目标路径**: `/root/autodl-tmp/struct_self_consist_ie/output_from_5090b/`  
**传输方式**: rsync via 公网 (connect.bjb2.seetacloud.com:11496)  
**总量**: 1.4G（压缩传输 151MB）

| 实验目录 | 大小 | 数据集 | greedy_f1 | oracle_f1 | headroom | verdict |
|---|---|---|---|---|---|---|
| conll_mf4v2_seed123 | 56M | conll2003 | 0.908 | 0.953 | 0.044 | **PASS** |
| conll_mf4v2_seed456 | 56M | conll2003 | 0.907 | 0.943 | 0.036 | **PASS** |
| fewnerd_mf4v2_seed42 | 642M | fewnerd | 0.788 | 0.878 | 0.090 | FAIL |
| fewnerd_mf4v2_seed123 | 653M | fewnerd | 0.788 | 0.889 | 0.101 | MARGINAL |
| scierc_mf4v2_seed42 | 20M | scierc | 0.663 | 0.781 | 0.118 | MARGINAL |
| fewnerd_mf4v2_seed456 | — | — | — | — | — | **源端为空目录，未迁移** |

5/6 目录迁移成功，文件大小与源端一致。`fewnerd_mf4v2_seed456` 在 bjb2-11496 上就是空目录（0 字节）。

---
