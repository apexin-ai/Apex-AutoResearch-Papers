# diagnose exp conll n16 failed

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_exp_conll_n16_failed_20260521T045315_result.json`
- **Structured JSON:** [`da479fa0f480885dfce1.json`](../../sessions/da/da479fa0f480885dfce1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

**根因**：`qwen3-8b-conll2003-merged` checkpoint 正在从另一台 AutoDL 实例 rsync 传输中，实验在传输完成前被启动。

**具体错误**：checkpoint 目录缺少 `vocab.json`（及 `tokenizer.json`、`tokenizer_config.json`、model safetensors 等），导致 Qwen2 tokenizer 初始化时 `vocab_file=None` → `TypeError: expected str, bytes or os.PathLike object, not NoneType`

**传输状态**：
- rsync PID 995204 仍在运行，当前 ~4.1GB / ~16GB
- 同时有 scp 进程也在传同一目录（有冲突风险）

**是否需要修复**：不需要代码修复。服务器上已有 `/tmp/auto_launch_conll.sh`（PID 995478）正确等待 rsync 完成后自动重启实验（s123→cuda:2, s456→cuda:3）。

**风险点**：launcher 脚本有 size check `< 15GB` 会 exit 1。rsync 完成后如果嵌套子目录 `qwen3-8b-conll2003-merged/qwen3-8b-conll2003-merged/` 残留（scp 造成），size 应该能过但目录结构需关注。建议 rsync 完成后确认 `vocab.json` 和全部 4 个 safetensors shard 都在顶层目录。

---
