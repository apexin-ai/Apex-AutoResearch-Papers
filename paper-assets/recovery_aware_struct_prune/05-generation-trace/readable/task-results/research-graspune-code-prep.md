# research graspune code prep

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_graspune-code-prep_20260514T082040_result.json`
- **Structured JSON:** [`f1dcbbbf2bf58f91898f.json`](../../sessions/f1/f1dcbbbf2bf58f91898f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已保存到项目 `memory.md`。

总结：

**GRASPrune (ACL 2026)** 是一个现成可用的 structured pruning baseline。核心发现：

1. **直接兼容**: 原生支持 Qwen 架构，attention pruning 天然在 KV group 粒度（`gate_score_kv` shape = `(num_key_value_heads,)`），完美满足 GQA group 硬约束。

2. **输出格式兼容**: 产出 `pruned_state_dict.safetensors` + `meta.json`，可直接被我们的 `rebuild.py:load_pruned_model()` 加载，无需修改现有代码。

3. **推荐方案**: 在服务器 clone 官方 repo，跑 `python train.py --model-family qwen --keep-ratio 0.65`，然后接入我们的 GRPO recovery pipeline。不需要重新实现。

4. **公平性注意点**: GRASPrune 有 rescale compensation（Standard/RASP 没有），校准数据默认用 WikiText2（我们用 GSM8K），论文中需讨论这些差异。

Sources:
- [GRASPrune paper](https://arxiv.org/abs/2604.19398)
- [GRASPrune GitHub](https://github.com/ZiY-Wang/GRASPrune)
- [Original GraSP (2020)](https://arxiv.org/abs/2002.07376)

---
