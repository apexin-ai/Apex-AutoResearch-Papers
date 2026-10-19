# research scienceworld grpo prep

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_scienceworld_grpo_prep_20260520T061757_result.json`
- **Structured JSON:** [`bdec65a199fe0d63cb89.json`](../../sessions/bd/bdec65a199fe0d63cb89.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已注册。以下是完整的准备总结：

---

## ScienceWorld GRPO Cell A 准备情况

### 已就绪 (无需修改)
- ScienceWorld env 代码 (`ragen/env/scienceworld/`) — 完整实现 BaseLanguageBasedEnv 接口
- env 注册在 `__init__.py` — `scienceworld` type 已可用
- SFT checkpoint — `/root/autodl-tmp/checkpoints/scienceworld_sft/huggingface` (Qwen3-1.7B)
- Java / scienceworld package — eval_v2 正在用，已验证可用
- 磁盘 61GB 可用

### 需要创建的 2 个文件

**1. envs.yaml 追加 `ScienceWorldSG` tag** — 包含全部 30 个任务、`&lt;answer>` tag 格式的 env_instruction、score=10.0、max_steps=100

**2. `_scienceworld_cell_a_grpo.yaml`** — 基于 ALFWorld hsweep_h2 的严格控制变量设计：
- 仅改 model_path、env tag、max_turn (50→100)、response_length (1024→512)
- 其余算法参数完全一致：step_independent h=2, GRPO γ=0.95, lr=1e-6, kl=0.01

### 具体配置内容和训练命令

详见 `artifacts/scienceworld_grpo_cell_a_prep.md`

### 关键风险
1. **JVM 开销** — 128 env 实例可能需要大量内存，监控后酌情降低 env_groups
2. **Prompt format mismatch** — SFT 用 bare-text action，RAGEN 用 `&lt;answer>` tags（有 fallback parser，不影响核心结论）
3. **连续 reward** — ScienceWorld reward ∈ [-10, +10] vs ALFWorld binary {0, 10}（sign misattribution 机制仍成立）

### 时间线
eval_v2 完成后（~10h），执行 pre-flight checklist (C002)，然后提交训练。

---
