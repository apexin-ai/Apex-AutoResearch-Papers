# paper write method section

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_write-method-section_20260515T174213_result.json`
- **Structured JSON:** [`eada791452bd4311827d.json`](../../sessions/ea/eada791452bd4311827d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

编译成功。method.tex 已完成，约 870 词，四个小节完整覆盖：

- **§2.1 Problem Setup**: 定义 patch $p$、test suite $T$、F2P/P2P 分区、正确性条件
- **§2.2 Verification Formulations**: \cls{}（单 token 二分类）、\cwm{}（变长生成 + exact match）、TRAJ（trajectory-level 控制组）
- **§2.3 CWM Failure Modes**: 三种失败模式分段论述——token-budget exhaustion、string-value prediction errors、format compliance collapse（强调后者质性区别）；末段论证 \cls{} 构造性规避全部三种并提出 complexity-dependent advantage 假说
- **§2.4 Oracle Framework**: $P_{\text{detect}}$、$k_{\text{eff}}$（ICC block-correlation）、$\mathbb{E}[\Delta]$ 三个公式；三条可检验预测 + P2P regression rate 分析

主要改进点（相对原 53 行草稿）：全文统一使用 `\cls{}`/`\cwm{}` 宏；format compliance collapse 独立成段并标注为 dominant error source；string-value errors 加入 $q^L$ 乘性论证；oracle 部分拆分为 detection probability / block-correlation / testable predictions 三段；增加 ICC 引用 `\citep{shrout1979icc}`。

---
