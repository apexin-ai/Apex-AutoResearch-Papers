# ssh ced score shard1

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_ced-score-shard1_20260515T044134_result.json`
- **Structured JSON:** [`25814ad414d8bf793a51.json`](../../sessions/25/25814ad414d8bf793a51.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Scoring 正常推进中。进度模式稳定（~3.5 min / 500 records），预计 ~13:21 完成。

**当前状态汇总：**
- 进程 PID 156417 在 cuda:1 上运行 CED scoring
- 输入：shard_1, 5552 records, 694 unique docs
- 进度：2000/5552 (36%)，速率 ~3.5 min/500 records
- 预计完成：~13:21（还需 ~25 分钟）
- 无错误，进程稳定

完成后输出将写入 `/root/autodl-tmp/rsft_scored_s1/`：
- `rsft_scores.jsonl`：带分数的完整记录
- `rsft_train.jsonl`：筛选后的 SFT 训练数据
- `rsft_report.json`：统计报告

进程在 nohup 后台运行，不会因 SSH 断连中断。完成后可通过以下方式查看结果：
```bash
cat /root/autodl-tmp/rsft_scored_s1/rsft_report.json
wc -l /root/autodl-tmp/rsft_scored_s1/rsft_train.jsonl
```

---
