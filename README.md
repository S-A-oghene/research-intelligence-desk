# Research Intelligence Desk

**Status:** ⏳ Pending Local Verification – update after execution  
**Nature:** Personal prototype – demonstrates research synthesis and decision support

This tool takes research notes in JSON and produces a structured executive brief. It follows the pipeline: question → discovery → capture → verify → synthesise → options → recommendation → next action.

## How to Run
1. Replace `research_data.json` with your own real research (do not keep placeholder data).
2. Run `python generate_brief.py`
3. The brief is saved to `examples/decision_brief.md`.

## Verification
I will replace the sample data with a genuine research exercise, run the script, and verify the output. See `VERIFICATION.md` for my results.

## Known Limitations
- Does not verify source credibility automatically.
- Recommendation is based on a simple scoring of pros vs cons.
- No integration with external research databases.