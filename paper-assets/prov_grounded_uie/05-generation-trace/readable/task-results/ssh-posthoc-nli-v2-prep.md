# ssh posthoc nli v2 prep

**prov grounded uie** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_posthoc-nli-v2-prep_20260512T231333_result.json`
- **Structured JSON:** [`119f7826699d1a3540ea.json`](../../sessions/11/119f7826699d1a3540ea.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

生成正常运行，已完成 2/124 批次（16/985 样本）。

**总结：**

**v1 卡死根因：**
1. **Qwen3 thinking mode 未禁用** — 每个样本生成大量 `&lt;think>` tokens，极大拖慢速度
2. **未设 CUDA_VISIBLE_DEVICES** — 可能与 cuda:0 上的任务竞争
3. **NLI scoring 跑在 CPU** — 不必要的慢

**v2 修复（共 4 处）：**
1. `apply_chat_template` 加 `enable_thinking=False` — 跳过思考阶段，直接输出 JSON
2. 进度日志改为每批打印（`batch 1/124`），而非每 50 样本
3. NLI evidence scoring 改为 `device="cuda"`（生成模型释放后）
4. NLI oracle scoring 同样改为 GPU

**posthoc_nli_v2 已在 cuda:1 上运行**，tmux session `posthoc_nli_v2`，日志 `/tmp/posthoc_nli_v2.log`，registry 已注册为 RUNNING。

---
