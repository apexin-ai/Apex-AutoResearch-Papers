# paper d010 method update

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_d010_method_update_20260517T063527_result.json`
- **Structured JSON:** [`2e57decac25585d43b87.json`](../../sessions/2e/2e57decac25585d43b87.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

无破折号，无违规 -ing 短语。修改完成。

**修改清单：**

1. **信号从 eff_rank → log_det** — S_t 定义改为 log-determinant，公式改为 $\sum_{i=1}^{d} \log \sigma_i$，删除 effective rank 的 Shannon entropy 公式
2. **信号选择动机段** — 在信号定义后加入 Phase 0 calibration 对比段（0.66% 不足、log-det 6.7× 更强、Pythia 1B temporal lead）
3. **τ = 0.005** — 从 0.02 改为 0.005，加入 calibration 方法说明（Phase 0 Generations 3-5 的 mean normalized decline rate）
4. **删除 ECE 扩展句** — "Token-level ECE is implemented as a planned extension" 已删除
5. **S̃_0 初始化说明** — 在 EMA 公式后补充 "$\tilde{S}_0$ is initialized from the spectral metrics computed on the first recursive generation (Generation 1), establishing the post-fine-tuning baseline."
6. **其他参数不变** — k=1.0, α=0.5, r_min=0.20, r_max=0.80 保留，末尾显式列出全部参数值
7. **条件列表 `(b)--(d)`** 改为 "conditions (b) through (d)"，消除 en-dash

---
