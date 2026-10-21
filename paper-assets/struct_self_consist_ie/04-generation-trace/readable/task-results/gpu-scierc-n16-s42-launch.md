# gpu scierc n16 s42 launch

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_gpu_scierc_n16_s42_launch_20260521T113725_result.json`
- **Structured JSON:** [`2994686a5e3c5b39a5ed.json`](../../sessions/29/2994686a5e3c5b39a5ed.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。汇报：

1. **cuda:1 安全检查**：通过。cuda:1 空闲（0MiB / 0% util），GPU 0/2/3 被其他 VLLM 进程占用，无冲突。
2. **模型/数据状态**：模型 `qwen3-8b-scierc-merged-v2`（~16GB，4 分片）和数据 `scierc/processed_data/`（train/dev/test.json，551 test instances）均存在。
3. **实验已成功启动**：vLLM 正在加载模型，已读取 551 条测试数据，架构识别为 Qwen3ForCausalLM，chunked prefill 启用。
4. **PID**: 314465，tmux session: `exp_scierc_n16_s42`，日志: `~/runs/struct_self_consist_ie/exp_scierc_n16_s42.log`

Registry 已更新为 RUNNING。

---
