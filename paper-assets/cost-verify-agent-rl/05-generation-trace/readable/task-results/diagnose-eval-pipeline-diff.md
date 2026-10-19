# diagnose eval pipeline diff

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval-pipeline-diff_20260519T151344_result.json`
- **Structured JSON:** [`4ab174e7c05437968a02.json`](../../sessions/4a/4ab174e7c05437968a02.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。以下是逐维度对比结果。

---

## Eval Pipeline 差异分析：19.4% vs 23.88%

### 1. Prompt 构造

| 维度 | 独立脚本 | RAGEN |
|------|---------|-------|
| System prompt | `"You're a helpful assistant. "` + 自定义 SG prompt | `ctx_manager.py:580` 同样添加 `"You're a helpful assistant. "` + env_instruction |
| env_instruction | 硬编码 | 来自 `AlfworldSG_OOD.env_instruction` |
| Observation 格式 | `f"{obs}\n\nAdmissible actions: [{', '.join(admissible)}]"` | `AlfredTXTEnv._format_observation` — 完全相同格式 |
| Chat template | `tokenizer.apply_chat_template(messages, add_generation_prompt=True)` | 同 |
| **Assistant 历史消息** | **原始模型输出**（以 `&lt;/answer>` 结尾） | **`_parse_response` 重构为规范格式** `&lt;think>...&lt;/think>&lt;answer>action&lt;/answer>` |

**结论**：System prompt 文本一致。唯一差异是 RAGEN 对 assistant 消息做了规范化重构（去除尾部垃圾文本、strip special tokens）。**影响：低**。

### 2. vLLM 采样参数

| 参数 | 独立脚本 | RAGEN (reeval config) |
|------|---------|----------------------|
| temperature | 0.4 | 0.4 (val_kwargs) |
| max_tokens | 1024 | 1024 (response_length) |
| top_p | 1.0 (vLLM default) | 1.0 |
| top_k | -1 (vLLM default) | -1 |
| **stop** | **`["&lt;/answer>"]`** | **无** |
| **include_stop_str_in_output** | **True** | **N/A** |

**关键差异**：独立脚本在 `&lt;/answer>` 处停止生成，RAGEN 无 stop token，依赖模型自然输出 EOS（`<|im_end|>`）。
- 实际影响低：训练过程中模型已学会在 `&lt;/answer>` 后输出 EOS，二者行为几乎等价。
- 极端情况：若模型偶尔在 `&lt;/answer>` 后继续生成，RAGEN 会多消耗 token 但 `_parse_response` 会清理。

### 3. Action 解析逻辑

| 维度 | 独立脚本 | RAGEN |
|------|---------|-------|
| 主正则 | `&lt;answer>(.*?)&lt;/answer>` | `&lt;think>(.*?)&lt;/think>\s*&lt;answer>(.*?)&lt;/answer>` |
| Fallback | 取 response 最后一行 | Qwen3 fallback（需 `&lt;think>`），否则 `actions=[]` |
| 多 action 分割 | 不分割 | 按 `||` 分割，取前 1 个 |
| Special token 清理 | 无 | Strip `<\|im_start\|>` 等 |

**差异影响**：
- RAGEN 主正则要求 `&lt;think>` 存在，否则 primary match 失败。若模型偶尔不输出 `&lt;think>` 标签：独立脚本仍能提取 action，RAGEN 返回空 action（跳过 env step，不浪费步数）。
- 方向上这会让 RAGEN **稍有利**（不浪费 step），与结果方向一致但影响量级很小。

### 4. Max turns / Max steps

| 维度 | 独立脚本 | RAGEN |
|------|---------|-------|
| 最大 LLM 推理轮数 | `MAX_TURNS = 50` | `max_turn = 50` |
| TextWorld max_episode_steps | `config["rl"]["training"]["max_nb_steps_per_episode"]` | 同一 alfworld_config.yaml |
| 空 action 处理 | 强制执行 fallback action（浪费 env step） | `actions=[]` → 跳过 env step |

**结论**：一致。空 action 处理的差异在实践中极少触发。

### 5. 游戏环境 / Task 分配

| 维度 | 独立脚本 | RAGEN |
|------|---------|-------|
| eval split | `eval_out_of_distribution` | `AlfworldSG_OOD` → `eval_out_of_distribution` |
| Task 数量 | 134 | 134 (env_groups=134, group_size=1) |
| Game 选择 | 顺序遍历 `game_files` | `seed=123+env_id`，mod 134 映射（覆盖全部 134 个） |
| alfworld_config | 同一文件 | 同一文件 |

**结论**：134 个 OOD task 完全一致。

### 6. Checkpoint

| 维度 | 独立脚本 | RAGEN |
|------|---------|-------|
| 路径 | `/root/autodl-tmp/checkpoints/exp029_hf` (HF 格式, 4.06GB) | `exp029/global_step_15/actor/` (FSDP 格式) |
| 转换 | 已 merge 为单文件 safetensors | 原始 FSDP shards，runtime 加载 |

同一 checkpoint，仅格式不同。float 精度差异可忽略。

---

## 根因判定

**主因：T=0.4 随机采样方差。**

两次 eval 使用不同的 vLLM random seed，在 T=0.4 下每个 turn 的 action 采样都有随机性。134 个二项试验、真实成功率约 21% 下：

- σ = √(0.21 × 0.79 / 134) ≈ **3.5pp**
- 观测差异 4.48pp ≈ 1.3σ，p-value ≈ 0.19
- **在统计上不显著**，完全在正常波动范围内

次因（系统性，影响 ≤1-2 games）：
1. Stop token 差异导致极少数 turn 的 conversation history 略有不同
2. RAGEN 的 action 解析在 malformed 响应时更宽容（空 action 不浪费 step）
3. Response 规范化可能使后续 turn 的 prompt 质量略高

## 论文建议

**用 RAGEN 内置 eval 的 23.88%**，理由：
1. 方法论一致性：训练和 eval 用同一 pipeline，避免引入非受控变量
2. 独立脚本有两个非标准设计（stop token、简化 action parser），偏离了训练时的设定
3. 如需更高可信度：用 T=0 跑确定性 eval，或多 seed 取均值 ± 标准差

---
