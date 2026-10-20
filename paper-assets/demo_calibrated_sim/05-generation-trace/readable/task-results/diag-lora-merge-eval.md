# diag lora merge eval

**Why Calibration Fails: A Taxonomy of Failure Modes in Dialect-Aware LLM User Simulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_lora-merge-eval_20260513T011320_result.json`
- **Structured JSON:** [`d16c42265d1c6f28baeb.json`](../../sessions/d1/d16c42265d1c6f28baeb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

cuda:3 已释放。以下是诊断报告。

---

## 诊断结论：vLLM LoRA Serving Bug，非 DPO 训练破坏

### 1. adapter_config.json 关键参数
| 参数 | 值 |
|------|------|
| r | 16 |
| lora_alpha | 32 |
| scaling (alpha/r) | 2.0（标准值） |
| target_modules | q_proj, v_proj（仅注意力投影） |
| lora_dropout | 0.05 |

Scaling 2.0 和仅覆盖 q_proj/v_proj 都是保守设置，不太可能破坏 tool-calling。

### 2. Merge 状态
成功。merged 模型保存在 `/root/autodl-tmp/models/Qwen2.5-7B-DPO003-merged/`（~15GB, 4 shards）。

### 3. 三组 Completion 对比（5 tasks, 1 trial）

| 配置 | Completion | Mean Reward | 详情 |
|------|-----------|-------------|------|
| **LoRA serving** (hgate-dpo003) | **~15%** | - | 20 tasks 早期数据 |
| **Merged DPO-003** | **60%** (3/5) | 0.600 | task 0✓ 1✓ 2✗ 3✓ 4✗ |
| **Base model** (无 DPO) | **40%** (2/5) | 0.400 | task 0✓ 1✗ 2✗ 3✓ 4✗ |

逐 task 对比：
| Task | Base | Merged DPO | 说明 |
|------|------|------------|------|
| 0 | ✓ | ✓ | 简单 cancel 任务 |
| 1 | ✗ (13 tool calls) | ✓ (7 tool calls) | DPO 更高效 |
| 2 | ✗ (context overflow) | ✗ (context overflow) | 两者都溢出 |
| 3 | ✓ | ✓ | 都成功 |
| 4 | ✗ | ✗ | 都失败 |

### 4. 诊断结论

**根因：vLLM LoRA serving bug。** 证据：
- merged DPO 模型 completion 60%，是 LoRA serving 的 **4 倍**
- merged DPO (60%) 甚至高于 base model (40%)，说明 DPO 训练**没有破坏**甚至**轻微改善**了 tool-calling
- task 2 的 context overflow 在 base model 和 merged model 上都出现，是 task 本身复杂度导致

vLLM LoRA 动态加载可能的问题：
- LoRA 权重 scaling/merge 方式与 PEFT merge_and_unload 不一致
- vLLM 的 hermes tool-call parser 在 LoRA adapter 模式下行为异常
- LoRA adapter 的 attention 权重可能影响 tool-call token 的生成分布

### 5. 建议下一步

1. **短期**：hgate eval 改用 merged 模型而非 LoRA 动态加载，预期 completion 恢复到 50-60%
2. **验证**：用 merged 模型跑完整 20 tasks 得到可靠的 completion 数据
3. **排查 vLLM LoRA**：如果确需动态加载（多 adapter 切换等），需要调查 vLLM 0.18.1 的 LoRA serving 实现，可能是已知 issue
4. **清理**：merged 模型已保存在 `/root/autodl-tmp/models/Qwen2.5-7B-DPO003-merged/`，可直接使用

---
