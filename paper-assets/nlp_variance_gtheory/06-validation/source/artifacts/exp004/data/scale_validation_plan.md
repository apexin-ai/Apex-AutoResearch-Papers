## Scale Validation 实验方案

### 模型

| Scale | Model ID | 显存需求 | 磁盘 | 需下载 | 备注 |
|-------|----------|---------|------|--------|------|
| 3B | `Qwen/Qwen2.5-3B-Instruct` | ~7 GB (1× A100) | ~6 GB | Y | 同 Qwen 系列，隔离 scale 为唯一变量 |
| 72B | `Qwen/Qwen2.5-72B-Instruct` | ~140 GB BF16 (4× A100 TP=4) | ~140 GB | Y | 4 卡张量并行 |

选择 Qwen2.5 系列的理由：同一代架构、相同 tokenizer 和训练分布，确保 scale 是唯一系统性差异。

### 实验设计

- **Benchmark**: MMLU (200 items, 10 subjects × 20)
- **Facets**: temperature(2: 0.0, 0.7) × prompt(6) × seed(6) × ordering(4) = **576 conditions per model**
- **Precision**: BF16 only (exp-001 已确认 bf16≈fp16)
- **Records**: 576 × 200 = **115,200 per model**
- **Total**: 2 models × 115,200 = 230,400 records

### 代码修改

1. **`src/config/model_paths.py`** — 增加 2 个模型映射：
   ```python
   "Qwen/Qwen2.5-3B-Instruct": "/root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B-Instruct",
   "Qwen/Qwen2.5-72B-Instruct": "/root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-72B-Instruct",
   ```

2. **`src/inference/vllm_runner.py`** — `VLLMRunner.__init__` 增加 `tensor_parallel_size` 参数：
   ```python
   def __init__(self, model_name, gpu_id=0, dtype="bfloat16", seed=42, tensor_parallel_size=1):
   ```
   - TP > 1 时不设 `CUDA_VISIBLE_DEVICES`（需要所有卡可见）
   - 传入 `tensor_parallel_size` 到 `LLM()` 构造

3. **`src/design/generate_design.py`** — 新增 `exp004_scale` 配置：
   ```python
   "exp004_scale": {
       "model": ["Qwen/Qwen2.5-3B-Instruct", "Qwen/Qwen2.5-72B-Instruct"],
       "precision": ["bfloat16"],
       "temperature_config": [
           {"temperature": 0.0, "top_p": None},
           {"temperature": 0.7, "top_p": 0.9},
       ],
       "prompt_template": [1, 2, 3, 4, 5, 6],
       "seed": [42, 123, 456, 789, 1024, 2048],
       "ordering": [1, 2, 3, 4],
       "expected_total": 1152,  # 2 models × 576
   }
   ```

4. **`run_experiment.py`** — 增加 `--tensor-parallel` CLI 参数，传递给 VLLMRunner

### GPU 需求

| Model | 卡数 | Latency/prompt (est.) | Time/condition | 576 conditions | 含加载 |
|-------|------|----------------------|----------------|----------------|--------|
| Qwen2.5-3B | 1× A100 | ~10 ms | ~2.0s | ~19 min | **~20 min** |
| Qwen2.5-72B (TP=4) | 4× A100 | ~65 ms | ~13s | ~125 min | **~2.5 hr** |

- 3B 推理时，剩余 3 卡空闲（可并行下载 72B 模型）
- 72B 推理独占全部 4 卡

**总 GPU 时间**: ~3 小时（含模型下载等待时间另计）

### 磁盘预算

| 项目 | 大小 |
|------|------|
| 当前已用 | 149 GB |
| Qwen2.5-3B-Instruct | +6 GB |
| Qwen2.5-72B-Instruct | +140 GB |
| **预计总用** | **295 GB** |
| 数据盘总容量 | 350 GB |
| 剩余 | 55 GB |

容量刚好够，但几乎没有余量。

### 执行顺序

1. 下载 Qwen2.5-3B-Instruct（~2 min via ModelScope）
2. 修改代码（4 个文件）
3. 跑 3B 推理（~20 min，单卡）
4. 下载 Qwen2.5-72B-Instruct（~30-60 min via ModelScope，可在 3B 推理时并行）
5. 跑 72B 推理（~2.5 hr，4 卡 TP）
6. G-study 分析：对比 3B/8B/72B 方差分解结果

### 风险

1. **磁盘空间紧张** — 72B 模型下载后仅剩 ~55GB，如果中间文件过大可能爆盘。缓解：推理完成后可删除 72B 缓存。
2. **72B 下载耗时** — AutoDL 代理下 HF 大文件极慢。缓解：用 ModelScope CDN（`modelscope download`）。
3. **72B 独占 4 卡** — 推理期间无法跑其他实验。安排在非高峰时段。
4. **vLLM TP 兼容性** — 72B + TP=4 + enforce_eager=True 可能影响性能。可能需关闭 enforce_eager 或调整 `max_model_len`。
5. **max_model_len** — 72B 的 KV cache 很大；200 条 MMLU prompt（~500 tokens each）需确认不超 GPU 显存。如超限可降低 `gpu_memory_utilization` 或减小 `max_model_len` 到 2048。

### 分析计划

Scale validation 成功标准：
- 3B 和 72B 的方差分量相对比例（prompt > seed > ordering）与 8 个 7B-9B 模型的结论一致
- 允许绝对值有差异（72B 可能方差更小），但排序应稳定
- 如果排序不同，需报告为 limitation 并讨论 scale-dependent variance structure
