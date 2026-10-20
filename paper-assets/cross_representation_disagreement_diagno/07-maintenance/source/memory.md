# Project Memory

## MVP Gate 5/5 PASS（109/204 partial data, 2026-05-14）

mvp_pipeline_004 在 109/204 样本处静默退出（无错误日志），但已完成数据通过全部 MVP gate：
- **All mode (n=103 effective): 5/5 PASS**
  - C1: 33.0% disagree (34/103) ≥10% ✓
  - C2: 88.2% diagnostic (30/34) ≥40% ✓
  - C3: 3 error types ≥2 ✓
  - C4: +11.6pp targeted vs blind (T:69.8% B:58.1%) >5pp ✓
  - C5: 81.8% localization (18/22) ≥60% ✓
- **Excl. Unknown mode (n=67): 4/5 PASS, C4 FAIL (+3.6pp)**
- Pipeline 可 --resume 续跑剩余 95 样本

## v4 truncation fix 是 MVP 通过的关键（2026-05-14）

v4 添加 finish_reason='length' 截断检测 + enable_thinking=False 重试，**同时解决了 FOL 和 Code 端的 crash/empty 问题**。80/204 中间数据 MVP 5/5 PASS（C1 32%, C2 87.5%, C3 3 types, C4 +22.6pp, C5 100%）。从 v1(2/5)→v2(3/5)→v3(1/5) 到 v4(5/5) 的突破。

## Code Unknown 是 lazy prompt 问题，非模型能力边界（2026-05-14）

46.3% Code=Unknown 的根因：LLM 生成代码主动 print("Unknown") 而非执行错误。两种模式：(A) 硬编码放弃（注释推理后直接 print Unknown）；(B) 条件 fallback（else 分支用 Unknown 替代 False）。v5b prompt 已设计（anti-lazy Unknown + 禁止 hardcode + 3 个 few-shot）待 v4 完成后验证。

## FOL 在 FOLIO 上压倒性优于 Code（2026-05-14）

Disagree 样本中 FOL 正确 78.3% vs Code 仅 8.7%。Z3 形式化在结构化逻辑推理上远强于 Python enumeration。这意味着 disagreement 的诊断方向主要是"Code 错 FOL 对"，targeted repair 主要修 Code 端。

## 禁止双进程启动 pipeline（2026-05-14，教训）

submit_on_allocated（tmux）和 nohup 同时启动了两个 pipeline 实例，写同一输出文件，导致竞争条件 + 数据损坏 + pipeline 静默退出。**启动 pipeline 只用一种方式，确认前一个进程已终止后再启动新的。**

## v5 closed-world 2-way 方案被撤回（D007, 2026-05-14）

Reviewer 指出强制 2-way 会在 ~39% Unknown-GT 样本上制造人为 disagreement（FOL=Unknown vs Code=False），污染诊断信号。**改为 v5b：保持 3-way + anti-lazy Unknown 约束**，确保 disagreement 信号来自推理差异而非假设差异。

## Qwen3-32B-AWQ baseline 精度（2026-05-14）

FOLIO validation set direct answer accuracy = 74%（50 samples），满足 ≤85% 门控。

## Code 端 thinking token 泄漏已解决（2026-05-14）

Qwen3 系列模型默认开启 thinking mode，Code generation 时 thinking tokens 泄漏到代码输出导致解析崩溃。解决：`enable_thinking=False` + `_strip_thinking`。v3 验证 code crash 40%→0%。
