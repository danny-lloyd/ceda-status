# ceda-status

## Introduction

This repo provides the schema and instance document for the JSON-format feed of status information for CEDA and JASMIN services.

## Editing

The JSON content used for the CEDA status page is stored in `status.json` and is fed by the "raw" view at the URL
https://raw.githubusercontent.com/cedadev/ceda-status/main/status.json

The schema file `statuspage.schema.json` is designed to be used in conjunction with the online [Json-Editor](https://pmk65.github.io/jedemov2/dist/demo.html) tool. Hence it includes some configuration for that tool as well as schema rules to validate a `statuspage` JSON document.

The JSON content can be edited manually, but the Json-Editor tool provides useful validation to avoid syntax / structural errors.

- Use the "upload" feature of the JSON-Editor to upload the schema file.
- Copy the content of the current `main` version of `status.json`
- Navigate to the "Output" tab
- Paste the copied JSON content into the "Output tab"
- Navigate to the "Form" tab
- Use the form to edit the status content and add new items as needed
- Navigate to the "Output" tab: the JSON content should be updated with (valid) changes
- Copy that JSON content back to your own editor as new content for `statuspage.schema.json`
- The CEDA status page at `www.ceda.ac.uk/status` has JQuery code to read the JSON feed from the "raw" URL above.
- Committing and pushing your changes to `status.json` in the `main` branch means that these changes are made live.
- A user viewing the status page should now see the updated status content in their browser.

## Content guidance

The JSON file can have 0 or more incidents, with each incident having the following fields:

Field | Required | Details | Example
--- | --- | --- | ---
status | yes | Overal current status of the incident | Must be one of `down`, `resolved`, `degraded` or `at risk`.
affectedServices | | Concise list of affected services | `LOTUS & GWSs having paths /gws/nopw/jo4/*` (free text)
summary | | Concise summary of the incident (but not its status) | `Issue with storage systems`
date | yes | date/time of initial report or future planned date of incident | `2024-03-31 09:00` (locale: en-GB)
updates | at least 1 | see below | |

while each `update` field should have the following:

Field | Required | Details | Example
--- | --- | --- | ---
date | yes | date of the update/report | format as above
details | yes | Concise text report | `Issue reported: under investigation`, `Issue now resolved, please report any further issues`, `Planned maintenance`, etc.

## Content management

- Order of incidents within the JSON file is not significant: the rendering page orders them by date automatically.
- The message-of-the-day script will order them in order of each incident's most recent update.
- Incidents should be removed after being marked as `resolved` for 5-7 days (enough time for people to take note that they're resolved).
- Future incidents should have an initial update, including date/time corresponding to the planned downtime and a `details` field with initially-expected impact. This can be superceded by subsequent updates.
- Leave previous updates in place on a particular incident (to provide a brief history), unless their continued presence causes confusion (eg. if initial diagnosis / impact was incorrect).
