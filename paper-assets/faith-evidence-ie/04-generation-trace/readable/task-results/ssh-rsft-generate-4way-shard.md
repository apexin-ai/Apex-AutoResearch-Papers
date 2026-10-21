# ssh rsft generate 4way shard

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_rsft-generate-4way-shard_20260515T013549_result.json`
- **Structured JSON:** [`8dadd596429fdfee2422.json`](../../sessions/8d/8dadd596429fdfee2422.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。总结：

## OOM 诊断

- **原因**：`batch_size=2` + 单 GPU 运行，每批生成 2×8=16 个序列。Qwen3-4B bf16 占 ~8GB 显存，KV cache 随长文档累积，到 151/1514 批次时触发系统 OOM Killer (EXIT_CODE=137)
- **之前已完成**：302 个文档（2416 行 generations.jsonl）

## 4-GPU 分片脚本

已在 `/root/autodl-tmp/scripts/` 创建：

| 脚本 | GPU | 数据范围 |
|------|-----|----------|
| `rsft_gen_shard0.sh` | cuda:0 | shard 0/4 (~757 docs) |
| `rsft_gen_shard1.sh` | cuda:1 | shard 1/4 (~757 docs) |
| `rsft_gen_shard2.sh` | cuda:2 | shard 2/4 (~757 docs) |
| `rsft_gen_shard3.sh` | cuda:3 | shard 3/4 (~756 docs) |

关键改动：
- `batch_size=1`（防 OOM）
- `--num_shards 4 --shard_id N`（代码内置自动均分 + 独立子目录 + 独立 progress.json）
- `CUDA_VISIBLE_DEVICES=N` 隔离 GPU
- 无 `--quantize`
- 输出到 `/root/autodl-tmp/rsft_data/shard_{N}/`

## Dry-run 验证

batch_size=1 + 2 文档：40 秒完成，16/16 format compliance，无 OOM。

## GPU 状态

4 块 GPU 全部空闲（0 MiB / 0%），可随时启动。

**预估时间**：~757 docs × ~30s/doc ÷ 1 = ~6.3 小时/shard（4 GPU 并行总时间 ~6.3h）。

---
