# Gen 2 进度检查 — 2026-05-16 07:41 UTC

**当前步骤**: Gen2 合成数据生成（gen2_synth），尚未进入 mixing/training/eval

**进度**:
- seed42: 46% (45.8M/100M tokens), ~12,944 tok/s, 预计剩余 ~70 min
- seed137: 47% (46.8M/100M tokens), ~13,210 tok/s, 预计剩余 ~67 min

**GPU 利用率**: cuda:0 94%, cuda:1 77%（两卡均正常工作）

**预计完成时间**: 合成数据生成约 08:50 UTC 完成。之后还需 mixing → training → eval，整个 gen2 阶段预计还需 2-4 小时。

**异常信号**: 无。`padding_side` 警告为已知无害告警，进程稳定运行中。
