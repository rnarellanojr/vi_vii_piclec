# PICLEC Quick Quiz

Four questions per attempt. One 60-second timer across the attempt. Scores are 2 + (2 × correct answers), from 2 to 10 points. Unanswered questions are incorrect. The bank contains exactly 50 recall and 10 understanding items based on the supplied notes for Module 2, sections 2.12–2.15.

Questions are drawn without replacement from a shuffled 60-item deck during the current page session. After 15 attempts, the deck reshuffles. Each four-question set has unique questions; choices also shuffle. The recall/understanding mix varies by attempt. Answers remain editable until manual or automatic submission. Explanations appear afterward. The last five completed attempts are kept on the same browser/device when browser storage is available. Attempts are practice records and are not sent to an instructor.

## Run offline or on GitHub Pages

Open `index.html` directly in a browser. The app works without an internet connection. To host on GitHub Pages, upload `index.html` to the root of the selected Pages branch and enable Pages for that branch.

## Edit the bank

In the source repository, edit `questions.json`, then run `python3 build.py`. Each `answer` is the zero-based position of the correct option in the source. The app shuffles the display choices. All questions have one best answer and four options. `dist/index.html` embeds the whole bank and app, so no build or dependency install is needed for the downloadable version.

The group names and numbering follow the supplied lecture notes. This quiz covers selected stable facts and conceptual relationships and does not reproduce all historical medicinal uses in the notes.
