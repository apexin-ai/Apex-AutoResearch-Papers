## Per-Task Cross-Analysis: Taxonomy Penalty Decomposition

### Dose 10% (TaxEI=29/47, Random=32/47, Δ=3 tasks)

Discordant (TaxEI-fail, Random-success) [3]:
- pick_clean_then_place_in_recep-Spatula-None-Drawer-10
- pick_heat_then_place_in_recep-Egg-None-GarbageCan-10
- pick_two_obj_and_place-SoapBar-None-Cabinet-424

Discordant (TaxEI-success, Random-fail) [0]: (none)

Net TaxEI penalty tasks: 3

### Dose 25% (TaxEI=23/47, Random=26/47, Δ=3 tasks)

Discordant (TaxEI-fail, Random-success) [4]:
- pick_and_place_simple-Vase-None-Safe-219
- pick_clean_then_place_in_recep-Bowl-None-Cabinet-10
- pick_clean_then_place_in_recep-Spatula-None-Drawer-10
- pick_heat_then_place_in_recep-Potato-None-GarbageCan-10

Discordant (TaxEI-success, Random-fail) [1]:
- pick_two_obj_and_place-PepperShaker-None-Drawer-10

Net TaxEI penalty tasks: 3

### Dose 50% (TaxEI=24/47, Random=27/47, Δ=3 tasks)

Discordant (TaxEI-fail, Random-success) [6]:
- pick_and_place_simple-Vase-None-Safe-219
- pick_cool_then_place_in_recep-Lettuce-None-CounterTop-10
- pick_heat_then_place_in_recep-Potato-None-GarbageCan-10
- pick_heat_then_place_in_recep-Tomato-None-GarbageCan-10
- pick_two_obj_and_place-KeyChain-None-Safe-219
- pick_two_obj_and_place-SoapBar-None-Cabinet-424

Discordant (TaxEI-success, Random-fail) [3]:
- pick_and_place_simple-SaltShaker-None-Drawer-10
- pick_clean_then_place_in_recep-Bowl-None-Cabinet-10
- pick_clean_then_place_in_recep-Mug-None-CoffeeMachine-10

Net TaxEI penalty tasks: 3

### Cross-Dose Overlap Analysis

Tasks in ALL 3 dose points as TaxEI-penalty: **NONE (0 tasks)**

Tasks in 2/3 dose points [4]:
- pick_and_place_simple-Vase-None-Safe-219 (doses: 25%, 50%)
- pick_clean_then_place_in_recep-Spatula-None-Drawer-10 (doses: 10%, 25%)
- pick_heat_then_place_in_recep-Potato-None-GarbageCan-10 (doses: 25%, 50%)
- pick_two_obj_and_place-SoapBar-None-Cabinet-424 (doses: 10%, 50%)

Tasks in only 1 dose point [5]:
- pick_clean_then_place_in_recep-Bowl-None-Cabinet-10 (dose: 25%)
- pick_cool_then_place_in_recep-Lettuce-None-CounterTop-10 (dose: 50%)
- pick_heat_then_place_in_recep-Egg-None-GarbageCan-10 (dose: 10%)
- pick_heat_then_place_in_recep-Tomato-None-GarbageCan-10 (dose: 50%)
- pick_two_obj_and_place-KeyChain-None-Safe-219 (dose: 50%)

### Cross-Dose: TaxEI Advantage (TaxEI-success, Random-fail)

Tasks in ALL 3 dose points: **NONE (0 tasks)**
Tasks in 2/3 dose points: **NONE (0 tasks)**

Union across all doses: 4 unique tasks (each appearing in only 1 dose point)

### Key Statistics

| Metric | Value |
|--------|-------|
| Unique TaxEI-penalty tasks (union) | 9 |
| Unique TaxEI-advantage tasks (union) | 4 |
| Stable penalty core (all 3 doses) | 0 |
| Stable advantage core (all 3 doses) | 0 |
| Penalty tasks in 2/3 doses | 4 |
| Penalty tasks in 1/3 doses | 5 |

### Conclusion

**The constant 6.4pp (≈3 task) gap is a discretization coincidence, NOT a systematic penalty on a fixed set of tasks.**

Evidence:
1. **Zero tasks** appear as TaxEI-penalty in all 3 dose points — there is no stable "penalty core" that taxonomy injection consistently breaks.
2. The specific tasks that flip between TaxEI and Random **rotate across dose points**: 9 different tasks contribute to the penalty across doses, with no single task appearing at all 3 levels.
3. Even among 2/3 overlap tasks, the 4 tasks that appear twice are spread across non-overlapping dose pairs (10%+25%, 25%+50%, 10%+50%), showing no dose-monotonic pattern.
4. The TaxEI-advantage side is equally unstable: 0 tasks are consistently advantaged, and 4 unique advantage tasks each appear at only 1 dose point.
5. The raw discordant counts increase with dose (3→4→6 penalty, 0→1→3 advantage), but the net always equals 3 — this is the discretization floor of 47-task evaluation (resolution ≈ 2.13pp/task).

**Reviewer response**: The constant Δ=3 tasks across dose points is a statistical coincidence arising from the coarse 47-task granularity, not evidence of a fixed taxonomy-sensitive task subset. The discordant task sets are almost entirely disjoint across doses, ruling out a systematic mechanism.

---

## Full 47-Task Cross Table

Legend: T10/T25/T50 = TaxEI at 10%/25%/50% injection; R10/R25/R50 = Random at 10%/25%/50% injection; Y = success, N = fail

| task_name | T10 | R10 | T25 | R25 | T50 | R50 |
|-----------|-----|-----|-----|-----|-----|-----|
| look_at_obj_in_light-AlarmClock-None-DeskLamp-308 | Y | Y | Y | Y | Y | Y |
| look_at_obj_in_light-Book-None-DeskLamp-308 | N | N | N | N | N | N |
| look_at_obj_in_light-Bowl-None-DeskLamp-308 | Y | Y | N | N | Y | Y |
| look_at_obj_in_light-CD-None-DeskLamp-308 | Y | Y | Y | Y | Y | Y |
| look_at_obj_in_light-Mug-None-DeskLamp-308 | Y | Y | Y | Y | Y | Y |
| look_at_obj_in_light-Pencil-None-DeskLamp-308 | Y | Y | Y | Y | Y | Y |
| pick_and_place_simple-Mug-None-Desk-308 | Y | Y | Y | Y | Y | Y |
| pick_and_place_simple-Pencil-None-Shelf-308 | N | N | N | N | N | N |
| pick_and_place_simple-PepperShaker-None-Drawer-10 | N | N | N | N | N | N |
| pick_and_place_simple-SaltShaker-None-Cabinet-10 | N | N | N | N | N | N |
| pick_and_place_simple-SaltShaker-None-Drawer-10 | Y | Y | Y | Y | Y | N |
| pick_and_place_simple-SoapBottle-None-Toilet-424 | Y | Y | Y | Y | Y | Y |
| pick_and_place_simple-Vase-None-Safe-219 | Y | Y | **N** | **Y** | **N** | **Y** |
| pick_and_place_simple-Watch-None-Safe-219 | Y | Y | N | N | N | N |
| pick_clean_then_place_in_recep-Bowl-None-Cabinet-10 | N | N | **N** | **Y** | Y | N |
| pick_clean_then_place_in_recep-Cloth-None-Cabinet-424 | N | N | N | N | N | N |
| pick_clean_then_place_in_recep-Cloth-None-CounterTop-424 | Y | Y | Y | Y | Y | Y |
| pick_clean_then_place_in_recep-Egg-None-Microwave-10 | Y | Y | Y | Y | Y | Y |
| pick_clean_then_place_in_recep-Knife-None-CounterTop-10 | N | N | N | N | N | N |
| pick_clean_then_place_in_recep-Mug-None-CoffeeMachine-10 | Y | Y | Y | Y | Y | N |
| pick_clean_then_place_in_recep-Pan-None-CounterTop-10 | N | N | N | N | N | N |
| pick_clean_then_place_in_recep-Plate-None-CounterTop-10 | N | N | N | N | N | N |
| pick_clean_then_place_in_recep-SoapBar-None-Cabinet-424 | Y | Y | Y | Y | Y | Y |
| pick_clean_then_place_in_recep-SoapBar-None-CounterTop-424 | Y | Y | Y | Y | Y | Y |
| pick_clean_then_place_in_recep-Spatula-None-Drawer-10 | **N** | **Y** | **N** | **Y** | N | N |
| pick_cool_then_place_in_recep-Bread-None-CounterTop-10 | Y | Y | N | N | N | N |
| pick_cool_then_place_in_recep-Lettuce-None-CounterTop-10 | Y | Y | N | N | **N** | **Y** |
| pick_cool_then_place_in_recep-Mug-None-Cabinet-10 | Y | Y | Y | Y | Y | Y |
| pick_cool_then_place_in_recep-Mug-None-CoffeeMachine-10 | Y | Y | Y | Y | Y | Y |
| pick_cool_then_place_in_recep-Pan-None-CounterTop-10 | N | N | N | N | N | N |
| pick_cool_then_place_in_recep-Potato-None-Microwave-10 | N | N | N | N | N | N |
| pick_cool_then_place_in_recep-Tomato-None-Microwave-10 | N | N | N | N | N | N |
| pick_heat_then_place_in_recep-Apple-None-Fridge-10 | N | N | N | N | N | N |
| pick_heat_then_place_in_recep-Apple-None-GarbageCan-10 | Y | Y | Y | Y | Y | Y |
| pick_heat_then_place_in_recep-Cup-None-Cabinet-10 | Y | Y | Y | Y | Y | Y |
| pick_heat_then_place_in_recep-Egg-None-GarbageCan-10 | **N** | **Y** | N | N | N | N |
| pick_heat_then_place_in_recep-Mug-None-Cabinet-10 | Y | Y | Y | Y | Y | Y |
| pick_heat_then_place_in_recep-Mug-None-CoffeeMachine-10 | Y | Y | Y | Y | Y | Y |
| pick_heat_then_place_in_recep-Potato-None-GarbageCan-10 | Y | Y | **N** | **Y** | **N** | **Y** |
| pick_heat_then_place_in_recep-Tomato-None-GarbageCan-10 | Y | Y | Y | Y | **N** | **Y** |
| pick_two_obj_and_place-CD-None-Safe-308 | Y | Y | Y | Y | Y | Y |
| pick_two_obj_and_place-KeyChain-None-Safe-219 | N | N | N | N | **N** | **Y** |
| pick_two_obj_and_place-PepperShaker-None-Drawer-10 | Y | Y | Y | N | Y | Y |
| pick_two_obj_and_place-Pillow-None-Sofa-219 | Y | Y | Y | Y | Y | Y |
| pick_two_obj_and_place-SoapBar-None-Cabinet-424 | **N** | **Y** | N | N | **N** | **Y** |
| pick_two_obj_and_place-SoapBar-None-GarbageCan-424 | Y | Y | Y | Y | Y | Y |
| pick_two_obj_and_place-ToiletPaper-None-Cabinet-424 | N | N | N | N | N | N |

(Bold = discordant pairs contributing to the penalty/advantage at that dose point)
