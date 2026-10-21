# code westd recovery checklist

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_westd_recovery_checklist_20260518T064046_result.json`
- **Structured JSON:** [`5fc6b496ee181188cda4.json`](../../sessions/5f/5fc6b496ee181188cda4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已写入 `artifacts/westd_recovery_checklist.md` 并注册。

文档包含 5 个步骤：
1. **服务器状态检查** — SSH 连通性 + GPU 状态 + 残留进程
2. **结果文件检查** — 5 个实验逐一 cat 结果 JSON + tail log，standard_20 和 rasp_20_v3 宕机前接近完成，有可能已写入结果
3. **结果读取** — Python 脚本批量解析已完成实验的 accuracy
4. **中断实验重提交** — 4 个 submit_training_job 命令，按优先级 standard > rasp > sft_cka_only > gsm8k 排序，标注预计耗时
5. **GPU 分配** — 4 张卡各跑一个，cuda:1/3 可能很快释放

关键提醒：gsm8k 的 log 在 /tmp，重启后可能丢失，重提交时需改路径到 ~/runs/。

---
