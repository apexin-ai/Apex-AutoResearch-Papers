# Memory — redundancy-compound-sparsity

## 2026-05-12: ⚠️ 架构误判修正 — DeepSeek-R1-Distill-Qwen-7B 不是 MLA

**错误认知**: 之前认为 DeepSeek-R1-Distill-Qwen-7B 是 MLA 架构，Llama 是 GQA，r 差异来自 MLA vs GQA。
**事实**: DeepSeek-R1-Distill-Qwen-7B 是标准 GQA (Qwen2ForCausalLM, num_key_value_heads=4)。MLA 只存在于原始 DeepSeek-V2/V3/R1-671B。蒸馏只传递推理能力，不传递注意力架构。

**真正的 confound 候选**: 推理训练 vs 指令训练
- DeepSeek-R1-Distill (R1 推理蒸馏): 长 CoT (1353-3588 tokens), token 多样性高 → r=0.147
- Llama-3.1-8B-Instruct (指令 SFT): 短回答 (~623 tokens), 重复模式多 → r=0.471
- 两者都是 GQA，但 KV head 数不同 (4 vs 8)

**对照实验设计**:
- confound-ctrl-001: DeepSeek-R1-Distill-Llama-8B (Llama GQA 8 heads + R1 推理) → 控制架构
- confound-ctrl-002: Qwen2-7B-Instruct (Qwen2 GQA 4 heads + 指令) → 控制训练方式

**教训**: 不要假设蒸馏模型继承原始模型的架构。必须验证 config.json 中的 architectures 和 num_key_value_heads。

## 2026-05-12: Per-layer 分析（仍然有效，但移除 MLA 框架）

- **Llama r 极其均匀**: 32 层 r 范围 0.393-0.485，每一层都是可靠冗余信号
- **DeepSeek-Distill 11 层死区**: r<0.05 集中在 L0-3 和 L13-20
- **Mid layers 差异最大**: DeepSeek L13-17 ≈ r=0，Llama 同区域 r=0.434
- **Δpert 方向**: Llama late layers (L20-31) 平均 +14.3%；DeepSeek mid+late -3.3% to -3.6%
- ⚠️ 架构解释（MLA latent compression）已被推翻，需要新的解释

## 2026-05-12: Cross-axis 假设仍未定论

### 实验汇总

| 实验 | 模型 | 架构 | KV heads | 训练 | r | Δpert@55% |
|------|------|------|----------|------|---|-----------|
| mvp-001b | DeepSeek-R1-Distill-Qwen-7B | GQA | 4 | R1 推理蒸馏 | +0.147 | -2.2% |
| mvp-001c | DeepSeek-R1-Distill-Qwen-7B | GQA | 4 | R1 推理蒸馏 | +0.159 | -1.2% |
| neg-cross-model-001 | Llama-3.1-8B-Instruct | GQA | 8 | 指令 SFT | +0.471 | +6.6% |

### 待解答
- 差异来自推理训练 vs 指令训练？还是 4 heads vs 8 heads？还是两者？
- confound-ctrl-001/002 将分离这些变量

## 2026-05-12: kv-bench-001 失败
- 脚本 `run_kv_benchmark.py` 静默退出，仅 4 条记录，无 error/traceback
- 需要 debug 后重跑，但优先级低于 confound 实验

## 2026-05-12: Worker 反复不用 submit_training_job
- kv-bench-001 Worker 用 tmux 直接提交而非 submit_training_job
- 需在 Worker prompt 中更强调 submit_training_job 是唯一的提交方式
