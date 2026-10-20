# Root Cause Analysis: Table 2 (w5) vs Appendix (d065) — Llama DocRED Greedy Constrained

## 1. 数字确认

用同一份 `eval_d064.py` 重评两个 JSONL 文件，数字完全复现：

|  | w5 (Table 2) | d065 (Appendix) |
|---|---|---|
| DR% | 0.21 (33 violations) | 0.00 (0 violations) |
| R-F1 | 43.78 | 44.70 |
| E-F1 | 83.94 | 84.71 |
| Parse Failures | 25 | 26 |
| Entities pred | 19077 | 19058 |
| Relations pred | 16074 | 16042 |

差异在 JSONL 本身——eval 脚本无问题。

## 2. 命令对比

### w5 (May 15-16)
```
python3 run_constrained_extraction.py \
  --mode full_s1 --dataset docred \
  --model_path /root/autodl-tmp/checkpoints/llama_lora_docred_merged \
  --data_path data/docred/dev.json \
  --constraints_path data/docred/ontology_constraints_docred.json \
  --output_path outputs/w5_llama_docred_lora_constrained_eval.jsonl \
  --batch_size 1 --max_new_tokens 4096
```
(seed=42 default, decoding_strategy=greedy default)

### d065 (May 20)
从 d065_llama_greedy_con.log 和 cascade script 推断 Llama 命令：
```
python run_constrained_extraction.py \
  --mode full_s1 --dataset docred \
  --model_path /root/autodl-tmp/checkpoints/llama_lora_docred_merged \
  --data_path data/docred/dev.json \
  --constraints_path data/docred/ontology_constraints_docred.json \
  --output_path /root/autodl-tmp/schema_outputs/d065_llama_docred_greedy_con_4096.jsonl \
  --device cuda:0 --max_new_tokens 4096 --seed 42 \
  --decoding_strategy greedy --skip_on_error
```

**参数完全一致**：同 model、同 dataset（998 docs）、同 mode (full_s1)、同 seed (42)、同 decoding (greedy)、同 max_new_tokens (4096)。唯一差异 `--skip_on_error` 只影响错误处理，不影响模型输出。

## 3. 根因：type_mask_processor.py 代码版本差异

### 关键证据

服务器上存在备份文件 `type_mask_processor.py.bak_before_grammar_fix`（May 18 00:05 创建），记录了一次重大 grammar fix：

| 版本 | 文件 | 大小 | 行数 | 时间 |
|---|---|---|---|---|
| w5 使用 | `.bak_before_grammar_fix` | 21KB | 544 行 | ≤ May 16 |
| d065 使用 | `type_mask_processor.py` (current) | 38KB | 938 行 | May 18+ |

w5 运行于 May 15-16，使用旧版 type_mask_processor (544 行)。
d065 运行于 May 20，使用新版 (938 行)。

### 新增的关键函数

旧版 → 新版新增了大量 token-level 约束机制：
- `_build_entity_type_prefix_map` — entity type 前缀匹配
- `_build_entity_type_collision_groups` — 消歧冲突 entity type
- `_needs_entity_type_continuation` + `_apply_entity_type_continuation_mask` — 多 token type 名续写约束
- `_apply_role_prefix_mask` + `_apply_role_continuation_mask` — relation type 前缀/续写约束
- `_build_char_token_map` / `_build_token_text_cache` — token 级别精细映射

### 这些变更如何影响输出

**205/998 (20.5%) 的 sample 输出不同。** 分类如下：
- 94 个 spacing-only 差异（如 `"February 3, 2008"` → `"February 3 , 2008"`）—— 新版更严格匹配 tokenized input
- 102 个结构性差异（entity type 分配不同）—— 新版在 generation 时强制 DR 约束
- 9 个 parse status 差异

**DR 消除机制**——新版 `_mask_tail_type` 在生成 relation 的 tail_type 时，根据当前 relation type 和 head_type 限制 allowed tail types，使输出自动满足 domain-range 约束。具体例子：

| 文档 | w5 输出 | d065 输出 | 说明 |
|---|---|---|---|
| Silvan Elves | `Thranduil(PER) --part of--> Middle-earth(LOC)` | `Thranduil(PER) --part of--> Middle-earth(ORG)` | P361 valid_pairs 不含 PER-LOC，含 PER-ORG |
| Between Five and Seven | `Paisley Park(LOC) --operator--> Prince(PER)` | `Paisley Park(LOC) --operator--> Prince(ORG)` | P137 valid_pairs 不含 LOC-PER，含 LOC-ORG |

w5 有 33 个这类 DR violations，d065 全部消除。

### F1 提升原因

entity type 改变影响 gold matching：
- 当新版 type 分配恰好与 gold 一致时，TP 增加 → F1 上升
- E-F1: 83.94 → 84.71 (+0.77)
- R-F1: 43.78 → 44.70 (+0.92)

## 4. 结论

| 因素 | 是否为根因 |
|---|---|
| max_new_tokens 不同 | 否——都是 4096 |
| decoding_strategy 不同 | 否——都是 greedy |
| seed 不同 | 否——都是 42 |
| model/checkpoint 不同 | 否——都是 llama_lora_docred_merged |
| 数据集不同 | 否——都是 dev.json 998 docs |
| eval 脚本版本不同 | 否——重评结果一致 |
| **type_mask_processor.py 版本不同** | **是——544 行 → 938 行，重大 grammar fix** |

**根因**：w5 和 d065 使用了不同版本的 `compiler/type_mask_processor.py`。May 18 的 grammar fix 大幅增强了 token-level 约束（entity type continuation masking、role prefix/continuation masking），使 d065 的 constrained decoding 在 generation 时就强制满足 domain-range 约束，消除了 w5 中的 33 个 DR violations，并改变了 ~20% sample 的输出，导致 F1 分数提升。
