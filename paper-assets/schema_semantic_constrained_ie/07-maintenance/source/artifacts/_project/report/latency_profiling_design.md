# OntoCoDec Latency Profiling 方案

## 1. 现有推理流程

```
main()
  ├── model.load()
  ├── grammar.compile()                    # 一次性，不计入 per-sample
  └── for sample in samples:
       ├── t0 = time.time()
       ├── run_single_pass() / run_s2_two_pass()
       │    ├── tokenizer.apply_chat_template()   # prompt 构建
       │    ├── tokenizer(text) → input_ids       # tokenization
       │    ├── [构建 LogitsProcessorList]
       │    │    ├── XGrammar LogitsProcessor     # Layer 1: 结构约束
       │    │    └── TypeConstraintProcessor      # Layer 2: 语义约束
       │    └── model.generate()
       │         └── per-token loop (inside HF generate):
       │              ├── model.forward()         # GPU forward pass
       │              ├── logits_processor[0]()   # XGrammar mask
       │              │    └── grammar_matcher.fill_next_token_bitmask()
       │              ├── logits_processor[1]()   # TypeConstraintProcessor
       │              │    ├── tokenizer.decode(generated_so_far)
       │              │    ├── PositionDetector.detect()  # regex O(n)
       │              │    └── _apply_type_mask()         # mask logits
       │              └── sampling (greedy argmax)
       ├── elapsed = time.time() - t0
       └── write record (已含 inference_time_seconds)
```

**关键观察**：
- `model.generate()` 是黑盒调用，内部 per-token loop 不可直接插桩
- LogitsProcessor 的 `__call__` 是唯一可侵入的 per-token hook 点
- TypeConstraintProcessor 每步做 decode+regex，开销随序列长度线性增长

## 2. 计时插入点设计

### 2.1 Per-sample 粗粒度计时（Level 1）

已有 `inference_time_seconds` 字段。补充 token 计数即可得到 tokens/sec：

```python
# 在 run_single_pass / run_s2_two_pass 返回前：
n_generated = output_ids.shape[1] - prompt_len
return raw, parsed, {"wall_time": elapsed, "n_tokens": n_generated, "prompt_len": prompt_len}
```

### 2.2 LogitsProcessor 内部分阶段计时（Level 2）

在 `TypeConstraintProcessor.__call__` 内部插入累计计时器：

```python
class TypeConstraintProcessor(LogitsProcessor):
    def __init__(self, ...):
        ...
        # Profiling accumulators
        self._profile_enabled = False
        self._time_decode = 0.0    # tokenizer.decode
        self._time_detect = 0.0    # PositionDetector.detect (regex)
        self._time_mask = 0.0      # _apply_type_mask
        self._n_calls = 0

    def __call__(self, input_ids, scores):
        if not self._profile_enabled:
            return self._original_call(input_ids, scores)

        self._n_calls += 1
        t0 = time.perf_counter()
        generated_text = self.tokenizer.decode(...)
        t1 = time.perf_counter()
        position = self._detect_position(generated_text)
        t2 = time.perf_counter()
        scores = self._apply_mask(position, scores)
        t3 = time.perf_counter()

        self._time_decode += (t1 - t0)
        self._time_detect += (t2 - t1)
        self._time_mask += (t3 - t2)
        return scores
```

**XGrammar processor** 同理，可 wrap 其 `__call__`：

```python
class ProfiledXGrammarProcessor:
    def __init__(self, original_processor):
        self._proc = original_processor
        self._total_time = 0.0
        self._n_calls = 0

    def __call__(self, input_ids, scores):
        t0 = time.perf_counter()
        result = self._proc(input_ids, scores)
        self._total_time += time.perf_counter() - t0
        self._n_calls += 1
        return result
```

### 2.3 Model Forward 时间隔离（Level 3）

无法直接在 `model.generate()` 内部插桩。但可以用差值法：

```
model_forward_time ≈ total_wall_time - xgrammar_time - semantic_time - overhead
```

或使用 PyTorch hook：

```python
total_forward_time = 0.0
def forward_hook(module, input, output):
    # 用 CUDA event 计时
    pass
model.register_forward_hook(forward_hook)  # 不推荐——太侵入
```

**推荐方案**：用 `torch.cuda.Event` 在 generate 前后测量 GPU 时间，减去 processor 时间（CPU 端），得到近似 forward 时间。实际上因为 greedy decoding 是同步的，差值法精度足够。

## 3. 计时开销控制

| 措施 | 原因 |
|------|------|
| 用 `time.perf_counter()` 而非 `time.time()` | ns 精度，更低 syscall 开销 |
| 累加器模式（不记录每 step 列表） | 避免 GC 压力和内存分配 |
| 仅在 profiling mode 启用 | 正常跑实验不受影响 |
| 不做 CUDA sync per token | 避免 pipeline stall（仅在 sample 结束时 sync 一次） |
| Warm-up 排除 | 前 5 个 sample 不计入统计 |

**预估额外开销**：`perf_counter()` 调用 ~100ns × 3次/token × ~200 tokens = ~60μs/sample，相对 5-15s 的推理时间可忽略 (<0.001%)。

## 4. 输出数据格式

### 4.1 Per-sample JSONL（`latency_profile_{mode}_{dataset}_{model}.jsonl`）

```json
{
  "doc_id": "X96-1059_sent0",
  "mode": "full_s1",
  "wall_time_sec": 8.234,
  "n_generated_tokens": 187,
  "prompt_tokens": 342,
  "tokens_per_sec": 22.71,
  "breakdown": {
    "xgrammar_total_sec": 0.412,
    "semantic_total_sec": 0.089,
    "semantic_decode_sec": 0.051,
    "semantic_detect_sec": 0.031,
    "semantic_mask_sec": 0.007,
    "model_forward_sec": 7.733,
    "n_processor_calls": 187
  }
}
```

### 4.2 Summary Statistics（`latency_summary.json`）

```json
{
  "config": {"model": "Qwen3-8B", "dataset": "scierc", "mode": "full_s1", "gpu": "RTX PRO 6000", "n_samples": 551, "warmup": 5},
  "wall_time": {"mean": 7.82, "std": 3.14, "p50": 6.9, "p95": 14.1, "total_sec": 4308},
  "tokens_per_sec": {"mean": 24.3, "std": 5.1, "p50": 23.8},
  "overhead_ratio": {"vs_unconstrained": 1.31, "grammar_only_ratio": 1.18, "semantic_only_ratio": 1.05},
  "breakdown_pct": {"model_forward": 93.8, "xgrammar": 5.3, "semantic": 0.9}
}
```

## 5. 实验矩阵

### Models
| Model ID | Path | 类型 |
|----------|------|------|
| Qwen3-8B (base) | `/root/autodl-tmp/models/Qwen3-8B-ms` | Base |
| Qwen3-8B-LoRA-SciERC | `/root/autodl-tmp/checkpoints/qwen3_8b_lora_scierc_merged` | SFT |
| Qwen3-8B-LoRA-DocRED | `/root/autodl-tmp/checkpoints/qwen_lora_docred_merged` | SFT |
| LLaMA-LoRA-SciERC | `/root/autodl-tmp/checkpoints/llama_lora_scierc_merged` | SFT |
| LLaMA-LoRA-DocRED | `/root/autodl-tmp/checkpoints/llama_lora_docred_merged` | SFT |

### Datasets
| Dataset | #Samples (test) | Avg seq length |
|---------|----------------|----------------|
| SciERC | 551 sentences | ~50 tokens input, ~200 tokens output |
| DocRED | ~100 documents | ~500 tokens input, ~500 tokens output |

### Modes（5 × 2 × 2 的论文核心矩阵）
| Mode | Grammar | Semantic | 说明 |
|------|---------|----------|------|
| unconstrained | ✗ | ✗ | Baseline |
| grammar_only | ✓ | ✗ | XGrammar only |
| semantic_only | ��� | ✓ | TypeConstraintProcessor only |
| full_s1 | ✓ | ✓ | Both, single-pass |
| full_s2 | ✓ | ✓ | Two-pass pipeline |

### 最小实验集（论文必需）

| Model | Dataset | Modes | 样本数 | 预估时间 |
|-------|---------|-------|--------|----------|
| Qwen3-8B | SciERC | all 5 | 551×5 | ~5×551×8s = 6.1h |
| Qwen3-8B | DocRED | all 5 | 100×5 | ~5×100×30s = 4.2h |
| LLaMA-LoRA-SciERC | SciERC | unconstrained + full_s1 | 551×2 | ~2.2h |
| LLaMA-LoRA-DocRED | DocRED | unconstrained + full_s1 | 100×2 | ~1.7h |

**总计**：~14h（单 GPU 串行）。双 GPU 并行可降至 ~7h。

### 可选扩展
- LoRA 模型全 5 modes（+8h）
- Batch size sensitivity（bs=1 vs bs=4，但 constrained decoding 通常只支持 bs=1）
- Sequence length bucketing（短/中/长文本分组分析 latency 趋势）

## 6. Warm-up 策略

- 前 5 个样本排除统计：覆盖 CUDA context init、JIT compilation、KV cache allocation
- Grammar compilation 时间单独记录（一次性开销，不计入 per-sample）
- 第一次 `model.generate()` 有 CUDA kernel lazy-loading，warm-up 必须覆盖

## 7. 实现方式建议

新建 `run_latency_profile.py`，import 现有模块：

```python
# 核心区别：
# 1. wrap LogitsProcessors with profiling
# 2. 收集 per-token timing breakdown
# 3. 输出 JSONL + summary

from run_constrained_extraction import (
    run_single_pass, load_scierc_data, load_docred_data,
    load_constraint_spec, build_full_schema, ...
)
```

不改动 `run_constrained_extraction.py` 本身——profiling 代码独立，避免影响正式实验的复现性。

## 8. 论文呈现建议

- Table: 5 modes × {tokens/sec, overhead ratio} for Qwen3-8B on SciERC/DocRED
- Figure: breakdown bar chart showing model_forward vs grammar vs semantic 占比
- Key claim: "Constrained decoding adds <X% overhead over unconstrained generation"
- 如果 overhead < 5%，可以强调 "near-zero cost"
- 如果 overhead > 20%，需要 discuss sequence length correlation 和优化方向
