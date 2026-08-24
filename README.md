# Research Intelligence Desk

**Status:** ✅ Personally Executed and Locally Verified  
**Verification Date:** 2026-08-24  
**Nature:** Personal prototype – demonstrates research synthesis and decision support

This tool takes research notes in JSON and produces a structured executive brief. It follows the pipeline: question → discovery → capture → verify → synthesise → options → recommendation → next action.

## Pipeline

1. **Question** – Define the research question
2. **Discovery** – Gather source materials
3. **Capture** – Record key findings
4. **Verify** – Check source quality
5. **Synthesise** – Combine findings
6. **Options** – Identify and evaluate options
7. **Recommendation** – Make evidence-based recommendation
8. **Next Action** – Define next steps

## How to Run

1. Replace `research_data.json` with your own real research (do not keep placeholder data)
2. Run: `python generate_brief.py`
3. The brief is saved to `examples/decision_brief.md`

### Sample Output Sections

- Executive Bottom Line – Recommended approach with score
- Key Findings – Evidence summary
- Sources – Cited references
- Options Analysis – Pros and cons for each option
- Trade-offs Summary – Scoring comparison
- Recommendation – Evidence-based recommendation
- Risks – Potential challenges
- Unknowns – What remains uncertain
- Next Actions – Concrete steps forward

## Quality Controls

See `quality_controls.md` for the research quality checklist applied to every brief.

## Verification

This project has been personally executed and locally verified. See `VERIFICATION.md` for complete test results.

## Known Limitations

- Processes structured research input only
- Does not independently verify source credibility
- Recommendation is based on a simple scoring of pros vs cons
- No integration with external research databases

---

*This is a personal research workflow tool.*
