# ops disk cleanup

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_disk_cleanup_20260519T072356_result.json`
- **Structured JSON:** [`bf9ccc5fa447359467e2.json`](../../sessions/bf/bf9ccc5fa447359467e2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 清理报告

| 指标 | 清理前 | 清理后 |
|------|--------|--------|
| 可用空间 | 1.3G (4%) | 2.9G (9%) |
| 已用空间 | 29G | 28G |

**已删除**（共 ~2.2G）：
- `runs/phase2_tg_s42_v3b/` (23M)
- `runs/phase2_tg_s42_v4_dryrun/` (23M)
- `runs/phase2_tg_s42_v6/` (23M)
- HF ultrachat 缓存 (1.6G)
- HF Qwen tokenizer 缓存 (551M)

**保留项确认完整**：
- `runs/phase2_tg_s42_v7/` — 91M ✓
- `runs/phase2_ug_s42/` — 91M ✓
- Qwen 权重 `/root/.cache/modelscope/Qwen/Qwen2___5-7B-Instruct/` — 15G ✓
- LoRA-only 训练 PID 46085 — 运行中 4m29s，GPU 98% 利用率 ✓

**未删除 — 需确认**：
- `/root/.cache/modelscope/hub/models/LLM-Research/Meta-Llama-3___1-8B-Instruct/` (11M) — **PID 45803 正在执行 `snapshot_download('LLM-Research/Meta-Llama-3.1-8B-Instruct')`**，删除可能干扰下载。另外发现同路径下还有一个 `Meta-Llama-3.1-8B-Instruct/` 目录（不带下划线转义），是这次下载正在写入的目标。需要你确认：是否要终止这个下载并清理，还是等下载完成后再处理？

**未达到预期**：可用空间 2.9G，低于预期的 ~7.8G。主要原因是 Qwen 权重占 15G（远超 551M 的 tokenizer 缓存），整体磁盘容量 30G 本身偏紧。

---
