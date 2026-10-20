# experiment multi seed qwen25 pw cuda0

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_experiment_multi-seed-qwen25-pw-cuda0_20260522T072945_result.json`
- **Structured JSON:** [`d3c7f0cd5ec67698051b.json`](../../sessions/d3/d3c7f0cd5ec67698051b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部就绪。汇总：

## 产出

**1. cuda:0 vLLM 部署**
- Qwen2.5-14B-Instruct on port 8005, PID 551162 (EngineCore 551459)
- 杀掉了之前空闲的 Qwen3 (port 8001)

**2. cuda:1 进度**
- FOLIO seed=123 ✅ 完成 (14:03)
- FOLIO seed=456 正在跑 (118/204, ETA ~1hr)
- FOLIO seed=789 未开始 (~2.5hr)
- **PW 部分预计 ~19:00 才开始**

**3. cuda:0 PW master**
- PID 552333，正在跑 PW seed=123 (1/600, ~50.7s/prob)
- 脚本：`scripts/multiseed_qwen25_pw_cuda0.sh`
- 日志：`/tmp/multiseed_qwen25_pw_cuda0_nohup.log`、`/tmp/qwen25_pw_seed{123,456,789}.log`

**4. ETA 估算**
- 每 seed ~8.4hr (600 × 50.7s)
- 3 seeds 顺序跑 ~25hr 总计
- seed=123 完成 ~5/23 00:00
- 全部完成 ~5/23 ~17:00

**5. 冲突风险**
cuda:1 master 跑完 FOLIO 后会顺序进入 PW，写到**同一目录** `results/multi_seed/qwen25_pw_seed*/`，且没带 `--resume`，会覆盖 cuda:0 的结果。两个选择：
- (A) cuda:1 FOLIO 跑完后手动 kill master，只保留 cuda:0 PW 结果
- (B) 两边都跑，cuda:1 覆盖也无所谓（同模型同参数，结果统计等价）

---
