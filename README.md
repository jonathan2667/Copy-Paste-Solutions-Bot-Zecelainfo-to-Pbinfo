# Copy-Paste-Bot 2.0: Problem Migration Tool 🤖

## Overview
Copy-Paste-Bot 2.0 is an advanced Python script designed to streamline the process of migrating problems from "zecelainfo.com" to "pbinfo.ro". Leveraging Selenium, this bot automates the task of copying problem descriptions from one website and pasting them onto another. With intelligent handling and error detection mechanisms, it ensures a smooth and efficient migration process.

## Key Features
- **Automated Migration:** Copies problem descriptions from "zecelainfo.com" to "pbinfo.ro" seamlessly.
- **Dual-Browser Operation:** Utilizes Firefox for "pbinfo.ro" and Chrome for "zecelainfo.com".
- **Error Handling:** Detects and handles issues such as invalid problems gracefully.
- **Minimal Human Intervention:** Runs autonomously, requiring minimal manual oversight.

## How it Works
1. The bot logs in to "pbinfo.ro" using predefined credentials.
2. It navigates to "zecelainfo.com" and iterates through a range of problems.
3. For each problem, it fetches the problem description and pastes it into the "pbinfo.ro" submission form.
4. The bot submits the problem description and moves on to the next one.

## Dependencies
- Python
- Selenium
- WebDriver (for Firefox and Chrome)

## Future Enhancements
- Integration of additional error handling mechanisms.
- Implementation of user feedback and reporting features.
- Optimization for performance and reliability.

## Note
While functional, the bot may require periodic updates to maintain compatibility with website changes.

Happy problem migration! 🚀
