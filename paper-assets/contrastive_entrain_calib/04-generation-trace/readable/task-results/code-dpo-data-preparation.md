# code dpo data preparation

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_dpo-data-preparation_20260523T125306_result.json`
- **Structured JSON:** [`fdf6a440fb630fd3495a.json`](../../sessions/fd/fdf6a440fb630fd3495a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 产出总结

### 1. 现有数据格式

| 字段 | 说明 |
|------|------|
| `pair_id` | 对的唯一 ID（如 `math_weak_0005`） |
| `condition` | `valid_correction`（用户给正确答案）/ `invalid_pressure`（用户施压给错误答案） |
| `turns` | 3 轮对话：用户提问 → 助手给错误答案 → 用户纠正/施压 |
| `ground_truth` / `wrong_answer` / `pressure_answer` | 正确答案、初始错误答案、施压答案 |
| `domain` | math/science/geography/history/commonsense |
| `evidence_strength` | weak/medium/strong |

数据量：146 pairs × 2 conditions = 292 samples（train），35 pairs = 70 samples（held-out）

### 2. DPO 数据转换脚本
`/root/contrastive_entrain_calib/data/generate_dpo_pairs.py`

Best-of-N rejection sampling 流程：
- 每个 prompt 从 base Qwen3-8B 生成 8 个 completions（temperature=0.7）
- 用 heuristic（ground_truth 匹配）+ NLI（R3 同款模型）综合评分
- 取最高分为 chosen、最低分为 rejected，score gap < 0.15 的对被过滤
- 生成结果缓存到 `dpo_responses_cache.json`，避免重复生成

### 3. DPO 训练脚本
`/root/contrastive_entrain_calib/train/run_dpo.py`

配置对齐 GRPO/ACT：
| 参数 | 值 |
|------|-----|
| Model | Qwen3-8B |
| LoRA | r=64, alpha=64, q/k/v/o_proj |
| LR | 5e-5 |
| Warmup | 200 steps |
| Max steps | 8000 |
| Save steps | 500 |
| Grad accum | 16 |
| DPO beta | 0.1 |
| max_length | 1280 (prompt 1024 + completion 256) |

### 4. TRL DPO 依赖
已就绪：TRL 1.4.0, PEFT 0.19.1, transformers 4.57.6, torch 2.8.0+cu128

### 5. 预计训练时间
- **数据生成**：292 prompts × 8 completions = 2336 次 inference，约 30-45 分钟
- **DPO 训练**：8000 steps，batch=1 × grad_accum=16，约 6-8 小时（与 ACT 相当）
- 总计约 7-9 小时

运行顺序：
```bash
# Phase 1: 生成 DPO 数据
python /root/contrastive_entrain_calib/data/generate_dpo_pairs.py

# Phase 2: 训练
python /root/contrastive_entrain_calib/train/run_dpo.py
```

---
