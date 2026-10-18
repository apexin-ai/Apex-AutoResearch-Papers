# analysis eval smart compress m16

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_eval_smart_compress_m16_20260518T050918_result.json`
- **Structured JSON:** [`dc8f1b30441f816ad4b1.json`](../../sessions/dc/dc8f1b30441f816ad4b1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。结果汇总：

**Overall SR: 55.8% (279/500)**, 95% CI: [51.4%, 60.1%]

**Per-task SR:**

| Task | Object | SR |
|------|--------|-----|
| 0 | alphabet soup | 56% (28/50) |
| 1 | cream cheese | 44% (22/50) |
| 2 | salad dressing | 72% (36/50) |
| 3 | bbq sauce | 56% (28/50) |
| 4 | ketchup | 62% (31/50) |
| 5 | tomato sauce | 40% (20/50) |
| 6 | butter | 78% (39/50) |
| 7 | milk | 54% (27/50) |
| 8 | chocolate pudding | 76% (38/50) |
| 9 | orange juice | 20% (10/50) |

**运行时间:** ~55 分钟, EXIT_CODE=0, 无实质性错误（仅 robosuite macros 和 OpenGL 的 benign warnings）

**Conclusion: success**

**Compression curve 对比：**
| Config | Tokens | Compression | Overall SR |
|--------|--------|-------------|------------|
| SmolVLA baseline | 128 | 0% | 44.8% |
| M=64 | 64 | 50% | 61.6% |
| M=32 | 32 | 75% | 61.6% |
| **M=16** | **16** | **87.5%** | **55.8%** |
| OpenVLA | - | - | 74.0% |

M=16 相比 M=32/M=64 下降了 5.8 个百分点，符合 hypothesis 预期：87.5% 极端压缩开始出现退化，建立了 compression curve 的下界。但仍显著高于 SmolVLA baseline（+11.0pp），说明即使在极端压缩下 smart compression 仍然有效。

---
