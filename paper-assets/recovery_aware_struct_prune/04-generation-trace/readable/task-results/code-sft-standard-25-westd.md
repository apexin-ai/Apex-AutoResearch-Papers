# code sft standard 25 westd

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_sft_standard_25_westd_20260516T055908_result.json`
- **Structured JSON:** [`9e2a856116f08e1597b9.json`](../../sessions/9e/9e2a856116f08e1597b9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

任务完成。总结：

1. **模型传输** — 通过将 westd 公钥加入 westb authorized_keys，成功从 westb (port 23072) scp 了 pruned_standard_25（10.8GB）到 westd
2. **训练提交** — 使用 conda 环境激活（`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`）解决了 `python: command not found` 问题
3. **状态** — sft_standard_25 在 westd-11672 cuda:1 上已正常运行，tmux session 存在，模型加载成功
4. **Registry** — 已更新为 RUNNING，spec 包含完整 provenance

---
