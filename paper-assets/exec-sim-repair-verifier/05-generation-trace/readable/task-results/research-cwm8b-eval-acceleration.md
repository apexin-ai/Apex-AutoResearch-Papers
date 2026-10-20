# research cwm8b eval acceleration

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_cwm8b-eval-acceleration_20260515T140851_result.json`
- **Structured JSON:** [`ae2c4e3d7fd7a4e05c83.json`](../../sessions/ae/ae2c4e3d7fd7a4e05c83.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

信息收集完毕。以下是完整评估。

---

## 评估结果

### 当前状态
- GPU 3: 17003/32607 MiB (15.1 GB 空闲)
- GPU 0: 4.8 GB 空闲 | GPU 1: 4.8 GB 空闲 | GPU 2: 1.4 GB 空闲
- 进度: 290/9784 已完成，写入 `/root/autodl-tmp/eval_results/cwm_8b_ckpt400_test/results_incremental.jsonl`
- 代码发现: **脚本已支持 batch 推理**（左 padding + attention mask），test split 默认 `batch_size=8`。当前 bs=1 是手动指定的。

---

### 方案 1: vLLM 推理

| 项目 | 结论 |
|------|------|
| 可行性 | YES — vLLM 已安装 (`/root/miniconda3/lib/python3.12/site-packages/vllm`)，支持 LoRA adapter |
| 实现成本 | **小时级** (1-2h) — 需重写推理逻辑（HF generate → vLLM engine），改 prompt 构建方式，调试兼容性 |
| 预估加速比 | 5-10x（continuous batching + PagedAttention） |
| 风险 | Qwen3-8B + LoRA + vLLM 的兼容性不确定，调试可能耗时 |

### 方案 2: 增大 batch_size

| 项目 | 结论 |
|------|------|
| 可行性 | **YES — 零代码改动**，脚本已完整支持 batch（左 padding + attention mask + batch generate） |
| 实现成本 | **0 分钟** — 只需去掉 `--batch_size 1`，默认就是 bs=8 |
| 显存评估 | bs=1 用 17GB，bs=8 额外 KV cache ~2.7GB（Qwen3-8B: 32层×8 KV heads×128dim, max 3072 tokens），总计 ~20GB，GPU 3 还剩 12GB，**不会 OOM** |
| bs=16/32 | 也可能 fit（KV cache ~5.4/10.8GB），但 padding 浪费增大，建议先试 bs=8 |
| 预估加速比 | **3-5x**（生成任务中 decode 阶段是 memory-bandwidth bound，增大 batch 提高算力利用率） |
| 预估耗时 | (9784-290) × 22 / 4 / 3600 ≈ **14.5h** (保守 4x) ~ **9.2h** (乐观 6x) → **满足 24h 目标** |
| 代价 | 需中断当前进程重启。290 条已存 incremental，重启自动 resume，无损失 |

### 方案 3: 多 GPU 分片并行

| 项目 | 结论 |
|------|------|
| 可行性 | **目前 NO** — GPU 0/1/2 空闲显存 < 5GB，8B bf16 模型需 ~16GB，无法加载第二份模型 |
| 若 GPU 释放后 | YES — 代码改动 ~15 行，分钟级 |
| 实现成本 | 加 `--start_idx` / `--end_idx` 参数 + `index_offset` + 不同 `--output_dir` |
| 预估加速比 | 线性（2 GPU = 2x，4 GPU = 4x），可与方案 2 叠加 |
| 结果合并 | 已有 incremental JSONL 格式，cat 两个文件后按 index 排序即可 |

---

## 推荐方案

**方案 2（增大 batch_size）**— 零代码改动，kill 当前进程后立即重启，290 条自动 resume。预估 9-15h 完成。

**方案 3 作为备选**— 如果 GPU 0-2 有任何一个释放，加分片代码后双 GPU 并行可再缩减一半时间。

---

## 方案 3 代码修改（备用）

需改 3 处，共 ~15 行：

**改动 1: argparse 加两个参数** (在 `--output_dir` 后面)
```python
p.add_argument("--start_idx", type=int, default=0, help="Start index for data sharding")
p.add_argument("--end_idx", type=int, default=None, help="End index for data sharding (exclusive)")
```

**改动 2: main() 中 load_jsonl 后加数据切片 + index_offset**
```python
    # 在 test_data = load_jsonl(data_path) 和 max_samples 之间加:
    index_offset = args.start_idx
    if args.start_idx > 0 or args.end_idx is not None:
        test_data = test_data[args.start_idx:args.end_idx]
        log.info(f"Sharding: indices [{args.start_idx}:{args.end_idx}], {len(test_data)} samples")
```

**改动 3: run_inference 函数签名加 `index_offset=0`，索引计算改为全局索引**

`run_inference` 签名：
```python
def run_inference(model, tokenizer, test_data, batch_size, max_seq_length,
                  max_new_tokens, device, incremental_path=None, 
                  completed_indices=None, index_offset=0):
```

循环内 `idx = i + j` 改为：
```python
            idx = index_offset + i + j
```

调用处传入：
```python
    results = run_inference(model, tokenizer, test_data, args.batch_size,
                            args.max_seq_length, args.max_new_tokens, args.device,
                            incremental_path=incremental_path,
                            completed_indices=completed_indices,
                            index_offset=index_offset)
```

**使用方式** (假设 GPU 0 释放):
```bash
# GPU 3: 前 5000 条 (当前进程 kill 后)
python eval_repo_cwm.py --checkpoint_dir &lt;ckpt> --device cuda:3 --start_idx 0 --end_idx 5000 \
    --output_dir /root/autodl-tmp/eval_results/cwm_8b_ckpt400_test_shard0/

# GPU 0: 后 4784 条
python eval_repo_cwm.py --checkpoint_dir &lt;ckpt> --device cuda:0 --start_idx 5000 --end_idx 9784 \
    --output_dir /root/autodl-tmp/eval_results/cwm_8b_ckpt400_test_shard1/
```

合并: `cat shard0/results_incremental.jsonl shard1/results_incremental.jsonl > combined.jsonl`

---

**总结**: 最省事的做法是 kill 当前 bs=1 进程，直接用默认 bs=8 重启（自动 resume 290 条）。代码零改动，预估 9-15h 完成，满足 24h 目标。方案 3 代码已备好，等 GPU 释放随时可用。

---
