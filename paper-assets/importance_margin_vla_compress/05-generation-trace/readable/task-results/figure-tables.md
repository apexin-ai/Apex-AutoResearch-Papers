# figure tables

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_figure_tables_20260526T074712_result.json`
- **Structured JSON:** [`7ce0d42501f089725696.json`](../../sessions/7c/7ce0d42501f089725696.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个表格已生成并注册。

**Table 1 (`tab_model_properties.tex`)**: 6 个 VLA 模型，按 Eval 类型分组（Closed-loop → Offline），组内按 CV 升序。7 列：Model, Params, Connector, Tokens, CV, Coupling, Eval。

**Table 2 (`tab_main_results.tex`)**: 8 列（Model, Suite, Method, Base, k=0.95/0.9/0.7/0.5），17 行数据。数据来源：
- **π₀.₅**: 4 个 suite（Obj/Goal/Long/Spat），registry + prompt 硬编码值
- **OpenVLA**: Obj + Goal，Goal 缺 k=0.95 和 k=0.7 数据（标 `--`）
- **X-VLA**: Obj + Goal，Obj baseline 用 99.2%（从 L2 k=0.9 估算，无显式 k=1.0 实验）
- **SmolVLA**: 灰色标注 "0% at all k"

加粗规则：每个 k 列内，L2 和 R 中较高者加粗。

注意事项：
- X-VLA Object baseline (99.2%) 是估算值，registry 中无显式 k=1.0 baseline
- X-VLA Goal 呈现非单调现象（k=0.95 性能低于 k=0.9），与 BART 解码器的 entangling 特性一致
- π₀.₅ Object Random 在 k=0.9 时骤降至 9%（其他 k 值 ~68-74%），zeromask 实验证实这是序列长度敏感性而非 token 选择问题

---
