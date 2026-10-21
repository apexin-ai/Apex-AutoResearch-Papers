# NLI Gate Validation — Annotation Guidelines

## Task

You will see 50 pairs of texts. For each pair, an **original** text and a **rewritten** version are shown. Your task is to judge whether the rewritten text **preserves the core meaning** of the original.

## What to judge

**Focus on semantic content only.** Ask yourself: "Does the rewritten version convey the same key information, facts, and claims as the original?"

- **Yes** = The rewritten text preserves the core meaning. The key information, factual claims, and main points are retained. Minor omissions of peripheral details are acceptable.
- **No** = The rewritten text loses, distorts, or substantially changes the meaning. Important information is missing, contradicted, or replaced with different content.

## What to ignore

- **Style differences**: formality, tone, register (academic vs. casual)
- **Verbosity differences**: one version may be longer or shorter
- **Phrasing differences**: different words expressing the same idea
- **Structural changes**: reordering of points, different paragraph breaks

## Examples

### Example 1: Yes (meaning preserved)

**Original:** "The study found that sleep deprivation significantly impairs cognitive function, particularly working memory and attention span, in adults aged 25-40."

**Rewritten:** "Research shows that not getting enough sleep really messes with your brain — especially your ability to remember stuff and stay focused. This was seen in people in their late 20s to early 40s."

Judgment: **Yes**. Same factual content (sleep deprivation → cognitive impairment → working memory + attention → age group). Style changed from formal to casual, but meaning preserved.

### Example 2: No (meaning changed)

**Original:** "The algorithm achieves 95% accuracy on the test set but only 78% on out-of-distribution samples, suggesting limited generalization."

**Rewritten:** "The algorithm performs well across all evaluation settings, demonstrating strong generalization capability with high accuracy scores."

Judgment: **No**. The original highlights a generalization *limitation* (95% vs 78%), while the rewritten text claims *strong* generalization. The core claim is reversed.

## Practical notes

- Each judgment should take 30-60 seconds. Read both texts carefully.
- Use the "Notes" field if you find a borderline case or want to explain your reasoning.
- There are no trick questions. Trust your judgment on whether meaning is preserved.
- If you are genuinely uncertain, lean toward "Yes" (preserves meaning).
