# Changelog

## 1.0.4 (2026-10-23)
- Remove internal notes from the README, translations, rule file (renamed to `rules/scope.mdc` where applicable) and skills. Local tests re-run and passed. Not tested in-app. Not submitted to the marketplace.

## 1.0.3 (2026-10-23)
- Translations: each language section in TRANSLATIONS.md now starts with a one-line notice in that language saying it is a machine translation, not reviewed by a native speaker, and that the English version is authoritative. README Languages section notes this. No behavior changes.
- Local tests re-run and passed. Not tested in-app. Not submitted to the marketplace.

## 1.0.2 (2026-10-22)
- Renamed from PlanPilot to PlanOmega (manifest `planomega`, repo github.com/OmnipotentCEOxJenny/planomega, skills `planomega-charter` and `planomega-schedule`, script `scripts/planomega_cpm.py`). The old name clashed with an App Store app and planpilotx.app. Releases 1.0.0 and 1.0.1 were made under the former name PlanPilot.
- Keywords: 40, with PlanOmega, JennyEcho and OmnipotentCeo. Logo artwork unchanged.
- No behavior changes.

## 1.0.1 (2026-10-22)
- Keywords follow Rob's settled rule 7: universals PlanOmega, JennyEcho, OmnipotentCeo in PascalCase; joined words PascalCase; single words lowercase. No behavior changes.

## 1.0.0 (2026-10-22)
- First version: skills `planomega-charter` and `planomega-schedule`, rule `scope.mdc`, optional critical-path helper `scripts/planomega_cpm.py`, worked example (PluginPulse v1.1 plan from the Course 5 hands-on), plain-language README.
- Method from Adrienne Watt, *Project Management* (BCcampus, CC BY 4.0).
- Tests: `tests/check_frontmatter.py` and `tests/test_cpm.py`.
- 40 search keywords (lowercase, no hyphens, PlanOmega-specific, per Rob's keyword rules) in the manifest plus `keywords.md`; 23 machine-translated summaries (not native-reviewed).
- Local tests only; not tested in-app. Not submitted to the marketplace.
