# check eval progress all 4

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_eval-progress-all-4_20260522T074512_result.json`
- **Structured JSON:** [`5465bd66e3ed5ba36b41.json`](../../sessions/54/5465bd66e3ed5ba36b41.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 进度汇总

| exp_id | GPU | 状态 | 进度 | running_acc | unparseable | ETA (UTC) |
|--------|-----|------|------|-------------|-------------|-----------|
| deepseek-cwm-repo-s123-eval-1epoch | 1 | RUNNING | 4188/9784 (42.8%) | 75.4% | — | ~23:00 |
| deepseek-cwm-repo-s123-e3-eval | 2 | RUNNING | 6612/9784 (67.6%) | 57.0% | 3372/6612 (51.0%) | ~20:00 |
| qwen3-8b-cwm-repo-s123-eval | 0 | RUNNING | 7276/9784 (74.4%) | 67.5%* | 4659/7276 (64.0%) | ~19:25 |
| qwen3-8b-cwm-repo-s456-eval | 3 | RUNNING | 6576/9784 (67.2%) | 66.6% | 3954/6580 (60.1%) | ~20:25 |

\*qwen s123 的 67.5% = 4910 correct / 7276 total（从 jsonl grep 计算，非日志直读）

## GPU 利用率
| GPU | 型号 | 利用率 | 显存占用 |
|-----|------|--------|---------|
| 0 | RTX 5090 | 83% | 22.2/32.6 GiB |
| 1 | RTX 5090 | 100% | 30.4/32.6 GiB |
| 2 | RTX 5090 | 85% | 30.4/32.6 GiB |
| 3 | RTX 5090 | 79% | 22.2/32.6 GiB |

## 关键观察

1. **所有 4 个 eval 都在正常运行**，无一完成。原始 ETA 预估偏乐观，实际都需更久。

2. **unparseable 率极高**：deepseek 3epoch 51%、qwen s123 64%、qwen s456 60%。对比之前 DS s42 的 62.5% 和 DS s456 的 57%，这个趋势一致 — CWM repo-level 任务的 unparseable 率普遍在 50-65%。

3. **deepseek 1epoch 的 running_acc 75.4% 显著高于 3epoch 的 57.0%**，这很值得注意 — 可能 3 epoch 出现了 overfitting（更多 epoch 导致更多 unparseable 输出，acc 反降）。1epoch 目前 unparseable 率尚未从 log 中获取（log 不含该字段），需等完成后确认。

4. **qwen 两个 seed**：s123 的 running_acc 67.5% 略高于 s456 的 66.6%，差距很小，seed 间一致性较好。

---
