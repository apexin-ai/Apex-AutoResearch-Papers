# Beam Search / Sampling 可行性检查报告

## 结论

| 方法 | 可行性 | 说明 |
|------|--------|------|
| **Sampling** (temperature/top_p/top_k) | **YES** | batch_size=1 下无需改代码，只需加 CLI 参数 |
| **Beam Search** (num_beams > 1) | **NEEDS_CODE_CHANGE** | TypeConstraintProcessor 单一共享 state 是 blocker |

---

## 1. 当前代码现状

### 参数支持

`run_constrained_extraction.py` (L602-615) argparse 中**无任何** beam/sampling 参数：

```python
parser.add_argument("--max_new_tokens", type=int, default=2048)
# 无 num_beams, do_sample, temperature, top_p, top_k
```

所有 `generate()` 调用（L441, L451, L483, L494, L542, L553）均硬编码 `do_sample=False`（greedy）。

### generate() 调用方式

`run_constrained_extraction.py:436-441`:
```python
gen_kwargs = dict(**inputs, max_new_tokens=max_new_tokens, do_sample=False)
if processors:
    gen_kwargs["logits_processor"] = processors
with torch.no_grad():
    output_ids = model.generate(**gen_kwargs)
```

---

## 2. XGrammar Layer — 多 beam 兼容性 ✅

`/root/miniconda3/lib/python3.12/site-packages/xgrammar/contrib/hf.py`:

```python
def __call__(self, input_ids, scores):
    if len(self.matchers) == 0:
        self.batch_size = input_ids.shape[0]  # 自动适配 beam 数
        self.matchers = [
            xgr.GrammarMatcher(self.compiled_grammars[i]) for i in range(self.batch_size)
        ]
```

XGrammar 在首次调用时根据 `input_ids.shape[0]`（beam search 下 = num_beams）创建**独立的 GrammarMatcher per beam**。每个 matcher 独立追踪 grammar state。**完全兼容 beam search。**

---

## 3. TypeConstraintProcessor (Semantic Layer) — Beam Search Blocker ❌

`compiler/type_mask_processor.py:188-200`:
```python
class TypeConstraintProcessor(LogitsProcessor):
    def __init__(self, spec, tokenizer, prompt_length=0):
        self.state = GenerationState()  # ← 单一 state 实例
```

`__call__` (L238-272):
```python
def __call__(self, input_ids, scores):
    batch_size = input_ids.shape[0]
    for batch_idx in range(batch_size):
        generated_text = self.tokenizer.decode(input_ids[batch_idx, self.prompt_length:].tolist(), ...)
        position = self._detect_position(generated_text)  # ← 修改 self.state
        if position == FieldPosition.RELATION_HEAD_TYPE:
            scores[batch_idx] = self._mask_head_type(scores[batch_idx])  # ← 读 self.state
```

**问题**：`_detect_position()` 调用 `PositionDetector.detect(generated_text, self.state)` 会**修改** `self.state`（entity_registry、current_relation_type、current_head_type 等）。Beam search 下 batch_size = num_beams，循环中每个 beam 的 parsing 都会**覆盖**同一个 state。

具体影响：
- Beam 0 注册 entity "BERT" → type "Method"，写入 `self.state.entity_registry`
- Beam 1 解析时可能尚未生成 "BERT"，但 registry 已污染
- `_mask_head_type()` / `_mask_tail_type()` 读取 `self.state.current_relation_type` 时得到的是最后一个 beam 的值

---

## 4. Sampling 的可行性

Sampling（`do_sample=True, temperature=T, top_p=P`）在 **batch_size=1** 下执行，`input_ids.shape[0]` 始终为 1，不存在 state 冲突。

**所需改动（纯参数传递，不涉及 processor 逻辑）：**

```python
# argparse 加 3 个参数
parser.add_argument("--do_sample", action="store_true")
parser.add_argument("--temperature", type=float, default=1.0)
parser.add_argument("--top_p", type=float, default=1.0)

# generate() 调用改为
gen_kwargs = dict(**inputs, max_new_tokens=max_new_tokens,
                  do_sample=args.do_sample,
                  temperature=args.temperature,
                  top_p=args.top_p)
```

改动量：~10 行。

---

## 5. Beam Search 所需改动

### 核心改动：per-beam state

`TypeConstraintProcessor` 需要维护 `List[GenerationState]` 而非单一 `GenerationState`：

```python
class TypeConstraintProcessor(LogitsProcessor):
    def __init__(self, spec, tokenizer, prompt_length=0, num_beams=1):
        self.states = [GenerationState() for _ in range(num_beams)]

    def __call__(self, input_ids, scores):
        if len(self.states) < input_ids.shape[0]:
            # 延迟初始化到实际 beam 数
            self.states = [GenerationState() for _ in range(input_ids.shape[0])]

        for batch_idx in range(input_ids.shape[0]):
            generated_text = self.tokenizer.decode(...)
            position = self.detector.detect(generated_text, self.states[batch_idx])
            # masking 函数也需接受 state 参数
            if position == FieldPosition.RELATION_HEAD_TYPE:
                scores[batch_idx] = self._mask_head_type(scores[batch_idx], self.states[batch_idx])
```

### 改动清单

| 文件 | 改动 |
|------|------|
| `compiler/type_mask_processor.py` | `self.state` → `self.states: List[GenerationState]`；`_mask_head_type`/`_mask_tail_type` 加 state 参数 |
| `compiler/type_mask_processor_cf_fallback.py` | 同上（相同结构） |
| `run_constrained_extraction.py` | 加 `--num_beams` 参数，传入 generate() |

### 改动量估算

- `type_mask_processor.py`: ~30 行改动（state 初始化 + 函数签名 + 索引）
- `type_mask_processor_cf_fallback.py`: ~30 行（相同改动）
- `run_constrained_extraction.py`: ~15 行（argparse + gen_kwargs）
- **总计：~75 行**

### 额外注意

- HF `generate()` 在 beam search 中可能做 beam reordering（选出 top-k beams 后重排序）。此时 `input_ids` 的顺序会变化，`states` 列表需要对应重排。不过由于 `PositionDetector.detect()` 每步都从完整 generated_text 重新解析（无增量 state），所以 reordering 不会导致 state 不一致——每步都是从文本重建 state。**这意味着 per-beam state 实际上不需要跨步维护**，因为 detect() 每次 full re-parse。
- 但 `entity_registry` 是累积的——每步 regex finditer 全文，所以即使 beam reorder 也能正确重建。

**结论：改动后 beam search 直接可行，无需处理 beam reorder。**

---

## 6. 总结

| 场景 | 可行性 | 改动量 | 风险 |
|------|--------|--------|------|
| Sampling (temp/top_p) | ✅ 立即可用 | ~10 行 | 无 |
| Beam search (num_beams) | ⚠️ 需改代码 | ~75 行 | 低（detect() 每步全文 re-parse，无增量 state 依赖） |

**推荐回复 reviewer**：sampling 已支持（或极易添加），beam search 需约 75 行改动使 TypeConstraintProcessor 支持 per-beam state，架构上无阻塞。
