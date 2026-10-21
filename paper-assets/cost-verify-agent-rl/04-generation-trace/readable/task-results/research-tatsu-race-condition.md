# research tatsu race condition

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_tatsu_race_condition_20260516T153213_result.json`
- **Structured JSON:** [`1fa53ccb2352a61b8bde.json`](../../sessions/1f/1fa53ccb2352a61b8bde.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。产出总结：

---

## 根因分析

TextWorld 1.7.0 有 4 个 **模块级单例** TatSu parser。`ParseContext.parse()` 每次调用都修改实例状态（`_tokenizer`、`_statestack`、`_last_node` 等），多线程并发调用会互相覆盖状态。

**最关键的是 #4 (CSGParser)**：它在每次 `env.step()` 时都被调用（`grammar.derive()` → `_parse_and_convert()` → `_PARSER.parse()`），即使 env 创建被锁保护，并行 step 仍会 race。

## 推荐方案

**Thread-local parser 实例**（方案 B）— 每个线程自动获得独立 parser，零锁竞争，内存开销可忽略。

排除方案：
- 方案 A（全局锁）：会序列化所有 step 中的 parse 调用，削弱并行收益
- 方案 C（升级 tatsu）：5.8.3→5.19.0 API 变化大，textworld 不兼容

## 验证结果

| 条件 | 结果 |
|------|------|
| 无 patch，4 线程并行 step | **7/8 崩溃**（IndexError/TypeError） |
| 有 patch，4 线程并行 step | **8/8 通过** |

## 文件位置

- Patch: `/root/cost-verify-agent-rl/RAGEN/patches/tatsu_parallel_fix.py`
- 测试: `/root/cost-verify-agent-rl/RAGEN/patches/test_tatsu_parallel.py`
- 文档: `/root/cost-verify-agent-rl/RAGEN/patches/README_tatsu_fix.md`

## 预估加速

`max_workers=4` 时 val 从 ~10min → **~2.5min**（4x），瓶颈转移到 env 创建（串行，受 fast_downward 限制）。

---
