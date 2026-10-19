# code dcgrpo trainer

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_dcgrpo_trainer_20260518T111356_result.json`
- **Structured JSON:** [`4c65d7c8240e198b035a.json`](../../sessions/4c/4c65d7c8240e198b035a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

No register_artifact tool available. The file is created and syntactically valid.

---

## 代码结构

```
dcgrpo_trainer.py
├── _resolve_transformer_layers()   # 处理 PEFT wrapper 找到 decoder layers
├── ActivationCache                 # Forward hook 缓存指定层 hidden states
│   ├── register(model)
│   ├── clear() / remove()
│   └── _make_hook(layer_idx)
├── DCGRPOConfig(GRPOConfig)        # 扩展 reward_layers, weights, NLI 配置
├── DCGRPOTrainer(GRPOTrainer)
│   ├── __init__                    # 存配置 → super().__init__ → load directions → register hooks
│   ├── _load_directions()          # 加载 d_syc from directions.pt
│   ├── reload_directions()         # 热更新 + cosine drift 检测 (阈值 0.7)
│   ├── _ensure_nli_model()         # 懒加载 DeBERTa-v3-base
│   ├── _find_asst_first_positions()# 定位最后一个 assistant turn 的首 token
│   ├── _extract_activations()      # 完整 forward pass + hook 提取
│   ├── compute_r1() / _batch()     # ±dot(h, d_syc), 跨 layers 平均
│   ├── compute_r2() / _for_group() # sigmoid(R1_valid - R1_invalid) - 0.5, 按 pair_id 配对
│   ├── compute_r3()                # NLI entailment, 分 batch 推理
│   ├── compute_rewards()           # w1*R1 + w2*R2 + w3*R3 组合
│   ├── generate_completions()      # 覆写: 标准生成 + 额外 forward pass 缓存激活
│   ├── _compute_step_rewards()     # 训练循环集成入口
│   └── cleanup()                   # 移除 hooks, 释放 NLI 模型
```

## 关键设计决策

1. **R1 用 dot product 而非 cosine**: d_syc 已 L2-normalized，dot product 让激活范数成为信号强度的一部分
2. **R2 采用 S1 rank-based 设计**: `sigmoid(R1_valid - R1_invalid) - 0.5`，避免 d_gen = -d_syc 退化问题（skeleton §8）
3. **激活传递用实例级缓存**: `generate_completions()` 写 `self._step_acts`，`_compute_step_rewards()` 读取后清空，与 TRL 的 text-only reward_funcs 接口解耦
4. **生成后单独 forward pass 提取激活**: `model.generate()` 用 KV cache 只暴露最新 token 的 hidden state，需要额外一次完整 forward 才能拿到 asst_first 位置的激活，开销 ~5-10%
5. **`_resolve_transformer_layers()` 处理 PEFT 包装**: TRL 内部用 peft_config 时会包一层 PeftModel，需要 unwrap 才能注册 hooks
6. **NLI 模型懒加载**: 首次调用 `compute_r3` 时才加载，避免不需要 R3 时占用显存
7. **`_noop_reward_fn` 占位**: GRPOTrainer 构造函数要求 reward_funcs 非空，传入占位函数，实际 reward 通过覆写方法计算

---
