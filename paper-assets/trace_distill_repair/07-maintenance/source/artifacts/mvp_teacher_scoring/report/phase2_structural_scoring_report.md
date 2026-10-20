# Phase 2 Structural Scoring — 完整统计报告

**生成时间**: 2026-05-14  
**数据源**: `pipeline_output/phase2_structural_scores.json`  
**Pipeline 参数**: mode=structural, dry_run=false, max_segments_per_instance=0(无上限), 耗时 1114.9s

---

## 1. Per-Instance 分布表

| instance | total | keep | drop | keep% | annotation | segment_types |
|----------|------:|-----:|-----:|------:|------------|---------------|
| black_1 | 4 | 0 | 4 | 0.0% | | 2 call_subtree, 1 basic_block, 1 exception_chain |
| black_14 | 3 | 0 | 3 | 0.0% | | 1 basic_block, 1 call_subtree, 1 exception_chain |
| black_2 | 3 | 0 | 3 | 0.0% | | 1 basic_block, 1 call_subtree, 1 exception_chain |
| black_5 | 3 | 0 | 3 | 0.0% | | 1 basic_block, 1 call_subtree, 1 exception_chain |
| cookiecutter_1 | 20 | 7 | 13 | 35.0% | | 15 call_subtree, 4 basic_block, 1 loop_iteration |
| cookiecutter_2 | 20 | 1 | 19 | 5.0% | | 15 call_subtree, 4 basic_block, 1 loop_iteration |
| cookiecutter_3 | 6 | 2 | 4 | 33.3% | | 3 call_subtree, 2 basic_block, 1 exception_chain |
| httpie_1 | 1 | 0 | 1 | 0.0% | too_small | 1 exception_chain |
| httpie_2 | 20 | 0 | 20 | 0.0% | | 13 loop_iteration, 6 basic_block, 1 call_subtree |
| luigi_1 | 20 | 2 | 18 | 10.0% | | 12 call_subtree, 4 basic_block, 2 exception_chain, 2 loop_iteration |
| luigi_10 | 4 | 0 | 4 | 0.0% | low_segment_count | 2 basic_block, 2 exception_chain |
| luigi_14 | 2 | 0 | 2 | 0.0% | low_segment_count | 2 exception_chain |
| luigi_2 | 20 | 0 | 20 | 0.0% | | 11 call_subtree, 5 loop_iteration, 2 exception_chain, 2 basic_block |
| luigi_5 | 3 | 0 | 3 | 0.0% | low_segment_count | 2 exception_chain, 1 basic_block |
| sanic_1 | 8 | 0 | 8 | 0.0% | | 4 basic_block, 3 call_subtree, 1 exception_chain |
| sanic_2 | 20 | 0 | 20 | 0.0% | | 10 loop_iteration, 8 call_subtree, 2 basic_block |
| scrapy_1 | 18 | 0 | 18 | 0.0% | | 10 loop_iteration, 5 basic_block, 3 exception_chain |
| scrapy_2 | 20 | 1 | 19 | 5.0% | | 10 loop_iteration, 7 basic_block, 2 call_subtree, 1 exception_chain |
| scrapy_3 | 19 | 0 | 19 | 0.0% | | 10 loop_iteration, 5 basic_block, 2 call_subtree, 2 exception_chain |
| scrapy_4 | 2 | 1 | 1 | 50.0% | too_small | 1 call_subtree, 1 exception_chain |
| scrapy_7 | 2 | 2 | 0 | 100.0% | too_small | 1 call_subtree, 1 exception_chain |
| thefuck_1 | 4 | 0 | 4 | 0.0% | | 2 call_subtree, 1 basic_block, 1 exception_chain |
| thefuck_2 | 4 | 0 | 4 | 0.0% | | 2 call_subtree, 1 basic_block, 1 exception_chain |
| thefuck_4 | 3 | 0 | 3 | 0.0% | | 2 call_subtree, 1 exception_chain |
| tornado_1 | 20 | 0 | 20 | 0.0% | | 16 loop_iteration, 2 call_subtree, 2 basic_block |
| tornado_2 | 20 | 1 | 19 | 5.0% | | 18 loop_iteration, 1 call_subtree, 1 basic_block |
| tornado_4 | 20 | 1 | 19 | 5.0% | | 16 loop_iteration, 3 call_subtree, 1 basic_block |
| tornado_5 | 20 | 1 | 19 | 5.0% | | 17 loop_iteration, 2 call_subtree, 1 basic_block |
| tornado_7 | 20 | 1 | 19 | 5.0% | | 15 loop_iteration, 3 call_subtree, 2 basic_block |
| tqdm_1 | 20 | 0 | 20 | 0.0% | | 9 call_subtree, 8 basic_block, 2 loop_iteration, 1 exception_chain |
| tqdm_2 | 2 | 0 | 2 | 0.0% | too_small | 1 call_subtree, 1 exception_chain |
| youtube-dl_1 | 20 | 1 | 19 | 5.0% | | 9 call_subtree, 9 loop_iteration, 1 basic_block, 1 exception_chain |
| youtube-dl_10 | 20 | 1 | 19 | 5.0% | | 10 loop_iteration, 5 call_subtree, 5 basic_block |
| youtube-dl_2 | 20 | 0 | 20 | 0.0% | | 11 loop_iteration, 6 call_subtree, 2 basic_block, 1 exception_chain |
| youtube-dl_20 | 20 | 1 | 19 | 5.0% | | 12 loop_iteration, 4 call_subtree, 2 basic_block, 2 exception_chain |
| youtube-dl_5 | 20 | 0 | 20 | 0.0% | | 9 loop_iteration, 7 call_subtree, 2 basic_block, 2 exception_chain |

---

## 2. Overall 统计

### 基础数据

| 指标 | 值 |
|------|-----|
| 总 instances | 36 |
| 排除的 instances | fastapi_1, fastapi_2, fastapi_3, fastapi_5 |
| 标注的 instances | httpie_1(too_small), tqdm_2(too_small), scrapy_4(too_small), scrapy_7(too_small), luigi_5(low_segment_count), luigi_10(low_segment_count), luigi_14(low_segment_count) |
| 总 segments | 451 |
| Keep | 23 |
| Drop | 428 |
| **Overall keep rate** | **5.1%** |

### Keep Rate 分布

| Keep Rate 区间 | Instance 数 |
|----------------|------------|
| 0%（全 drop） | 22 |
| >0% | 14 |
| >10% | 4 |
| >20% | 4 |
| >30% | 4 |
| >50% | 1 |
| 100% | 1 |

**结论**: 61% 的 instance（22/36）被完全 drop，仅 4 个 instance keep rate 超过 10%。

### 按 Segment Type 分组的 Keep Rate

| segment_type | total | keep | drop | keep_rate | avg_keep_tokens |
|-------------|------:|-----:|-----:|----------:|----------------:|
| basic_block | 81 | 1 | 80 | 1.2% | 482 |
| call_subtree | 137 | 13 | 124 | 9.5% | 392 |
| exception_chain | 36 | 5 | 31 | 13.9% | 1876 |
| loop_iteration | 197 | 4 | 193 | 2.0% | 303 |

**结论**: exception_chain keep rate 最高（13.9%），call_subtree 次之（9.5%）。loop_iteration 数量最多（197）但 keep rate 最低（2.0%），说明循环迭代中大量冗余。basic_block 几乎全部 drop（1.2%）。

---

## 3. Keep Segments 分析

### 最多 Keep 的 Instances（Top 14）

| instance | keep | total | keep_rate | avg_keep_tokens |
|----------|-----:|------:|----------:|----------------:|
| cookiecutter_1 | 7 | 20 | 35.0% | 323 |
| cookiecutter_3 | 2 | 6 | 33.3% | 1036 |
| luigi_1 | 2 | 20 | 10.0% | 3344 |
| scrapy_7 | 2 | 2 | 100.0% | 485 |
| cookiecutter_2 | 1 | 20 | 5.0% | 295 |
| scrapy_2 | 1 | 20 | 5.0% | 1046 |
| scrapy_4 | 1 | 2 | 50.0% | 319 |
| tornado_2 | 1 | 20 | 5.0% | 405 |
| tornado_4 | 1 | 20 | 5.0% | 482 |
| tornado_5 | 1 | 20 | 5.0% | 142 |
| tornado_7 | 1 | 20 | 5.0% | 142 |
| youtube-dl_1 | 1 | 20 | 5.0% | 159 |
| youtube-dl_10 | 1 | 20 | 5.0% | 661 |
| youtube-dl_20 | 1 | 20 | 5.0% | 522 |

### Keep Segments Type 分布

| segment_type | count | 占比 |
|-------------|------:|-----:|
| call_subtree | 13 | 56.5% |
| exception_chain | 5 | 21.7% |
| loop_iteration | 4 | 17.4% |
| basic_block | 1 | 4.3% |

### Keep Segments Token 统计

| 指标 | 值 |
|------|---:|
| 总 keep segments | 23 |
| Mean token_estimate | 703 |
| Median token_estimate | 319 |
| Min | 142 |
| Max | 6364 |
| Mean confidence | 0.61 |
| Confidence range | 0.50 – 0.95 |

**结论**: Keep segments 以 call_subtree 为主（56.5%），token 中位数仅 319，说明保留的多为短小精干的函数调用。但 max=6364（luigi_1）存在较长 keep segment。confidence 均值 0.61 偏低，模型对 keep 决策不太确定。

---

## 4. Structural vs Line Segments 对比（Line Scoring 预备数据）

| instance | struct_segs | line_segs | ratio | ~trace_tokens | >2K |
|----------|----------:|----------:|------:|--------------:|:---:|
| black_1 | 4 | 11 | 2.8x | 4,481 | Y |
| black_14 | 3 | 9 | 3.0x | 3,865 | Y |
| black_2 | 3 | 10 | 3.3x | 4,210 | Y |
| black_5 | 3 | 9 | 3.0x | 4,048 | Y |
| cookiecutter_1 | 20 | 37 | 1.9x | 13,598 | Y |
| cookiecutter_2 | 20 | 37 | 1.9x | 13,601 | Y |
| cookiecutter_3 | 6 | 8 | 1.3x | 3,319 | Y |
| httpie_1 | 1 | 1 | 1.0x | 528 | |
| httpie_2 | 20 | 130 | 6.5x | 47,669 | Y |
| luigi_1 | 20 | 666 | 33.3x | 240,695 | Y |
| luigi_10 | 4 | 391 | 97.8x | 143,439 | Y |
| luigi_14 | 2 | 390 | 195.0x | 142,768 | Y |
| luigi_2 | 20 | 664 | 33.2x | 239,398 | Y |
| luigi_5 | 3 | 391 | 130.3x | 142,746 | Y |
| sanic_1 | 8 | 16 | 2.0x | 7,306 | Y |
| sanic_2 | 20 | 140 | 7.0x | 49,861 | Y |
| scrapy_1 | 18 | 41 | 2.3x | 15,133 | Y |
| scrapy_2 | 20 | 34 | 1.7x | 12,096 | Y |
| scrapy_3 | 19 | 32 | 1.7x | 11,370 | Y |
| scrapy_4 | 2 | 2 | 1.0x | 621 | |
| scrapy_7 | 2 | 2 | 1.0x | 621 | |
| thefuck_1 | 4 | 7 | 1.8x | 2,744 | Y |
| thefuck_2 | 4 | 7 | 1.8x | 2,742 | Y |
| thefuck_4 | 3 | 6 | 2.0x | 2,656 | Y |
| tornado_1 | 20 | 1,412 | 70.6x | 481,846 | Y |
| tornado_2 | 20 | 990 | 49.5x | 333,755 | Y |
| tornado_4 | 20 | 1,283 | 64.2x | 443,480 | Y |
| tornado_5 | 20 | 273 | 13.7x | 95,607 | Y |
| tornado_7 | 20 | 288 | 14.4x | 101,267 | Y |
| tqdm_1 | 20 | 94 | 4.7x | 32,504 | Y |
| tqdm_2 | 2 | 2 | 1.0x | 770 | |
| youtube-dl_1 | 20 | 13,449 | 672.5x | 5,244,031 | Y |
| youtube-dl_10 | 20 | 6,073 | 303.6x | 2,329,908 | Y |
| youtube-dl_2 | 20 | 11,931 | 596.5x | 4,584,057 | Y |
| youtube-dl_20 | 20 | 12,764 | 638.2x | 4,975,971 | Y |
| youtube-dl_5 | 20 | 10,435 | 521.8x | 3,960,131 | Y |

### >2K Token 子集

**32 / 36 instances** 属于 >2K token 子集（仅 httpie_1, scrapy_4, scrapy_7, tqdm_2 低于 2K）。

### Line/Structural 比率分层

| 比率区间 | instances | 代表 |
|---------|----------:|-------|
| 1.0x–2.0x（几乎等粒度） | 8 | httpie_1, scrapy_4/7, tqdm_2, cookiecutter_3, scrapy_2/3, thefuck_1/2 |
| 2.0x–10x（中等差异） | 10 | black_*, cookiecutter_1/2, sanic_*, scrapy_1, tqdm_1, thefuck_4 |
| 10x–100x（大差异） | 8 | httpie_2, luigi_1/2/10, tornado_1/2/5/7 |
| >100x（极端差异） | 10 | luigi_5/14, tornado_4, youtube-dl_* |

**结论**: structural segmentation 大幅压缩了 segment 数量。对小 trace（<10K tokens）两者差异不大（1–3x），但对大 trace（特别是 youtube-dl 的 5M+ tokens）差异达 600x+。这意味着 line scoring 在大 trace 上面临巨大的 LLM 调用开销，structural scoring 的粗粒度过滤价值在大 trace 上最突出。

---

## 5. 关键发现摘要

1. **Structural scoring 极度激进**: 整体 keep rate 仅 5.1%（23/451），61% instance 全部 drop
2. **Exception chain 最有诊断价值**: keep rate 13.9%，远高于其他类型；keep 的 exception_chain 平均 1876 tokens，信息密度高
3. **Loop iteration 大量冗余**: 占总 segments 44%（197/451），但 keep rate 仅 2.0%
4. **Cookiecutter 系列表现最好**: cookiecutter_1 keep 7/20 (35%)，是唯一多 segment keep 的 instance
5. **Confidence 偏低**: keep 决策的平均 confidence 0.61，模型对"保留"不太确定，可能需要调低 keep 阈值或提供更好的 prompt 上下文
6. **Line scoring 开销预估**: 总 line segments 约 61,443（vs structural 451），line scoring LLM 调用量将是 structural 的 ~136 倍
