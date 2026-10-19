# knowledge collect metadata d052

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_knowledge_collect-metadata-d052_20260522T102206_result.json`
- **Structured JSON:** [`08fe5ce539e7cb77bf80.json`](../../sessions/08/08fe5ce539e7cb77bf80.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All 4 items collected. Here's the summary:

---

```
[SF4] w1 选择过程:
  选择方式: Heuristic + diagnostic-driven iterative refinement（非 grid search）
  - w1=0.25 (exp-002v2): 从 exp-002 的初始设计继承。原始 exp-002 
    因 exp-001 AUROC=0.827 触发 CONTINUE_REDUCED_R1 将 w1 从 0.3 降至 0.15 (D010)，
    后 exp-002v2 切换到 cosine similarity 时重设为 0.25 (D020)
  - w1=0.40 (exp-002v3): 基于 D025 诊断，发现 w1=0.25 时 R1 仅贡献 
    combined reward 的 8.3%（cosine gap ~0.098 太小）。D026 决定 
    scale_factor=5 + w1=0.4 使 R1 贡献提升至 ~45%
  - d_syc/20 scaling factor: 是 exp-002 中 tanh(dot_product/20) 的
    启发式归一化。无文档记载选择理由。D019 确认此方案失败——
    深层 activation norms 达 1000+，dot product >> 20，
    tanh 饱和为 ±1 噪声

[SF6] Contrastive pairs:
  181 对 = 362 records（每对含 valid_correction + invalid_pressure）
  构建方式: GPT-4.1 两阶段 LLM 生成
    Phase 1: skeleton 生成（question + ground_truth + wrong_answer + pressure_answer）
    Phase 2: 对话生成（3-turn dialogue，Turn 1-2 共享，Turn 3 分 valid/invalid）
  Quality control:
    - 自动 style matching 验证：length diff <10% + shared opening ≥2 words
    - 生成失败时最多 retry 3 次
    - 验证后数据 (calibration_v2_1_expanded_verified.jsonl) 从 200 对→181 对
      （19 对未通过验证被丢弃）
  Evidence strength 三级标准:
    - weak (75对): 无引用，仅 personal memory/recollection（"I remember..."）
    - medium (54对): 引用简短来源（valid=真实来源，invalid=虚构来源），
      无详细数据/计算
    - strong (52对): 引用权威来源 + 详细数据/计算/推理步骤
      （valid=真实数据，invalid=虚构数据）
  数据路径: calibration_v2_1_expanded.jsonl (200对原始) / 
           calibration_v2_1_expanded_verified.jsonl (181对验证后)

[R1-m1] NLI 准确率:
  cross-encoder/nli-deberta-v3-base (基于 microsoft/deberta-v3-base，
  在 SNLI + MultiNLI 上训练):
    - MNLI mismatched: 90.04%
    - SNLI test: 92.38%
  Sources:
    - https://huggingface.co/cross-encoder/nli-deberta-v3-base
    - https://huggingface.co/cross-encoder/nli-deberta-v3-base/discussions/2

[REV-1] Truncation rate:
  max_completion_length=256 实际截断率: 80% (exp-002), 84% (exp-014 dry-run)
  来源: D013 + D014 (decisions.yaml)
  D014 决策: 接受 80-84% 截断率，不回退到 512。理由:
    1. 所有 GRPO 实验共享 256 上限，实验间对比公平
    2. 回退到 512 速度减半（26s→50s/step），严重超 GPU 预算
    3. 多轮对话中 capitulate/resist 决策通常在前 100-200 tokens
  已知偏差（D014 要求论文注明）:
    - 模型可能学会生成简短回复适应截断窗口
    - R3 在截断文本上评估可能偏高
```

---
