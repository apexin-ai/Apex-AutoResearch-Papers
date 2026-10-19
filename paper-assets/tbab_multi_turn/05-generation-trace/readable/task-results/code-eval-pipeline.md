# code eval pipeline

**tbab multi turn** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_eval-pipeline_20260518T065009_result.json`
- **Structured JSON:** [`154675ec172e1202784f.json`](../../sessions/15/154675ec172e1202784f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。评估管线已在 westd-29046 上实现并验证。

**产出文件** (`/root/tbab_multi_turn/eval/`):

| 文件 | 功能 | 验证结果 |
|---|---|---|
| `metrics.py` | P̄/A⁹⁰/U₁₀⁹⁰ 计算 | mock 数据通过 |
| `tbab_inference.py` | 自定义 position_ids + 4D causal mask + bridge token 插入 | 3 种位置模式逻辑正确 |
| `model_local.py` | 本地模型推理，替代 model_openai.py | 4 种条件均生成合理输出 |
| `attention_analysis.py` | 逐频段 RoPE 注意力分析 | 3 层×32 头×3 频段分析正常运行 |
| `run_eval.py` | 主评估脚本（mock + 实际模式） | mock 流程端到端通过 |
| `configs/eval_config.yaml` | 评估配置 | - |
| `lost_in_conversation/` | 上游仓库（627 样本） | code 91 + math 81 (≥5 shards) |

**关键发现**:
- Bridge token IDs 必须在 vocab 范围内（Mistral vocab_size=32000），训练时需扩展 tokenizer
- 基座模型 mid_dominant_ratio=0.18（远低于 0.6 阈值），符合预期：TBAB 训练前不应有频段偏好
- 实际评估待 OpenAI API key 到位后执行：`python run_eval.py --model_path &lt;adapter_path> --condition full_tbab`

---
