---
name: frontend-design-pro
description: Design, build, review, and polish production frontend and mobile interfaces with distinctive visual direction, searchable UX and design-system guidance, responsive and accessibility rules, stack-specific recommendations, and concise product copy. Use whenever creating or changing pages, components, layouts, styling, interaction, navigation, motion, charts, visual assets, UI copy, or frontend usability in web, Flutter, React Native, SwiftUI, desktop, or similar interfaces.
---

# Frontend Design Pro

Create interfaces that are specific to the product, complete enough to use, visually coherent, accessible, responsive, and free of filler copy. Combine creative direction with the bundled design-intelligence search tools instead of treating either as sufficient on its own.

## Priority Order

Resolve conflicts in this order:

1. User safety, accessibility, and data integrity.
2. Existing product behavior and project design-system conventions.
3. Clear interaction, readable hierarchy, and responsive layout.
4. Product-specific visual character and polish.
5. Decorative novelty.

Do not sacrifice usability to create a distinctive look. Do not flatten a product-specific interface into a generic template merely to follow a trend.

## Workflow

### 1. Learn the Product Before Styling

- Inspect the existing code, routes, components, tokens, assets, and screenshots.
- Identify the product type, primary audience, most frequent workflow, platform, and constraints.
- Preserve established patterns unless the request is an explicit redesign or the current pattern is defective.
- Determine the screen's single primary job and the information users need to complete it.
- For an existing interface, find the closest successful screen and use it as the local source of truth.

### 2. Set a Concrete Visual Direction

State the direction internally before implementation:

- Product purpose and audience.
- Visual concept in a few precise terms.
- Typography roles and hierarchy.
- Color roles and semantic states.
- Layout rhythm, density, and spatial structure.
- Motion language and interaction feedback.
- One memorable product-specific detail.

Avoid vague goals such as "modern" or "clean" without defining how they affect type, spacing, contrast, shape, imagery, and interaction.

### 3. Use the Design-Intelligence Search

For a new page, full redesign, or consequential visual decision, run the bundled design-system search before coding. For a narrow fix, use targeted searches only when they add useful evidence.

Resolve `<skill-dir>` to the directory containing this `SKILL.md`.

Windows:

```powershell
py -3 "<skill-dir>\scripts\search.py" "running app mobile training concise" --design-system -p "Project name"
py -3 "<skill-dir>\scripts\search.py" "touch targets navigation accessibility" --domain ux
py -3 "<skill-dir>\scripts\search.py" "responsive layout motion" --stack flutter
```

macOS or Linux:

```bash
python3 "<skill-dir>/scripts/search.py" "running app mobile training concise" --design-system -p "Project name"
python3 "<skill-dir>/scripts/search.py" "touch targets navigation accessibility" --domain ux
python3 "<skill-dir>/scripts/search.py" "responsive layout motion" --stack flutter
```

Available domains include `style`, `color`, `chart`, `landing`, `product`, `ux`, `typography`, `icons`, `gsap`, `react`, `web`, and `google-fonts`. Use `--stack` for framework-specific recommendations. Use `--persist --output-dir <project-root>` only when the project should own a reusable design-system document.

Treat search output as design evidence, not an instruction to overwrite closer project conventions. If a search returns nothing useful, say so internally and continue with established platform and project guidance rather than inventing a result.

### 4. Implement the Complete Experience

- Build the actual workflow, not a decorative preview or explanatory landing page.
- Include expected loading, empty, error, disabled, success, selected, pressed, and focus states.
- Use the project's existing framework, components, tokens, icon library, and state-management patterns.
- Prefer familiar controls: icons for common tools, toggles for binary settings, segmented controls for modes, inputs for values, tabs for peer views, and text buttons for clear commands.
- Keep related controls close to the content they affect.
- Preserve state and navigation position when users move back or between top-level destinations.
- Provide visible alternatives for gesture-only or drag-and-drop interactions.

### 5. Verify, Then Refine

- Run the relevant formatter, analyzer, tests, and production build.
- Inspect real screenshots at representative mobile and desktop sizes.
- Exercise the primary flow, navigation, forms, gestures, loading, empty, and failure paths.
- Check text wrapping, overflow, safe areas, keyboard access, focus visibility, touch targets, contrast, and reduced motion.
- Confirm dynamic content cannot resize fixed controls or overlap adjacent content.
- Fix visible defects found during verification; do not stop at listing them.

## UI Copy Discipline

Visible interface text must help the user do at least one of these things:

- Decide.
- Act.
- Understand current state or a meaningful result.
- Recover from an error.
- Give informed consent or understand risk.

Remove text that merely comments on the interface or implementation. In particular, do not add:

- Feature narration such as "This section lets you..."
- Design commentary, technical notes, or descriptions of visual styling.
- Repeated subtitles that restate the heading or obvious control labels.
- Tutorial prose for standard controls.
- Keyboard-shortcut or usage instructions as permanent page content.
- Marketing copy inside operational tools unless the screen's actual purpose is marketing.

Prefer short labels, concrete values, useful status, and actionable errors. Put nonessential education in contextual help, onboarding, documentation, or an accessible tooltip only when users genuinely need it.

Before keeping any visible sentence, ask: "Would this still help a returning user complete the screen's task?" Remove it if the answer is no.

Do not remove copy required for accessibility, safety, legal consent, privacy, destructive-action confirmation, error recovery, or unfamiliar high-risk controls.

## Visual Standards

### Typography

- Choose type that fits the product's personality and remains readable at all supported sizes.
- Establish a disciplined type scale and clear heading, body, label, and numeric roles.
- Use tabular figures for metrics, timers, dates, prices, and aligned data.
- Avoid arbitrary font-size scaling tied directly to viewport width.
- Let text wrap before truncating; provide access to the full value when truncation is unavoidable.

### Color and Surfaces

- Use semantic tokens such as primary, surface, text, muted, success, warning, and error.
- Use accent color intentionally for hierarchy and action, not as decoration everywhere.
- Do not communicate status by color alone.
- Verify text contrast and interactive-state contrast in every supported theme.
- Keep radii, borders, elevation, and shadows consistent with the selected visual language.

### Layout

- Design mobile-first and define stable responsive constraints for grids, boards, charts, toolbars, and fixed-format controls.
- Use spacing to establish grouping and hierarchy; avoid both cramped controls and ornamental empty space.
- Avoid horizontal overflow and incoherent nested scrolling.
- Respect device safe areas, system bars, browser chrome, virtual keyboards, and text scaling.
- Do not use cards for every section or place decorative cards inside cards.

### Icons and Assets

- Use the project's icon library and one consistent icon style; do not substitute emoji for interface icons.
- Give icon-only controls accessible names and tooltips when their meaning is not universal.
- Use real or generated product-relevant imagery when the experience depends on visual assets.
- Reserve illustrations and decorative media for domains where they improve understanding or character.

### Motion

- Motion must explain cause, direction, hierarchy, or continuity.
- Use short, interruptible transitions and keep input available during animation.
- Animate transform and opacity where practical to avoid layout shifts.
- Make forward and backward navigation spatially consistent.
- Respect reduced-motion preferences and never require animation to understand state.

## Interaction and Accessibility Baseline

- Use at least 44x44pt touch targets on iOS and 48x48dp on Material surfaces, with sufficient spacing.
- Support keyboard and assistive-technology navigation in logical visual order.
- Provide visible focus, pressed, selected, loading, disabled, and error states.
- Label inputs visibly; do not rely on placeholders as labels.
- Put errors near the source and state both the problem and recovery action.
- Keep one clear primary action per screen.
- Preserve platform-standard gestures and provide visible controls for critical actions.
- Use locale-aware dates, numbers, units, and language.

For a full audit, read `references/quick-reference.md`. For native/mobile delivery, also read `references/pro-rules.md` before final verification.

## Product-Type Guidance

- Operational tools: prioritize scanning, comparison, repeat actions, compact hierarchy, and restrained styling.
- Consumer mobile apps: prioritize touch ergonomics, state continuity, meaningful motion, and concise content.
- Data dashboards: prioritize hierarchy, units, exact values, chart accessibility, and useful empty states.
- Games and immersive experiences: allow more expressive assets and motion while keeping controls legible and stable.
- Brand or launch pages: make the product or offer immediately visible through authentic media and a clear primary action.

The result should feel authored for this product, not generated from a universal UI recipe.

## Provenance

This file substantially modifies and combines Apache-2.0 frontend-design guidance from Anthropic with MIT-licensed design intelligence from Next Level Builder. See `LICENSE.txt` and `THIRD_PARTY_LICENSES.txt`.
