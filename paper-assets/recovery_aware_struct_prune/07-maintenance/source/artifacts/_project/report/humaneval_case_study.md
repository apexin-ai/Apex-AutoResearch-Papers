# HumanEval Case Study: GRPO CKA-only vs GRPO RASP fair

## Summary
- GRPO CKA-only: 33/164 passed (pass@1 = 20.12%)
- GRPO RASP fair: 18/164 passed (pass@1 = 10.98%)
- Both passed: 5
- CKA-only passed: 28
- RASP-only passed: 13
- Both failed: 118

## Failure Pattern Breakdown

| Pattern | CKA-only failures | RASP-fair failures |
|---------|---:|---:|
| Reasoning-as-code (NL text instead of Python) | 47 | 59 |
| Other syntax error | 36 | 35 |
| Logic error (valid code, wrong output) | 8 | 27 |
| Max length hit (2048 tokens, no other error) | 36 | 18 |
| Type/Name/Index error | 1 | 5 |
| Other runtime error | 3 | 2 |

**Response length stats (failures only):**
- CKA: mean=1667, median=2048, hit max length 91/131
- RASP: mean=1422, median=2048, hit max length 90/146

## Category 1: CKA passed, RASP failed (28 cases)

RASP failure breakdown: reasoning-as-code (11), logic error (8), max length (4), syntax error (3), other (2).

### Example 1: HumanEval/139 (RASP: reasoning-as-code)
**Task**: `special_factorial` (compute sum of squares with ceiling/rounding rules)
**CKA output** (passed): resp_len=1629, produced valid Python code
**RASP output** (failed): resp_len=2048, generated natural language: `First, we'll write a function to calculate the factorial of a number.`
**Failure pattern**: RASP emitted reasoning text instead of code, causing SyntaxError. Hit max token length (2048) while still "thinking."

### Example 2: HumanEval/112 (RASP: logic error)
**Task**: `reverse_delete` (delete chars from string, check palindrome)
**CKA output** (passed): resp_len=1250
**RASP output** (failed): resp_len=359, produced valid Python but assertion failed on `candidate("abcde","ae") == ('bcd',False)`
**Failure pattern**: RASP generated syntactically correct code but implemented the logic incorrectly. Shorter output suggests it produced a concise but wrong solution.

### Example 3: HumanEval/7 (RASP: logic error)
**Task**: `filter_by_substring`
**CKA output** (passed): resp_len=526
**RASP output** (failed): resp_len=606, assertion failed on empty list input `candidate([], 'john') == []`
**Failure pattern**: RASP code failed to handle edge case (empty list).

## Category 2: RASP passed, CKA failed (13 cases)

CKA failure breakdown: max length hit (6), reasoning-as-code (4), syntax error (2), logic error (1).

### Example 1: HumanEval/102 (CKA: reasoning-as-code)
**Task**: `choose_num` (find biggest even integer in range)
**CKA output** (failed): resp_len=2048, generated: `Okay, I need to write a Python function called choose_num that takes two positive numbers x and y and returns the biggest even integer in the range [x, y] inclusive...`
**RASP output** (passed): resp_len=185, produced concise correct code
**Failure pattern**: CKA entered chain-of-thought mode, exhausted 2048 tokens on reasoning without ever producing code. RASP solved it with a compact 185-token solution.

### Example 2: HumanEval/47 (CKA: max length)
**Task**: `median` (compute median of a list)
**CKA output** (failed): resp_len=2048, started with: `Okay, I need to write a Python function to calculate the median of a list...`
**RASP output** (passed): resp_len=161, produced correct code
**Failure pattern**: CKA again entered verbose reasoning mode and ran out of tokens. RASP produced a short, correct solution.

### Example 3: HumanEval/13 (CKA: reasoning-as-code)
**Task**: `greatest_common_divisor`
**CKA output** (failed): resp_len=897, generated: `I think the best way to find the GCD is to use the Euclidean algorithm because it's efficient...`
**RASP output** (passed): resp_len=355
**Failure pattern**: CKA generated an essay about the Euclidean algorithm instead of implementing it.

## Category 3: Both passed (5 cases)

Task IDs: HumanEval/3, HumanEval/12, HumanEval/48, HumanEval/100, HumanEval/151

### Example: HumanEval/12
**CKA**: resp_len=474
**RASP**: resp_len=614
**Note**: Both solved it, CKA with slightly more concise output.

## Category 4: Both failed (118 cases)

### Example: HumanEval/118 (different failure modes)
**Task**: `get_closest_vowel`
**CKA output** (failed): resp_len=2048, SyntaxError from reasoning text: `First, I need to understand what a "vowel" is...`
**RASP output** (failed): resp_len=229, AssertionError on `candidate("yogurt") == "u"`
**Failure pattern**: CKA failed by generating reasoning text (never produced code). RASP produced code that compiled and ran but returned wrong answer. Same task, fundamentally different failure modes.

### Example: HumanEval/0 (both reasoning/syntax)
**Task**: `has_close_elements`
**CKA output** (failed): resp_len=2048, generated: `Okay, I need to write a Python function that checks if any two numbers in a list are closer to each other than a given threshold...`
**RASP output** (failed): resp_len=1027, SyntaxError: `for i in range(len(numbers):` (missing closing parenthesis)
**Failure pattern**: CKA failed due to pure reasoning output. RASP attempted code but had a syntax error (missing `)` in `range()`).

## Key Findings

1. **CKA-only preserves more coding ability overall** (33 vs 18 correct, +83% relative). The 28 problems CKA solves but RASP cannot far outnumber the 13 RASP-only successes.

2. **Reasoning-as-code is the dominant failure mode for both models**, but RASP suffers more (59 vs 47 cases). Both GRPO-trained models struggle to stay in "code generation" mode and frequently slip into chain-of-thought reasoning as if they are in an instruction-following context rather than a code completion context.

3. **When RASP does produce code, it is more error-prone**: RASP has 27 logic errors vs CKA's 8. RASP's pruning appears to damage the model's ability to implement correct algorithms, not just its ability to produce code format.

4. **CKA's failures are more often "almost right"**: CKA failures are dominated by max-length hits (36) and reasoning-as-code (47). When CKA does produce code, it is more likely to be correct. RASP produces more code that runs but gives wrong answers.

5. **RASP's 13 unique successes tend to be simpler problems** (shorter output: median ~250 tokens) where a compact solution suffices. CKA fails these by entering verbose reasoning mode. This suggests CKA's "reasoning trap" is somewhat random and not correlated with problem difficulty.

6. **Implication for RASP vs CKA pruning**: CKA-only recovery better preserves the model's code generation capabilities. The additional structural awareness in RASP (Recovery-Aware Structured Pruning) with its current fair weighting degrades both the model's formatting discipline (more reasoning-as-code) and its algorithmic accuracy (more logic errors).