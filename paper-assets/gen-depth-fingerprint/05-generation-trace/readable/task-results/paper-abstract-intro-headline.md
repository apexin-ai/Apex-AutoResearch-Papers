# paper abstract intro headline

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_abstract-intro-headline_20260515T222641_result.json`
- **Structured JSON:** [`5179491815480e46ca15.json`](../../sessions/51/5179491815480e46ca15.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

改动汇总：

| 位置 | 改前 | 改后 |
|------|------|------|
| `abstract.tex:6` | `(95\% CI: [0.717, 0.729])...with per-generator consistency (std=0.051)` | 删除 CI，改为 `with per-generator F1 ranging from 0.68 to 0.86` |
| `introduction.tex:25` | `(95\% CI: [0.717, 0.729])...with per-generator consistency (std=0.051)` | 删除 CI，改为 `with per-generator F1 ranging from 0.68 (Qwen3-8B) to 0.86 (Pythia-1B)` |
| `introduction.tex:34` | `(95\% CI: [0.717, 0.729])...with per-generator consistency (std=0.051)` | 删除 CI，改为 `with per-generator F1 ranging from 0.68 to 0.86` |

验证项：
- **Rd2-N1** (CI 误用): 3 处 CI 全部替换为 per-generator F1 range，不再有 ± 格式
- **Rd2-N2** (Gen-0 泄露): headline 已是 binary F1 = 0.723 (gen-1 vs gen-2+)，无需改动
- **D019** (instruct 反转): 两文件均无 "inverted DDR" claim，line 20 仅声明 instruct 模型 untested
- **数字一致性**: abstract 和 intro 三处均为 F1 = 0.723, range 0.68–0.86
- **3-class F1**: 两文件均未出现，无需处理
- **写作规范**: range 同时报 worst (0.68) 和 best (0.86)，intro 正文标注了对应 generator 名

---
