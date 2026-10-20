# ssh rsft parallel 4gpu restart

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_rsft-parallel-4gpu-restart_20260515T013720_result.json`
- **Structured JSON:** [`69ff5a059ea1a75fb757.json`](../../sessions/69/69ff5a059ea1a75fb757.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。总结：

**已执行操作：**
1. GPU 确认无残留进程 → 清洁
2. 已有 302 docs 数据完整（progress.json + generations.jsonl）
3. 脚本修改：添加 `model.generation_config.do_sample = True`（L250）。其他覆盖项（temperature=0.7, top_k=0, top_p=0.95）和 batch_size=1 已存在
4. 利用已有的 `--start_idx` / `--end_idx` / `--shard_id` 参数 + `CUDA_VISIBLE_DEVICES` 环境变量实现 4 卡分片
5. 已 kill 掉 registry 自动提交的重复进程（使用了错误分片策略，从 doc 0 开始）
6. 4 个实验已注册为 RUNNING

**当前状态：**

| Shard | GPU | Docs | 进度 | 速度 |
|-------|-----|------|------|------|
| s0 | cuda:0 | 302–984 (682) | ~11/682 | ~17s/doc |
| s1 | cuda:1 | 984–1665 (681) | ~8/681 | ~17s/doc |
| s2 | cuda:2 | 1665–2346 (681) | ~6/681 | ~20s/doc |
| s3 | cuda:3 | 2346–3027 (681) | ~5/681 | ~16s/doc |

显存占用 11-17GB/卡，无 OOM 风险。预计 ~3h 完成全部 2725 docs。

---
