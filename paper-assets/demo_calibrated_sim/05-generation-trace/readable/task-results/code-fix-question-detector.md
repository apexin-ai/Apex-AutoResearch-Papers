# code fix question detector

**Why Calibration Fails: A Taxonomy of Failure Modes in Dialect-Aware LLM User Simulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix-question-detector_20260512T124406_result.json`
- **Structured JSON:** [`379e9c90252bb49f44f1.json`](../../sessions/37/379e9c90252bb49f44f1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Code looks clean. Here's the summary:

## 修改结果

**文件**: `artifacts/code/behavioral_fingerprint.py` — `QuestionDetector` 内部逻辑重写，接口不变。

### 新增过滤层
| 过滤器 | 正则 | 作用 |
|--------|------|------|
| `_MODAL_REQUEST_RE` | `^(Can\|Could\|Would\|Will\|Shall\|May) (you\|we\|I) .+\?$` | 过滤 "Can you check my order?" 类请求 |
| `_CONFIRMATION_RE` | `^Aux that (correct\|right\|ok\|work\|sound...)...\?$` | 过滤 "Is that correct?" 类确认 |
| `_IS_THERE_CHANCE_RE` | `^Is there any chance you could...\?` | 过滤伪装成 yes/no 的礼貌请求 |
| `_AUX_YOU_RE` | `^Aux you ...` | 过滤 "Do you have access?" 类请求 |
| `_WH_QUESTION_RE` (增强) | 支持前导连词 And/But/So... | 捕获 "And what payment methods...?" |

### 82-turn 验证结果

| 指标 | OLD | NEW |
|------|-----|-----|
| 检出 turns | 42/82 (51.2%) | 2/82 (2.4%) |
| Precision | ~19% | **100%** (2/2 均为真实信息查询) |
| 检出内容 | — | "What color options are available for the glass bookshelf?" + "And what payment methods do you offer for the refund?" |

### H1 阈值影响

**H1 (question_rate ≥ 15%) 不再成立。** 3-task quick test 基线：

- OLD: 7/7 traces PASS，mean = 68.8%
- NEW: 3/7 traces PASS，mean = 11.4%

H1 阈值需要从 15% 下调（建议 ≥ 5%）来适配修正后的检测器，否则多数 trace 会被误判为"无问题行为"。

---
