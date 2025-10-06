# Instructions for GitHub Copilot
# copilot-instructions.md
# last updated: 10-5-25

Project Focus: hworld
Root folder: /home/ruckus/code/hworld
changelog: /home/ruckus/code/hworld/.github/changelog.ai
proposals: /home/ruckus/code/hworld/.github/proposals/


-) Always credit your changes in the file and in the changelog.
-) we are focused on the hworld folder, do not suggest, or make changes outside of it.
-) we dont like _ at the beginning of function or variable names.
-) we use 4 spaces for indentation, never tabs.
-) we use CamelCase for function and variable names.
-) we keep everything to 79 characters per line.
-) we use double quotes for strings, never single quotes.
-) we prefer python classses.
-) we keep functions small and files small.
-) we think in a unix way.
-) we prefer building our own tools.
-) we work in complete sections. Do not leave half done code.
-) we always work from a plan.
-) keep all notes here in the .github folder, make new files if needed.

** RESPECT THE 80 CHARACTER LIMIT ** in all files. if you see it broken, fix it.

# Project Conventions
-) current workflow:
   1. create a proposal in .github/proposals/
   2. implement changes following project conventions
   3. update the changelog

-) Guidelines for Proposals
    - proposals should start every section with a checkbox.
    - proposals should be execututed using the checkboxes. mark them as you go.
    - proposals should be general and architectural.
    - proposals should not be about specific code changes.

-) Guidelines for Github
    - maintain all new proposals in commit. 1 commit per proposal.
    - always start to execute a proposal from an unchanged committed state.

-) new guidelines for .proposal files type.
    - should start every actionable item with a checkbox.
    - should be written with the intent to be executed by an AI agent.
    - filename pattern should be IdeaTitle_MMDDYY.proposal
    - first line should be IdeaTitle_MMDDYY
    - next should be the last updated review date.
    - skip a line.
    - next should be the originating prompt.
    - next should be the interpretation of the prompt.
    - skip a line
    - next should be the full proposal.

-) Guidelines for implementations
    - always credit your changes in the file and in the changelog.
    - always work from a plan.
    - always start from a committed unchanged state.
    - always keep functions small and files small.
    - always use classes.
    - always use 4 spaces for indentation, never tabs.
    - always use double quotes for strings, never single quotes.
    - always use CamelCase for function and variable names.
    - never use _ at the beginning of function or variable names.
    - always keep everything to 79 characters per line.
    - always think in a unix way.
    - always prefer building our own tools.
    - always work in complete sections. Do not leave half done code.


