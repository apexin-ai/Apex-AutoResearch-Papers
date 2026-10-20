# write paper method experiments r3

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_write_paper-method-experiments-r3_20260514T231133_result.json`
- **Structured JSON:** [`edf12fc9630f3c53ccb2.json`](../../sessions/ed/edf12fc9630f3c53ccb2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。Method 和 Experiments 两个章节已写入，包含：

**Method** (sec:method): Task+GRPO → STA 协议 → ISR 公式 (Eq.1) + 局限性声明 (component-count confound) → 6 reward conditions → 7-mode hacking taxonomy 定义

**Experiments** (sec:experiments): 
- **4.1 Setup**: Qwen3-4B, GRPO K=8, 500 steps, 3 seeds, train_500_seed42.jsonl
- **4.2 Diagnostic** (Claim 1): ISR 崩塌 0.642→0.132→0.003, 3-seed 分化 (σ=47pp), SFT 92.9% non-hacking
- **4.3 Goodhart** (Claim 2): β=0.1 H7=64.5% vs Random 0%, premise-count-matched 1.06x, β=0.3 PR 18% vs 48%
- **4.4 Cross-logic** (Claim 3): Prolog exec-only ISR≈0 诊断迁移, Prolog STA 3/3 universal Goodhart 0% genuine
- **4.5 Taxonomy**: 7 modes, hacking composition vs prevalence

所有数字已与 registry 交叉验证，每个定量 claim 附 `%% registry:` 注释。Provenance 覆盖率 100%。

---
