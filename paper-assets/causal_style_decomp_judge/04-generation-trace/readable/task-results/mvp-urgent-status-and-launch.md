# mvp urgent status and launch

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_mvp_urgent_status_and_launch_20260520T140237_result.json`
- **Structured JSON:** [`449996af0ae4dbaf2c45.json`](../../sessions/44/449996af0ae4dbaf2c45.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个 key 相同，都是 `tum_XXB3...` 格式。API 端点 `http://47.94.22.126/v1` 拒绝认证。

**当前阻塞点：judge_scoring 需要有效的 API key 才能调用 GPT-4o。**

## Pipeline 状态总结

| 步骤 | 文件 | 状态 |
|------|------|------|
| 1. data_prep | mvp_samples.jsonl (100行) | ✅ |
| 2. counterfactual_gen | counterfactuals.jsonl (100行) | ✅ |
| 3. content_verification | verified.jsonl (100行) | ✅ 刚完成 |
| 4. judge_scoring | scored.jsonl | ❌ **API key 401** |
| 5. ate_analysis | - | 🔒 等待 step 4 |

### content_verification 结果（修复 NLI bug 后）
- **CF pass rate**: 36/100 (36%) — 瓶颈是 BERTScore < 0.92（63 条不达标）
- **NLI mean**: 0.9422（修复前 0.075，确认是 tuple vs dict 格式 bug）
- casual→formal 通过率 57.9% vs formal→casual 22.6%

### 修复记录
- `content_verification.py`: NLI pipeline 输入必须用 dict `{"text": a, "text_pair": b}` 格式（本地+服务器已修复）

### 需要你提供
API endpoint `http://47.94.22.126/v1` 返回 401，`tum_XXB3...` key 无效。需要提供有效的 API key 或替代 endpoint 来运行 judge_scoring（36 条 × 3 次评分 = 108 次 GPT-4o 调用）。

---
