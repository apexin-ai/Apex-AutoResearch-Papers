# code phase2 eval scripts

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_phase2_eval_scripts_20260518T060557_result.json`
- **Structured JSON:** [`1d0fdb1f0a919a663c91.json`](../../sessions/1d/1d0fdb1f0a919a663c91.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

语法检查通过。

创建了 3 个文件：

| 文件 | 功能 |
|------|------|
| `eval_phase2_gar.py` | 加载 LoRA+gate checkpoint，用 Phase 1 相同对话测 GAR，输出 JSON + 对比曲线 |
| `eval_phase2_mtbench.py` | 简化 MT-Bench 评估（10 题 × 2 turns），训练模型生成 → 基线模型 judge 评分 |
| `compare_phase2.py` | 读取 TG/UG 结果 JSON，生成对比表格 + 三线图 + Pass/Fail（TG mid GAR > UG + 3pp） |

设计要点：
- `eval_phase2_gar.py` 直接加载 `AutoModelForCausalLM(attn_implementation="eager")` 而非 `ThreadGatedModel` 构造函数，确保 `output_attentions=True` 能正常返回注意力权重
- 手动注册与 ThreadGatedModel 相同的 gating hooks（`layer_input + gate * (layer_output - layer_input)`），兼容 PEFT 包装后的模型层级
- 生成阶段不启用 gating hooks（避免 ThreadGate 的 turn_features 问题），仅 GAR 测量时激活
- `_find_hf_model()` 处理 plain HF model 和 PeftModel 两种包装路径

---
