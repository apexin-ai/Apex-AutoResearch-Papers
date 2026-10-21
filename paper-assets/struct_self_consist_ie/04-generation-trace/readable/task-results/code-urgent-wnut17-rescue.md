# code urgent wnut17 rescue

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_urgent_wnut17_rescue_20260519T092707_result.json`
- **Structured JSON:** [`a229502850e1d0702444.json`](../../sessions/a2/a229502850e1d0702444.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

排查完成，汇报结果：

---

## 任务 1：WNUT-17 (autodl-5090-c) — 未崩溃，下载慢

**根因：7B 模型下载仍在进行中，pipeline 在等待下载完成。**

| 项目 | 状态 |
|------|------|
| GPU 0,1 | 100% 占用（14B s42 训练中） |
| GPU 2,3 | 空闲（等 7B 下载完才启动） |
| screen `exp_wnut17_7b` | 存活，`wait_and_train.sh` 每 60s 轮询 |
| modelscope download (PID 53556) | 活跃，4 个 shard 并行下载到 `._____temp/` |
| 下载进度 | ~13.3GB / ~15.2GB（4/4 shards 都在下载） |
| 下载速率 | ~1 MB/s 总计 |
| **预计完成** | **~30-35 分钟后** |

下载完成后 modelscope 会将文件从 `._____temp/` 移到主目录 → `wait_and_train.sh` 检测到 4 个 safetensors → 自动触发 `run_wnut17_qwen25_7b_pipeline.sh`（已确认 `CUDA_VISIBLE_DEVICES=2,3`）。

**无需干预，pipeline 会自动启动。**

注：registry 查询 `exp_wnut17_qwen25_7b` 返回 0 条结果，可能实验 ID 不同或未注册。

---

## 任务 2：32B 下载 (autodl-5090) — 已完成 ✓

| 项目 | 状态 |
|------|------|
| safetensors | 17/17 全部就绪 |
| config.json | ✓ |
| tokenizer_config.json | ✓ |
| .incomplete 文件 | 无 |
| 总大小 | 62GB |
| 剩余磁盘 | 88GB |

**Qwen2.5-32B-Instruct READY**，路径：`/root/autodl-tmp/.hf_cache/models--Qwen--Qwen2.5-32B-Instruct/snapshots/5ede1c97bbab6ce5cda5812749b4c0bdf79b18dd/`

---
