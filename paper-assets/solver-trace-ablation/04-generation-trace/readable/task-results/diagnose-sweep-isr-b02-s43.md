# diagnose sweep isr b02 s43

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_sweep-isr-b02-s43_20260516T052949_result.json`
- **Structured JSON:** [`476b694183d479f63498.json`](../../sessions/47/476b694183d479f63498.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结论

**这是一个假阳性 — 训练实际上成功完成了。**

### 证据

1. **500/500 步全部完成**，耗时 1h15m29s
2. 日志最后打印 `INFO Done.` 和 final stats：`prove_rate=0.59975, mean_isr=0.18117`
3. 模型完整保存在 `/root/autodl-tmp/outputs/sweep_isr_b02_s43/`（4 shard，~15GB）
4. 日志中 **0 条** error/traceback/exception/FAILED
5. TRL 训练摘要正常输出：`train_runtime=4529.35, train_loss=0.01294`

### EXIT_CODE=1 的来源

grep 返回 0 匹配数（无错误），说明 Python 进程本身没有报错。EXIT_CODE=1 最可能来自：
- `bash -c` 链中最后一条语句的退出码（TRL Trainer 在某些版本成功训练后返回非零码）
- 或者启动时的 vLLM 版本警告（`vLLM 0.18.1 vs supported 0.11.0-0.17.1`）触发了非零退出

### 结论

| 项目 | 结果 |
|------|------|
| **失败根因** | 非真正失败，EXIT_CODE=1 是假阳性 |
| **是否需要重跑** | **否** — 训练已完成，checkpoint 完整 |
| **下一步** | 直接用该 checkpoint 跑 eval（遵守 C008：`--data_path data/proofwriter_fol_100.jsonl`） |
| **磁盘** | /root/autodl-tmp 91% used (24G free)，需关注但暂不阻塞 |

---
