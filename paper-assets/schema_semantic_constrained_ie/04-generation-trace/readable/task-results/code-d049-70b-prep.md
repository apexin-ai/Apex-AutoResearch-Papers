# code d049 70b prep

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_d049_70b_prep_20260518T095552_result.json`
- **Structured JSON:** [`902c34fd228d9e62315c.json`](../../sessions/90/902c34fd228d9e62315c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总完成。

---

## P1: 70B 模型可用性与量化支持

| 项目 | westd-16980 | westd-21461 |
|------|-------------|-------------|
| **GPU** | 2× RTX PRO 6000 Blackwell, 98GB/卡 | 同左 |
| **70B 缓存** | 无 | 无 |
| **已缓存模型** | Llama-3.1-8B, Mistral-7B, DeepSeek-R1-14B | Mistral-7B, Qwen3-8B |
| **PyTorch** | 2.10.0+cu128 (miniconda3) | 2.8.0+cu128 (miniconda3) |
| **bitsandbytes** | 0.49.2 ✓ | 无 |
| **autoawq / auto-gptq** | 无 | 无 |
| **vllm** | 0.18.1 ✓ | 无 |
| **accelerate** | 1.13.0 ✓ | 1.13.0 ✓ |
| **磁盘可用** | 119GB (/root/autodl-tmp) | 207GB (/root/autodl-tmp) |

**脚本量化支持**: `run_constrained_extraction.py` 无任何量化代码。模型加载为：
```python
model = AutoModelForCausalLM.from_pretrained(
    model_path, torch_dtype=torch.bfloat16,
    device_map=args.device, trust_remote_code=True,
)
```
改动量极小——添加 `quantization_config` 参数 + CLI flag 即可。

**VRAM 评估**: 98GB 单卡跑 AWQ/NF4 4-bit 70B (~45-55GB) 绰绰有余。

**推荐方案**:
- **首选**: westd-16980 已有 bitsandbytes，直接用 `BitsAndBytesConfig(load_in_4bit=True, bnb_4bit_compute_dtype=torch.bfloat16)` 加载 `meta-llama/Llama-3.1-70B-Instruct`，无需下载预量化模型
- **备选**: 安装 autoawq，下载 `hugging-quants/Meta-Llama-3.1-70B-Instruct-AWQ-INT4`（~35GB）

---

## P2: Post-hoc Filtering 脚本分析

**存在**: `posthoc_filter.py` (455行) 和 `posthoc_filter_v2.py` (471行)

**逻辑**: 三步过滤 pipeline
1. **Relation vocabulary** — fuzzy match 关系名（token overlap >0.8 或 Levenshtein ≤2），失败则删除
2. **Entity type** — 归一化实体类型，不在有效集则删除
3. **Domain/range** — 检查 (head_type, tail_type) ∈ valid_pairs

输入: unconstrained JSONL（parsed_output + gold）→ 输出: filtered JSONL + metrics report

**硬编码程度**: 重度。SciERC 和 DocRED 各有完全独立的函数和归一化映射表，CLI 只支持 `--dataset scierc|docred`。

**复用于 EE 需要的改动**（中等，~200行）:
1. 新增 WikiEvents event types / entity types / argument roles 的归一化函数
2. **数据结构适配**: RE 是 `(head, tail, relation)` 三元组，EE 是 `(trigger, event_type, [(role, argument)])` 嵌套结构——filtering 逻辑需重构
3. 新增 EE constraints JSON 格式: event_type → valid_roles → valid_argument_types
4. 评估指标适配: trigger F1 + argument identification/classification F1（而非 relation F1）

---
