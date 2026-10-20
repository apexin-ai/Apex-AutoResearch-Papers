# code cka rasp pipeline

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_cka-rasp-pipeline_20260514T024929_result.json`
- **Structured JSON:** [`ff990644500d91d020d4.json`](../../sessions/ff/ff990644500d91d020d4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有输出结构正确：
- CKA overlap: 28 层 × 28 heads (attn) + 28 层 × 28 groups (MLP)
- Importance: 28 层 × 28 heads (attn) + 28 层 × 28 groups (MLP)

## 汇报

### 1. 代码文件路径和功能

| 文件 | 功能 |
|------|------|
| `src/cka_overlap.py` | 计算 Linear CKA 功能重叠 F(h)，per-layer 注意力头和 MLP 通道组的 intra-layer 相似度 |
| `src/importance_score.py` | 梯度 Taylor 展开重要性 I(h) = \|\|w_h * grad_h\|\|₂，支持 GQA 7:1 映射 |
| `src/rasp_scoring.py` | 组合得分 S(h) = I(h) × (1 - F(h))^α，支持 standard 和 rasp 两种模式 |
| `src/prune.py` | 结构化剪枝：切片 Q/K/V/O 注意力权重和 gate/up/down MLP 权重，GQA 感知 KV head 删除 |
| `src/train_grpo.py` | GRPO RLVR 恢复训练，trl GRPOTrainer + GSM8K 答案匹配奖励函数 |
| `src/eval_gsm8k.py` | GSM8K 测试集评估，贪心解码 + 答案抽取（\boxed{} / #### / 末位数字） |
| `src/run_mvp.sh` | 5 步流水线：CKA → Importance → Pruning(并行) → GRPO(并行) → Eval(并行) |

### 2. Dry-run 验证结果

- **--help**：5/5 脚本全部通过 ✓
- **CKA dry-run** (n_samples=4, cuda:0)：EXIT_CODE=0，输出 28 层 × 28 结构的 overlap tensor ✓
- **Importance dry-run** (n_samples=4, cuda:1)：EXIT_CODE=0，输出 28 层 × 28 结构的 importance tensor ✓
- 输出维度与模型架构匹配（28 层、28 heads、28 MLP groups）

### 3. 需要注意的问题

1. **vLLM 版本警告**：trl 提示 vLLM 0.18.1 超出支持范围 (0.11-0.17)，不影响 GRPO 训练（不走 vLLM 生成路径）
2. **`torch_dtype` 弃用警告**：transformers 5.8.0 建议用 `dtype` 替代 `torch_dtype`，功能不受影响
3. **flash-attn 正在编译**：后台编译中（CUDA kernel 编译耗时 ~15 分钟），完成后正式实验可获得推理加速
4. **Dry-run importance 全为 0**：4 个样本梯度累积不足，正式 512 样本没有此问题

---
