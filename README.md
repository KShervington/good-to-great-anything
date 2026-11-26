# Good to Great: Anything

**A Claude skill that takes something already *good* and works out what its *great* version would be.**

It runs your subject through the ideas in Jim Collins's *Good to Great* (plus *Built to Last* and *How the Mighty Fall*). Collins wrote about companies, but noted the principles apply more widely, so this skill works on a business, a product, a team, a nonprofit, a career or a side project.

You get a short verdict in the chat, plus a **guided report page**: a single HTML file that walks you through the result one idea per screen (verdict, brutal facts, Hedgehog, flywheel, stop doing, people, plan, risks, gate log). A "Show all" switch turns it into one printable page. It works offline, on a phone, and in light or dark mode, and every inferred figure is flagged as an assumption.

The report covers:

- **The Hedgehog Concept:** the one thing the subject can be best in the world at, that drives its economic (or resource) engine and that its people care about, in one sentence.
- **The flywheel:** how each win feeds the next, and which link is weakest.
- **A stop-doing list:** the attractive things to say no to.
- **The brutal facts:** what's true and uncomfortable, ranked by severity.
- **The bus:** who and what to keep, move, add or let go.
- **A scorecard and a 90-day plan.**
- **A risk register:** including how this particular subject could decline.
- **A gate log:** what passed, what's conditional, and why.

## How it works

The subject passes through 11 gates in order. Each gate produces an artifact and a verdict (`PASS`, `CONDITIONAL` or `FAIL`):

| Gate | Question |
|---|---|
| 0 Fit | Can the framework work on this subject at all? |
| 1 Baseline | Is it actually good? Is it not yet good, good but not great, or already great? |
| 2 Level 5 leadership | Does the person in charge put the endeavor ahead of their ego? |
| 3 First who, then what | Are the right people (and commitments) in the right seats? |
| 4 Brutal facts | What's true that nobody wants to say? |
| 5 Hedgehog Concept | What sits at the intersection of best-at, economic engine and passion? |
| 6 Culture of discipline | What goes on the stop-doing list? |
| 7 Technology | Which tools accelerate the Hedgehog, and which are distractions? |
| 8 Flywheel | Does the loop close? Is there a doom loop? |
| 9 Built to last | What makes the greatness outlive one person? |
| 10 How the mighty fall | How could this particular subject decline, and what's the early warning? |

It adapts to the subject:

- **Not yet good:** the run stops at Gate 1 and says what "good" would look like and how to prove it. Greatness work on a core that doesn't work yet would be built on sand.
- **Once good, now in crisis:** the run becomes a turnaround, with the brutal facts and survival actions first.
- **Already great:** it says so plainly and switches to *stewardship mode*. It confirms the existing Hedgehog instead of inventing a new one, lists only the real temptations to refuse, and doesn't manufacture weaknesses to justify a long plan.

It works in two modes:

- **Interview (default):** it asks one batch of up to five questions, then checks the Hedgehog candidates with you.
- **Autonomous ("just run it"):** it infers what it can and marks every inference `[ASSUMPTION]` so you can correct it.

## Example

[examples/linewright](examples/linewright) shows a full run on a fictional solo-founder desktop app:

- [dossier.md](examples/linewright/dossier.md): the input, the founder's notes.
- [report.html](examples/linewright/report.html): the guided report page. Download it and open it in a browser.
- [output.md](examples/linewright/output.md): the same analysis as plain markdown.

The verdict opens with:

> **Verdict: good, not yet great. The core is eroding quietly while the founder considers a new product.**

## Install

**Claude Code (plugin):**

```
/plugin marketplace add KShervington/good-to-great-anything
/plugin install good-to-great-anything@good-to-great-anything
```

**Claude Code (personal skill):** copy `skills/good-to-great-anything/` into `~/.claude/skills/`.

**Claude.ai / Claude desktop:** zip the `skills/good-to-great-anything/` folder and upload it in Claude's skill settings.

Then ask something like *"Run good-to-great on my consulting practice"* or *"Take my open-source project from good to great. Just run it."* It works best with real numbers. Paste in or attach whatever you have: revenue, users, retention, team, what you're debating.

## How it was tested

The skill was evaluated and improved against 58 case studies:

- Collins's own great companies and their direct comparisons.
- Great companies that later fell, judged at their peak.
- Synthetic subjects with built-in traps.
- Companies that were already great and should be left mostly alone.

Each output was graded against an answer key by a separate judge model, never by the model that wrote it.

- **The original skill** scored 91–92 out of 100.
- **Two improvement rounds** produced this version. It writes a shorter, sharper verdict (top marks in every held-out run), recognizes already-great subjects instead of inventing problems for them, and makes the right Gate 1 call on not-yet-good and in-crisis subjects.
- **On 16 cases held back until the end,** it scored **93.95 vs 92.02**.

The gain is consistent but modest. The full method, the numbers and the limits are in the evaluation repo: **[good-to-great-eval](https://github.com/KShervington/good-to-great-eval)**.

The report page (v1.1) was added after the evaluation. It changes how the result is presented, not the analysis: the gates, wording and content rules are the ones that were tested.

## Repo layout

| Path | What it is |
|---|---|
| `skills/good-to-great-anything/SKILL.md` | The skill. |
| `skills/good-to-great-anything/assets/report-template.html` | The report page. The skill fills in its JSON block. |
| `skills/good-to-great-anything/assets/report-schema.md` | The JSON fields the page reads. |
| `examples/linewright/` | A worked example: input, report page, markdown output and the page's data. |
| `tools/build_report.py` | Rebuilds a report page from a JSON file: `python tools/build_report.py data.json out.html`. |

## Limits worth knowing

- Collins studied winners after the fact, and some of his "great" companies later declined. Treat the output as **disciplined hypotheses to test**, not guarantees.
- The evaluation measured agreement with Collins's analysis, not real-world results. The real test is yours: the skill offers a 90-day re-check, so take it.
- It is only as good as the evidence you give it. A run with real numbers on the core gates beats a complete run built on assumptions.

## License and credit

MIT. Not affiliated with or endorsed by Jim Collins or his publishers. The skill paraphrases the frameworks in its own words. For the real thing, read the books.
