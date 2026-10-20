# analysis d029 failure mode analysis

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_d029-failure-mode-analysis_20260514T191625_result.json`
- **Structured JSON:** [`34ce41c276150c7eb377.json`](../../sessions/34/34ce41c276150c7eb377.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

代码和社区经验都已到手。关键发现：CED reward 对非匹配 triple 无 hard negative（p_neg=0），存在系统性 shortcut。下面给出完整分析。

---

## 根因分析

通过代码审查和社区数据，识别出 **3 个互相叠加的根因**：

### 根因 1：lr=5e-5 对 GRPO 太激进（主因）

社区共识：GRPO+QLoRA 的 lr 应为 **5e-6**（[Unsloth RL Guide](https://unsloth.ai/docs/get-started/reinforcement-learning-rl-guide)），HuggingFace 官方示例用 **1e-5**（[TRL GRPO cookbook](https://huggingface.co/learn/cookbook/en/fine_tuning_llm_grpo_trl)），MS-SWIFT 对 Qwen 甚至用 **1e-6**（[MS-SWIFT](https://qwen.readthedocs.io/en/latest/training/ms_swift.html)）。当前 5e-5 是推荐值的 **5-10 倍**。

证据：ckpt-10（仅 10 步！）rel_f1 从 SFT 的 0.4057 崩到 0.003。这不是 reward hacking，是 **on-policy 更新步幅过大导致的灾难性遗忘**。GRPO 不同于 SFT——SFT 有 teacher forcing 锚定正确分布，GRPO 的梯度完全来自采样 reward，更新方向噪声更大，lr 必须更保守。

### 根因 2：CED reward 的 recall shortcut（代码级确认）

审查 `grpo_trainer.py` L221-280 的 `CEDRewardWrapper.__call__`：

```python
# 对每个 predicted triple:
matched_gold = gold_map.get(key, {})  # 非匹配 triple → {}
hard_neg_ids = matched_gold.get("hard_negative_sent_ids", [])  # → []
hard_neg_sents = [...]  # → []

# 在 ced_reward.py 中:
if not hard_negative_sents:
    p_neg = 0.0  # ← 无 hard negative 时 p_neg=0
reward = max(0, p_pos - p_neg) * float(p_pos > tau)
# → 简化为: p_pos * I(p_pos > tau)
```

**Shortcut 机制**：非匹配 predicted triple（不在 gold 中）没有 hard negatives → p_neg=0 → CED 退化为 flat NLI → 任何"看起来合理"的 triple 都能拿到高 CED。F1 gate 只要求 **至少 1 个** triple 匹配 gold 就放行全部 triples 的 CED 计算。

**结果**：模型学会（1）少预测以提高 per-triple 平均 CED，（2）集中预测 NLI 容易判 entail 的 triple。这解释了 pred_count ↓50%、recall 崩塌、EDCR 虚高。

### 根因 3：Train/eval 分布不匹配

训练用 temperature sampling（8 candidates 取 reward 最高的更新），eval 用 greedy。Training f1_reward 0.02→0.72 持续上升，但 eval rel_f1 远低于预期。说明 model 偶尔在高 temperature 下采样到好输出拿高 reward，但 greedy mode 走不到那条路径。这是 GRPO 固有问题，但 **lr 过高放大了这个 gap**——policy 被少数高 reward 样本的梯度大幅拉偏。

---

## Top-3 可执行方案

### 方向 1: 降 lr 到 5e-6
**诊断依据**:
- ckpt-10 rel_f1=0.003（10 步摧毁 SFT 全部 extraction 能力）
- 社区标准 GRPO+QLoRA lr = 5e-6（vs 当前 5e-5，高 10x）
- [HuggingFace GRPO Trainer](https://huggingface.co/docs/trl/main/en/grpo_trainer) 文档：val/ratio 偏离 1.0 太远 → lr 太高
- 即使不改 reward 设计，lr 下降可能大幅缓解遗忘+hacking

**实验配置**:
- 改动: `--learning_rate 5e-6`（其余完全不变）
- 命令 diff:
  ```diff
  - --learning_rate 5e-5
  + --learning_rate 5e-6
  ```
- max_steps: 200（lr 降 10x，给更多步收敛）
- save_steps: 20
- 预计 GPU 时间: ~4h（单卡 RTX 5090，200 steps）

**预期结果**:
- 如果假说正确: ckpt-20 rel_f1 > 0.30（SFT 的 75%+），ckpt-100 rel_f1 ≥ 0.40，evi_f1 保持 > 0.70
- 风险: 收敛太慢看不到 reward 上升 → 下一轮试 1e-5

**优先级**: **P0** — 这是阻塞性问题，lr 不降其他修复无意义

---

### 方向 2: 修复 CED recall shortcut
**诊断依据**:
- 代码确认：非匹配 triple 的 p_neg=0，CED 退化为 flat NLI
- pred_count: 18815 → 9250（-50%），recall: 0.407 → 0.117
- EDCR: 0.71 → 0.89-0.99（proxy 被过度优化）
- F1 gate 阈值太低（1 个匹配就放行所有 triple 的 CED）

**实验配置** — 改 CEDRewardWrapper（两种选项，推荐 A）:

**选项 A: 严格匹配 — 只对 gold-matched triple 计算 CED**
```python
# grpo_trainer.py CEDRewardWrapper.__call__ 中
# 替换当前 "对所有 pred triple 算 CED" 的逻辑:
for p in pred:
    key = (head, relation, tail)
    if key not in gold_map:
        continue  # 非匹配 triple 直接跳过，不计入 CED
    # 只有 matched triple 进 CED 计算
    ...
# 如果没有 matched triple → reward = 0 (F1 gate 已处理)
```

**选项 B: recall penalty 加权**
```python
# 在 CED reward 最后乘以 recall factor
recall = matched_count / len(gold_set) if gold_set else 0
final_reward = mean_ced * recall
```

- 命令 diff: 代码修改 + `--learning_rate 5e-6`（与方向 1 组合）
- 预计 GPU 时间: ~4h（200 steps）

**预期结果**:
- 如果假说正确: pred_count 不再下降，recall 恢复到 SFT 水平（0.40+），EDCR 适度提升（0.75-0.85 而非 0.99）
- 风险: 严格匹配可能让 CED reward 太稀疏（多数 triple 拿不到分），失去 CED-as-stabilizer 作用 → 用选项 B 折中

**优先级**: **P1** — 与方向 1 组合使用

---

### 方向 3: MO-GRPO 风格 reward 归一化
**诊断依据**:
- [MO-GRPO](https://arxiv.org/abs/2509.22047) 指出标准 GRPO 按 sum 归一化 advantage，variance 大的 reward 主导梯度
- format reward variance≈0（已最大化），f1 和 CED 的 variance 不同，CED 可能主导
- 当前 WeightedRewardFn 只做静态权重，不做 variance normalization
- 实现简单：TRL GRPOTrainer 内部对 rewards 做 group-level normalization，只需改 reward_funcs 返回方式

**实验配置**:
- 改动: 在 WeightedRewardFn 外层 wrapper，对每个 reward channel 的 advantage 独立归一化后再求和
- 或者更简单：移除 format reward（已无信号），只用 f1 + CED 两个 channel，参考 MO-GRPO 的 per-objective normalization
- 与方向 1+2 组合: `--learning_rate 5e-6` + CED shortcut fix + MO-GRPO normalization
- 预计 GPU 时间: ~4h

**预期结果**:
- 如果假说正确: f1 和 CED 同步提升，不再出现 CED 单边优化
- 风险: TRL 内部 normalization 可能与自定义 normalization 冲突，需仔细对接

**优先级**: **P2** — 在 P0+P1 效果不够时再叠加

---

## 执行建议

| 优先级 | 实验 | 关键改动 | 验证标准 |
|--------|------|---------|---------|
| **P0** | lr=5e-6 | `learning_rate 5e-6`, max_steps=200 | ckpt-20 rel_f1 > 0.30 |
| **P1** | P0 + CED shortcut fix | 只对 gold-matched triple 计算 CED | pred_count 不下降, recall > 0.35 |
| **P2** | P0+P1 + MO-GRPO norm | per-objective advantage normalization | f1/ced 同步上升 |

**建议先单独跑 P0**（只改 lr），如果 ckpt-20 rel_f1 > 0.30 确认 lr 是主因，再叠加 P1。P0 和 P1 可以并行跑（如果有两张空闲卡）以节省时间。

Sources:
- [Unsloth RL Guide — lr=5e-6 for GRPO](https://unsloth.ai/docs/get-started/reinforcement-learning-rl-guide)
- [HuggingFace GRPO Trainer docs](https://huggingface.co/docs/trl/main/en/grpo_trainer)
- [TRL GRPO cookbook — lr=1e-5](https://huggingface.co/learn/cookbook/en/fine_tuning_llm_grpo_trl)
- [MO-GRPO: Mitigating Reward Hacking](https://arxiv.org/abs/2509.22047)
- [Reward Hacking in GRPO — blog](https://ishanjmukherjee.github.io/reward-hacking-grpo)
- [MS-SWIFT Qwen GRPO — lr=1e-6](https://qwen.readthedocs.io/en/latest/training/ms_swift.html)

---
