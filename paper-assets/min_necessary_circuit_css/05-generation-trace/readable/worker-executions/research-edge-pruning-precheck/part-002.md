# research edge pruning precheck — Part 2 of 2

**Transformer Model EAP-IG** · Worker execution logs

[← Part 1](part-001.md) · [Transcript overview](../research-edge-pruning-precheck.md) · [Structured JSON](../../../sessions/da/da2924d65169d22c9a04.json)

## Round 5

### Assistant

_source line 415_

<details><summary>Logged reasoning block</summary>

```text
Excellent! Now I have all the information I need. Let me compile the comprehensive report. Key findings:

1. **Edge Pruning repo** supports GPT-2, CodeLlama-13B, and Tracr. It does NOT natively support Qwen, Gemma, or Llama-3.

2. **FLlama (CodeLlama) implementation** already handles:
   - RMSNorm
   - GQA (Grouped Query Attention)
   - RoPE (rotary embeddings)
   - Single embedding node (no separate pos embed)
   - bfloat16 training
   - FSDP distributed training

3. **Key community finding**: `melodyycui/Edge-Pruning` fork has a `modeling_fqwen.py` for Qwen2 (targeting Qwen2.5-0.5B). Active as of May 2026 but incomplete (no task scripts, eval scripts).

4. **Architecture compatibility analysis**: Qwen-2.5 0.5B is LLaMA-like with RMSNorm, GQA, RoPE, and SwiGLU—very similar to CodeLlama with a community fork already available. Gemma-2 2B is next on my list to evaluate.

5. **Comparing implementation approaches**: Llama-3.1 8B shares the same core architecture as CodeLlama, so the FLlama codebase would be the closest reference. I'm also considering auto-circuit as an alternative since it supports all three models through TransformerLens and has equivalent mask optimization capabilities, though it comes with memory overhead and lacks multi-GPU support.

Let me now write the report.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "25261dc0-d7f3-4e7f-8a0a-f535e5991f9b",
  "uuid": "36f0155d-3008-4e65-9b88-71ae16fb3b5a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LLvgth5oYFb8oeM14wcvGn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2066,
      "cache_creation_input_tokens": 4288,
      "cache_read_input_tokens": 30299,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4288
      },
      "output_tokens": 40,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Assistant

_source line 416_

所有调研数据已收集完毕，开始撰写报告。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "25261dc0-d7f3-4e7f-8a0a-f535e5991f9b",
  "uuid": "5e087167-0682-444e-afb5-09f63e218057",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LLvgth5oYFb8oeM14wcvGn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2066,
      "cache_creation_input_tokens": 4288,
      "cache_read_input_tokens": 30299,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4288
      },
      "output_tokens": 40,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool call

_source line 417_

<details open><summary>🔧 Tool call — Bash · `toolu_01TSicLmm438HSaByye7CL21`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/ 2>/dev/null || echo \"dir exists check\"",
  "description": "Check artifacts directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "25261dc0-d7f3-4e7f-8a0a-f535e5991f9b",
  "uuid": "4028641a-5a2a-41e2-80f4-2b95d1bbe4dc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LLvgth5oYFb8oeM14wcvGn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2066,
      "cache_creation_input_tokens": 4288,
      "cache_read_input_tokens": 30299,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4288
      },
      "output_tokens": 40,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 418 · 2026-05-13T02:18:14.341Z_

<details><summary>↩ Tool result · `toolu_01TSicLmm438HSaByye7CL21`</summary>

```text
D020_acdc_edge_selection.md
__pycache__
_project
analysis
analyze_mvp_results.py
css.py
deploy_phase2.sh
eap_ig_scoring.py
edge_pruning_scoring.py
ifr_scoring.py
literature_jaccard_overlap.md
literature_map.yaml
literature_survey_related_work.md
manifest.yaml
model_adapter.py
mvp_pilot_gpt2_ioi_v3
mvp_status_report_20260512.md
phase2_configs.yaml
related_work_notes.md
run_circus.py
run_phase2_experiment.py
structfuse-mvp
test_css.py
test_eap_ig_scoring.py
test_edge_pruning_scoring.py
test_ifr_scoring.py
test_run_circus_fixes.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "25261dc0-d7f3-4e7f-8a0a-f535e5991f9b",
  "uuid": "bc73be87-c48b-4ed8-b4a0-d36d753541db",
  "tool_use_result": {
    "stdout": "D020_acdc_edge_selection.md\n__pycache__\n_project\nanalysis\nanalyze_mvp_results.py\ncss.py\ndeploy_phase2.sh\neap_ig_scoring.py\nedge_pruning_scoring.py\nifr_scoring.py\nliterature_jaccard_overlap.md\nliterature_map.yaml\nliterature_survey_related_work.md\nmanifest.yaml\nmodel_adapter.py\nmvp_pilot_gpt2_ioi_v3\nmvp_status_report_20260512.md\nphase2_configs.yaml\nrelated_work_notes.md\nrun_circus.py\nrun_phase2_experiment.py\nstructfuse-mvp\ntest_css.py\ntest_eap_ig_scoring.py\ntest_edge_pruning_scoring.py\ntest_ifr_scoring.py\ntest_run_circus_fixes.py",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---


### Tool call

_source line 419_

<details open><summary>🔧 Tool call — Write · `toolu_01MVwLKhNEU5XTCCRbWVVqQZ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/edge_pruning_precheck_report.md",
  "content": "# Edge Pruning 大模型适配预检报告\n\n> 日期：2026-05-13\n> 目标：评估 `princeton-nlp/edge-pruning` 对 Qwen-2.5 0.5B / Gemma-2 2B / Llama-3.1 8B 的支持情况\n\n---\n\n## 1. 支持情况总结\n\n| 模型 | 原生支持 | 社区适配 | 架构相似度 | 适配难度 | 预估工时 |\n|------|---------|---------|-----------|---------|---------|\n| Qwen-2.5 0.5B | ❌ | ✅ 有 fork（未完成） | 极高（≈LLaMA） | **低** | 6-10h |\n| Gemma-2 2B | ❌ | ❌ | 中（有独特机制） | **中** | 16-24h |\n| Llama-3.1 8B | ❌ | ❌ | 极高（≈CodeLlama） | **低-中** | 8-14h |\n\n## 2. 仓库现状\n\n### 2.1 原生支持的模型\n\nEdge Pruning（NeurIPS 2024 Spotlight）仅实现了三种模型：\n\n- **GPT-2**（`modeling_fpt2.py`，1713行）— IOI/GT/GP 任务，单 GPU\n- **CodeLlama-13B**（`modeling_fllama.py`，2050行）— Boolean Expressions，32 GPU FSDP\n- **Tracr**（`modeling_erazr.py`，1105行）— 合成模型\n\nREADME 提到 *\"Extension to other models should be straightforward by mimicking modeling_{fpt2/fllama}.py\"*，但未提供更多架构的实现。\n\n### 2.2 核心机制\n\nEdge Pruning 的实现方式决定了适配工作的性质：\n\n1. **残差流扩展**：hidden state 从 `(batch, seq, hidden)` 扩展为 `(n_writers, batch, seq, hidden)`，每个 writer slot 对应一个组件的输出\n2. **Reader 掩码读取**：每个 reader（Q/K/V/MLP input）通过 `einsum(\"wbsd,wh->hbsd\", writers, mask)` 加权求和读取输入\n3. **Writer 门控写入**：每个 writer 输出经 node mask 门控后放入对应 slot\n4. **L0 正则化**：`log_alpha` 参数通过 stretched concrete 分布采样，Lagrangian 松弛驱动稀疏度\n\n**关键含义**：适配新模型 = 重写整个 forward pass，将标准 HuggingFace 模型改造为 writer/reader DAG 结构。不是简单的 hook 注入，而是深度改造。\n\n### 2.3 社区贡献\n\n- **PR**：仅 1 个（typo 修复），无模型扩展\n- **Issues**：7 个，均不涉及新模型\n- **关键 Fork**：`melodyycui/Edge-Pruning` 添加了 `modeling_fqwen.py`（54KB），实现 Qwen2 的 edge pruning 支持。活跃至 2026-05-11，但缺少 pruning scripts / eval scripts / run scripts。可作为 Qwen 适配的参考起点。\n\n---\n\n## 3. 逐模型详细分析\n\n### 3.1 Qwen-2.5 0.5B\n\n**架构特性**：\n- RMSNorm ✅（FLlama 已支持）\n- GQA ✅（FLlama 已支持，`num_kv_heads` ≠ `num_heads`）\n- RoPE ✅（FLlama 已支持）\n- SwiGLU MLP ✅（FLlama 已支持）\n- 单一 embedding（无 position embedding）✅（FLlama 已支持）\n\n**结论**：Qwen-2.5 架构与 LLaMA 高度同构。`modeling_fllama.py` 可直接作为模板。社区 fork `melodyycui/Edge-Pruning` 已有 `modeling_fqwen.py` 参考实现。\n\n**适配路径**：\n1. 基于 `modeling_fllama.py` 修改，替换 HuggingFace 的 `Qwen2ForCausalLM` 类层次\n2. 参考 `melodyycui` 的 `modeling_fqwen.py` 处理 Qwen2 特有的 config 字段映射\n3. 调整 attention bias 处理（Qwen2 有 `attention_bias` config 选项）\n4. 编写 pruning script 和 eval script\n\n**预估**：6-10 小时（有社区参考代码，且 0.5B 单 GPU 即可运行）\n\n### 3.2 Gemma-2 2B\n\n**架构特性**：\n- RMSNorm ✅（FLlama 已支持）\n- GQA ✅（FLlama 已支持）\n- RoPE ✅（FLlama 已支持）\n- GeGLU MLP — 与 SwiGLU 同为 gated MLP，门控函数不同，改动小\n- **Logit soft-capping** ⚠️ — attention logits 和 final logits 有 tanh soft-cap，需在 edge pruning 的 attention 实现中加入\n- **交替 sliding window / global attention** ⚠️ — 偶数层用 sliding window（4096），奇数层用 global attention，attention mask 处理更复杂\n- **Pre/Post-norm 混合** ⚠️ — 每个 sublayer 前后都有 RMSNorm（post-norm 对 writer 输出的归一化有影响）\n\n**需要额外处理的部分**：\n1. Sliding window attention 与 global attention 的交替——影响 writer/reader 的因果 mask 构建\n2. Logit soft-capping——在修改后的 attention forward 中添加 `tanh(logits / soft_cap_value) * soft_cap_value`\n3. Pre/Post-norm 混合——post-norm 改变了 writer 输出到残差流的路径，需要调整 `attn_write` 和 `mlp_write` 逻辑\n4. Gemma2 的 HuggingFace 实现类名不同（`Gemma2DecoderLayer` 等）\n\n**预估**：16-24 小时（sliding window + post-norm 的交互需要仔细处理，且 2B 参数量需要考虑显存优化）\n\n### 3.3 Llama-3.1 8B\n\n**架构特性**：\n- RMSNorm ✅\n- GQA ✅（8 KV heads / 32 Q heads）\n- RoPE ✅（Llama-3 用 theta=500000 的高频 RoPE）\n- SwiGLU MLP ✅\n\n**与 CodeLlama-13B 的差异**：\n- Llama-3.1 用 `LlamaForCausalLM`（HF class），CodeLlama 也是 `LlamaForCausalLM`——类层次完全一致\n- GQA 比例不同（Llama-3.1 8B: 8 KV heads / 32 Q heads；CodeLlama-13B: 40 KV heads / 40 Q heads 即 MHA）\n- 实际上 `modeling_fllama.py` 已经完整支持 GQA（K/V read log_alphas 有独立维度）\n\n**适配路径**：\n1. `modeling_fllama.py` 几乎可以直接使用——只需确认 HuggingFace `transformers` 版本的 API 兼容性\n2. 主要工作在于 FSDP / 显存管理（8B 模型 + writer tensor 扩展 = 显存大幅增加）\n3. 原 CodeLlama-13B 用 32 GPU FSDP 训练；8B 可能 4-8 GPU 可行（取决于序列长度和 batch size）\n\n**额外挑战（规模相关）**：\n- Writer tensor 从 `(n_writers, batch, seq, hidden)` 维度上，8B 模型有 32 层 × 32 heads = 1024 个 attention writer + 32 MLP writer + 1 embed = 1057 writers\n- 每个 writer slot 占 `batch × seq × 4096` × bf16 = 较大显存开销\n- 可能需要 gradient checkpointing + FSDP offload\n\n**预估**：8-14 小时（代码适配简单，主要时间花在 FSDP 配置调试和显存优化）\n\n---\n\n## 4. 显存估算\n\nEdge Pruning 的核心开销是 writer tensor 的显存扩展：\n\n| 模型 | 层数 | Heads | Writers | Hidden | Writer Tensor (bf16, bs=1, seq=64) |\n|------|------|-------|---------|--------|-------------------------------------|\n| GPT-2 Small | 12 | 12 | 157 | 768 | 157 × 64 × 768 × 2B ≈ 15 MB |\n| Qwen-2.5 0.5B | 24 | 14 | 361 | 896 | 361 × 64 × 896 × 2B ≈ 41 MB |\n| Gemma-2 2B | 26 | 8 | 235 | 2304 | 235 × 64 × 2304 × 2B ≈ 69 MB |\n| Llama-3.1 8B | 32 | 32 | 1057 | 4096 | 1057 × 64 × 4096 × 2B ≈ 553 MB |\n| CodeLlama 13B | 40 | 40 | 1641 | 5120 | 1641 × 64 × 5120 × 2B ≈ 1.07 GB |\n\n注：这只是 writer tensor 本体。实际训练还需要：模型参数、log_alpha 参数、优化器状态、激活缓存、梯度等。Llama-3.1 8B 预计单卡（A6000 48GB）显存不足，需 2-4 卡或 FSDP offload。\n\n---\n\n## 5. 替代方案分析\n\n### 5.1 auto-circuit（UFO-101/auto-circuit）\n\n| 维度 | auto-circuit | Edge Pruning |\n|------|-------------|-------------|\n| 后端 | TransformerLens（HookedTransformer） | 自定义 HF 模型改造 |\n| 模型支持 | Qwen ✅ Gemma ✅ Llama-3 ✅（通过 TransformerLens） | 仅 GPT-2 + CodeLlama |\n| 掩码优化 | Subnetwork Probing（hard_concrete + L0） | 同（stretched concrete + Lagrangian） |\n| 算法数 | 18 种（含 EAP、ACDC、mask gradient 等） | 1 种（mask optimization） |\n| 分布式 | ❌ 无 | ✅ FSDP |\n| 已验证规模 | ≤ 2.8B（Pythia） | ≤ 13B（CodeLlama，32 GPU） |\n| 显存效率 | 差（TransformerLens 额外 20-30% 开销 + 所有 edge 需缓存激活） | 较好（直接改造 HF 模型） |\n\n**评估**：auto-circuit 对小模型（Qwen-2.5 0.5B）是可行的替代方案，开箱即支持且 Subnetwork Probing 与 Edge Pruning 方法论等价。但对 Llama-3.1 8B，TransformerLens 的显存开销 + 无分布式支持 = 不可行。\n\n### 5.2 建议\n\n- **Qwen-2.5 0.5B**：可同时考虑 Edge Pruning 直接适配（有社区参考）和 auto-circuit（开箱即用），选易于集成到 CSS pipeline 的方案\n- **Gemma-2 2B / Llama-3.1 8B**：必须走 Edge Pruning 适配路线，auto-circuit 不适用于此规模\n\n---\n\n## 6. 适配工作分解\n\n### 共性工作（一次性）\n\n| 任务 | 预估 | 说明 |\n|------|------|------|\n| 理解 FLlama 代码结构 | 2h | 吃透 writer/reader DAG、log_alpha 管理、mask 采样 |\n| 抽取通用模板 | 3h | 从 FLlama 提取可复用的基类或工具函数 |\n| 编写通用 pruning script | 2h | 复用 `fpt2_custom.py` 的数据加载 + trainer 逻辑 |\n| 编写通用 eval script | 1h | 掩码二值化 + circuit 提取 |\n| **小计** | **8h** | |\n\n### Qwen-2.5 0.5B\n\n| 任务 | 预估 | 说明 |\n|------|------|------|\n| `modeling_fqwen.py` | 4h | 参考 FLlama + 社区 fork，适配 Qwen2 类层次 |\n| 验证 + 调试 | 2-4h | 单 GPU 验证 forward pass、mask 采样、circuit 提取 |\n| CSS pipeline 集成 | 2h | 接入 `edge_pruning_scoring.py` |\n| **小计** | **6-10h** | |\n\n### Gemma-2 2B\n\n| 任务 | 预估 | 说明 |\n|------|------|------|\n| `modeling_fgemma.py` | 10h | 需处理 sliding window、logit soft-cap、pre/post-norm |\n| FSDP 配置 | 2h | 2B 可能需 2 GPU |\n| 验证 + 调试 | 4-8h | Gemma-2 独特机制的交互可能引入 bug |\n| CSS pipeline 集成 | 2h | |\n| **小计** | **16-24h** | |\n\n### Llama-3.1 8B\n\n| 任务 | 预估 | 说明 |\n|------|------|------|\n| `modeling_fllama3.py` | 2h | FLlama 代码几乎可直接使用 |\n| FSDP 配置 + 显存优化 | 4-6h | gradient checkpointing、offload 调试 |\n| 验证 + 调试 | 2-4h | |\n| CSS pipeline 集成 | 2h | |\n| **小计** | **8-14h** | |\n\n### 总计\n\n| 场景 | 总工时 |\n|------|-------|\n| 仅 Qwen-2.5 0.5B | 14-18h |\n| 全部三模型 | 38-56h |\n| 全部三模型（含通用模板） | 30-48h（复用模板后递减） |\n\n---\n\n## 7. 风险与缓解\n\n| 风险 | 影响 | 缓解措施 |\n|------|------|---------|\n| Gemma-2 sliding window + edge pruning 交互导致 mask 逻辑错误 | 高 | 先在小规模（2层）上验证 attention mask 正确性 |\n| Llama-3.1 8B 显存不足 | 中 | FSDP offload + gradient checkpointing；或降低 batch size / seq length |\n| HuggingFace transformers 版本不兼容 | 中 | 锁定 transformers 版本；README 已警告过此问题 |\n| 社区 Qwen fork 代码质量不确定 | 低 | 作为参考而非直接使用，自行验证 |\n| Writer tensor 扩展改变模型行为（数值不稳定） | 低 | bf16 + gradient clipping；FLlama 已验证此路线可行 |\n\n---\n\n## 8. 结论与推荐路径\n\n### 可行性判断：**可行，但需要非平凡的工程投入**\n\nEdge Pruning 不是即插即用的库——每个新模型都需要重写完整的 forward pass（1500-2000行代码）。但 `modeling_fllama.py` 已经为 LLaMA 架构铺好了路，且 Qwen-2.5 和 Llama-3.1 都是 LLaMA-like 架构，适配成本可控。Gemma-2 因其独特的 attention 机制需要更多工作。\n\n### 推荐路径\n\n**Phase 2 优先级排序**：\n\n1. **Qwen-2.5 0.5B（第一个）**：适配成本最低、有社区参考、单 GPU 可跑、快速验证 CSS 方法在大模型上的效果\n2. **Llama-3.1 8B（第二个）**：代码适配简单但需要多 GPU 工程、验证 CSS 在真正的大模型上的可扩展性\n3. **Gemma-2 2B（第三个或酌情跳过）**：适配成本最高、独特架构特性增加 bug 风险。如果 Qwen + Llama 已足够证明方法的通用性，可考虑将 Gemma-2 降级为 optional\n\n**Phase 2 方法配置确认**：大模型用 EAP-IG + Edge Pruning + IFR（2 因果 + 1 相似度），不含 ACDC。Edge Pruning 作为唯一的 mask-based optimization 方法，必须适配成功。auto-circuit 可作为 Qwen-2.5 0.5B 的备选方案，但不推荐作为主路线（与 CSS pipeline 的集成成本更高，且不支持大模型分布式训练）。\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "25261dc0-d7f3-4e7f-8a0a-f535e5991f9b",
  "uuid": "8550fd51-19f1-4e5c-8635-05d3a0d8cbca",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CaKNtS7nqnoGDpAdP2GBo9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2902,
      "cache_read_input_tokens": 34587,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2902
      },
      "output_tokens": 66,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 420 · 2026-05-13T02:19:50.686Z_

<details><summary>↩ Tool result · `toolu_01MVwLKhNEU5XTCCRbWVVqQZ`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/edge_pruning_precheck_report.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "25261dc0-d7f3-4e7f-8a0a-f535e5991f9b",
  "uuid": "aec252e8-1208-4ce8-8d94-4af0a6876125",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/edge_pruning_precheck_report.md",
    "content": "# Edge Pruning 大模型适配预检报告\n\n> 日期：2026-05-13\n> 目标：评估 `princeton-nlp/edge-pruning` 对 Qwen-2.5 0.5B / Gemma-2 2B / Llama-3.1 8B 的支持情况\n\n---\n\n## 1. 支持情况总结\n\n| 模型 | 原生支持 | 社区适配 | 架构相似度 | 适配难度 | 预估工时 |\n|------|---------|---------|-----------|---------|---------|\n| Qwen-2.5 0.5B | ❌ | ✅ 有 fork（未完成） | 极高（≈LLaMA） | **低** | 6-10h |\n| Gemma-2 2B | ❌ | ❌ | 中（有独特机制） | **中** | 16-24h |\n| Llama-3.1 8B | ❌ | ❌ | 极高（≈CodeLlama） | **低-中** | 8-14h |\n\n## 2. 仓库现状\n\n### 2.1 原生支持的模型\n\nEdge Pruning（NeurIPS 2024 Spotlight）仅实现了三种模型：\n\n- **GPT-2**（`modeling_fpt2.py`，1713行）— IOI/GT/GP 任务，单 GPU\n- **CodeLlama-13B**（`modeling_fllama.py`，2050行）— Boolean Expressions，32 GPU FSDP\n- **Tracr**（`modeling_erazr.py`，1105行）— 合成模型\n\nREADME 提到 *\"Extension to other models should be straightforward by mimicking modeling_{fpt2/fllama}.py\"*，但未提供更多架构的实现。\n\n### 2.2 核心机制\n\nEdge Pruning 的实现方式决定了适配工作的性质：\n\n1. **残差流扩展**：hidden state 从 `(batch, seq, hidden)` 扩展为 `(n_writers, batch, seq, hidden)`，每个 writer slot 对应一个组件的输出\n2. **Reader 掩码读取**：每个 reader（Q/K/V/MLP input）通过 `einsum(\"wbsd,wh->hbsd\", writers, mask)` 加权求和读取输入\n3. **Writer 门控写入**：每个 writer 输出经 node mask 门控后放入对应 slot\n4. **L0 正则化**：`log_alpha` 参数通过 stretched concrete 分布采样，Lagrangian 松弛驱动稀疏度\n\n**关键含义**：适配新模型 = 重写整个 forward pass，将标准 HuggingFace 模型改造为 writer/reader DAG 结构。不是简单的 hook 注入，而是深度改造。\n\n### 2.3 社区贡献\n\n- **PR**：仅 1 个（typo 修复），无模型扩展\n- **Issues**：7 个，均不涉及新模型\n- **关键 Fork**：`melodyycui/Edge-Pruning` 添加了 `modeling_fqwen.py`（54KB），实现 Qwen2 的 edge pruning 支持。活跃至 2026-05-11，但缺少 pruning scripts / eval scripts / run scripts。可作为 Qwen 适配的参考起点。\n\n---\n\n## 3. 逐模型详细分析\n\n### 3.1 Qwen-2.5 0.5B\n\n**架构特性**：\n- RMSNorm ✅（FLlama 已支持）\n- GQA ✅（FLlama 已支持，`num_kv_heads` ≠ `num_heads`）\n- RoPE ✅（FLlama 已支持）\n- SwiGLU MLP ✅（FLlama 已支持）\n- 单一 embedding（无 position embedding）✅（FLlama 已支持）\n\n**结论**：Qwen-2.5 架构与 LLaMA 高度同构。`modeling_fllama.py` 可直接作为模板。社区 fork `melodyycui/Edge-Pruning` 已有 `modeling_fqwen.py` 参考实现。\n\n**适配路径**：\n1. 基于 `modeling_fllama.py` 修改，替换 HuggingFace 的 `Qwen2ForCausalLM` 类层次\n2. 参考 `melodyycui` 的 `modeling_fqwen.py` 处理 Qwen2 特有的 config 字段映射\n3. 调整 attention bias 处理（Qwen2 有 `attention_bias` config 选项）\n4. 编写 pruning script 和 eval script\n\n**预估**：6-10 小时（有社区参考代码，且 0.5B 单 GPU 即可运行）\n\n### 3.2 Gemma-2 2B\n\n**架构特性**：\n- RMSNorm ✅（FLlama 已支持）\n- GQA ✅（FLlama 已支持）\n- RoPE ✅（FLlama 已支持）\n- GeGLU MLP — 与 SwiGLU 同为 gated MLP，门控函数不同，改动小\n- **Logit soft-capping** ⚠️ — attention logits 和 final logits 有 tanh soft-cap，需在 edge pruning 的 attention 实现中加入\n- **交替 sliding window / global attention** ⚠️ — 偶数层用 sliding window（4096），奇数层用 global attention，attention mask 处理更复杂\n- **Pre/Post-norm 混合** ⚠️ — 每个 sublayer 前后都有 RMSNorm（post-norm 对 writer 输出的归一化有影响）\n\n**需要额外处理的部分**：\n1. Sliding window attention 与 global attention 的交替——影响 writer/reader 的因果 mask 构建\n2. Logit soft-capping——在修改后的 attention forward 中添加 `tanh(logits / soft_cap_value) * soft_cap_value`\n3. Pre/Post-norm 混合——post-norm 改变了 writer 输出到残差流的路径，需要调整 `attn_write` 和 `mlp_write` 逻辑\n4. Gemma2 的 HuggingFace 实现类名不同（`Gemma2DecoderLayer` 等）\n\n**预估**：16-24 小时（sliding window + post-norm 的交互需要仔细处理，且 2B 参数量需要考虑显存优化）\n\n### 3.3 Llama-3.1 8B\n\n**架构特性**：\n- RMSNorm ✅\n- GQA ✅（8 KV heads / 32 Q heads）\n- RoPE ✅（Llama-3 用 theta=500000 的高频 RoPE）\n- SwiGLU MLP ✅\n\n**与 CodeLlama-13B 的差异**：\n- Llama-3.1 用 `LlamaForCausalLM`（HF class），CodeLlama 也是 `LlamaForCausalLM`——类层次完全一致\n- GQA 比例不同（Llama-3.1 8B: 8 KV heads / 32 Q heads；CodeLlama-13B: 40 KV heads / 40 Q heads 即 MHA）\n- 实际上 `modeling_fllama.py` 已经完整支持 GQA（K/V read log_alphas 有独立维度）\n\n**适配路径**：\n1. `modeling_fllama.py` 几乎可以直接使用——只需确认 HuggingFace `transformers` 版本的 API 兼容性\n2. 主要工作在于 FSDP / 显存管理（8B 模型 + writer tensor 扩展 = 显存大幅增加）\n3. 原 CodeLlama-13B 用 32 GPU FSDP 训练；8B 可能 4-8 GPU 可行（取决于序列长度和 batch size）\n\n**额外挑战（规模相关）**：\n- Writer tensor 从 `(n_writers, batch, seq, hidden)` 维度上，8B 模型有 32 层 × 32 heads = 1024 个 attention writer + 32 MLP writer + 1 embed = 1057 writers\n- 每个 writer slot 占 `batch × seq × 4096` × bf16 = 较大显存开销\n- 可能需要 gradient checkpointing + FSDP offload\n\n**预估**：8-14 小时（代码适配简单，主要时间花在 FSDP 配置调试和显存优化）\n\n---\n\n## 4. 显存估算\n\nEdge Pruning 的核心开销是 writer tensor 的显存扩展：\n\n| 模型 | 层数 | Heads | Writers | Hidden | Writer Tensor (bf16, bs=1, seq=64) |\n|------|------|-------|---------|--------|-------------------------------------|\n| GPT-2 Small | 12 | 12 | 157 | 768 | 157 × 64 × 768 × 2B ≈ 15 MB |\n| Qwen-2.5 0.5B | 24 | 14 | 361 | 896 | 361 × 64 × 896 × 2B ≈ 41 MB |\n| Gemma-2 2B | 26 | 8 | 235 | 2304 | 235 × 64 × 2304 × 2B ≈ 69 MB |\n| Llama-3.1 8B | 32 | 32 | 1057 | 4096 | 1057 × 64 × 4096 × 2B ≈ 553 MB |\n| CodeLlama 13B | 40 | 40 | 1641 | 5120 | 1641 × 64 × 5120 × 2B ≈ 1.07 GB |\n\n注：这只是 writer tensor 本体。实际训练还需要：模型参数、log_alpha 参数、优化器状态、激活缓存、梯度等。Llama-3.1 8B 预计单卡（A6000 48GB）显存不足，需 2-4 卡或 FSDP offload。\n\n---\n\n## 5. 替代方案分析\n\n### 5.1 auto-circuit（UFO-101/auto-circuit）\n\n| 维度 | auto-circuit | Edge Pruning |\n|------|-------------|-------------|\n| 后端 | TransformerLens（HookedTransformer） | 自定义 HF 模型改造 |\n| 模型支持 | Qwen ✅ Gemma ✅ Llama-3 ✅（通过 TransformerLens） | 仅 GPT-2 + CodeLlama |\n| 掩码优化 | Subnetwork Probing（hard_concrete + L0） | 同（stretched concrete + Lagrangian） |\n| 算法数 | 18 种（含 EAP、ACDC、mask gradient 等） | 1 种（mask optimization） |\n| 分布式 | ❌ 无 | ✅ FSDP |\n| 已验证规模 | ≤ 2.8B（Pythia） | ≤ 13B（CodeLlama，32 GPU） |\n| 显存效率 | 差（TransformerLens 额外 20-30% 开销 + 所有 edge 需缓存激活） | 较好（直接改造 HF 模型） |\n\n**评估**：auto-circuit 对小模型（Qwen-2.5 0.5B）是可行的替代方案，开箱即支持且 Subnetwork Probing 与 Edge Pruning 方法论等价。但对 Llama-3.1 8B，TransformerLens 的显存开销 + 无分布式支持 = 不可行。\n\n### 5.2 建议\n\n- **Qwen-2.5 0.5B**：可同时考虑 Edge Pruning 直接适配（有社区参考）和 auto-circuit（开箱即用），选易于集成到 CSS pipeline 的方案\n- **Gemma-2 2B / Llama-3.1 8B**：必须走 Edge Pruning 适配路线，auto-circuit 不适用于此规模\n\n---\n\n## 6. 适配工作分解\n\n### 共性工作（一次性）\n\n| 任务 | 预估 | 说明 |\n|------|------|------|\n| 理解 FLlama 代码结构 | 2h | 吃透 writer/reader DAG、log_alpha 管理、mask 采样 |\n| 抽取通用模板 | 3h | 从 FLlama 提取可复用的基类或工具函数 |\n| 编写通用 pruning script | 2h | 复用 `fpt2_custom.py` 的数据加载 + trainer 逻辑 |\n| 编写通用 eval script | 1h | 掩码二值化 + circuit 提取 |\n| **小计** | **8h** | |\n\n### Qwen-2.5 0.5B\n\n| 任务 | 预估 | 说明 |\n|------|------|------|\n| `modeling_fqwen.py` | 4h | 参考 FLlama + 社区 fork，适配 Qwen2 类层次 |\n| 验证 + 调试 | 2-4h | 单 GPU 验证 forward pass、mask 采样、circuit 提取 |\n| CSS pipeline 集成 | 2h | 接入 `edge_pruning_scoring.py` |\n| **小计** | **6-10h** | |\n\n### Gemma-2 2B\n\n| 任务 | 预估 | 说明 |\n|------|------|------|\n| `modeling_fgemma.py` | 10h | 需处理 sliding window、logit soft-cap、pre/post-norm |\n| FSDP 配置 | 2h | 2B 可能需 2 GPU |\n| 验证 + 调试 | 4-8h | Gemma-2 独特机制的交互可能引入 bug |\n| CSS pipeline 集成 | 2h | |\n| **小计** | **16-24h** | |\n\n### Llama-3.1 8B\n\n| 任务 | 预估 | 说明 |\n|------|------|------|\n| `modeling_fllama3.py` | 2h | FLlama 代码几乎可直接使用 |\n| FSDP 配置 + 显存优化 | 4-6h | gradient checkpointing、offload 调试 |\n| 验证 + 调试 | 2-4h | |\n| CSS pipeline 集成 | 2h | |\n| **小计** | **8-14h** | |\n\n### 总计\n\n| 场景 | 总工时 |\n|------|-------|\n| 仅 Qwen-2.5 0.5B | 14-18h |\n| 全部三模型 | 38-56h |\n| 全部三模型（含通用模板） | 30-48h（复用模板后递减） |\n\n---\n\n## 7. 风险与缓解\n\n| 风险 | 影响 | 缓解措施 |\n|------|------|---------|\n| Gemma-2 sliding window + edge pruning 交互导致 mask 逻辑错误 | 高 | 先在小规模（2层）上验证 attention mask 正确性 |\n| Llama-3.1 8B 显存不足 | 中 | FSDP offload + gradient checkpointing；或降低 batch size / seq length |\n| HuggingFace transformers 版本不兼容 | 中 | 锁定 transformers 版本；README 已警告过此问题 |\n| 社区 Qwen fork 代码质量不确定 | 低 | 作为参考而非直接使用，自行验证 |\n| Writer tensor 扩展改变模型行为（数值不稳定） | 低 | bf16 + gradient clipping；FLlama 已验证此路线可行 |\n\n---\n\n## 8. 结论与推荐路径\n\n### 可行性判断：**可行，但需要非平凡的工程投入**\n\nEdge Pruning 不是即插即用的库——每个新模型都需要重写完整的 forward pass（1500-2000行代码）。但 `modeling_fllama.py` 已经为 LLaMA 架构铺好了路，且 Qwen-2.5 和 Llama-3.1 都是 LLaMA-like 架构，适配成本可控。Gemma-2 因其独特的 attention 机制需要更多工作。\n\n### 推荐路径\n\n**Phase 2 优先级排序**：\n\n1. **Qwen-2.5 0.5B（第一个）**：适配成本最低、有社区参考、单 GPU 可跑、快速验证 CSS 方法在大模型上的效果\n2. **Llama-3.1 8B（第二个）**：代码适配简单但需要多 GPU 工程、验证 CSS 在真正的大模型上的可扩展性\n3. **Gemma-2 2B（第三个或酌情跳过）**：适配成本最高、独特架构特性增加 bug 风险。如果 Qwen + Llama 已足够证明方法的通用性，可考虑将 Gemma-2 降级为 optional\n\n**Phase 2 方法配置确认**：大模型用 EAP-IG + Edge Pruning + IFR（2 因果 + 1 相似度），不含 ACDC。Edge Pruning 作为唯一的 mask-based optimization 方法，必须适配成功。auto-circuit 可作为 Qwen-2.5 0.5B 的备选方案，但不推荐作为主路线（与 CSS pipeline 的集成成本更高，且不支持大模型分布式训练）。\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
```

</details>

---


### Tool call

_source line 421_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01Xy1NaT3QchodpHHk3XY8td`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__save_project_file",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "25261dc0-d7f3-4e7f-8a0a-f535e5991f9b",
  "uuid": "f99b17ab-354d-472b-9879-a3fb59e275aa",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SWkP8nba65ecuFvtw938yV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5436,
      "cache_read_input_tokens": 37489,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5436
      },
      "output_tokens": 46,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 422 · 2026-05-13T02:19:54.870Z_

<details><summary>↩ Tool result · `toolu_01Xy1NaT3QchodpHHk3XY8td`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__save_project_file"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "25261dc0-d7f3-4e7f-8a0a-f535e5991f9b",
  "uuid": "645cc391-8a2f-4bc8-93b8-5066fa622da1",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__save_project_file"
    ],
    "query": "select:mcp__agent-ml-research__save_project_file",
    "total_deferred_tools": 22
  }
}
```

</details>

---


### Assistant

_source line 423_

<details><summary>Logged reasoning block</summary>

```text
The `save_project_file` tool has a strict whitelist and only allows writing to memory.md, writing_plan.yaml, paper_framing.md. The artifact file is already saved locally. I need to register it using `register_artifact`. Let me search for that tool.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "25261dc0-d7f3-4e7f-8a0a-f535e5991f9b",
  "uuid": "008956c8-06a7-49a6-b55e-d490ce3c3216",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UiRorwNjDQRLbbDdngRaVq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 363,
      "cache_read_input_tokens": 42925,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 363
      },
      "output_tokens": 28,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool call

_source line 424_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01NejVgjiQaxsoqs5raHbdAt`</summary>

```json
{
  "query": "register_artifact",
  "max_results": 3
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "25261dc0-d7f3-4e7f-8a0a-f535e5991f9b",
  "uuid": "9e279ac8-f0d8-44e3-9edf-d57bcb85eab9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UiRorwNjDQRLbbDdngRaVq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 363,
      "cache_read_input_tokens": 42925,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 363
      },
      "output_tokens": 28,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 425 · 2026-05-13T02:20:00.459Z_

<details><summary>↩ Tool result · `toolu_01NejVgjiQaxsoqs5raHbdAt`</summary>

```text
No matching deferred tools found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "25261dc0-d7f3-4e7f-8a0a-f535e5991f9b",
  "uuid": "27e1a4e2-eb5c-4549-aff5-14b3884d9517",
  "tool_use_result": {
    "matches": [],
    "query": "register_artifact",
    "total_deferred_tools": 22
  }
}
```

</details>

---


### Tool call

_source line 426_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01BVVc4BfpEzYSpe2dQhnWAD`</summary>

```json
{
  "query": "artifact",
  "max_results": 5
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "25261dc0-d7f3-4e7f-8a0a-f535e5991f9b",
  "uuid": "f661c3e1-b89b-40ad-9d9e-c5c91d734fbf",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013zL33FeAhr8kBVVpiVf3m9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 171,
      "cache_read_input_tokens": 43288,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 171
      },
      "output_tokens": 56,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 427 · 2026-05-13T02:20:03.139Z_

<details><summary>↩ Tool result · `toolu_01BVVc4BfpEzYSpe2dQhnWAD`</summary>

```text
No matching deferred tools found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "25261dc0-d7f3-4e7f-8a0a-f535e5991f9b",
  "uuid": "ad7969ec-d591-4e3b-9ba4-68853f96b01f",
  "tool_use_result": {
    "matches": [],
    "query": "artifact",
    "total_deferred_tools": 22
  }
}
```

</details>

---


### Tool call

_source line 428_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_015Y1NNLV8BfkuHEKt3CH5ND`</summary>

```json
{
  "query": "mcp agent-ml-research",
  "max_results": 10
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "25261dc0-d7f3-4e7f-8a0a-f535e5991f9b",
  "uuid": "ec922549-d127-4612-891f-7c58acfa32fc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EDwgRfCsyAUBKYe4ZvwEhs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 90,
      "cache_read_input_tokens": 43459,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 90
      },
      "output_tokens": 62,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 429 · 2026-05-13T02:20:05.522Z_

<details><summary>↩ Tool result · `toolu_015Y1NNLV8BfkuHEKt3CH5ND`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__append_idea"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__read_project_file"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__save_project_file"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "ListMcpResourcesTool"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "ReadMcpResourceTool"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "WebFetch"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "25261dc0-d7f3-4e7f-8a0a-f535e5991f9b",
  "uuid": "87e50fe3-19ca-4463-a5f6-6a59ddc39bd3",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__append_idea",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__save_project_file",
      "ListMcpResourcesTool",
      "ReadMcpResourceTool",
      "WebFetch"
    ],
    "query": "mcp agent-ml-research",
    "total_deferred_tools": 22
  }
}
```

</details>

---


### Assistant

_source line 430_

`register_artifact` 不在可用工具列表中。报告已保存至本地文件。

---

## 预检结论

**报告路径**：`artifacts/edge_pruning_precheck_report.md`

**核心发现**：

| 模型 | 适配难度 | 预估工时 | 关键依据 |
|------|---------|---------|---------|
| Qwen-2.5 0.5B | **低** | 6-10h | LLaMA-like 架构 + 社区 fork 有 `modeling_fqwen.py` 参考 |
| Llama-3.1 8B | **低-中** | 8-14h | `modeling_fllama.py` 几乎直接可用，主要工作在 FSDP 显存优化 |
| Gemma-2 2B | **中** | 16-24h | sliding window attention + logit soft-cap + pre/post-norm 混合需要额外处理 |

**推荐优先级**：Qwen-2.5 0.5B → Llama-3.1 8B → Gemma-2 2B（可选）

**关键风险**：Edge Pruning 不是 hook 注入，而是重写整个 forward pass（每个模型 1500-2000 行）。`modeling_fllama.py` 已为 LLaMA-like 架构铺好路，Qwen 和 Llama-3 适配成本可控。Gemma-2 的独特 attention 机制增加了复杂度和 bug 风险。

**替代方案**：auto-circuit 通过 TransformerLens 开箱支持三模型，但无分布式训练、显存效率差，仅适用于 Qwen-2.5 0.5B 级别作为备选。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "25261dc0-d7f3-4e7f-8a0a-f535e5991f9b",
  "uuid": "0550e5a6-34fd-410b-9046-538f17795026",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012ggTvn2YG18cnsELWgp72s",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1688,
      "cache_read_input_tokens": 43549,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1688
      },
      "output_tokens": 2,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Task result

_source line 431_

`register_artifact` 不在可用工具列表中。报告已保存至本地文件。

---

## 预检结论

**报告路径**：`artifacts/edge_pruning_precheck_report.md`

**核心发现**：

| 模型 | 适配难度 | 预估工时 | 关键依据 |
|------|---------|---------|---------|
| Qwen-2.5 0.5B | **低** | 6-10h | LLaMA-like 架构 + 社区 fork 有 `modeling_fqwen.py` 参考 |
| Llama-3.1 8B | **低-中** | 8-14h | `modeling_fllama.py` 几乎直接可用，主要工作在 FSDP 显存优化 |
| Gemma-2 2B | **中** | 16-24h | sliding window attention + logit soft-cap + pre/post-norm 混合需要额外处理 |

**推荐优先级**：Qwen-2.5 0.5B → Llama-3.1 8B → Gemma-2 2B（可选）

**关键风险**：Edge Pruning 不是 hook 注入，而是重写整个 forward pass（每个模型 1500-2000 行）。`modeling_fllama.py` 已为 LLaMA-like 架构铺好路，Qwen 和 Llama-3 适配成本可控。Gemma-2 的独特 attention 机制增加了复杂度和 bug 风险。

**替代方案**：auto-circuit 通过 TransformerLens 开箱支持三模型，但无分布式训练、显存效率差，仅适用于 Qwen-2.5 0.5B 级别作为备选。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 535604,
  "duration_api_ms": 1115067,
  "num_turns": 12,
  "stop_reason": "end_turn",
  "session_id": "25261dc0-d7f3-4e7f-8a0a-f535e5991f9b",
  "total_cost_usd": 4.20964325,
  "usage": {
    "input_tokens": 4292,
    "cache_creation_input_tokens": 33396,
    "cache_read_input_tokens": 311016,
    "output_tokens": 8579,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 33396,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 3,
        "output_tokens": 509,
        "cache_read_input_tokens": 43549,
        "cache_creation_input_tokens": 1688,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 1688
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 711996,
      "outputTokens": 45096,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.9374760000000001,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 27899,
      "outputTokens": 34993,
      "cacheReadInputTokens": 1644282,
      "cacheCreationInputTokens": 229713,
      "webSearchRequests": 0,
      "costUSD": 3.272167249999999,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "d816c7a7-924e-4aab-9cf0-423ddfeccafd"
}
```

</details>

---
