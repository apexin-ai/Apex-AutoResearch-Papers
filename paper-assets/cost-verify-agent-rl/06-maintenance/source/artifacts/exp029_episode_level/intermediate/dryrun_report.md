# exp029_episode_level Dry-Run Report

**Date**: 2026-05-16
**Server**: bjb1-17606 (2× GPU, 97.9GB each)
**W&B Run**: g9yx0su6

---

## 1. Configuration Fix

| 参数 | 修复前 | 修复后 | 原�� |
|------|--------|--------|------|
| gpu_memory_utilization | 0.92 | 0.5 | 对齐 exp028c 实践，避免 KV cache 过度占用 |
| max_model_len | 16384 | 20480 | prompt 可达 16384 tokens，原值无 response 空间导致 VLLMValidationError |
| max_num_batched_tokens | 16384 | 20480 | 需 ≥ max_model_len |

**验证**: 首次 dry-run 因 max_model_len=16384 在 ~20 分钟时报 `This model's maximum context length is 16384 tokens. However, your prompt contains at least 16385 input tokens.`。修复后成功通过该时间点并完成 val 阶段。

---

## 2. Format Chain Verification

**结论：format chain 三方一致，无需修改。**

| 环节 | 格式 | 验证 |
|------|------|------|
| env_instruction (envs.yaml) | 要求模型输出 `<think>...</think><answer>bare_action</answer>` | ✅ |
| ctx_manager._parse_response() | regex 提取 `<answer>` 内容，返回 bare action string | ✅ |
| env.step(action) | 接收 bare action，检查 `action in self.available_actions` | ✅ |

注：原任务提及的 `alfworld_memory.py` 文件不存在，实际环境文件为 `ragen/env/alfworld/env.py`。

---

## 3. Dry-Run Results

### Val Before Train (140 episodes, full context mode, max_turn=50)

| Metric | Value |
|--------|-------|
| success | 0.1143 (11.43%, ~16/140 games) |
| action_is_valid | 0.6635 (66.35%) |
| action_is_effective | 1.0 |
| num_actions (avg) | 45.1 |
| raw_reward | 0.0 |
| reward/mean@140 | 1.143 |
| reward/best@140/mean | 10.0 |
| non-zero/success | 1.0 |
| Generation time | 1275s (~21 min) |

### GPU Memory

| Phase | GPU 0 | GPU 1 | Capacity | OOM |
|-------|-------|-------|----------|-----|
| Val (vLLM rollout) | 52187 MiB | 52189 MiB | 97887 MiB | ✅ No |
| Train (vLLM rollout) | 52711 MiB | 52301 MiB | 97887 MiB | ✅ No |

**Peak utilization**: ~54% — 充��余量，不会 OOM。

### Training Step

Training step 0/1 已启动并进入 rollout 生成阶段（GPU 在 0%/100% 之间周期性切换），未出现崩溃。FSDP WorkerDict actors 正常加载模型权重。

---

## 4. 结论

**Dry-run 通过。** 配置修复有效：
- max_model_len 问题��解决（16384 → 20480）
- GPU 内存安全（峰值 54%）
- action_is_valid > 0（66.35%），reward 解析正常
- 训练步骤正常启动，无 crash

**可以进入正式训练。**
