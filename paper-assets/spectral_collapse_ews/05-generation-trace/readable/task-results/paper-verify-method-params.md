# paper verify method params

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_verify_method_params_20260517T062344_result.json`
- **Structured JSON:** [`ae60c346fb72bdd8f480.json`](../../sessions/ae/ae60c346fb72bdd8f480.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

修复完成。

## 检查结果

**参数一致性：全部一致**
| 参数 | method.tex | config.py / controller.py |
|------|-----------|--------------------------|
| τ | 0.02 (隐含) | 0.02 ✓ |
| k | (隐含) | 1.0 ✓ |
| α | 0.5 | 0.5 ✓ |
| r_min | (隐含) | 0.20 ✓ |
| r_max | (隐含) | 0.80 ✓ |

**公式不一致（已修复）：**
- uniform residual 分母：paper 原为 `T-t`，code 为 `T-t-1`（`remaining_gens = T - self.t`，self.t 在计算前已递增）
- 已修正为 `T-t-1` 并改 underbrace 标注为 "forward baseline"
- 添加了 `$T-t-1$ is the number of subsequent generations (from $t+2$ to $T$)` 说明

**Controller 触发机制（代码验证）：**
1. 每代训练后，对 probe set 做 forward pass 计算 effective rank S_t
2. EMA 平滑：S̃_t = 0.5·S_t + 0.5·S̃_{t-1}
3. 归一化下降率：Δ_t = (S̃_{t-1} - S̃_t) / |S̃_0|
4. 仅当 Δ_t > τ=0.02 时触发 reactive boost（死区内不响应）
5. boost 大小 = k·(Δ_t - τ)，与下降速率成正比
6. 输出经 budget-constrained clipping 保证剩余每代至少获得 r_min

---
