# ops d066 llama docred beam1 unc check relay

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_d066_llama_docred_beam1_unc_check_relay_20260520T131524_result.json`
- **Structured JSON:** [`8c25c22bd13427b0181c.json`](../../sessions/8c/8c25c22bd13427b0181c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

模型加载完成，已开始推理。

**结果汇报：**

1. **Llama DocRED beam1 unc** — 完成，200 行 JSONL，196 成功 / 4 失败
2. **新启动配置** — `llama_docred_200_beam1_full_s1`，PID 209444（实际子进程），GPU1 已占用 18266 MiB
3. **GPU 状态**：
   - GPU0: PID 194615 (d065_qwen_greedy_4096_r2), 18910 MiB
   - GPU1: PID 209444 (d066_llama_docred_beam1_s1), 18266 MiB
   - 双卡满载

**DocRED Llama 剩余队列**：beam4 unc → beam4 s1（等 GPU1 空闲后继续）。

---
