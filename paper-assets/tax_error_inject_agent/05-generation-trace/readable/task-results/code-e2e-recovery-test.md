# code e2e recovery test

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_e2e-recovery-test_20260514T085709_result.json`
- **Structured JSON:** [`8bc08e5e30d82ebe6a3e.json`](../../sessions/8b/8bc08e5e30d82ebe6a3e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇报：

---

### 结果汇报

**1. API recovery 生成**：成功。10 条轨迹计划 10 个注入变体，生成 9 条（1 条因轨迹过短注入失败，属正常）。9 次 API 调用，共 4,316 input + 1,816 output tokens，费用 $0.029。

**2. Recovery 内容抽检**：真实推理，非占位符。模型能识别注入造成的历史不一致并正确推理下一步动作。示例：
- P1_step_order_swap：`"The history is a bit inconsistent: after 'use desklamp 1' the game prints a fresh room description... the best next step is to go to the bed to find the pillow."`
- P2_sub_goal_deletion：`"History is consistent: you navigated among coffeetables and drawers, opening drawers 1–3 and finding them empty... open drawer 4."`

**3. SFT 格式化验证**：
- Vanilla SFT: 10 条
- TaxEI SFT: 19 条（10 vanilla + 9 injected）
- 无 DRY_RUN 占位符

**4. formatter.py 安全检查**：已在服务器和本地两份 formatter.py 中加入 `[DRY_RUN]` 检测，写入 JSONL 前会 raise `ValueError`。经测试验证可正确拦截。

**5. API 配置备注**：API key 需要通过 `--api_key` 参数传入（从 `collect_trajectories.py` 中获取的 key），base_url 和 model 使用默认值即可。

---
