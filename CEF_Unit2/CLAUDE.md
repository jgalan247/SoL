# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is **LIBF Level 2 Certificate in Financial Education — Unit 2: Financial Capability, Money Management and the Economy**. It is a static educational website with 11 interactive topic pages, quizzes, activities, and downloadable PDF tests for students.

Unit 1 (Finance, the Individual and Society) is the reference implementation at https://github.com/jgalan247/finance_CEF. **Unit 2 must follow the same structure, patterns, and conventions as Unit 1.**

## Unit 2 Curriculum (from `Unit 2 FULL.pdf`)

| Topic | Title | Key Learning Outcomes |
|-------|-------|----------------------|
| 1 | Financial planning and money management | Financial planning terminology, need for planning, financial providers and products, sources of advice |
| 2 | Different plans for different people | Personal factors affecting planning, attitude to risk, adapting plans |
| 3 | Planning for now and for the future | Short/medium/long-term planning, objectives and goals, savings products |
| 4 | Budgeting | Budgeting terminology, importance of budgeting, managing budgets |
| 5 | What can affect a budget? | External factors (inflation, interest rates, exchange rates), calculating impact |
| 6 | Personal budgets and spending choices | Budget calculations, unexpected spending, impact on economy |
| 7 | Using tools to manage money | Money management systems, accessing money, transferring money |
| 8 | Pay and tax | Income types, employed vs self-employed tax, payslips, P45/P60, tax calculations |
| 9 | The real cost of spending | Value for money, hidden charges, VAT principles |
| 10 | Borrowing products | Reasons for borrowing, UK personal debt, borrowing costs, product features |
| 11 | The implications of borrowing | Factors in borrowing decisions, cost calculations, impact on budget and economy, payment default |

## Technology Stack

- **Pure vanilla HTML5, CSS3, JavaScript (ES6+)** — no frameworks, no build tools, no npm
- **jsPDF 2.5.1** (CDN) — only external dependency, used for test PDF generation
- **GitHub Pages** deployment (static hosting)

## Architecture (mirrors Unit 1)

```
CEF_Unit2/
├── index.html                          # Homepage with 11-topic card grid
├── css/
│   ├── styles.css                      # Main stylesheet (CSS variables for theming)
│   └── test-styles.css                 # Test page styling
├── js/
│   ├── quiz.js                         # Quiz and QuickCheck classes
│   ├── card-sort.js                    # CardSort and MatchingActivity classes
│   ├── activities.js                   # FlipCards, TrueFalse, FillBlanks, RevealAnswer classes
│   └── test-engine.js                  # FISTest class with timed exam + PDF generation
├── topics/
│   ├── topic-1-financial-planning/index.html
│   ├── topic-2-different-plans/index.html
│   └── ... (topic-3 through topic-11)
└── tests/
    ├── topic-1-test.html
    └── ... (topic-2-test through topic-11-test)
```

### Topic Folder Slugs
| Topic | Folder slug |
|-------|------------|
| 1 | `topic-1-financial-planning` |
| 2 | `topic-2-different-plans` |
| 3 | `topic-3-planning-future` |
| 4 | `topic-4-budgeting` |
| 5 | `topic-5-budget-factors` |
| 6 | `topic-6-spending-choices` |
| 7 | `topic-7-managing-money` |
| 8 | `topic-8-pay-tax` |
| 9 | `topic-9-cost-spending` |
| 10 | `topic-10-borrowing-products` |
| 11 | `topic-11-implications-borrowing` |

### Path Conventions
- **Topic pages** are at `topics/<slug>/index.html` — they reference CSS/JS via `../../css/` and `../../js/`
- **Test pages** are at `tests/topic-N-test.html` — they reference CSS/JS via `../css/` and `../js/`
- **Homepage** is at root — references via `css/` and `js/`
- The site abbreviation is **FCMME** (Financial Capability, Money Management and the Economy). Unit 1 uses "FIS" — do not mix them, though the JS class is still called `FISTest` for compatibility.

## Reusable Activity Classes (from Unit 1 JS)

All classes are exposed on `window` and instantiated inline in topic HTML files:

| Class | File | Usage Pattern |
|-------|------|---------------|
| `Quiz` | quiz.js | `new Quiz('container-id', [{question, options, correct, explanation}])` |
| `QuickCheck` | quiz.js | `new QuickCheck('id', question, options, correctIndex, explanation)` |
| `CardSort` | card-sort.js | `new CardSort('id', terms[], zones[])` — drag-and-drop categorisation |
| `MatchingActivity` | card-sort.js | `new MatchingActivity('id', pairs[])` — click-to-match term/definition |
| `FlipCards` | activities.js | `new FlipCards('id', [{front, back}])` — 3D flip reveal cards |
| `TrueFalse` | activities.js | `new TrueFalse('id', [{statement, isTrue, explanation}])` |
| `FillBlanks` | activities.js | `new FillBlanks('id', text_with_{0}_placeholders, blanks[])` |
| `RevealAnswer` | activities.js | `new RevealAnswer('buttonId', 'contentId')` — show/hide model answers |
| `FISTest` | test-engine.js | `new FISTest('id', {topicNumber, topicName, questions[], caseStudies[]})` |

## Key Conventions

### Topic Page Structure
Each topic HTML page follows this exact order:
1. Header with topic title + learning objective subtitle
2. Breadcrumb navigation (Home > Current Topic)
3. Content sections with `<h2>` numbered headings (e.g., `1.1 Terminology`)
4. Interactive activities embedded between content sections (numbered with blue circle icons)
5. Summary section
6. CTA button linking to the topic test
7. Previous/Home/Next navigation buttons
8. Footer

### Test Pages
- Section A: standalone multiple-choice questions
- Case studies: scenario text with 3+ sub-questions each
- Auto-generates and downloads a PDF with student name, score, date, and reference number
- 50% pass mark

### CSS Theming
- CSS custom properties in `:root` for colours (`--primary`, `--secondary`, `--accent`, `--topic-1` through `--topic-11`)
- Each topic has a unique accent colour used on card borders and number badges
- Single responsive breakpoint at `768px`
- Activity containers use `.activity` class with `.activity-header` (icon + title)

### HTML/JS Patterns
- Scripts loaded at bottom of topic pages: `../../js/quiz.js`, etc.
- Activities instantiated in inline `<script>` blocks immediately after their container `<div>`
- No global state management — each activity class is self-contained
- DOM created via `innerHTML` in class `render()` methods

## Development

No build step. Open `index.html` directly in a browser or serve with:
```
python3 -m http.server 8000
```

The JS and CSS files from Unit 1 can be reused directly — copy them from the finance_CEF repo as the starting point.
