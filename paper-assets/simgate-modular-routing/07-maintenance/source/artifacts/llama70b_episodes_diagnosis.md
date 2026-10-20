# Llama-70B Episode Collection 诊断报告

**日期**: 2026-05-24
**服务器**: westd-18266
**进程**: PID 196843
**判定**: ✅ 成功完成

## 总体结果

11 个 task types × 20 episodes = **220 episodes** 全部完成，共 **2070 labeled steps**。

## 每个 Task 的数据量

| Task | Episodes | Steps | det-pref | int-pref | no-pref |
|------|----------|-------|----------|----------|---------|
| chemistry-mix | 20 | 240 | 8 | 0 | 12 |
| find-animal | 20 | 210 | 7 | 0 | 13 |
| find-non-living-thing | 20 | 180 | 4 | 2 | 14 |
| freeze | 20 | 150 | 5 | 0 | 15 |
| grow-fruit | 20 | 90 | 3 | 0 | 17 |
| identify-life-stages-1 | 20 | 180 | 6 | 0 | 14 |
| identify-life-stages-2 | 20 | 150 | 5 | 0 | 15 |
| inclined-plane-determine-angle | 20 | 210 | 7 | 0 | 13 |
| lifespan-longest-lived | 20 | 150 | 5 | 0 | 15 |
| lifespan-longest-lived-then-shortest-lived | 20 | 240 | 8 | 0 | 12 |
| measure-melting-point-unknown-substance | 20 | 270 | 9 | 0 | 11 |
| **Total** | **220** | **2070** | **67** | **2** | **151** |

## Label 分布摘要

- det-preferred: 67/220 (30.5%)
- int-preferred: 2/220 (0.9%)
- no-preference: 151/220 (68.6%)

int-preferred 仅出现在 find-non-living-thing（2 次），其余 10 个 task 的 int-preferred 均为 0。

## 日志末尾摘要

日志最后记录了 `measure-melting-point-unknown-substance` task 的最后几个 episode（variation 5-19），然后输出了 GLOBAL SUMMARY。进程正常退出，无错误信息。

关键观察：
- internal 策略频繁死亡（score=-100），deterministic 策略存活率高
- det-preferred 标签主要来自 `death_asymmetry`（internal 死亡而 det 未死亡）
- no-preference 标签主要来自 `tied_alive`（两者均存活但得分相同）和 `both_dead`

## 输出文件位置

`/root/autodl-tmp/simgate-modular-routing/results/llama70b/`

每个 task 子目录包含：
- `episodes.jsonl` — episode 级数据
- `episode_summary.jsonl` — episode 摘要
- `labeled_steps.jsonl` — step 级标注数据
