# code self consistency baseline

**Cross-Representation Disagreement as a Diagnostic Signal for LLM Reasoning Errors** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_self_consistency_baseline_20260515T072259_result.json`
- **Structured JSON:** [`b8f67647a9e3d5719fa3.json`](../../sessions/b8/b8f67647a9e3d5719fa3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

语法和参数解析都正常。

---

**代码架构**：

| 模块 | 复用内容 |
|------|---------|
| `formalize.py` | `FOL_SYSTEM_PROMPT`, `CODE_SYSTEM_PROMPT`, 对应 user template, `_extract_code`, `_strip_thinking`, `_get_client` |
| `executor.py` | `execute_code` — 沙箱执行生成的代码，提取 verdict |
| `data_loader.py` | `load_folio` — 加载 FOLIO 204 样本 |
| `config.py` | API 连接参数、token 计费、路径 |

**独立实现的部分**：
- `_call_llm_temp` — 基于 `_call_llm` 逻辑，增加 temperature 参数（原版硬编码 0.7）
- 独立的 token tracking（`_sc_usage`），不污染 formalize 的全局计数器
- `majority_vote` — Counter-based 投票
- CRD 结果加载 + 正确性判断（处理 agree/disagree/repair 等情况）
- JSONL streaming + resume（与 pipeline.py 一致的模式）

**运行命令**：
```bash
# 完整运行（204 样本 × k=5 × 2 表征 = 2040 次 LLM 调用）
python3 src/self_consistency_baseline.py \
    --output results/sc_baseline.jsonl \
    --k 5 \
    --crd-results results/mvp_v4_full.jsonl

# 小规模测试
python3 src/self_consistency_baseline.py \
    --output results/sc_baseline_test.jsonl \
    --k 5 --max-examples 5

# 断点续跑
python3 src/self_consistency_baseline.py \
    --output results/sc_baseline.jsonl \
    --k 5 --resume results/sc_baseline.jsonl \
    --crd-results results/mvp_v4_full.jsonl
```

**预估 token 成本**：
- 每次 FOL 调用：~1500 input + ~800 output ≈ 2300 tokens
- 每次 Code 调用：~1200 input + ~600 output ≈ 1800 tokens
- 单样本 k=5：(2300 + 1800) × 5 = 20,500 tokens
- 204 样本总计：204 × 20,500 ≈ **4.18M tokens**（约为 CRD single-pass 的 5× 倍）
- 本地 Qwen3-32B-AWQ 推理，无 API 费用，仅耗 GPU 时间

---
