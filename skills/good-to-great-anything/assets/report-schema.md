# Report page data schema

`report-template.html` renders a guided walkthrough (one idea per screen, with a "Show all" switch to a single page) from one JSON object. Fill in only that object. Every field is optional except `subject`, `state` and `verdict.headline`. A missing field just hides its part of the page.

## Writing rules

- **Same content as the analysis.** This is a presentation of the deliverable, not a new analysis. Don't add claims that aren't in it.
- **Short strings.** Each string is one sentence or a short phrase. Put the detail in `why`, `detail` or `evidence`, never in a title.
- **Inline formatting:** `**bold**`, `*italic*` and `` `code` `` work inside strings. Keep `[ASSUMPTION]` or `[ASSUMPTION: note]` tags on inferred figures exactly as in the analysis: the page shows them as amber flags.
- **Valid JSON.** Use double quotes and no trailing commas. Escape `"` as `\"`, and write `</` as `<\/` so the script block can't close early.
- **Gate verdicts** are `PASS`, `CONDITIONAL` or `FAIL`. Severities are `high`, `medium` or `low`. Bus calls are `keep`, `move`, `add`, `not_yet` or `off`.

## Fields

```jsonc
{
  "subject": "Linewright",                       // name shown in the top bar
  "subject_type": "Solo-founder product",        // optional; a nonprofit, social or civic type relabels the engine as a "resource engine"
  "as_of": "end of Q3, Year 0",
  "mode": "autonomous",                          // "interview" | "autonomous"
  "state": "good",                               // "not_yet_good" | "good" | "turnaround" | "already_great"

  "verdict": {
    "headline": "Good, not yet great. ...",      // the first screen's big line
    "hedgehog": "One sentence.",
    "weakest_link": "...",
    "top_stop": ["...", "...", "..."],           // top three stop-doing items
    "temptations": ["..."],                      // stewardship mode: use this instead of top_stop
    "brutal_fact": "The most urgent one.",
    "missing_numbers": ["..."],
    "confidence": { "level": "moderate", "rests_on": "..." }
  },
  "greatness_potential": 22,                     // 0-100, same number as the analysis

  "takeaways": {                                 // optional: override each step's big line
    "facts": "...", "hedgehog": "...", "flywheel": "...", "stop": "...",
    "people": "...", "plan": "...", "risks": "...", "record": "...", "milestones": "..."
  },

  "not_yet_good": {                              // only when state is "not_yet_good"
    "what_good_looks_like": "...",
    "why": "...",
    "milestones": [{ "text": "...", "evidence": "what would prove it" }]
  },

  "great_version": "One paragraph: the subject when it's great.",

  "hedgehog": {
    "sentence": "...",
    "circles": {
      "best":    { "kept": "...", "ruled_out": ["..."] },
      "engine":  { "kept": "...", "ruled_out": ["..."] },
      "passion": { "kept": "...", "ruled_out": ["..."] }
    },
    "denominator": "profit per X, and why",
    "tests": [{ "name": "Explains past wins?", "result": "Mostly", "note": "..." }],   // result starting Yes / Mostly / Partly / No sets the color
    "confirmation_tests": ["..."]
  },

  "flywheel": {
    "steps": [{ "short": "Deepest spec library", "detail": "..." }],               // 4-7 steps, in loop order
    "weakest": { "from": 6, "to": 1, "why": "..." },                               // 1-based step numbers; "to" must be the next step in the loop
    "current_push": ["..."],
    "doom_loop": "..."
  },

  "stop_doing": [{ "text": "Building the Lite app", "why": "..." }],

  "brutal_facts": [{ "fact": "...", "evidence": "...", "severity": "high", "owner": "..." }],
  "faith_statement": "...",
  "truth_climate": "...",

  "bus": [{ "who": "Mac contractor", "call": "move", "why": "..." }],

  "next_90_days": [{ "text": "Split the renewal number", "owner": "You", "when": "Weeks 1-3", "detail": "..." }],
  "scorecard": [{ "output": "...", "current": "...", "target": "...", "trajectory": "..." }],

  "risks": [{ "source": "Gate 5 (CONDITIONAL)", "risk": "...", "warning": "...", "clears": "..." }],
  "shared_root_problems": "...",
  "recheck": "When and how to re-check.",

  "ideology": { "values": ["..."], "purpose": "...", "bhag": "...", "mechanisms": ["..."] },
  "gates": [{ "n": 0, "name": "Fit", "verdict": "PASS", "note": "..." }],            // all 11, Gates 0-10
  "details": [{ "title": "Baseline sheet (Gate 1)", "body": ["paragraph", "paragraph"] }],
  "assumption_note": "Autonomous run: inferences are marked."
}
```

## Steps the page shows, in order

1. **Verdict:** headline, Hedgehog, greatness potential, confidence, urgent fact, weakest link, top stop-doing items and gate strip.
2. **Milestones:** only for a subject that is not yet good.
3. **Brutal facts:** most severe first.
4. **Hedgehog:** the great version, the three circles and the denominator.
5. **Flywheel:** the ring with the weakest link marked.
6. **Stop doing,** or temptations in stewardship mode.
7. **People:** the bus.
8. **Next 90 days:** the plan and the scorecard.
9. **Risks:** the risk register and the re-check.
10. **Gate log:** gates, ideology and working notes.

Each step's big line comes from the data, for example the most severe fact or the Hedgehog sentence. Override it with `takeaways` when the automatic line reads poorly.
