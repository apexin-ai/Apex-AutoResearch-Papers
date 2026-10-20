# diagnose c4 entropy check

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_c4_entropy_check_20260514T082648_result.json`
- **Structured JSON:** [`e28af0518f91b7458b1c.json`](../../sessions/e2/e28af0518f91b7458b1c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**c4_entropy 实验已完成。** 进程 93190 已退出。

结果摘要：

- **总耗时**: 69.1 min，30/30 problems 全部完成
- **完成时间**: 2026-05-14 16:26:16
- **产出文件**: `/root/autodl-tmp/pacs/results/c4_attention_entropy/c4_entropy_results.json` (1.7MB)
- **GPU 状态**: cuda:1 已释放（0% 利用率，0 MiB 显存）

关键结果：

| Config | Entropy Δ | Gini Δ | CV Δ |
|--------|-----------|--------|------|
| s015 importance | -0.0402 | -0.0301 | -0.564 |
| s015 random | +0.1283 | -0.0309 | -1.021 |
| s020 importance | -0.0472 | -0.0404 | -0.774 |
| s020 random | +0.1360 | -0.0403 | -1.203 |
| s025 importance | -0.0446 | -0.0647 | -1.287 |
| s025 random | +0.2171 | -0.0620 | -1.923 |
| s030 importance | -0.0436 | -0.0806 | -1.665 |
| s030 random | +0.2327 | -0.0732 | -2.137 |

Importance pruning 一致性地**降低** entropy（注意力分布更集中），random pruning **增加** entropy（分布更散），且差异随 sparsity 增大而扩大。符合预期假设。

---
